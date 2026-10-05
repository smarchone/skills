---
name: feel
description: Builds a lived-in feel for how a system, tool, platform, or SaaS behaves at a given scale or during a given operation — simulated scenes with concrete numbers, for a senior engineer.
user-invocable: true
disable-model-invocation: true
---

# Feel

Give a **curious senior engineer** the felt experience of a situation they haven't lived through:
what it *feels like* to scale a service from 100 to 10K RPS, partition a live billion-row table,
run Kafka at 1M msgs/s, or get the first big Snowflake bill. Afterwards they should be able to
recall "10K RPS" the way an operator does: the dashboards, the pod count, the GC line, the page
at 3 a.m., the cost.
Scope: situations and operations. For how a concept works, point to `/intuition`; for a company's
history, `/evolve`; for who uses a tool, `/adoption`.

## Voice & Style
- **Audience:** Senior. Skip basics. They know what GC is; they don't know what it *looks like* at this scale.
- **Format:** Scenes, dashboards, artifacts (log lines, command output, Slack messages). Skimmable.
- **Tone:** Concrete: instance types, versions, counts, ms, GB, $/month. No hype, no generic advice.
- **Length:** 8-12 min read.

## Step 1: Pin the situation
- Situation is vague ("what does scale feel like") → ask for one: the system, the from → to, or the operation.
- Stack unstated → pick a common one and state it in the setup (e.g. Go 1.23 on EKS, c7g.2xlarge,
  Postgres 16 on RDS, Redis). The user can swap it. Don't ask unless the choice changes the answer.
- Fix the workload shape that drives every number: payload size, read/write mix, p99 target,
  downstream fan-out, traffic curve (peak ÷ avg). Write these down; everything else derives from them.

## Integrity
- It's a simulation, and the numbers must be **plausible and consistent with each other**. Derive
  them; don't decorate with them. Check against:
  - Little's law: in-flight = RPS × latency → goroutines, threads, DB connections.
  - Alloc rate = RPS × bytes/request → heap growth → GC frequency and GC CPU.
  - Capacity: cores = RPS × CPU-ms/request ÷ target utilization → pods → nodes → $.
  - Rows × row size → table GB; ÷ throughput → hours to backfill; WAL/replication volume follows.
- Show the derivation for the key numbers (one line: `10K rps × 40ms = 400 in flight`), so the
  reader can re-derive them in their head later. That's the part that sticks.
- Tool-specific behavior (Postgres lock levels, Kafka rebalance, Go GC pacer, vendor limits) must be
  real. Unsure → mark *(unverified)* or leave it out. Pricing carries a year: "~$0.045/GB NAT (2025)".
- Characters, companies, and incidents are invented. Don't attach them to real companies.

## Step 2: Write it
The experience is carried by **scenes**, not explanation. Each scene is a moment where the scale or
the operation makes itself felt: a page, a dashboard that looks wrong, a design review, a cutover.

**Scene rules:**
- Named people with roles (on-call SRE, staff eng, DBA, EM, finance). ~6-12 turns. Every turn carries
  an observation, a number, or a decision. Cut pleasantries.
- Put real-looking artifacts on the page: a `gctrace` line, `pg_stat_activity` rows, `kubectl top`,
  a Grafana panel read out, a Slack alert, the AWS bill line. The reader should see what the operator saw.
- At least one **wrong hypothesis** per incident scene, and why it's wrong. That's how the system is learned.
- At least one **surprise** across the piece: the thing nobody planned for at this scale
  (conntrack full, DNS QPS, ephemeral ports, log bill, NAT cost, autovacuum, rebalance storm).
- End each scene with what changed, and what it cost.

## Output
Use this structure and order:

````text
# What <situation> feels like
<1-line: from → to, or the operation> · <stack> · <timeline, e.g. "6 weeks" or "one Saturday night">

## Setup
| Assumption | Value |
|------------|-------|
(5-8 rows: stack, instance type, payload, read/write mix, p99 target, fan-out, peak ÷ avg.
Everything below derives from these.)

## The Dashboard
| Metric | <state A, e.g. 100 RPS> | <B, e.g. 1K> | <C, e.g. 10K> |
|--------|------|------|------|
(10-15 rows across layers: pods/nodes, CPU, in-flight / goroutines, heap, GC cycles/s and GC CPU %,
DB connections and QPS, cache hit %, p50/p99, network, log volume/day, $/month, pages/week.
For an operation (migration, partitioning), columns are phases instead: before · during · cutover · after,
with rows like rows copied/s, replication lag, WAL GB/h, lock waits, disk, ETA.)
Key derivations:
- `<metric> = <formula> = <number>` (3-5 lines)

## Scenes
### <T+time> · <scene name>
<1-2 lines of setting: where we are, what's on screen>
```
<artifact: log line / command output / alert / panel>
```
**<Name> (<role>):** …
**<Name> (<role>):** …
**What changed:** … · **Cost:** …

(4-6 scenes in time order; each at a different layer or moment. Build toward the hardest one.)

## What it feels like
- **You stop caring about:** … (things that mattered at the smaller scale)
- **You start caring about:** …
- **Slow now:** … (deploys, rollbacks, schema changes, cache warm-up)
- **A 1% regression now means:** … (in cores, $, or pages)
(4-6 bullets. Sensory: what a veteran would say to someone about to live through it.)

## Recall card
```
<situation> in ~8 lines: the numbers worth memorizing,
the tell that you've arrived, the thing that bites first.
```
````

## Follow-ups
Offer 2-3 next steps: the next order of magnitude, the same situation on a different stack, or
zooming into one scene ("replay the cutover minute by minute").
