# 05 · OOM in prod, flat in staging

- **Model (internal):** one-truth (analysis)
- **Role & stakes:** Software engineer on-call. Thursday 11:20 AM. `pdf-renderer` pods in production are OOMKilling every ~4 hours. You ran a 2x-RPS load test in staging all night and memory stayed completely flat.
- **Across the table:** Marcus, a senior SRE helping you compare prod and staging.

## Opening brief

> "Prod `pdf-renderer` pods are OOMKilling every 4 hours at 2GB. We ran staging at 2x prod traffic for 12 hours and memory didn't budge. Same Docker image, same 2GB limit. What do you want to check?"

- **D1 (Opening):**
```
pod memory (2GB limit)
prod:     ╱╱╱✕ OOM  ╱╱╱✕ OOM   (every ~4h)
staging:  ──────────────────── (flat at 210MB, 2x RPS)
```

## Locked facts (reveal on ask)

- **Process heap / RSS (D2 — key turn):**
```
prod pod just before OOM:
  container memory_working_set:  1.98 GB
  app process RSS + heap:         215 MB  (flat!)
```
- **Recent deploys (D3 — red herring):** `pdf-renderer v1.14` shipped 2 days ago ("added retry header"). Same image is running in staging.
- **Prod vs. staging traffic & status codes (D4):**
```
status codes     prod     staging (load test)
200 OK           95.6%    100.0%
499 (client off)  4.1%      0.0%
5xx               0.3%      0.0%
```
  Prod has real mobile clients on flaky networks that cancel/disconnect mid-render. Staging's load generator always waits for 200.
- **Filesystem / `/tmp` check (D5 — root cause):**
```
df -h /tmp (inside prod pod before OOM):
  tmpfs   2.0G   1.76G   240M   88%  /tmp
  1,420 orphaned files: /tmp/render-*.pdf
```
  `/tmp` is a RAM-backed `tmpfs` (counted toward the pod's 2GB cgroup memory limit).
- **Code / cleanup behavior (D6):** `pdf-renderer` writes temp PDFs to `/tmp/render-<id>.pdf` and deletes them in the post-response handler—which is skipped when the HTTP request context cancels early on a `499` client disconnect.

## Hidden truth

There is no app memory leak—process RSS is flat at 215MB. Prod has 4.1% `499` client disconnects (which staging's load test doesn't simulate), skipping temp-file cleanup and filling RAM-backed `/tmp` (`tmpfs`) until the cgroup OOMs.

## Closing prompt

Post a 2–4 line update in `#eng-oncall` explaining why prod is OOMing while staging is flat, and the fix.
