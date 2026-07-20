---
name: explain-levels
disable-model-invocation: true
description: Explains a blog post, article, paper, technology, codebase design, or abstract idea at several increasing levels of complexity — by default 4 rungs, from total-novice up to expert-level depth — where each level refines the one before it, never contradicts it. Use whenever the user asks to "explain this at different levels," "explain like I'm 5 then like an expert," "give me the ELI5 through PhD version," wants a "ladder" or "levels" explanation, asks for a beginner and an advanced version of the same thing, or wants to go from simple to deep at their own pace. Respects an explicit level count if given (e.g. "in 3 levels" or "give me 6 levels"). This is NOT explain-feynman (one rebuilt explanation, hunting the explainer's own gaps) and NOT explain-big-picture (zooms out to ecosystem context at one resolution) — this skill's product is several self-contained explanations of the same target at different resolutions, so a reader can stop at whichever rung matches what they know.
---

# Explain: Levels

The format this skill produces is familiar from things like WIRED's "5 Levels" videos: the same
concept explained to a child, then a teenager, then a student, then an expert. The appeal isn't just
"simple version, then complicated version" — it's that a reader can stop reading at the rung that
matches what they already know and walk away with something true. That last word is the whole craft
challenge. It's easy to write a "kid version" that's simple because it's actually wrong, and then have
the "expert version" quietly contradict it. That's a **lie-to-children**: a simplification you have to
retract rather than build on. The discipline of this skill is to write simplifications that are
*true but incomplete* — every later level adds precision, mechanism, or nuance, but never says
"actually, level 2 was wrong."

## Read the target first

Read the actual blog post, file, paper, or stated idea in full before writing any level — don't work
from a title or your own prior sense of the topic. If the user hands you a bare concept rather than a
document ("explain quantum entanglement at different levels"), treat their framing as the target and
draw on your own knowledge as the source material.

## How many levels

Default to **4 levels**. If the user specifies a different count, use that instead — the ladder
metaphor and the "refine, don't contradict" rule apply the same way whether it's 3 rungs or 7. Don't
pad out extra levels just to hit a round number, and don't compress genuinely distinct levels into one
just to hit 4 exactly if the user asked for more; let the requested count drive how finely you divide
the material.

## Choosing the ladder that fits the target

The classic ladder is an **expertise/audience ladder**, and it's the right default for most technical
concepts, science topics, and technologies:

1. A child — no jargon at all, pure analogy and everyday experience.
2. A curious teenager or interested layperson — same core idea, but willing to hold a bit more
   structure and a first real technical term or two.
3. A student or practitioner in the field — real vocabulary, the actual mechanism, assumes the
   reader has the relevant background (e.g. basic physics, basic programming).
4. An expert or researcher — full technical precision, edge cases, caveats, competing views, open
   questions.

But not every target has a natural audience ladder. A business decision, an internal design doc, or a
process doesn't obviously have a "child" version. For those, pick whichever ladder actually fits:

- **Depth/resolution ladder** (headline → how it works → why it works this way and not another way →
  edge cases, failure modes, and open questions) — good for design decisions and architecture choices.
- **Role ladder** (new hire → their manager → the domain expert who owns this → the person who
  originally built it) — good for internal processes and organizational context.

If the user names their own levels explicitly ("explain this to a 10-year-old, then to my
co-founder, then to an investor"), use their framing rather than defaulting to the audience ladder.

## The one rule that makes this work: refine, don't contradict

Before finalizing anything, check every level against the ones below it: could someone who only read
level 1 carry that belief up to level 4 without ever having to unlearn it? A good simplification
survives being built on top of; a bad one collapses the moment more detail arrives.

This doesn't mean lower levels have to be hedged and cautious — a level-1 analogy is allowed to leave
things out entirely. It just can't assert something that's false. "Electrons orbit the nucleus like
planets around the sun" is a lie-to-children (electrons don't have orbits in that sense at all).
"Electrons are usually found in a cloud of specific spots around the nucleus, and it's more useful to
think of them as being *somewhere in that cloud* than tracing a path" is simple, still a child-level
sentence, and it's actually true — level 4 can add the wave function and probability density on top of
it without ever contradicting it.

If you find yourself wanting to write "actually, that's not quite right" going up a level, that's a
signal to go back and fix the lower level's wording — not a normal or acceptable part of the ladder.

## What should actually change between levels

Resist making the only difference between levels "more words" or "shorter sentences." Real
differences, level to level:

- **Vocabulary**: level 1 uses zero technical terms; each level up introduces the real field-standard
  terms, defining them in place the first time.
- **Mechanism vs. surface**: low levels can describe *what happens*; higher levels explain *why it
  happens that way mechanically*, and eventually *why it couldn't easily happen another way*.
- **Analogy vs. the real thing**: analogies are a scaffold for low levels, not a permanent substitute
  — by the top level, the explanation should stand on the real mechanism, with the analogy dropped or
  demoted to a passing aside.
- **Certainty and nuance**: only the top level or two should surface genuine controversy, exceptions,
  or open research questions — introducing them too early can overwhelm without adding truth, but
  burying them entirely at the top level would leave an expert-level reader with a falsely tidy
  picture.

## Format

Use a clear header per level naming who it's for, then the explanation:

```
## Level 1 — Explain it to a child
[explanation]

## Level 2 — Explain it to a curious teenager
[explanation]

## Level 3 — Explain it to a student/practitioner in the field
[explanation]

## Level 4 — Explain it to an expert
[explanation]
```

Adjust the audience labels to whatever ladder you chose (role ladder, depth ladder, or the user's own
named audiences) — keep whichever labels make it obvious at a glance who each rung is written for.

## A short worked example (compressed)

**Target:** how a Bloom filter decides "have I seen this before."

**Level 1 — a child:** Imagine a magic notebook with a bunch of little lights in it, all off. Every
time you show it something new, it lights up a few of the lights. Later, if you show it something and
*all* the lights it would light up are already on, it says "yeah, probably seen that." If even one
light is off, it says "nope, definitely never seen that."

**Level 2 — a curious teenager:** It's a big array of on/off switches. Adding an item runs it through
a few different math formulas (hash functions), each pointing at a switch, and flips those switches
on. Checking an item runs the same formulas and checks if all those switches are on. It can be fooled
into a false "yes" if other items happened to flip the same switches — but it can never wrongly say
"no" to something really added, because switches only ever get flipped on, never off.

**Level 3 — a practitioner:** A Bloom filter is a bit array of size *m* plus *k* independent hash
functions. Insert(x) sets bit `hi(x) mod m` for each of the *k* hashes; Query(x) checks that all *k*
bits are set. False positive rate is roughly `(1 - e^(-kn/m))^k` after *n* insertions, so you tune
*m* and *k* against expected *n* and your acceptable error rate. No deletion, because bits are shared
across items.

**Level 4 — an expert:** Standard Bloom filters trade a tunable false-positive rate for O(k) constant-
time membership tests in sublinear space, but the construction has known extensions worth knowing:
counting Bloom filters swap bits for small counters to support deletion at the cost of more memory;
scalable Bloom filters chain filters of increasing size to handle an unknown *n* without fixing *m* up
front; and cuckoo filters offer better space efficiency and true deletion support at the cost of a
different (and slightly more complex) collision-resolution scheme. The choice between them is a real
engineering tradeoff, not a settled "always use X."

Notice level 4 never contradicts level 1's "off switches turn on, never off" — it just adds that some
*variants* change that rule on purpose, which is a refinement, not a retraction.

## Edge cases worth handling deliberately

- **Target has no real depth** (a one-line fact, a trivial announcement): say so, and either collapse
  to fewer levels or note that a ladder isn't earning its keep here.
- **Genuine controversy or unsettled science**: surface it at the top level(s) rather than baking a
  false consensus into the lower levels — a level-1 analogy can still avoid the controversy entirely
  without lying, since it's allowed to leave things out.
- **Can't access the target** (broken URL, missing file, empty paste): say so plainly and stop — don't
  build a ladder from the title or from assumption alone.
- **User asks for a specific single level only** ("just give me the ELI5 version"): produce that one
  level well rather than the full ladder — the multi-level structure is for when they want the whole
  climb.
