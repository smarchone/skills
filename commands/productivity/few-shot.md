---
description: Teaches a concept, tool, idea, or system through a small "dataset" of nontrivial worked examples, the way few-shot learning teaches a model — for a curious senior engineer who wants to learn fast.
disable-model-invocation: true
argument-hint: "<target>"
---

# Few-shot

A **curious senior engineer** wants to learn a concept, tool, idea, or system fast. Don't explain it.
Hand them a small dataset of examples (inputs paired with what happens) and let them infer the
rule, the way a model learns from a few shots.

## The dataset
- **Pin the target.** New, niche, or unfamiliar → don't look it up yourself. Say what you're unsure of and ask
  the user whether to look it up. Never swap in a nearby, better-known concept.
- **Map first.** List the target's core abstractions and use cases, most important first.
- **Highest-quality shots first.** No fixed count. The first set is 80-20: only the shots that give most
  of the feel. Don't dump everything; leave the rest for when the user asks for more. Draw from these types:
  - **Canonical**: the plain case, done properly. Not a toy.
  - **Edge**: where the obvious reading breaks or a boundary shows.
  - **Near-miss**: looks like the concept but isn't, or the wrong tool for the job. The contrast is what teaches.
  - **Real-world**: how it shows up in production: messy, with trade-offs.
- **Nontrivial.** Every shot should teach something the others don't. Skip hello-world.
- **Concrete.** Real code, commands, configs, traces, numbers. Unsure → mark *(unverified)*. Never invent an
  API, schema, or flag and present it as the target's.
- **Show, then label.** Give the input and what happens first. The takeaway comes after, in one line.

## Output
Two modes, same shots. **Distilled is the default.** Give **Detailed** when the user asks for it
("detailed", "elaborate", "go deeper", "full version").

### Distilled (default)
One table, one row per shot. Scannable in seconds; cut words, not insight. Write cells as short plain
sentences, not shorthand. Keep artifacts tiny: an inline command, prompt, or config line, in `code` when it is code.
The rule section is plain English: each bullet is a bold rule, then one short sentence on what it means for you.

````text
# <Target>, distilled
<one line: what it is, at most 15 words>

## The <N> shots

| # | Situation | What happens | Lesson |
|---|---|---|---|
| 1 | <the input or setup, a sentence or `inline code`> | <what happens> | <the one thing it teaches> |

## The rule
- **<Rule in a few words>.** <what it means in practice, one short sentence>   (3-5 bullets)

## Your turn
<one held-out case in one or two lines>

**<the question the user should answer>** (don't give the answer)

*Say **more** for: <the rest of the map>.*
````

### Detailed (on request)
Each shot gets its own section with a full artifact (real code, traces, numbers), so you can show more
than a table cell holds.

````text
# <Target> in <N> shots
<one line: what it is, at most 15 words>

## Shot 1 · <type> · <short title>
**Input:** <the situation, code, or command>
```
<artifact>
```
**Output:** <what happens: result, trace, behavior>
**Signal:** <the one thing this shot teaches>

## Shot 2 …

## Pattern
<3-5 bullets: the rule the shots add up to>

## Coverage
Covered: <abstractions the shots hit> · Not yet: <the rest of the map>

## Your turn
<one held-out case. The user predicts the output; don't give the answer>
````

## Follow-ups
User replies with a prediction → give the answer and say which shot it follows from.
Asked for more → scale up: write more shots aimed at the **more** / **Not yet** list (not variations on covered
ground), and update Coverage until the map is done.
Offer: the detailed version, more shots, or a harder held-out case.
