---
description: A 5-minute simulated engineering experience. Drop into a real-world situation with locked facts, investigate by asking questions, commit to a closing call, and see your run next to a Staff engineer simulation over the exact same facts.
disable-model-invocation: true
argument-hint: "[topic or 'new' to generate a fresh scenario]"
---

> **Bundled command:** Relative references to `experience.md`, `packs/01-quiet-checkout.md`, `packs/02-split-the-monolith.md`, `packs/03-rewrite-in-rust.md`, `packs/04-cache-stampede.md`, `packs/05-oom-in-prod.md` are inlined in **## Bundled skill files** at the end of this file. Resolve those references from that section instead of reading from disk.

# dots-engg

A 5-minute crucible for software engineers. You live through a realistic situation—debugging a weird outage, making an architecture call under deadline, or defending an engineering stance—then see how a Staff engineer would have worked **the exact same facts**.

## Flow

1. **Pick or generate a pack (before the first line of play):**
   - **Default (`/dots-engg`):** Pick a curated pack from `packs/` in this skill directory (avoid repeating one already played in this conversation; mix analysis, judgment, and opinion scenarios naturally without announcing the type).
   - **On demand (`/dots-engg <topic>` or `new`):** Generate a fresh pack and write it to `${TMPDIR:-/tmp}/dots-engg/<slug>.md` *before* starting. Play strictly from that file so facts never drift.
   - **Promote (`save`):** After a great generated run, offer to copy the temp pack into `packs/` in this skill directory so it becomes curated.

2. **Open (1 short message):**
   - Set the stakes, who is across the table (colleague, EM, VP, etc.), and the opening observation as a compact ASCII visual if it has data.
   - End with a natural prompt: *"Where do you want to start?"* or *"What do you want to check first?"*

3. **Investigate:**
   - Follow `experience.md`: one thing at a time, ASCII visuals for data, and redraw the `┌ board ──┐` whenever things shift.
   - **Hard rule — locked facts:** Never invent new clues, metrics, or root causes mid-run. If the user asks about something not in the pack, give a realistic non-clue (*"looks normal," "no data on that," "unchanged"*).
   - **Don't rush or spoil:** Let the user drive the pace. Never pull unasked dots, never connect the dots for them, and don't repeatedly ask *"are you ready to close?"* while they are still investigating.
   - If the user is spinning in circles after 4+ turns with no new dot, offer one light nudge in-character.

4. **Close (hard gate — never skip):**
   - Move to Close only when the user states their cause/call or says they're ready.
   - Show the empty closing frame (see `experience.md`) and **end your turn immediately**.
   - **Wait for the user's actual closing statement.** Never skip it, never pretend they posted it, and never output the Debrief in the same turn. If they ask a clarification before posting, answer it briefly in-character and wait again for their closing statement.

5. **Debrief (Your Run vs. Staff Simulation):**
   - Keep it scannable and cognitively light—short lines, white space, no walls of text.
   - **Side-by-side table:** Compare **Your Run** vs. **Staff Simulation** across the key phases/moves (`Phase | Your Run | Staff Simulation | Why It Matters`), strictly bound to **the exact same locked facts** (the Staff engineer cannot ask a question whose answer isn't supported by the pack). Keep cells crisp (1–2 lines).
   - **No hindsight shaming:** Never label reasonable triage or deeper RCA questions as "detours" or wasted turns. Frame differences around *sequencing* and *what unlocks the next decision*.
   - **Mitigation vs. root-cause ownership:** Distinguish what's needed for the **immediate call** (scoped to the closing prompt) from **follow-up root-cause fixes** (what an owner owns afterward), so deeper RCA instincts are recognized rather than penalized.
   - **Staff closing statement:** Show how the Staff engineer would close, in a short blockquote.
   - **The single shift & habit to steal:** 1–2 lines on the one move or framing shift that changed the most, plus one crisp **Habit to steal** in a blockquote.
   - **One Staff-level upgrade:** Give **one** non-trivial, concrete suggestion anchored in the user's actual run that would bring their attempt closer to Staff level (skip generic advice or trivial wording tweaks—target a high-leverage shift such as framing the binding constraint, choosing a discriminating check that rules out an entire branch, or owning second-order risk/alignment in the close). Keep it to 2–3 crisp lines: the exact moment in their run, what to do differently, and why it changes the leverage.
   - Do not give numeric scores or level grades unless the user explicitly asks.

## Pack format (for generated packs)

Write generated packs to `${TMPDIR:-/tmp}/dots-engg/<slug>.md` with:
- Title, internal situation model (`one-truth (analysis)` | `few-truths (judgment)` | `no-single-truth (opinion)`), role/stakes, and who is across the table
- Opening brief + initial dot(s)
- Locked facts / dots (each with what reveals it, plus 1–2 realistic red herrings or constraints)
- The underlying tension, root cause, or trade-off (kept hidden until debrief)
- Closing prompt

---

## Bundled skill files

The files below are bundled from the skill directory. Infer any relative file or directory references above (e.g. `experience.md`, `packs/`) from these sections instead of reading from disk.

<!-- BEGIN BUNDLED FILE: experience.md -->
### `experience.md`

# Experience

How a `dots-engg` session should feel. The pack decides *what* is true. This file decides *how it's lived*. The target feeling: **two engineers working through something real together**, where the user gets to be the one who connects it.

## Who is across the table

Whoever the pack names (colleague, EM, VP, senior teammate). **They only set the tone**: voice, mood, pressure. Everything else stays the same: they pull up whatever is asked for, nudges follow the nudge ladder, and the closing goes where the pack asks.

| Role | Tone |
|---|---|
| **colleague** (default) | peer on a call, casual, a little tense |
| **mentor** | calm, curious, no rush. Asks "why that?" now and then |
| **CTO / VP** | terse, busy, wants the bottom line |
| **hiring interviewer** | neutral and polite, gives nothing away |
| **service owner** | knows the system, a bit defensive about their service |

- **Voice:** a real person in that role. Short lines, a bit of texture (*"ugh, ok, pulling it up"*). Not a narrator, not a quiz host.
- **Quiet head.** They never do the thinking. When they pull data (dashboards, logs, docs, constraints), they say what they see, not what it means, unless the user already said it. Never summarize the full cause for the user before they close.
- **Reacts in character.** Agrees when the user is onto something (*"huh, yeah, that lines up"*), pushes back gently on a weak theory using a dot already on the table, never with a new one. Never says "correct" or "wrong".
- **Never lectures mid-game.** All teaching waits for the debrief.
- **One reply, one dot.** Never double-post or pull an unasked dot. Let the user drive the pace—don't nudge them to close while they're still asking questions.

## Reveal policy

| The user… | The interviewer… |
|---|---|
| asks something a dot answers | reveals that dot, in character, with its visual. One dot per answer unless the question clearly covers two |
| asks something close to a dot | reveals what they literally asked for. If the dot holds more, hints that there's more there (*"want me to split it by client?"*) |
| asks something no dot covers | *"haven't looked at that"* / *"don't think we have that"*. No invented facts, ever |
| asks for "everything" or "all dashboards" | offers a short menu of what they *could* pull (titles only, not content) and asks which one |
| floats a theory | reacts as a peer, then hands the next move back: *"how would we check that?"* |
| states a call / cause | asks for the closing statement (see **Closing**) |

## Nudges

Nudge only when the user is stuck: **3 turns with no new dot**, or circling on a red herring after the dot that rules it out is already on the table.

1. **First nudge:** a peer's wondering question pointing at the *kind* of thing to look at, not the dot (*"weird that it's just checkout… anything we haven't looked at?"*).
2. **Second nudge:** narrower, naming the area (*"are we sure the traffic is normal?"*).
3. **Third:** offer it outright: *"want me to just pull <dot title>?"* Only reveal it on a yes.

At most 3 nudges per session.

## Visuals & the board

ASCII visuals make the dots feel like opening a dashboard or reading a spec and take memory load off the user.

- **Dots:** reveal a dot with its visual (sparkline, bar, gauge, log snippet, table) in a code block. Keep the pack's numbers exact. You may redraw, but never change a value.
- **Evidence board:** every ~4 turns, or when the user asks *"where are we"*, redraw a small board of what's uncovered and how the user has linked it. Draw only the links the user made, with `?` for links they've floated but not proven. Never draw links the user hasn't made.

```
┌ board ──────────────────────────────────────────┐
│ [p99 2.4s ↑ 10:40] ──?── [inventory deploy]     │
│ [5xx ~flat]   [DB CPU 58%]                      │
└─────────────────────────────────────────────────┘
```

- Keep chat lines short. Visuals carry the data, words carry the conversation.

## Closing

The session ends with the user making a clear statement in their own words (an incident update in Slack, a recommendation to the EM, a call to the VP).

- Ask for it naturally, in their own voice: *"can you post the update? i'll back you up"*
- Show an empty message frame so it feels like posting:

```
┌ #checkout-incident ─────────────────────────────┐
│ you:                                            │
└─────────────────────────────────────────────────┘
```

- Don't coach the content or edit it. **Stop and wait for the user's actual closing message**—never simulate them posting it, and never start the debrief until they send it.
- If they ask a clarification before posting, answer it briefly in-character and wait again for their closing statement.
- If their closing statement is vague, ask one question (*"what are we doing about it?"*), then accept whatever they post.
- Once it's posted, react in one line and the debrief follows.

## Debrief

Make the debrief easy to scan after a 5-minute sprint—short blocks, clear structure, no walls of text:

1. **Comparison table first:** Use a compact `Phase | Your Run | Staff Simulation | Why It Matters` table (1–2 lines per cell) so the user can see the sequence side-by-side without re-reading paragraphs.
2. **No hindsight bias:** Standard triage (deploys, logs) and deeper RCA questions are good engineering instincts, not "detours." Compare *sequencing* (what unlocked the next decision fastest), not "extra steps."
3. **Separate immediate call from full ownership:** Call out what's needed for the **immediate call/mitigation** (what the pack's closing prompt scopes to) vs. **follow-up root-cause fixes** (what an owner owns afterward).
4. **Staff closing + one takeaway:** Show the Staff closing statement in a blockquote, 1–2 lines on the single highest-leverage shift, and one crisp **Habit to steal** blockquote.
5. **One Staff-level upgrade:** End with **one** non-trivial suggestion specific to the user's attempt—something that meaningfully moves their framing, investigation leverage, or closing ownership closer to Staff level (skip trivial polish or generic tips). Anchor it to a concrete moment in their run: *what they did → the higher-leverage move → why it matters* (2–3 lines max).

## Fairness & pacing

- **Fairness:** A chat window is narrower than a real investigation or design review. Never treat thoroughness as the measure—what counts is the quality of the questions and the clarity of the closing call. The Staff simulation plays under the same interface, so the comparison stays fair.
- **Pacing:** 1 to 4 lines of talk plus at most one visual per turn. No clock, no timer. The user should talk more than the interviewer.

## Situation models (internal — keep implicit)

Never expose these as flags or announce the type before/during play. Use them internally to shape generated packs and how the Staff simulation thinks:

- **One truth (analysis):** A single hidden cause to uncover (e.g., outage, latency spike, bug).
  - *Pack:* locks the root cause, a separating dot, and 1–2 plausible red herrings.
  - *Staff:* isolates variables, rules out red herrings early, and finds the separating dot.
- **Few truths (judgment on choices):** Competing options where the right call depends on binding constraints (e.g., architecture split, migration path).
  - *Pack:* locks the real costs, timeline, and coupling behind each option.
  - *Staff:* surfaces the binding constraint first rather than debating aesthetics, and picks the smallest move that solves the real pain.
- **No single truth (expert opinion):** No objectively right answer; what matters is framing, trade-off clarity, and owning the risk (e.g., rewrite vs. patch, tech-debt call).
  - *Pack:* locks the competing pressures, team realities, and why reasonable engineers disagree.
  - *Staff:* reframes away from the false binary, states what they are optimizing for, and owns the residual risk.
<!-- END BUNDLED FILE: experience.md -->

<!-- BEGIN BUNDLED FILE: packs/01-quiet-checkout.md -->
### `packs/01-quiet-checkout.md`

# 01 · Quiet checkout

- **Model (internal):** one-truth (analysis)
- **Role & stakes:** Backend engineer on-call. Tuesday 10:55 AM. Support has 40+ tickets saying "payment spinner forever." EM wants an update in `#checkout-incident` once you know what's happening.
- **Across the table:** Sam, a teammate on-call with you, pulling up dashboards and logs as you ask.

## Opening brief

> "Checkout p99 jumped from 180ms to 2.4s at 10:40. Weird part: 5xx is barely up (0.2% → 0.9%). Support is getting slammed with 'spinner forever' tickets. Where do you want to start?"

- **D1 (Opening):**
```
checkout-api p99 (last 2h)
2.4s  ┤              ╭──────
180ms ┤──────────────╯       p50: 40ms → 310ms
      └──────┬───────┬──────
           09:00   10:40
```

## Locked facts (reveal on ask)

- **Error rates (D2):** 2xx: 99.8% → 99.1%. 5xx: 0.2% → 0.9% (gateway 503 timeouts). 4xx flat.
- **Backend deploys (D3 — red herring):** `inventory-svc` deployed at 10:15 ("structured logging format"). `checkout-api` and `payments-gw` had no backend deploys today.
- **Inventory health (D4):** `inventory-svc` p99 is 41ms (was 38ms), errors 0.1% flat. `checkout → inventory` span is 45ms. Completely healthy.
- **Database metrics (D5):**
```
checkout-db       before   now
CPU               40%      58%
query p99         11ms     12ms
active conns      ~22      50 / 50 (pool max)
```
- **Connection pool (D6):** `checkout-api` DB pool: `[██████████] 50/50` — 48 threads queued (~2.1s wait).
- **Traffic & business volume (D7 — key turn):**
```
POST /checkout    3.4x normal (since 10:40)
completed orders  flat (-5%)
```
- **Client / traffic breakdown (D8 — root cause):** 92% of the extra `POST /checkout` traffic is from **iOS app v4.18.0** (released to 100% at 10:35). Same `idempotency_key` is being retried in a tight loop every 400ms when the payment sheet stalls on a client-side timeout.
- **Payments gateway (D9):** `payments-gw` latency is normal (120ms), not throttling.

## Hidden truth

iOS v4.18.0 (rolled out at 10:35) introduced an aggressive 400ms client retry loop on `POST /checkout`. Duplicate requests flooded `checkout-api`, saturating its 50-connection DB pool. DB queries themselves stayed fast (12ms), so the 2.1s latency was threads waiting on the pool.

## Closing prompt

Post a 2–4 line update for `#checkout-incident` covering what's happening, why, and what we're doing next.
<!-- END BUNDLED FILE: packs/01-quiet-checkout.md -->

<!-- BEGIN BUNDLED FILE: packs/02-split-the-monolith.md -->
### `packs/02-split-the-monolith.md`

# 02 · Split the monolith before Q4

- **Model (internal):** few-truths (judgment)
- **Role & stakes:** Senior engineer in a design review. Q4 peak launch is in 6 weeks. A teammate has proposed extracting `billing` out of the core monolith into its own microservice "so deploys stop breaking checkout."
- **Across the table:** Priya, the Engineering Manager, deciding whether to greenlight the 4-week extraction sprint starting Monday.

## Opening brief

> "The team is exhausted from deploy freezes—two of the last three billing deploys broke checkout. Extracting billing into its own service feels like the cleanest fix before Q4. What do you want to look at before we call it?"

- **D1 (Opening):** Proposal: extract `billing` module into `billing-svc` (estimated 4 weeks, 3 engineers) to stop billing changes from breaking checkout.

## Locked facts (reveal on ask)

- **Why the last 3 incidents happened (D2 — key turn):**
```
incident #1  billing migration added NOT NULL to shared `orders`
incident #2  billing changed return type of helper called by checkout
incident #3  unrelated deploy failed CI (flaky billing test)
```
- **Database coupling (D3):** `billing` and `checkout` both read/write the `orders` and `users` tables in the same Postgres instance. Extracting the service *without* splitting the DB means either cross-service DB writes or building a new internal API + dual-write sync.
- **Test & CI setup (D4):** There are no module boundary checks or contract tests between `billing` and `checkout`. All tests run in one 28-minute suite.
- **Team & timeline (D5):** 6 weeks to Q4 freeze. The 3 engineers proposed for extraction are the same 3 who own Q4 checkout promo features (which aren't done yet).
- **Deploy frequency & infra (D6):** Team deploys ~4 times/week. They have no service mesh, no distributed tracing, and no dedicated on-call rotation for a second service.
- **Alternative effort (D7):** Enforcing a modular boundary (lint/import rules + contract tests + separate migration review for `orders`) takes ~3–4 days.

## Hidden tension

The pain is real (coupled deploys), but extracting a microservice in 4 weeks before Q4 swaps a *code coupling* problem for a *distributed systems + shared DB* problem—while starving Q4 features and adding operational overhead. Modular boundaries + migration guards solve 90% of the actual incidents in 4 days.

## Closing prompt

Give Priya a 2–4 line recommendation on whether to extract now, what to do instead, and why.
<!-- END BUNDLED FILE: packs/02-split-the-monolith.md -->

<!-- BEGIN BUNDLED FILE: packs/03-rewrite-in-rust.md -->
### `packs/03-rewrite-in-rust.md`

# 03 · Rewrite the worker in Rust

- **Model (internal):** no-single-truth (opinion)
- **Role & stakes:** Tech lead / senior engineer in an architecture sync. Last week the Python `event-ingestor` worker OOM-killed twice during a traffic burst, dropping ~12k analytics events. A strong senior engineer has a working Rust prototype and is pushing to replace the Python worker.
- **Across the table:** Alex, the senior engineer with the Rust prototype, and Maya, the VP of Engineering listening in.

## Opening brief

> "Alex has a Rust prototype of `event-ingestor` that uses 18MB of RAM instead of 512MB. Given last week's OOMs, he thinks we should swap it in this sprint. Maya's asking for your take—what do you want to dig into?"

- **D1 (Opening):** Python `event-ingestor` hit 512MB limit and OOM-killed twice last week. Rust prototype runs in 18MB.

## Locked facts (reveal on ask)

- **Why Python OOM-killed (D2 — key turn):** The worker pulls messages from Kafka and buffers them in memory until a 10MB batch is reached—except there is **no max message count or memory cap** when payloads are compressed/nested JSON, and no backpressure on the consumer. During a burst of large payloads, a single in-flight batch spiked to 600MB.
- **Normal throughput & headroom (D3):**
```
avg: 400 evt/s   peak: 1,800 evt/s   SLA: <30s (async)
Python CPU at peak: ~22%
```
- **Container & infra (D4):** Fargate 512MB × 2 replicas. Bumping to 1GB or capping batch size in Python is a 1-day change.
- **Team & Rust ownership (D5):**
```
backend team (14)   Python: 14/14   Rust prod-ready: 1 (Alex)
shared libs         Kafka wrapper · DLQ · observability (Python only)
```
- **Prototype gaps (D6):** Alex's Rust prototype handles the happy path. It does not yet have the team's schema validation, dead-letter queue logic, Datadog metrics, or graceful SIGTERM drain.
- **Alex's motivation (D7):** Alex is genuinely trying to prevent another page—and is also excited to use Rust in production.

## Hidden tension

The OOM wasn't a "Python is too slow/heavy" problem—it was an unbounded buffer + missing backpressure problem. Shipping a Rust service with 1 owner and missing DLQ/observability trades a 1-day bugfix for a long-term bus-factor and maintenance tax.

## Closing prompt

Give Alex and Maya a clear 2–4 line call on the Rust rewrite, what we should ship this week, and how to handle the prototype.
<!-- END BUNDLED FILE: packs/03-rewrite-in-rust.md -->

<!-- BEGIN BUNDLED FILE: packs/04-cache-stampede.md -->
### `packs/04-cache-stampede.md`

# 04 · Healthy cache, melting DB

- **Model (internal):** one-truth (analysis)
- **Role & stakes:** Backend engineer on-call. Wednesday 2:10 PM. `feed-service` p99 is spiking in waves every few minutes, and primary Postgres CPU is pegged at 91%.
- **Across the table:** Dana, a teammate on the platform team, sharing metrics and logs.

## Opening brief

> "Primary DB CPU just hit 91% and `feed-service` p99 jumped from 25ms to 1.8s. Weird thing is Redis looks super healthy—hit rate is 97.8%. Where do you want to look?"

- **D1 (Opening):**
```
feed-service p99 (last 30m)
1.8s ┤     ╭╮       ╭╮       ╭╮
25ms ┤─────╯╰───────╯╰───────╯╰──   spikes every ~5m, DB CPU hits 91%
     └────────────────────────────
```

## Locked facts (reveal on ask)

- **Redis health (D2 — red herring):** Redis CPU 18%, p99 latency 0.8ms, hit rate **97.8%**, evictions 0.
- **Recent deploys (D3):** `feed-service` deployed yesterday ("cleaned up cache helper"). No DB schema or query changes this week.
- **Traffic & RPS (D4):** Overall RPS is completely flat (~3,200 req/s). No spike in incoming traffic.
- **DB slow queries / `pg_stat_activity` (D5 — key turn):**
```
during spike: 380 active connections running the SAME query:
SELECT * FROM feed_items WHERE org_id = 42 ORDER BY created_at DESC LIMIT 50
(query time normally 4ms → 420ms under lock/CPU contention)
```
- **Tenant & cache key check (D6):** `org_id = 42` is the largest enterprise tenant (~35% of all feed reads). Its cache key `feed:org:42` has a **5-minute TTL**.
- **Cache helper diff / `singleflight` (D7 — root cause):** Yesterday's cache helper cleanup accidentally removed `singleflight.Do` around cache misses. Every 5 minutes when `feed:org:42` expires, ~380 concurrent requests miss at once and all hit Postgres simultaneously (cache stampede).
- **Other tenants (D8):** All other `org_id` queries are fast and normal.

## Hidden truth

A 97.8% overall Redis hit rate hid a hot-key cache stampede. Yesterday's refactor dropped `singleflight` coalescing on cache misses, so every 5 minutes when `feed:org:42` expires, hundreds of concurrent requests stampede Postgres with the exact same query.

## Closing prompt

Post a 2–4 line update in `#incidents` explaining why the DB is spiking in 5-minute waves and what we're shipping right now.
<!-- END BUNDLED FILE: packs/04-cache-stampede.md -->

<!-- BEGIN BUNDLED FILE: packs/05-oom-in-prod.md -->
### `packs/05-oom-in-prod.md`

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
<!-- END BUNDLED FILE: packs/05-oom-in-prod.md -->
