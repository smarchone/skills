---
name: intuition
description: Build deep intuition on a topic, blog, paper, or concept by attacking it from many complementary angles. Writes intuition_{topic}.md.
---

# Intuition

Help the user genuinely *understand* an idea — reconstruct it, explain it, spot it in the wild, know
its edges — not memorize a definition. You do this by hitting one concept from many independent
angles; each is a different cognitive handle, and together they triangulate real understanding.

The deliverable is a keepable markdown file, `intuition_{topic}.md`.

## What makes this work

The failure mode is a polished doc that's just a Wikipedia summary rephrased eight ways. Each
section exists to force a *different* kind of thinking — compression (what's the core?), motivation
(why does this exist?), reconstruction (could you derive it?), honesty (where don't you get it?). If
two sections start saying the same thing, one is failing. Be concrete: vivid specific examples beat
abstract restatement — the reader should feel it click, not nod politely.

## Step 1 — Get the source

URL → fetch and read it (build on the actual content, not your prior knowledge of the title). File →
read it. Pasted text → use directly. Bare topic → use your knowledge, but if it's obscure, niche, or
fast-moving, say so and offer to fetch — intuition on a hallucinated idea is worse than useless. If
the topic is broad ("machine learning"), ask the user to narrow it. One concept per doc.

## Step 2 — Understand it yourself first

Before writing, make sure *you* grasp the non-obvious part. If you can't name the single key insight,
reread the source — the doc's quality is capped by your understanding.

## Step 3 — Write intuition_{topic}.md

**Default: keep it tight.** Lead with **Elevator Pitch**, **The Key Insight**, **Explain in Levels**,
and add one or two other angles only where they earn their place. A short doc that lands beats a long
one the user won't reread. **Only on "go deep" / "be thorough"** use the full toolkit — every
section, richer examples, longer ladders.

Order what you include so the doc builds: hook → motivation → deeper angles → honesty check. Skip
any section that doesn't fit rather than forcing it.

### Template

```markdown
# Intuition: {Topic}

## Elevator Pitch
[3-4 sentences: the whole idea for a smart person in a hurry.]
**If you remember nothing else:** [one sentence — the irreducible core.]

## The Key Insight
[The single non-obvious "aha" the idea rests on — the thing that makes everything
else feel inevitable. Name it. What did people believe/do before, and what flipped?]

## Why It Exists (STAR)
- **Situation:** [the world/status quo before this idea]
- **Task:** [the problem or tension that needed resolving]
- **Action:** [what this idea actually does — the move it makes]
- **Result:** [what changed; what it unlocked]

## Analogy — and Where It Breaks
[One vivid concrete analogy, then where it fails. The breaking point is usually
exactly where the real subtlety lives, so much of the intuition transmits here.]

## Explain in Levels
**To a student:** [plain language, one simple example, no jargon.]
**To an engineer:** [how it works mechanically, tradeoffs, when to reach for it.]
**To a PhD:** [precise formulation, assumptions, deeper connections, open subtleties.]

## Rediscover / Apply It (Simulated Conversation)
[A short natural dialogue driven by real reasoning, not scripted Q&A. Pick the fit:
 REDISCOVER — two people reason from a problem toward the idea ("what if... no,
 that fails because... so we'd need..."), showing it as an inevitable answer; or
 APPLY — someone works a concrete real situation through the idea.]

## Question Ladder
[A chain of questions that drills DOWN to first principles ("but why is that true?")
or builds UP to the full idea. Include short answers or leave some as self-tests.
Following the chain should reconstruct the concept from the ground.]

## Feynman Gap-Check
[Explain the whole thing simply, then honestly flag the 2-3 spots where the simple
version hand-waves. These gaps are the reader's to-do list — where understanding is
still borrowed, not earned. Honesty here beats sounding complete.]
```

## Step 4 — Hand it off

Save as `intuition_{topic}.md` (snake_case short slug, e.g. `intuition_backpropagation.md`). Tell the
user where it is and offer to go deeper on any single section they want to dwell on.
