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
