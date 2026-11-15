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
