---
name: origin-story
description: Tells the origin story of a technology, company, or idea for a curious senior engineer — the world before it, the concrete problem that forced it, what inspired it, who failed before, the duct-tape v0.1, its core mental model and guarantees, key design decisions, and where it fits in the ecosystem. Use when the user asks how something came to be, "origin story of X", "why does X exist", "history of X", "how was X born", or "what problem did X solve". On "more", serves the add-on (timeline and key people, evolution, major incidents and lessons).
user-invocable: true
disable-model-invocation: true
---

# Origin Story

Explain how a tech, company, or idea came to be, for a **curious senior engineer**.

## Voice & Style
- **Audience:** Senior. Skip basics; explain specifics.
- **Format:** Dense, skimmable, bullets, tables. One idea/line. No fluff/hype.
- **Tone:** Concrete (names, dates, versions, real quotes).
- **Length:** Core = 5-7 min read, ~1 screen/section.
- **Integrity:**
  - Real quotes only, with inline sources.
  - Mark dramatizations as *(reconstructed)*.
  - Mark conflicting accounts as *(disputed)* and give credible version.
  - Acknowledge unknowns briefly; don't guess.

## Subject Focus
- **Tech/Tool:** Emphasize mental model, guarantees, design decisions.
- **Company:** Emphasize problem, v0.1, timing, market fit (core insight + business model = mental model).
- **Idea/Concept:** Emphasize inspiration, failed attempts, core model.
*Drop or shrink irrelevant sections. No padding.*

## Default Output
Use this structure and order:

```text
# <Subject> — origin story
<1-line what it is> · <year> · <creator/org>

## TL;DR
- **Pitch:** "Wouldn't it be interesting if…" or 1-line STAR.
- **Aha:** Core takeaway sentence.

## Before → After
| Before (how the world coped) | After (what it made possible) |
|------------------------------|-------------------------------|
(3-5 rows of workaround cost vs concrete change)

## The Catalyst Problem
Brief story (5-12 lines): who hit what wall, when, why existing options failed. Use real names/numbers.

## Lineage
- **Borrowed from:** Prior ideas/fields.
- **Tried before:** Past failures → why (timing/tech/econ) → lesson.
- **Why then:** The shift making it possible now.

## v0.1 (Duct-Tape)
First hacky version: size, stack, faked parts, initial users, build time.

## Mental Model
- **Abstractions:** 3-5 concepts explaining 80%.
- **Guarantees:** What it promises.
- **Non-guarantees:** What it deliberately doesn't do → trade-off bought.
- **Think of it as:** 1 analogy for seniors.

## Key Design Decisions
| Chose | Over | Because |
|-------|------|---------|
(3-5 forks in the road)

## Ecosystem Fit
ASCII map/list: upstream, downstream, competitors, replaced tech, built on top.

---
*Say **more** for: timeline & key people · evolution · major incidents & lessons.*
```

## Add-on (on "more")
Serve all three sections unless specifically requested otherwise. Don't repeat the core.

```text
## Timeline & Key People
| When | What happened | Who |
(5-8 trajectory-changing moments)

## Evolution
- **v1 vs today:** Radical changes.
- **Pivots:** Turns taken and why.
- **Regrets:** Creators' hindsight (real quotes).

## Incidents & Lessons
| Incident (date) | What happened | Lesson |
(3-5 outages, breaches, forks, etc.)
```
