# Slow checkout, quiet errors

role: backend engineer (L2–L3) · domain: e-commerce checkout service · type: one-truth (RCA)

## Stakes

- **Default interviewer:** Sam, a colleague: a backend engineer on the same team, on-call with you today. Sam knows the
  checkout system well and has dashboard, log and trace access, but hasn't dug into this yet. Sam is
  pulling up whatever you ask for.
- **Pressure:** it's 10:55 on a Tuesday. Support tickets about a slow checkout are climbing. The eng
  manager has asked for an update in #checkout-incident "when you have something". Mood: focused, a
  little tense, not panicked.
- **Tone:** two peers on a call. Sam is friendly and quick, and says "I don't know" honestly.
- **Closing:** post an update in #checkout-incident covering what's happening, why, and what we're doing
  about it. The eng manager and support will read it.
- **The opening brief below is Sam's.** For another interviewer, keep its facts (D1, the 10:40 start, the
  tickets) and retell it in their tone.

## Situation

> hey, thanks for jumping on. checkout's been slow since ~10:40. p99 went from like 180ms to over 2
> seconds. weird thing is errors are barely up. support has ~40 tickets saying "payment spinner forever".
> i've only looked at the latency graph so far. where do you want to start?

## Dots

### D1 · Checkout latency · reveal: opening
Reached by: the opening brief.
```
checkout-api latency (p50 / p99), last 2h
p99 2.4s ┤                    ╭────────
         │                    │
p99 180ms┤────────────────────╯         p50: 40ms → 310ms
         └──────┬─────────────┬────────
              09:00        10:40
```

### D2 · Error rates · reveal: on-ask
Reached by: errors, 5xx, status codes, failures.
```
checkout-api responses     before    now
2xx                        99.8%     99.1%
5xx                         0.2%      0.9%   (mostly 503 "upstream timeout" at gateway)
4xx                         flat      flat
```
Sam: "so mostly it's just… slow. not failing much."

### D3 · Deploys today · reveal: on-ask
Reached by: deploys, what changed, recent changes, releases (backend).
```
10:15  inventory-svc  v2.31  "structured logging format"   ✓ healthy
--     checkout-api   no deploy since Monday
--     payments-gw    no deploy this week
```
Sam: "only inventory shipped. checkout calls inventory to reserve stock, so… maybe?"
*(This is the red herring. Only backend deploys are on this list. Mobile releases are tracked
elsewhere, see D8.)*

### D4 · Inventory service health · reveal: on-ask
Reached by: inventory latency, inventory errors, checking the inventory deploy.
```
inventory-svc  p99   38ms → 41ms     errors 0.1% flat
checkout → inventory call span p99: 45ms (unchanged)
```
Sam: "inventory looks totally fine actually."

### D5 · Database metrics · reveal: on-ask
Reached by: DB, database, CPU, queries, slow queries.
```
checkout-db (postgres)        before    now
CPU                            40%      58%
query p99                      11ms     12ms
active connections             ~22      50 (= checkout pool max)
```
Sam: "queries aren't slower. but connections are pinned at 50."

### D6 · Connection pool · reveal: on-ask
Reached by: connection pool, pool, threads, waiting, saturation; or following up on D5's connections.
```
checkout-api db pool (max 50)
in use   ██████████████████████████ 50/50   since 10:41
waiting  180 requests queued
acquire wait p99: 1.9s
```

### D7 · Request rate vs orders · reveal: nudge
Reached by: traffic, RPS, request rate, load, "is traffic up", orders, business metrics.
```
                    09:00–10:30    now
checkout RPS          ~400        ~680    ▲ 1.7x
orders / sec          ~364        ~370    ─ flat
```
Sam: "huh. way more requests, same number of orders."
*(The separating dot. The load is not real demand.)*

### D8 · Traffic by client · reveal: nudge
Reached by: splitting traffic by client, platform, app version or user agent; asking who is sending
the extra requests; asking about mobile or client releases.
```
checkout RPS by client       before    now     requests per order
web                           100      102          1.1
android 6.x                    80       82          1.1
iOS 4.11                      220      112          1.1
iOS 4.12                        0      384          3.8   ◀
```
Sam: "iOS is most of our checkout traffic. 4.12 is the new release. rollout went 20% → 50% at 10:35, i saw it in #mobile."

### D9 · iOS 4.12 release notes · reveal: on-ask (after D8 or when asking about mobile changes)
Reached by: 4.12 changes, mobile release notes, what changed in the app, retry policy.
```
iOS 4.12 — migrated to new networking layer (NetKit 3)
  • request timeout: 1.0s
  • retry on timeout: up to 3 times, immediate (no backoff)
  • staged rollout: 20% @ 10:00 → 50% @ 10:35
```

### D10 · Checkout logs · reveal: on-ask
Reached by: logs, warnings, exceptions, grep, access logs, idempotency keys.
```
10:47:12 WARN  Timeout acquiring connection from pool after 2000ms
10:47:12 WARN  Timeout acquiring connection from pool after 2000ms
10:47:13 INFO  POST /checkout idem=7f3a.. ua=iOS/4.12  2310ms
10:47:14 INFO  POST /checkout idem=7f3a.. ua=iOS/4.12  2280ms
10:47:15 INFO  POST /checkout idem=7f3a.. ua=iOS/4.12  2405ms
```
Sam: "same idempotency key three times in a row. that's one person's checkout."

### D11 · A slow trace · reveal: on-ask
Reached by: traces, tracing, a slow request, spans, where the time goes.
```
POST /checkout  2.31s
├─ auth                     4ms
├─ db.pool.acquire       1,920ms  ◀
├─ db.query (order)        12ms
├─ inventory.reserve       44ms
└─ payments.authorize     210ms
```

## Hidden connection

```
iOS 4.12 rollout to 50% (10:35)
  └─▶ new client: 1.0s timeout, 3 immediate retries, no backoff          [D8, D9]
        └─▶ each slow checkout becomes up to 4 requests                   [D10]
              └─▶ checkout RPS 1.7x while orders stay flat                 [D7]
                    └─▶ DB pool (50) saturated, requests wait ~1.9s        [D5, D6, D11]
                          └─▶ p99 2.4s > the client's 1.0s timeout → more retries
                                └─▶ feedback loop (a retry storm)          [D1]
```

- **Why 10:40, not 10:00:** at 20% rollout the pool still had headroom. At 50% the extra load
  tipped it into saturation, and from there the retries fed themselves.

- **Root cause:** a client retry policy (immediate retries, no backoff, timeout below server latency)
  amplifying load into a saturated connection pool, which feeds back on itself.
- **Mechanism vs cause:** pool saturation is the *mechanism*. The iOS 4.12 retry policy is the *cause*.
  Stopping at "pool is full, raise the pool size" is the classic L3 miss. It would push more load onto
  the DB and doesn't stop the storm.
- **Red herrings:** the inventory deploy (D3, ruled out by D4); DB CPU up (D5, a symptom of more
  load: query latency is flat).
- **Good mitigation:** pause or roll back the 4.12 rollout, or remote-config the client retries off.
  Optionally rate-limit or dedupe by idempotency key at the gateway. Long-term: backoff with jitter,
  a retry budget, and a client timeout above server p99.

## Level traits

- **L3:** starts from the service's own symptoms: errors (D2), then deploys (D3), and gets pulled
  toward the inventory deploy and checks it (D4). Goes to the DB (D5), finds the pool full (D6) and
  wants to raise the pool size. Needs a nudge ("why is the pool full, though?") to look at traffic
  (D7, D8). About 9 questions. First question: "what are the errors?"
- **L5:** looks at the shape first: slow but not failing means waiting, not breaking. Goes to traces or
  the pool (D11/D6), then asks the key question, "is load actually up, and is it real?" (D7). Splits by
  client (D8), reads the release notes (D9). About 5 questions. First question: "where's the time going
  in a slow request?"
- **Staff:** opens with "what changed anywhere that touches checkout today, including clients?" and
  "is traffic up?" in the same breath (D7). Goes straight to D8 → D9 and calls it a retry storm.
  **Proposes mitigation before full proof** ("let's pause the 4.12 rollout now, cheap and reversible,
  and confirm with logs while it drains"), then confirms with D10. About 3 questions. First question:
  "what changed — including mobile?"

## Grader

Two axes, graded separately and never blended.

**Competence:** did you work out what happened?

| Dimension | L3 | L5 | Staff |
|---|---|---|---|
| **Mechanism**: found the pool saturation / waiting | found it, maybe late | found it early via shape or traces | inferred it, confirmed quickly |
| **Cause**: got past mechanism to the retry amplification from iOS 4.12 | stopped at the pool, or needed nudges | found it via traffic → client split | went there first |
| **Evidence**: linked cause to effect with dots, not vibes | partial chain | full chain (D7/D8 + D6) | full chain + the feedback loop |
| **Red herrings**: dismissed with evidence | chased inventory, eventually dropped it | checked it once with D4, moved on | skipped it, or ruled it out in one line |
| **Efficiency**: questions to the cause, nudges used | 8+ or 2+ nudges | 4–7, ≤1 nudge | ≤4, no nudges |

**Conduct:** did you handle the situation?

| Dimension | L3 | L5 | Staff |
|---|---|---|---|
| **Mitigation**: proposed a safe, reversible action | "raise the pool size" (harmful) | roll back 4.12 | pause the rollout first, prove second, plus dedupe at gateway |
| **Closing update**: clear to the manager and support | symptom + guess ("DB pool is full, investigating") | cause + evidence + action | cause, action already taken, impact, next update time, in a few lines |

**Habit to steal:** when load goes up but the business doesn't, the traffic is lying. Find who's
sending the extra requests.

Alternate, if the user found the cause but went after the mechanism first: **"ask what changed, and
include the callers, not just your service."** If the user proved everything but never mitigated:
**"stop the bleeding before you finish the proof."**
