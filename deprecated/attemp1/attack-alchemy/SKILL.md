---
name: attack-alchemy
user-invocable: true
disable-model-invocation: true
description: >-
  Deconstructs a concept, idea, blog post, design, or plan to first principles,
  then rebuilds it from them. Phase one asks recursive question chains — "what
  must be true for this to work?" — until they bottom out in fundamentals
  (constraints, incentives, math, definitions a skeptic accepts), listing the
  question decompositions and the fundamentals. Phase two rebuilds the idea
  from ONLY those fundamentals and reports the residue: steps needing
  ingredients not on the list (hidden assumptions), forks the fundamentals
  permit equally well (arbitrary choices), and parts that can't be re-derived
  at all. Use whenever the user says "attack-alchemy", "first-principles this",
  "break this down to fundamentals", "melt this down", or wants no stone left
  unturned. NOT explain-feynman
  (teaches from first principles — this audits derivability), NOT attack-gaps
  (hunts assumptions directly — this surfaces them as reconstruction failures),
  NOT explain-socrates (tests the logic of STATED premises).
---

# Attack: Alchemy

Ideas arrive as finished assemblies — the author shows you the machine, not the parts list, and
certainly not the assembly choices they made along the way. Alchemy melts the machine down to its
elements and then tries to forge it again from nothing but those elements. The attack is in the
re-forging: if the rebuilt idea comes out different from the stated one, the difference is a
finding — a hidden ingredient the author never declared, a fork where they picked one branch
without noticing the other existed, or a part that simply cannot be derived and is held on by
assertion. And if the idea rebuilds perfectly, that's a finding too: it's load-bearing proof the
idea is sound all the way down. Either way, no stone is left unturned.

This is a derivability audit, not a teaching exercise. explain-feynman uses first principles to
make an idea *understood*; this skill uses them to test whether the idea is *earned*.

## Read the whole target first

Read the full source (fetch the complete URL, read the whole file, or take the full idea as given)
before decomposing anything. You cannot melt down what you haven't fully picked up — a
deconstruction based on a skim will bottom out in the wrong fundamentals, and every reconstruction
finding after that is noise. If the target is one vague sentence, say so: the right move is to ask
the clarifying questions that would pin the idea down, not to run alchemy on words that aren't
there.

## Phase 1 — Deconstruct: question your way to bedrock

Start from the idea's central claim and decompose by *asking questions*, not by listing parts.
For each claim or design choice, ask the question whose answer it depends on — "why does this
work?", "what must be true for this step to hold?", "what is this really made of?" — then ask the
same of each answer, recursively, until a chain bottoms out in a fundamental.

**Stopping rule — what counts as a fundamental:** a statement a skeptical reader would accept
without further argument. Usual bedrock: physical or mathematical constraints, definitions,
well-established human behavior (incentives, attention limits, trust), economic constraints
(scarcity, transaction costs), and hard platform facts (what the runtime/API/law actually permits).
If you can still meaningfully ask "but why is that true?", you haven't hit bedrock — keep digging.
If a chain bottoms out in something contestable ("users prefer X"), mark it as **sediment, not
bedrock**: it goes on the fundamentals list flagged as an assumption the reconstruction will have
to lean on visibly.

Use the Feynman move (restate an answer in plain words a child would follow — jargon is where
un-decomposed assemblies hide) and the Socratic move (ask the question that would embarrass the
answer if it's hollow) whenever a chain stalls.

Present this phase as two artifacts, both required:

1. **Question decompositions** — the actual chains, indented, from surface claim down to what each
   rests on. Show the questions, not just the conclusions; the chain is the audit trail.
2. **Fundamentals list** — the deduplicated bedrock statements the chains bottomed out in, each
   one line, numbered (F1, F2, …) so the reconstruction can cite them, with sediment items
   explicitly flagged.

## Phase 2 — Reconstruct: rebuild from the fundamentals alone

Now forget the original. Starting from ONLY the numbered fundamentals, rebuild the idea as if you
were deriving it fresh: given F1–Fn, what would you build? Derive each major element of the design
step by step, citing which fundamentals it follows from. This must be an honest derivation, not a
retelling — the test of honesty is that each step would make sense to someone who never saw the
original idea.

Three kinds of trouble can surface, and each is a distinct finding — name them as you hit them:

- **Missing ingredient:** a step in the rebuild needs something that is not on the fundamentals
  list. That something is a hidden assumption the original smuggled in — state it explicitly and
  say whether it's defensible or load-bearing-and-shaky.
- **Fork:** the fundamentals support two or more branches equally well, and the original picked
  one without argument. That's an arbitrary choice — name the road not taken; it's often a variant
  worth exploring, and at minimum the original owes a justification.
- **Unreachable part:** an element of the original that no combination of the fundamentals gets
  you to. It's held on by assertion, fashion, or inertia — the strongest finding alchemy produces,
  and it deserves the most careful write-up (double-check you didn't just miss a chain in Phase 1
  before declaring it).

End the phase by stating plainly how close the rebuild landed to the original.

## Report structure

```
## The idea, as stated
One or two sentences — proof you absorbed the whole target before melting it.

## Deconstruction
### Question chains
The indented question decompositions, one tree per major claim.
### Fundamentals
F1, F2, … — one line each; sediment flagged as (assumption).

## Reconstruction
The step-by-step rebuild from F1–Fn, citing fundamentals inline, with findings
called out where they occur: **[missing ingredient]**, **[fork]**, **[unreachable]**.

## Residue
What the rebuild could not account for, gathered and ranked by how much of the
original idea rests on it. If the rebuild was clean, say so — "fully derivable"
is a real verdict, not a failed attack.
```

Scale depth to the target: a one-paragraph idea might need two chains and five fundamentals; a
long design doc might need six chains and fifteen. Don't pad — a fundamentals list bloated with
trivia buries the two contestable items that matter.

## Edge cases worth handling deliberately

- **Can't access the target** (broken URL, missing file, empty paste): say so plainly and stop —
  don't run alchemy on an idea you never read.
- **The idea is already primitive** (a single claim, near-bedrock): say so — a two-line
  deconstruction and "nothing to reconstruct" beats a ceremonial full report.
- **Multiple distinct ideas in one target:** melt each down separately — fundamentals from idea A
  contaminate the rebuild of idea B, and the forks stop being meaningful.
- **The rebuild is better than the original:** it happens — the fundamentals sometimes derive a
  cleaner design than the one shipped. Say so directly and describe the delta; that's the most
  valuable output this skill can produce, not a digression.
