---
name: attack-gaps
user-invocable: true
disable-model-invocation: true
description: >-
  Interrogates a stated idea — a business idea, proposal, design doc, plan, blog
  post argument, or strategy — for the gaps in its foundations: implicit
  assumptions it depends on, cognitive biases shaping its framing, and blindspots
  (whole categories it never looks at). Each gap is paired with the smallest
  question, test, or statement that would close it, so the output is a punch-list
  for completing the idea, not a takedown. Use whenever the user says "find the
  gaps", "challenge my assumptions", "what am I missing / not seeing", "what am I
  taking for granted", "poke at this idea", "pre-mortem my reasoning", "where are
  my blindspots", "what biases are in this", says "complete-gaps", or wants an
  idea/plan stress-tested before committing. NOT explain-anti (maps negative space
  to sharpen what a thing IS), NOT explain-socrates (tests whether the STATED
  premises hold — this hunts what was never stated), NOT adversarial red-teaming
  (simulates how the idea fails in the world — this audits the reasoning it stands
  on).
---

# Complete: Gaps

A stated idea is the visible part of an iceberg. Underneath sit the assumptions the author didn't
know they were making, the biases that chose this framing over others, and the whole categories of
consideration that never entered the frame. Ideas rarely die from the weaknesses their authors
argue about — they die from the load-bearing beliefs nobody noticed were beliefs. The job of this
skill is to make that invisible scaffolding visible and challenge it — and the name says the intent:
the point of finding gaps is to **complete** the idea, not to kill it. Every gap you surface must
come with the smallest thing that would close it, so the output reads as a work-list for making the
idea sturdier, not a verdict against it.

## Read charitably first, then dig

Read the whole target (fetch the full URL or file — don't work from a snippet or your prior sense
of the topic). Before hunting gaps, make sure you can state the idea in its strongest form — a
"gap" that a careful reading of the source actually addresses is a false positive that costs you
the reader's trust for every real gap that follows. If the idea is only described secondhand or in
one vague sentence, the vagueness itself is the finding: surface the clarifying questions that
would pin the idea down instead of doing assumption-archaeology on words that aren't there.

## The three lenses

Work through all three deliberately — they catch different things, and skipping one is itself a
blindspot. But report only what each lens actually finds; an empty lens is a fine result.

**1. Implicit assumptions** — things that must be true for the idea to work but are never stated.
Hunt for them by asking, for each major claim or step: *what would have to be true for this to
hold?* Common hiding places: assumptions about users ("people will bother to configure this"),
scale ("this works at 100 customers — and at 10,000?"), stability ("the API/regulation/market stays
as it is today"), incentives ("the team maintaining this will care as much as the author does"),
and resources ("someone has time to review these"). The test for load-bearing: if this assumption
is wrong, does the idea degrade or collapse? Only collapse-grade and degrade-grade assumptions are
worth reporting.

**2. Biases** — the forces that shaped which idea got stated and how. Look for survivorship bias
(reasoning from visible winners), confirmation shaping (only supporting evidence cited when
counter-evidence obviously exists), planning-fallacy optimism (timelines/costs with no slack and no
reference to past similar efforts), anchoring (the first solution considered became the only one
considered), and availability (the recent vivid incident driving a general policy). Naming a bias
is an accusation, so hold it to a higher standard than the other lenses: point at the specific
sentence or reasoning move that exhibits it, and say what unbiased reasoning would have looked at
instead. A bias you can't anchor to the text is name-calling — leave it out.

**3. Blindspots** — entire categories of consideration absent from the frame. Where assumptions
are wrong answers to questions the author implicitly asked, blindspots are questions never asked at
all. Scan for the standard missing categories: unconsidered stakeholders (who is affected but never
mentioned?), second-order effects (what does the solution cause once it works?), the maintenance
and operations story after the exciting part ships, abuse and misuse by actors with different
incentives, what happens at 10× and at 1/10th the assumed scale, and how anyone would know if the
idea is failing (no exit criteria or kill signal is one of the most common blindspots in otherwise
careful plans).

## Every gap earns its place

The failure mode of gap-finding is the laundry list — twenty pedantic observations that bury the
two that matter. Apply these filters before a gap makes the report:

- **Load-bearing, not exhaustive.** "The doc doesn't discuss X" is only a gap if X being wrong or
  absent changes the decision. An idea is allowed to not be an encyclopedia.
- **Anchored.** Tie each gap to something specific in the target — the claim that depends on the
  assumption, the sentence that shows the bias, the section where the missing category should live.
- **Closeable.** Pair each gap with the smallest concrete move that would close it: a question to
  answer, a number to look up, an experiment to run, a sentence to add ("this assumes X; if X fails
  we do Y"), or a person to ask. This is the "complete" in complete-gaps — a gap without a closing
  move is just anxiety.
- **Ranked.** Lead with what would change the decision. If the user addresses only the first item,
  that should have been the right one to address.

## Report structure

```
## The idea, steelmanned
One or two sentences stating the idea in its strongest form — proof you understood before you dug.

## Gaps
Ordered by leverage. For each:

### [Short gap title] — assumption | bias | blindspot
**The gap:** what's unstated/unexamined, anchored to the specific claim or passage it hides under.
**Why it matters:** what degrades or collapses if this goes the wrong way.
**To close it:** the smallest question, test, statement, or lookup that resolves it.

## Already solid
What the idea genuinely handles well — so the user knows what NOT to revisit, and so the gaps
above read as calibrated judgment rather than reflexive criticism.

## If you only close three
The top gaps restated in one line each — the minimum work before committing to the idea.
```

Scale the depth to the target: a one-paragraph idea might yield three gaps and no "top three"
section; a 20-page strategy doc might yield ten. Don't pad to fill the template.

## Edge cases worth handling deliberately

- **Can't access the target** (broken URL, missing file, empty paste): say so plainly and stop —
  don't audit an idea you haven't read.
- **The idea is genuinely well-examined**: say so. "I found two minor gaps and the rest is
  well-covered" is a valuable, trust-building result — inventing gaps to look thorough teaches the
  user to ignore this skill's output.
- **The user's own idea vs. someone else's**: same rigor either way, but remember the posture is
  collaborator, not prosecutor — the user brought the idea here to make it stronger. This matters
  most for the bias lens: "this framing shows anchoring" lands differently on someone's own plan,
  so anchor it to the text extra carefully.
- **Multiple distinct ideas in one target**: give each its own gap analysis rather than blending
  them — a gap in idea A is noise when read against idea B.
- **The gaps are mostly unknowns, not flaws** (early-stage brainstorm): shift the framing from
  "what you got wrong" to "what to find out next" — for a young idea, the closing moves ARE the
  plan, and the report is effectively a research agenda.
