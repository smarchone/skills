---
name: explain-feynman
disable-model-invocation: true
description: Reconstructs a blog post, article, paper, codebase design, or abstract idea from first principles using the Feynman Technique — teach it in plain language as if to a beginner, catch the exact spots where the explanation leans on jargon or hand-waving instead of real understanding, close those gaps against the source, then rebuild the explanation from its atomic building blocks (definitions, mechanisms, brute facts) rather than the source's own scaffolding. Use whenever the user asks to "feynman this," "explain like I actually understand it," "explain in plain English from first principles," "simplify until it makes sense," wants to test whether they (or the source) truly understand a concept, or wants something taught as if to a beginner, showing the work. This is NOT a soundness check on an argument (see explain-socrates) and NOT a narrative retelling (see explain-stories) — the product is a plain-language explanation rebuilt from the ground up, every jargon gap named and closed rather than papered over.
---

# Explain: Feynman

The Feynman Technique is built on a specific claim: if you can't explain something simply, you don't
actually understand it — you've memorized its vocabulary. The technique isn't "make it sound
simple," it's a diagnostic: attempt the plain-language explanation, watch for the exact moment you
reach for a term you can't unpack, and treat that moment as a real gap in understanding rather than a
stylistic problem to smooth over. Then close it, and only then simplify.

The failure mode to avoid is producing a superficially simple explanation that never surfaces where
it struggled — swapping jargon for a synonym and calling it done. If your plain-language pass didn't
stall anywhere, be suspicious of yourself and re-read the source for the part you skipped past.

## Read the target first

Read the actual blog post, file, or stated idea in full before explaining it — don't work from a
title, abstract, or your own prior knowledge of the topic. If the user hands you a bare concept
rather than a document ("explain how TCP congestion control works," "feynman this: monads"), treat
their framing as the target and proceed the same way, drawing on your own knowledge as the source
material.

## Phase 1 — Teach it plain

Write a first-pass explanation of the target as if to someone bright but with zero background in the
field — no jargon, no unexplained acronyms, no "as is well known." If a technical term is truly
load-bearing, define it in plain words the first time it's used rather than assuming the reader
already has it.

Write this in your own words, not by lightly rephrasing the source's sentences — if you're just
swapping synonyms into the original's structure, you're not actually testing your understanding,
you're paraphrasing. Use a concrete analogy or example if it helps carry the mechanism, but don't let
the analogy replace explaining the actual mechanism.

## Phase 2 — Hunt the gaps

Reread your Phase 1 explanation looking for the tells that you papered over something rather than
understanding it:
- A term you used but didn't define ("the scheduler handles this via backpressure" — what *is*
  backpressure, mechanically?).
- A step that jumps straight to a conclusion without the mechanism ("...which makes it thread-safe" —
  *why* does the prior step make it thread-safe?).
- A place you fell back on the source's own phrase because you couldn't find a simpler one.
- A claim you asserted with confidence but couldn't actually derive if pressed.

List each gap explicitly, quoting the exact sentence or phrase where it happened. This list is the
most useful output of the whole exercise — it's the honest map of what wasn't actually understood on
the first pass, not a list of cosmetic wording issues.

## Phase 3 — Close the gaps

Go back to the target (or, for a bare concept, to what you actually know rather than what you
assumed) and resolve each gap from Phase 2 one at a time. For each one, find the underlying
mechanism, definition, or fact that makes it true, and state it in plain language. If a gap turns out
to be unresolvable — the source itself doesn't explain it, or it rests on something outside the
target's scope — say so plainly rather than inventing a mechanism to fill the hole.

## Phase 4 — Rebuild from first principles

Now write the final explanation, but build it upward rather than patching Phase 1. Start from the
smallest true statements the idea depends on — definitions, brute facts, or primitive mechanisms that
don't themselves need further unpacking — and construct the target concept as something that follows
from those, step by step. The test for "first principles" here is structural: could a reader who
granted only the starting definitions and facts, with no other background, follow each step to the
same conclusion the source reaches? If a step in your rebuild still requires an unstated leap, that's
a gap Phase 2 missed — go close it before finishing.

This final explanation should read as clean and simple as Phase 1, but it will actually be more
complete — the gaps are gone, not hidden.

## Close with a short ledger

After the rebuilt explanation, add a few sentences, in plain prose:
- Which gaps you found in Phase 2 and how each was closed.
- Anything that stayed genuinely unresolved (the source didn't explain it, or it's out of scope) —
  name it rather than glossing over it.

This lets someone who skims past the full rebuild still see exactly where the real difficulty was.

## A short worked example

**Target:** A blog post explaining that "Rust's borrow checker prevents data races by enforcing that
data is either read by many or written by one, never both, at compile time."

**Phase 1 (plain teach):** Rust makes sure that if a piece of memory is being changed, nothing else
can be looking at it at the same time — and it checks this before the program even runs, so the bug
can't happen at runtime.

**Phase 2 (gap hunt):** "It checks this before the program runs" — *how*? That's just restating
"compile time" in different words without saying what's actually being checked. Also: "if a piece of
memory is being changed" — changed by what, and how does the checker know a change is happening
somewhere else in the program?

**Phase 3 (close gaps):** The compiler tracks, for every variable, who currently has access to it via
a system of references: at any point in the code, a variable can have either one mutable reference or
any number of read-only references, never both — and this is tracked lexically, by looking at which
reference is in scope at each line, not by running the program.

**Phase 4 (rebuild):** Start from the primitive: every value in Rust has exactly one owner at a time,
and access to a value happens through references that are either mutable (can change it) or
immutable (can only read it). The compiler walks the code and, for every value, checks which
references to it are alive at the same point in the program — if it ever finds a mutable reference
alive at the same time as any other reference (mutable or not), it refuses to compile. Because this
check happens by reading the code's structure rather than running it, the guarantee holds before a
single instruction executes — which is what "compile time" was standing in for.

**Ledger:** One real gap: "checks at compile time" was asserted without saying what is checked or how
— closed by explaining the one-mutable-or-many-immutable rule and that it's enforced via static scope
analysis, not execution. Nothing stayed unresolved.

## Calibrating length and depth

A narrow, well-defined mechanism might only produce one or two gaps and a short rebuild — don't
manufacture extra gaps to look thorough. A dense or unfamiliar topic can legitimately produce many
gaps across several concepts; work through each rather than stopping at the first clean-sounding
explanation. Match the depth of Phase 2's hunt to how much you actually had to reach for language you
couldn't back up, not to a fixed quota.

## Edge cases worth handling deliberately

- **You already understand the target cold and Phase 1 produces no real gaps.** That's a legitimate
  outcome — say so, and skip straight to Phase 4 rather than inventing gaps for form's sake.
- **The source itself is confused or self-contradictory.** Note this in the ledger rather than
  silently smoothing it into a coherent rebuild that the source doesn't actually support.
- **Can't access the target** (broken URL, missing file, empty paste): say so plainly and stop —
  don't rebuild from title or assumption alone.
- **The target is highly mathematical or notation-heavy.** Plain language still applies to the
  mechanism and intuition, but don't strip out notation that's actually load-bearing — translate it
  alongside a plain-language reading rather than deleting it.
