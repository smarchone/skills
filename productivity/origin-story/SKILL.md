---
name: origin-story
description: Tells the origin story of a technology, company, or idea for a curious senior engineer — the world before it, the concrete problem that forced it, what inspired it, who failed before, the duct-tape v0.1, its core mental model and guarantees, key design decisions, and where it fits in the ecosystem. Use when the user asks how something came to be, "origin story of X", "why does X exist", "history of X", "how was X born", or "what problem did X solve". On "more", serves the add-on (timeline and key people, evolution, major incidents and lessons).
user-invocable: true
disable-model-invocation: true
---

# Origin Story

Explain how a technology, company, or idea came into the world, for a **curious senior engineer**.

## Reader and voice

- The reader is senior. Don't define basics (what a database, a hash, or a VC is). Explain only what's specific to the subject.
- Keep it dense and skimmable: short bullets, tables where you're comparing, and one idea per line. No throat-clearing, no hype adjectives, no "In today's fast-paced world".
- Be concrete over abstract. Use names, numbers, dates, versions, and real quotes.
- Each section should fit on about one screen. The whole core should be a 5–7 minute read.
- Honesty rules:
  - Never invent quotes. Use real ones (mailing-list posts, papers, talks, commits) and name the source inline.
  - If you dramatize a conversation or scene to tell the story, label it *(reconstructed)*.
  - If accounts conflict or it's a known origin myth, say *(disputed)* and give the more credible version in one line.
  - If you don't know something, say so briefly rather than filling the gap.

## Adapt to the subject

- **Technology or tool** (Kafka, Git, React): lean on the mental model, guarantees, and design decisions.
- **Company** (Stripe, Figma): lean on the problem, the v0.1, why then, and market fit. The "mental model" becomes the core insight or business model.
- **Idea or concept** (MapReduce, CRDTs, public-key crypto): lean on inspiration, failed attempts, and the core model.

Drop a section, or shrink it to one line, if it genuinely doesn't apply. Don't pad.

## Core output (default)

Use this structure and order.

```
# <Subject> — origin story
<one line: what it is> · <year born> · <creator(s) / org>

## TL;DR
- **Pitch:** "Wouldn't it be interesting if …?" (ideas/tech)  — or a 1-line STAR (companies/events)
- **Aha:** the one sentence the reader should walk away with

## Before → After
| Before (how the world coped)        | After (what it made possible)       |
|-------------------------------------|-------------------------------------|
| workaround + its cost               | concrete change, with evidence      |
(3–5 rows)

## The problem that forced it
A short story or conversation (5–12 lines): who hit what wall, when, and why the
existing options broke. Name the real people, systems, and numbers.

## Lineage
- **Borrowed from:** earlier ideas, papers, people, or fields it stood on
- **Tried before:** prior attempts → why they failed (timing / hardware / economics / ergonomics) → lesson
- **Why then:** what changed that made it possible at that moment

## v0.1 — the duct-tape version
What the first hacky version looked like: size, stack, what was faked or
hard-coded, what was cut, first users, and how long it took to build.

## Mental model
- **Core abstractions:** the 3–5 concepts that explain 80% of it
- **Guarantees:** what it promises
- **Non-guarantees:** what it deliberately doesn't do (and the trade-off bought)
- **Think of it as:** one analogy or model a senior engineer can reason with

## Key design decisions
| Chose | Over | Because |
|-------|------|---------|
(3–5 rows: the forks in the road that shaped it)

## Where it fits
A small ASCII map or list: upstream, downstream, competitors / alternatives,
what it replaced, and what's now built on top of it.

---
*Say **more** for: timeline & key people · evolution · major incidents & lessons.*
```

## Add-on (only when the user says "more")

Don't repeat the core. Serve all three add-on sections below unless the user asks for one specifically.

```
## Timeline & key people
| When | What happened | Who |
(5–8 rows: only the moments that changed its trajectory)

## Evolution
- **v1 vs today:** what's radically different
- **Pivots:** the turns it took and why
- **Regrets:** what the creators later said they'd do differently (quote if real)

## Major incidents & lessons
| Incident (date) | What happened | Lesson |
(outages, breaches, forks, lawsuits, community splits — 3–5 rows)
```
