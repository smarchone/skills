---
name: idea-attack
user-invocable: true
disable-model-invocation: true
description: >-
  Attacks an idea's assumptions and proposed approaches, websearches for prior art,
  hunts failure modes, and returns effort-value suggestions
---

# Idea Attack

Pressure-test an idea. Report only what you actually find — an empty lens is fine, and a manufactured
weakness wastes the user's time. You attack to strengthen, not to win.

## Move 0 — Attack

- **Assumptions** — what must be true but is never said. Only the ones that would collapse or
  seriously degrade the idea if false.
- **Approaches** — for each approach the idea proposes, where it breaks or a simpler path exists.
- **Prior art** — always run a real websearch. Name specific existing products/papers/tools, or say
  "searched X, found none." For each match, one line on how this differs — or admit it doesn't.
- **Failure modes** — tell the specific story of *how* it fails, not generic risk. 

## Move 1 — Effort-value suggestions

For each thing worth doing, one line: what to do · effort · what it buys. Rank cheapest-per-unit-of-
value; say which one to do first.

**Not one-shot.** If the user pushes back, they may know something you don't — update and re-attack
the parts in question.

## Report structure

Scale depth to the idea; don't pad.

```
## Assumptions     — the shaky ones, ranked by leverage
## Approaches      — where each breaks · simpler path if any
## Prior art       — named matches + how this differs (or "found none")
## Failure modes   — specific how-it-fails stories, ranked by likelihood × damage
## Suggestions     — do · effort · buys · ranked · do first: [one move]
```
