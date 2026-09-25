---
name: adoption
description: Shows how a tool or system is used across companies — grouped by usage pattern, how it fits each backend, and who moved off it — for a senior engineer.
user-invocable: true
disable-model-invocation: true
---

# Adoption

Show how a **tool or system** is used in the real world, for a **curious senior engineer**: the distinct roles it plays, where it sits in each company's backend, and where it stops fitting.
Scope: tools and systems only. For how it was born, point to `/origin-story`; for how it changed over time, `/evolve`.

## Voice & Style
- **Audience:** Senior. Skip basics; explain specifics.
- **Format:** Brief. Tables, one line per company, ASCII per pattern. No fluff/hype.
- **Tone:** Concrete (company names, numbers, versions).
- **Length:** 4-6 min read.

## Integrity
- Default: answer from knowledge. Include only publicly known usages (engineering blogs, talks, papers). Unsure → mark *(unverified)* or drop it. Don't invent companies, numbers, or dates.
- Scale numbers always carry a year: "~1T msgs/day (2019)".
- Conflicting accounts → *(disputed)*, give the more credible version.

## Research (optional)
Run only when the user asks ("research", "grounded") or the tool is niche/new (then offer first). Budget ~8-12 searches/fetches.
- **Source priority:**
  1. Engineering blogs and conference talks by the company itself.
  2. Papers, case studies, vendor customer stories (treat vendor numbers as claims).
- Verify numbers against the primary source, not search snippets. Research grounds the content; don't add citations.

## Rules
- **At least 10 company instances** across all patterns. Fewer known → say so; don't pad.
- **Group by usage pattern** (the role the tool plays), not by company. 3-5 patterns.
- **One ASCII sketch per pattern** (≤ 6 lines), showing where the tool sits between neighbors. Not per company.
- A company with two distinct roles may appear under two patterns.

## Output
Use this structure and order:

````text
# <Tool> — adoption
<1-line what it is> · <N instances across M patterns>

## Pattern 1: <role, e.g. CDC backbone>
```
[OLTP DB] ──CDC──> [<Tool>] ──> [search | cache | warehouse]
```
| Company | How it fits | Scale (year) | Replaced / why chosen |
|---------|-------------|--------------|-----------------------|
(2-4 rows, one line each)

## Pattern 2: …

## Moved Off
| Company | Moved to | Why |
|---------|----------|-----|
(1-3 rows; skip if none known)

## Takeaway
- **Sweet spot:** where it fits best, in one line.
- **Stops fitting when:** the pressure that pushes teams off it.
````
