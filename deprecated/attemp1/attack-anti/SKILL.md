---
name: attack-anti
disable-model-invocation: true
description: Sharpens understanding of a concept, idea, blog post, article, spec, or file by mapping its negative space — what it's commonly confused with, what it explicitly excludes or disclaims, and what gaps or unstated assumptions it leaves unaddressed — then uses all of that to restate a tighter definition of what the target actually is. Use this whenever the user asks "what is this NOT", "what does this leave out", "what's missing here", "what am I not getting", wants a concept defined "by contrast" or "via negativa", asks what a term is often confused with, wants gaps or blind spots surfaced in a post/spec/design doc, or says "explain-anti". This is NOT a validity/soundness check on an argument's logic (that's explain-socrates, which interrogates whether premises hold up) and NOT an analysis of how a piece of writing is structured or persuades (that's narrative-structure) — this skill's only goal is drawing a sharper boundary around what the target IS by naming everything around it that it ISN'T.
---

# Explain: Anti

The fastest way to understand what something is often isn't a better positive definition — it's
finding its edges. "A cache is fast temporary storage" is vague until you know a cache is NOT a
database (it can vanish without consequence), NOT a queue (order doesn't matter), and doesn't cover
data that's written once and read never. The negative space around a concept is often more
informative than the positive description, because positive descriptions can be true and still leave
the boundary fuzzy — negation forces precision.

This skill is about definition, not debate. It does not ask "is this argument correct" — it asks
"what surrounds this thing that isn't it, and what does that tell us about what it actually is."

## Read the whole target first

Read the full source (fetch the complete URL, read the whole file, or take the full concept as
given) before analyzing anything. If the target is a bare concept with no source document, that's
fine — you'll rely on what's generally true about the concept rather than quoting a text.

## Produce a report with these sections

Use all three investigative sections below, then close with a synthesis. Skip a section only if it
would genuinely be empty for this target — don't pad it with something thin just to fill the
template, and say explicitly when a section came up empty rather than silently omitting it (the
absence itself is informative — e.g., "this piece states no explicit scope limits" is a real
finding, not a gap in your work).

### 1. Confused With — adjacent concepts that get mistaken for this one

Name 2-4 things people genuinely mix this up with — near neighbors, earlier/simpler versions of the
same idea, or terms used loosely as if they were synonyms. For each one, give the one-line
distinction: not just "X is different from Y" but *what specifically* someone would get wrong if
they treated them as the same thing. Pick real confusions, the kind that actually happen in
conversation or in code reviews — not technically-true-but-nobody-actually-confuses-these pairings.

```
- **Not [neighboring concept]:** [the specific thing you'd get wrong if you conflated them]
```

### 2. Stated Exclusions — what the target itself says it doesn't cover

If the target is a document (post, spec, README, design doc), look for places where the author
explicitly draws a boundary: "this doesn't handle X," "out of scope," "assumes Y is already true,"
a caveat, a "future work" section that's really an admission of a current gap. Quote or closely
paraphrase these — this section should reflect the author's own stated limits, not your inference.
If the target is a bare concept with no author to quote, say this section doesn't apply rather than
inventing exclusions no one stated.

### 3. Unstated Gaps — what's missing that nobody said out loud

This is the section that takes real thought. Look for:
- A claim that's asserted but would only hold under a precondition the piece never mentions
- An edge case or failure mode a reasonable reader would ask about that goes unaddressed
- A step that's skipped because the author assumed it was obvious, but it's only obvious to someone
  who already understands the answer
- For a bare concept: the misunderstanding a beginner would form from the one-sentence description,
  because the one-sentence description is technically true but omits the part that actually matters

Don't confuse this with nitpicking — the point isn't to list every conceivable objection, it's to
find the 2-4 gaps that, once named, actually change how well someone understands the target.

### 4. Sharper Definition — what this synthesis reveals the target actually is

Close with a tightened definition or explanation of the target, written using what you just carved
away. This should read differently — more precise — than a definition you'd have written before
doing sections 1-3. A useful test: if this closing definition could have been written without doing
any of the negative-space work above, it isn't tight enough yet; it should visibly incorporate at
least one distinction, exclusion, or gap from above (e.g. "unlike [neighbor from section 1], and
without assuming [gap from section 3], X is really just...").

## Calibrate to the target

A short, well-scoped spec might have a real Stated Exclusions section but almost no Unstated Gaps.
A vague blog post making a big claim might have the opposite — no explicit exclusions at all, but
several load-bearing gaps. A bare technical term might have no exclusions section at all but a rich
Confused With section. Let the target dictate which sections carry the most weight rather than
forcing even coverage across all four.
