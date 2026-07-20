---
name: explain-situation
disable-model-invocation: true
description: Explains a blog post, article, paper, product announcement, business idea, codebase, or abstract concept as a problem-solving arc — Situation → Problem → Solution/Action → Impact/Result — the case-study shape consultants and incident reports use. If the source contains several situation→result pairs, every one gets its own four-beat narration. Use whenever the user asks to "explain this as situation/problem/solution", says "explain:situation", mentions SCQA, STAR, or SOAR format, asks "what problem does this solve and did it actually work," wants a case-study or post-mortem style breakdown, or wants an idea framed for a stakeholder who will ask "why did we need this and what did we get." NOT elevator-pitch (one compressed plain-English pitch, no structured beats), NOT explain-stories (character-driven anecdotes), NOT narrative-structure (analyzes the craft of the writing itself) — reach for THIS when the user wants the idea's causal arc as four labeled beats to interrogate one at a time.
---

# Explain: Situation

Situation → Problem → Solution/Action → Impact/Result is the shape of a case study, a consulting
memo, an incident post-mortem, a grant report. Its power is that it turns any idea into a causal
chain a reader can interrogate one link at a time: *Was the situation really like that? Is the
problem real, or manufactured? Does the action actually address that problem? Does the claimed
impact trace back to the action, or would it have happened anyway?* Most explanations blur these
questions together; this format forces them apart, which is exactly what makes weak ideas look weak
and strong ideas look strong in it. Your job is to pour the target into that shape honestly — not to
make it look better or worse than it is.

## Read the target first

Read the whole target (fetch the full URL or file — don't work from a title, snippet, or your prior
sense of the topic) before writing any beat. If the user hands you a bare concept rather than a
document ("explain OAuth as situation→problem→solution"), treat their framing as the target and
draw on your own knowledge as the source material.

## The four beats — and the line between each pair

```
## Situation
The world before the idea: context, who's involved, what was true and stable. Neutral — no tension yet.

## Problem
What made that situation untenable: the cost, risk, limit, or pain. Why the status quo couldn't hold.

## Solution / Action
What was done or is proposed: the intervention and the mechanism by which it attacks the problem.

## Impact / Result
What changed, measured in the problem's own terms — with evidence, tradeoffs, and honest labeling
of what's demonstrated vs. merely expected.
```

Each beat is a short paragraph (or a few bullets, if the source is dense with specifics). The craft
is in keeping the boundaries clean, because each boundary has a characteristic way of smearing:

- **Situation vs. Problem.** The situation must be tension-free — a reader should be able to nod
  along thinking "sure, sounds fine." If your situation paragraph already contains words like
  "unfortunately" or "however," you've let the problem leak backward. The whole point of separating
  them is that the reader gets to judge whether the problem *follows* from the situation or was
  smuggled in.
- **Problem vs. Solution.** State the problem in terms of what it costs, not in terms of the missing
  fix. "Deploys took 40 minutes and blocked the whole team" is a problem; "we didn't have a CI
  pipeline" is a solution wearing a problem's clothes — it presupposes the answer and forecloses
  alternatives.
- **Solution vs. Impact.** The most common failure: impact that just restates the solution ("we
  built a cache" → "now we have a cache"). Impact must be measured in the *problem's* terms — if
  the problem was 40-minute deploys, the impact is what deploy time became, not that a pipeline now
  exists. If the source never closes this loop, that's a finding worth surfacing, not a gap to
  paper over.

## Be honest about what the source actually supports

Keep the source's claims and your own inferences visibly separate. If the target is a proposal or
announcement whose results don't exist yet, write the last beat as **Expected impact** and say what
evidence would confirm it. If the source claims results, report them as claims ("the post reports a
60% reduction") rather than facts you've verified. If you had to reconstruct an unstated beat —
common with pure how-it-works writing that never names its problem — mark it *(inferred — the
source doesn't state this)*. A reader using this to evaluate an idea needs to know which links in
the chain the author actually forged and which ones you added to complete the picture.

## One arc or several

If the target contains multiple situation→result arcs (a retrospective covering three incidents, a
paper with two contributions, a post that solves one problem and then a follow-on problem the fix
created), narrate **every one of them** — each gets its own titled four-beat block, in the order
they appear or grouped logically if they're scattered through the piece. Don't cherry-pick the main
arc and drop the rest: the user may be relying on this to see everything the source actually
claims, and a secondary arc is often where the interesting tradeoff or failure lives. After the
blocks, add a sentence or two connecting them back to the target's central idea.

When the target is a single idea, keep it to one arc — don't split it into fake sub-arcs just to
look thorough; the format earns its keep by clarity, not volume. The test for "is this really a
separate arc?" is whether it has its own situation *and* its own result: a mere sub-step of the
main solution doesn't qualify, but a distinct problem with its own outcome does, even if it's minor.

## A compressed worked example

**Target:** a blog post announcing that a team moved from nightly batch ETL to streaming ingestion.

**Situation:** The analytics team fed its dashboards from a nightly batch job — a well-understood
pipeline that had run reliably for three years while the company's data fit comfortably in it.

**Problem:** The business began making same-day pricing decisions, but dashboards were always up to
24 hours stale — the post describes pricing errors that stood uncorrected for a full day, costing
real revenue. The batch cadence, fine for three years, was now directly misaligned with how decisions
were made.

**Solution/Action:** They replaced the nightly job with streaming ingestion (Kafka into an
incrementally-updated warehouse), keeping the old batch path running in parallel for a quarter as a
correctness check before cutting over.

**Impact/Result:** Dashboard staleness dropped from ~24 hours to under 5 minutes, and the post
reports pricing corrections now land the same hour. Tradeoff acknowledged in the source: the
streaming path costs roughly 2× the batch infrastructure and added on-call burden. *(The post does
not say whether the revenue loss from stale pricing actually stopped — the impact is measured in
staleness, one step short of the problem's own terms.)*

That last parenthetical is the format doing its job: laying the arc out beat by beat is what makes
the unclosed loop visible.

## Edge cases worth handling deliberately

- **Can't access the target** (broken URL, missing file, empty paste): say so plainly and stop —
  don't build an arc from the title or from assumption.
- **Target has no problem** (a pure reference doc, a purely descriptive explainer): don't
  manufacture drama. Either reconstruct the implied problem and clearly mark it as inferred, or
  tell the user the format doesn't fit this target and offer what it *is* (a description, not an
  argument).
- **Target is an opinion or prediction** rather than a done thing: the arc still works — Situation
  and Problem come from the author's framing, the Solution is what they advocate, and Impact is
  their forecast, labeled as such with whatever reasoning they offer.
- **User asks for a specific beat only** ("just tell me what problem this solves"): answer that
  beat well rather than forcing the full arc.
