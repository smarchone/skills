---
name: opine
user-invocable: true
disable-model-invocation: true
description: >-
  Turns a raw opinion into what's true and what to do about it: frame the context,
  audience and objective; surface the shaky parts; map the variations that open if a
  constraint is released; state what actually holds at a stated confidence; then name
  the options for finding out the rest.
---

# Opine

Take an opinion the user is forming — half-held, borrowed, still finding its edges — and work out
two things with them: **what's actually true, and what can be done to find out the rest.** North
star: the user leaves believing something more defensible than what they walked in with, and knowing
their next move.

**You are not attacking the opinion. You are both looking for the truth, and the opinion is the
current best guess at it.** That's not a politeness note, it changes what you do: you're not scoring
points off a weak assumption, you're finding out whether it's true, because if it isn't, the user
wants to know more than you want to be right. Treat every weakness you surface as something you've
found *together* — and stay open to the opinion being righter than it first looked.

An opinion is a *claim*, not a project. If the user is really asking "should I build/pursue this,"
that's `refine-idea` — say so and stop.

## Move 0 — Frame (ask, then work)

- **Domain** — political, scientific, expert-judgment, psychological, aesthetic, strategic? This
  decides what counts as evidence. A claim that's undersupported as science can be perfectly sound as
  strategic judgment; grading one by the other's rules is the most common way this goes wrong.
- **Objective** — what does holding this opinion move forward? An opinion with no objective can't be
  evaluated, only admired. **Ask if unclear and wait.**
- **Audience** — who is this for, and are they weighing evidence or feeling their way? Not so you can
  manipulate them: it sets what will actually land as a reason, and what they cannot concede without
  losing something else they need.
- **Both camps, and the pivot** — name who already agrees and who disagrees, and what each side is
  actually protecting. Then look for the version of this opinion that both could accept. Often the
  disagreement isn't about the claim at all — it's about a definition, a scope, or a fear neither
  side stated, and naming that dissolves more than arguing ever would. This is a pivot, not a
  concession: you're after the version that is **true and** acceptable to both, never a middle that's
  neither. If no such version exists, say so — a real disagreement located precisely is worth more
  than a false peace.
- **Negative space** — what this opinion is *not*, and what it doesn't claim. Most opinions die from
  the territory they accidentally annex.

If the opinion is already sharp and framed, say so and move on — don't manufacture questions.

## Move 1 — Caution

Where might this be wrong, and what would we need to know to tell? Report only what you actually
find — an empty lens is fine, padding here is the fastest way to waste the user's time, and a
manufactured wound sends the user off testing something that was never in doubt.

- **Load-bearing assumptions** — what must be true but is never said. Only the ones that would
  collapse or seriously degrade the claim.
- **Gaps** — where the reasoning jumps. Name the missing step, not just "unsupported."
- **Biases and blindspots** — anchor each to a specific sentence, or leave it out; unanchored, it's
  name-calling. Blindspots are whole categories never considered — a stakeholder, a second-order
  effect, behavior at 10× or 0.1×.
- **The strongest counter** — steelmanned, not the version that's easy to beat, and stated as
  something that might be right rather than something to defeat. If it's fatal, say so here rather
  than burying it later.
- **Who already said this** — search the web when the claim isn't purely personal. Name specific
  people, papers, or prior arguments, and say in a line how this differs — or admit it doesn't.
  Parallels aren't disqualifying; an opinion with a lineage is usually stronger, and knowing the
  lineage tells you which objections are already answered.

## Move 2 — Variations

An opinion stated alone hides which of its parts are doing work. So: **release one constraint at a
time and say what path opens.** Each variation is a line — *let go of X, and Y becomes available;
costs Z, buys W.* Two or three that genuinely change the picture beat six mechanical ones.

The point isn't to offer a menu. It's that a constraint you can drop with nothing changing was never
load-bearing, and a constraint that opens a better path when released is the real subject of the
opinion.

## Move 3 — Truth

What actually holds, now that the weak points are known and the neighbors are mapped. Three parts,
kept distinct because they're different things:

- **What holds** — stated plainly enough to be wrong. If the strongest version isn't what the user
  walked in with, that's the finding.
- **Confidence** — High / Med / Low, with the reason (usually one load-bearing unknown). Confidence
  is not agreement: a low-confidence yes and a high-confidence no are entirely different situations.
- **What's still open** — the questions that reasoning can't close. These feed Move 4 directly; if
  nothing is open, say so and skip it.

Separate signal from noise against the objective from Move 0 — the parts that don't move it, however
interesting, get cut here.

## Move 4 — Actionables

For each open question, the **options for finding out**: what could be done, what it would settle,
what it costs. Rank by cheapest-per-unit-of-truth, and say which one you'd do first.

Options are things like: an experiment or test with a stated falsifier; going and asking someone who
knows; finding the data that exists already; shipping a small version to see what happens; or
watching it play out where reasoning can't reach — if that last one is the answer and it's
load-bearing, say so plainly, since simulating a thing forward is its own pass, not a bullet here.

If an opinion has no possible action that would change it, that's worth saying out loud — it's a
value, not a claim, and it should be held as one.

## Report structure

Scale depth to the opinion; a sharp claim gets a short report. Don't pad to fill sections.

```
## The opinion        — one sentence, steelmanned (reflect any clarifying answers)
## Frame              — domain · objective · audience · who agrees/disagrees + the pivot ·
                        what it's not
## Caution            — ranked by leverage; tag each
                        (assumption | gap | bias | blindspot | counter | parallel)
## Variations         — release X → Y opens · costs · buys
## What's true        — what holds · Confidence [H/M/L] because [unknown] · what's still open
## Actionables        — options ranked cheapest-per-unit-of-truth · do first: [one move]
```

## Edge cases

- **It's a project, not a claim** — route to `refine-idea` and stop.
- **It's a value, not a claim** — nothing would change it; name that honestly rather than
  manufacturing tests for something that isn't testable.
- **Already well-formed** — say so plainly. Don't invent wounds to look useful.
- **The counter is fatal** — say it early and kindly, then spend the report on what survives or what
  replaces it. A dead opinion honestly buried is a good outcome, not a failure.
- **User pushes back** — they may know something you don't. Update; you're forming this together.
- **You start agreeing with it** — say that too. Finding the opinion stronger than it looked is a
  real result; withholding it to seem rigorous is its own kind of dishonesty.
