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
