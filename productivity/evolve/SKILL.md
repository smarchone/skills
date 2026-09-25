---
name: evolve
description: Traces how a company or system evolved — business - tech, and each architecture shift as a before → after picture, for a senior engineer.
user-invocable: true
disable-model-invocation: true
---

# Evolve

Explain how a **company or system** grew after birth, for a **curious senior engineer**: how the business and the tech shaped each other, and how the architecture changed, one before → after picture per shift.
Scope: companies and systems only. For an idea or concept, say it's out of scope. For how something was born, point to `/origin-story`.

## Voice & Style
- **Audience:** Senior. Skip basics; explain specifics.
- **Format:** Dense, skimmable, bullets, tables. One idea/line. No fluff/hype.
- **Tone:** Concrete (names, dates, versions, numbers).
- **Length:** 6-10 min read. Sketches carry the picture; keep prose and tables lean.

## Integrity
- Default: answer from knowledge. Unsure of a claim → mark *(unverified)* or drop it. Don't invent numbers or dates.
- Scale numbers always carry a year: "~1B users (2023)".
- Conflicting accounts → *(disputed)*, give the more credible version.

## Research (optional)
Run only when the user asks ("research", "grounded") or the subject is obscure/fast-moving (then offer first). Budget ~8-12 searches/fetches.
- **Source priority:**
  1. Engineering blogs (migration/rewrite posts, architecture overviews), papers, postmortems.
  2. Conference talks (QCon, Strange Loop, re:Invent, etc.).
  3. SEC filings, shareholder letters (revenue, business model).
- Verify numbers against the primary source, not search snippets. Research grounds the content; don't add citations.

## Subject Focus
- **Company:** Lean on business ↔ tech and how the architecture followed the business.
- **System** (Kafka, Kubernetes): Lean on architecture evolution. Business ↔ tech covers who funds/sells it (vendor, foundation, cloud offerings); skip revenue if none.
*Drop or shrink irrelevant sections. No padding.*

## Output
Use this structure and order:

````text
# <Subject> — evolution
<1-line what it is today> · <scale (year)> · <age / founded>

## Business ↔ Tech
- **End solution:** What customers actually get or pay for.
- **Revenue model:** Who pays, for what, how it scales. (Skip if N/A.)
| Business need | Tech answer |
|---------------|-------------|
(3-5 rows: the technical bets the business depends on)

## Architecture Evolution
<era> → <era> → … (one-line strip of all shifts)

### <year(s)> · <shift name> (<from> → <to>)
**Forced by:** the pressure (scale, cost, latency, freshness, product, org, failure), with a number.
```
BEFORE
  ASCII sketch: boxes + arrows, ≤ 10 lines
AFTER
  same layout; mark changed parts with *…*
```
| | Before | After |
|---|---|---|
| <component> | … | … |
(2-3 rows: what the sketch can't show — the metric that moved (freshness, latency, cost, scale)
and any key number. Don't repeat what the sketch already shows.)
**Trade-off:** what got harder, or the new bottleneck (→ which forces the next shift).

(One block per shift. Complete: founding → today, no gaps; each "After" is the next "Before".
Cover every major layer (storage, processing, serving) across the timeline; a layer that appears
in an After must have appeared in some Before. If the history is too broad, keep only major shifts, ~5-8 blocks.)
````
