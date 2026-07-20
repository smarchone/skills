---
name: explain-socrates
disable-model-invocation: true
description: Interrogates a blog post, article, file, codebase design, or abstract idea by Socratic questioning — repeatedly asking "why" and "what does that assume" until the argument bottoms out at its atomic axioms — then rebuilds it by retracing the same question path upward, checking at each step whether the next claim actually follows. Use this whenever the user wants something "questioned to first principles," "steelmanned," "taken apart and rebuilt," asks "what does this actually rest on," "poke holes in this," "is this argument as solid as it sounds," "what's the Socratic method version of this," or wants to find the hidden assumptions / load-bearing premises in a claim, essay, design decision, or belief. This is NOT a summary (see elevator-pitch) and NOT a rhetorical/structural analysis of how a piece is written (see narrative-structure) — it's an epistemic stress test of whether a claim actually holds, presented as a real dialogue, not a bullet-point audit.
---

# Socratic Deconstruction & Rebuild

Most critiques of an argument attack it from the side — "here's a counterexample," "here's a
missing citation." This skill attacks it from underneath: find the claim, ask what it depends on,
ask what *that* depends on, and keep going until you hit something that can't be reduced any
further — a definition, a brute empirical fact, a value judgment the author is entitled to just
hold. Then walk back up the same staircase and check whether each step actually bears the weight of
the one above it. Some arguments survive this fully intact, just now visibly grounded. Most don't —
somewhere on the way up there's a step that only *looks* load-bearing, and finding it is the entire
point of the exercise.

The failure mode to avoid is performing "Socratic style" as decoration — a few rhetorical "but why?"
questions followed by the same conclusion you'd have written without them. If the rebuild ends up
exactly where the original argument started, with every premise fully vindicated, be suspicious of
yourself: check whether you stopped questioning too early rather than congratulating the argument
for being sound.

## Read the target first

Read the actual blog post, file, or stated idea in full before questioning it. Quote or closely
paraphrase its real language when you put words in the Respondent's mouth — a generic Socratic
dialogue that could be reskinned onto any topic means you weren't actually reasoning about *this*
argument. If the user hands you a bare concept or idea rather than a document ("is free will
compatible with determinism," "should we use microservices here"), treat their framing of it as the
opening claim and proceed the same way.

## Phase 1 — Name the claim under test

Before questioning begins, state in one or two sentences the single claim you're going to
interrogate. Pick the load-bearing one, not a minor aside — if the piece argues five things, find
the one the other four depend on. This is a target-lock step, not the analysis itself; keep it
short and move on.

## Phase 2 — The Descent

Write this as an actual dialogue between **Q** (the questioner, playing Socrates) and **R** (the
respondent, voicing the argument as charitably and specifically as it can be voiced — steelman it,
don't strawman it). Q's only tool is asking what a claim assumes or depends on; Q never asserts a
counter-position. R answers as the argument's best advocate would, using specifics pulled from the
actual target, not hand-wavy restatement.

Each exchange should peel back exactly one layer — "why do you believe that," "what would have to
be true for that to hold," "what do you mean by that word, precisely" — and R's answer becomes the
next thing Q questions. Don't skip layers to rush toward a dramatic finish; the value is in the
path, not just the destination.

**Recognizing bedrock.** Stop descending on a given thread when R's answer becomes one of:
- A **definition** — the argument is just using a word a certain way, and once stated plainly there's
  nothing further to ask (e.g. "by 'fair' I mean each party bears costs in proportion to benefit received").
- A **brute empirical fact** — something checkable in the world that the argument is simply built on
  top of, not derived from ("compilers exist and are deterministic").
- A **value or preference the author is entitled to just hold** — not everything reduces to fact;
  some things bottom out at "I think X matters more than Y" and that's a legitimate axiom, not a
  cop-out, provided it's stated openly rather than smuggled in.

Don't confuse bedrock with a stall. "It's just obviously true" or "everyone knows that" is R
dodging, not an axiom — Q should push once more before accepting it. Genuine bedrock feels
*settleable*, not just *unquestioned*.

Different sub-claims inside the argument may bottom out at different axioms — that's normal. Run
the descent on each thread that matters to the central claim, not just the first one you find.

## Phase 3 — The Rebuild

This is the part most Socratic exercises skip, and it's the part that actually earns the format.
Starting from the axioms found in Phase 2, retrace the *same path* in reverse — Q now asks, at each
step going back up, "granting that, does the next claim actually follow, or does something else
need to be true first?" This can be a continuation of the same Q/R dialogue, or a clearly marked
second dialogue that climbs the same staircase.

Three honest outcomes, all valid — don't force it toward the first one:
1. **It holds.** Each step really does follow from the one below; the rebuild arrives back at
   (something very close to) the original claim, now visibly supported rather than merely asserted.
2. **It survives, weakened.** The rebuild reaches a real conclusion, but a narrower or more qualified
   one than the original — e.g. "true for the specific case argued, not the general rule claimed."
3. **It collapses at a joint.** Somewhere going up, a step doesn't actually follow from what's below
   it — there's a gap the original argument crossed by assertion, transition words ("clearly,"
   "so"), or an unstated premise doing the real work. Name that step specifically; this is usually
   the most useful sentence in the whole piece.

## Close with a plain-language ledger

After the dialogue, drop out of character and state, in normal prose (not Q/R format):
- The axioms the argument actually rests on, stated plainly.
- Any hidden assumption you uncovered that the original piece never surfaced.
- Which outcome the rebuild reached (holds / survives weakened / collapses), and at which specific
  step, if it didn't fully hold.

Keep this short — a few sentences. Its job is to let someone who skims past the dialogue still walk
away with the verdict.

## A short worked example

**Target claim:** "We should switch this service to microservices because it will let teams move
faster."

**Phase 1:** The load-bearing claim is that decomposing into microservices *causes* faster team
velocity — not that it's technically feasible, which nobody disputes.

**Phase 2 (Descent):**
> **Q:** Why would splitting the service make teams move faster?
> **R:** Because each team can deploy independently, without waiting on other teams' changes.
> **Q:** What has to be true for independent deploys to actually remove waiting?
> **R:** That the service boundaries line up with team boundaries — each team owns a piece it can
> ship alone.
> **Q:** And what has to be true for boundaries to line up that way?
> **R:** That the domain naturally decomposes into pieces with low coupling between them.
> **Q:** Is that a fact about this particular service, or an assumption being imported from
> elsewhere?
> **R:** ...it's an assumption. We haven't actually mapped this service's coupling — we're assuming
> it decomposes cleanly because microservices worked that way at a previous company.

That last answer is bedrock, but not the kind that vindicates the claim — it's an unexamined
assumption, imported wholesale from a different context.

**Phase 3 (Rebuild):** Granting that *some* services do decompose cleanly (a fact, verifiable in
general), does it follow that *this* service does? No — that requires actually mapping this
service's coupling, which was never done. The step from "microservices help teams that have
low-coupling domains" to "microservices will help this team" doesn't hold without that missing
mapping.

**Ledger:** The argument rests on one unexamined import — "our domain decomposes like the one at my
last company did" — stated nowhere in the original pitch. Outcome: collapses at the step from
general benefit to this-service benefit. Fix isn't to abandon microservices, but to do the coupling
analysis the claim quietly assumed was already done.

## Calibrating length and depth

A tight blog post or a narrow technical decision might bottom out in two or three exchanges per
thread — don't manufacture depth that isn't there. A dense philosophical essay or an
architecture-wide design choice can warrant a much longer descent with several parallel threads.
Match the dialogue's length to how much the claim actually resists being questioned, not to a fixed
template.

If the user hands you an idea rather than someone else's argument (their own belief, a decision
they're about to make), the same shape applies — Q interrogates, R is the user's position argued as
well as it can be argued, and the rebuild tells them what it's actually standing on.
