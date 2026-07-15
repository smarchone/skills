---
name: refine
user-invocable: true
disable-model-invocation: true
description: >-
  Refines a raw idea into a sharper, scoped one and rules on whether to pursue it:
  scope down, draw boundaries, search prior art, attack the reasoning and for
  failure, then reconstruct the strongest surviving version plus a verdict with a
  separate confidence level.
---

# Refine

Take a raw idea — over-scoped, fuzzy-edged, maybe already built, resting on unexamined beliefs — and
hand back a sharper, smaller version plus an honest call on whether to pursue it. **North star: the
idea comes out stronger, or gets a well-reasoned death — never just a list of wounds.** You break it
only to reconstruct it. Posture is collaborator, not prosecutor; even a "kill" should feel like a
gift that saved months.

## Move 0 — Scope first (ask, then attack)

Read the whole target (fetch the full URL/file, not a snippet). Then check:
- **One idea or several?** Raw ideas are often three ideas in one coat. Name the sub-ideas and ask
  which to refine — the sharpest, smallest one is usually the real idea.
- **Concrete enough to have a failure mode?** If you can't picture it succeeding or failing, it's
  too abstract to attack — the vagueness is the finding.

If under-scoped, **ask 2–4 targeted clarifying questions and wait** (who it's for, what problem it
removes, what "done" looks like, what's excluded). If already sharp, say so and go straight to the
attack — don't manufacture questions.

## Move 1 — Boundaries

State the idea in one strong sentence (steelman). Then draw edges: **in scope** (the core it lives
or dies by), **out of scope** (adjacent temptations it's deliberately NOT), **deferred** (real, but
not now). Fuzzy boundaries are themselves a finding.

## Move 2 — Prior art (always search)

Always run a real websearch, even for internal ideas. **Name specific existing products/papers/
tools** (or state "searched X, found none"). For each close match, say how this differs in one line —
or admit it doesn't. Reinvention isn't automatically fatal (incumbents may be bad, or serve a
different user); report it and let the verdict weigh it.

## Move 3 — Attack the reasoning

Report only what you actually find; an empty lens is fine. Tag each finding.
- **Unstated assumptions** — must-be-true-but-never-said. Ask *what would have to hold?* Report only
  collapse- or serious-degrade-grade ones.
- **Biases** — survivorship, confirmation, planning-fallacy optimism, anchoring. Anchor each to a
  specific sentence or leave it out (unanchored = name-calling).
- **Alarm claims without proof** — urgent-sounding assertions carrying the argument's weight with no
  evidence. Flag each; say what would verify it.
- **Blindspots** — whole categories never considered: unmentioned stakeholders, second-order
  effects, maintenance after launch, abuse, behavior at 10× / 0.1× scale, no failure signal.

## Move 4 — Attack for failure (premortem)

It's 18 months later and it failed — tell the specific story of *how*, not generic risk. Cover the
killers that apply: no demand, out-competed, unbuildable with real resources, broken economics, or
can't reach anyone. Rank by likelihood × damage; the top one or two are what the verdict must face.

## Move 5 — Reconstruct and rule (never skip, even for a kill)

- **Strongest surviving version:** rebuild the idea with what the attacks revealed — tightened
  scope, assumptions turned into tests, failure modes designed around. State it concretely enough to
  act on tomorrow. If it can't be salvaged, say what would've had to be true.
- **Verdict + separate confidence:** verdict is **Pursue / Pursue-with-changes / Pivot / Kill**;
  confidence is **High / Med / Low** with the reason (usually the one load-bearing unknown). Keep
  them distinct — a low-confidence pursue and a high-confidence kill are entirely different
  situations. Then give **the one cheapest next move** that would most raise confidence.

## Report structure

Scale depth to the idea; don't pad.

```
## The idea, sharpened   — one sentence (reflect any clarifying answers)
## Boundaries            — In scope / Out of scope / Deferred
## Prior art             — named matches + how this differs (or "found none")
## What the attack found  — ranked by leverage; merge duplicate findings; tag each
                            (assumption | bias | alarm-claim | blindspot | failure-mode)
## What survived          — what the attacks failed to dent
## The strongest version  — the reconstructed, actionable idea
## Verdict                — [Pursue/Changes/Pivot/Kill] · Confidence [H/M/L] because [unknown]
                            Do next: cheapest confidence-raising move
```

## Edge cases

- **Can't access the target:** say so and stop.
- **Already excellent:** say so plainly — don't manufacture wounds.
- **Genuinely dead:** deliver the kill kindly, with the reason and what would've changed it.
- **User pushes back:** they may know something you don't — update, you're refining together.
- **Overlap:** `attack-*` skills are single adversarial lenses and `redteam` fans them all out;
  refine is the end-to-end scope→verdict pass. Point users there if they want only the attack.
```
