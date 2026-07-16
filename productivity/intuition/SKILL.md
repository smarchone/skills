---
name: intuition
description: Build deep intuition on a topic, blog, paper, or concept by attacking it from many complementary angles.
user-invocable: true
disable-model-invocation: true
---

# Intuition

Help the user genuinely *understand* one idea — reconstruct it, spot it in the wild, know its edges
— not memorize a definition. Each section below is a different cognitive handle; together they
triangulate. **If two sections start saying the same thing, one is failing** — that's the whole
failure mode here, a Wikipedia summary rephrased eight ways.

## Step 1 — Get the source

URL or file → read it; build on the actual content, not your prior knowledge of the title. Pasted
text → use directly. Bare topic → use your knowledge, but if it's obscure, niche, or fast-moving,
say so and offer to fetch — intuition on a hallucinated idea is worse than useless. Broad topic
("machine learning") → ask the user to narrow it. One concept per response.

Then make sure *you* grasp the non-obvious part. If you can't name the key insight, reread — your
output is capped by your understanding.

## Step 2 — Write it

**Keep it tight.** Lead with **Elevator Pitch**, **In the Wild**, **The Key Insight**, **Explain in
Levels**; add more only where they earn their place. Order so it builds: hook → motivation → deeper
angles → honesty check. Skip what doesn't fit rather than forcing it.

**Applicability is the motivation.** Nobody wants an idea; they want it *for* something. The
situation comes before the answer — a reader who feels the pressure will chase the insight, and one
who doesn't won't care what flipped. When in doubt, make the situation more concrete, not the
explanation more complete. **Only on "go deep" / "be thorough" /
"more"**: the full toolkit, richer examples, longer ladders.

**Be concrete.** A vivid specific example beats abstract restatement — the reader should feel it
click, not nod politely.

**Be skimmable.** Density is not depth, and insight the reader gives up on is worth nothing. One
idea per paragraph, whitespace between them, repeating content in a repeating labeled shape. Bold
the phrase that carries the point, not whole sentences — skimming the bold and headers alone should
still deliver the shape of the idea.

### Sections

<!-- ALT blocks are candidate rewrites — pick one, delete the other. Not both. -->

```markdown
# Intuition: {Topic}

## Elevator Pitch
Not a summary. A summary compresses everything that's there; a pitch throws
almost all of it away and keeps only: why would someone who's never heard of this care,
and when would they reach for it. 3-4 sentences, no jargon, no feature list. If it reads
like a shorter version of the source, it failed.]
**If you remember nothing else:** [one sentence — the irreducible core.

## In the Wild (STAR)
One concrete situation where this idea is the right answer — the reader's reason to care.
**Invent it if the source has none**: this is a recognition template, not a historical
claim. Specific enough to picture, typical enough to generalize.

- **Situation:** [the setup. Plant the details that will turn out to matter.]
- **Task:** [what forces a move — the reader should feel the pressure BEFORE seeing the
  answer. If they'd shrug, the situation is too comfortable; make it bite.]
- **Action:** [the idea, applied. The move, not the theory.]
- **Result:** [what changed — and what it cost. Every application has a bill.]

**The tell:** [the 1-2 features of the Situation that signalled "this idea applies here."]

Two rules do the work. A Result with no cost is an ad. And the tell is the point of the
whole section — four beats about a scenario is a story; four beats that end with the
signature you'd recognize next time is intuition.

## The Key Insight
The one non-obvious thing everything else follows from. Test: state it, and
the rest of the idea should feel forced rather than invented. Name what people believed
or did before, and the exact belief that flipped. If you can't say what flipped, you've
found a feature, not the insight — keep looking. Only one; a list means you missed it.

## Negative Space
What it is NOT. For each near-neighbor, the distinction must be a CONSEQUENCE,
not a category — "a cache is not a database" is useless; "a cache can vanish without
consequence" is the boundary. "Not a queue" → order doesn't matter. Two or three
neighbors, then the problem it never claimed to solve. If a neighbor is "kind of the same
thing," you haven't found the consequence that separates them yet.

## Failure Space
Where the idea breaks. Every idea rests on assumptions that hold in the cases it was built
for; a failure mode is one of them silently ceasing to hold. Give 2-3, each on its own
labeled lines — never one dense paragraph per mode:

**{Short name — 2-4 words}**
- **Trigger:** [the condition that sets it off. One line.]
- **Mechanism:** [what actually goes wrong. "It doesn't scale" is a symptom — say WHY.]
- **Breaks:** [the assumption nobody knew they were making.]

The Breaks line should read like something nobody would think to say out loud ("reads and
writes are the same budget") — that's the tell you found an assumption and not a caveat.
Prefer failures where nothing warns you: it keeps running, looks fine, quietly wrong.
Include misuse only when the idea invites it — a shape that's routinely misapplied is a
property of the idea, not its users.

If you can't break it, you don't understand what's holding it up yet.

## Explain in Levels
**To a student:** [plain language, one simple example, no jargon.]
**To an engineer:** [how it works mechanically, tradeoffs, when to reach for it.]
**To a PhD:** [precise formulation, assumptions, deeper connections, open subtleties.]

Not three separate explanations — one explanation at three resolutions. Each
rung REFINES the one before and must never contradict it: a reader who stops at rung 1
walks away with something TRUE, not a lie they'll unlearn at rung 3. The usual cheat is a
simple-but-false story at the bottom; if rung 3 has to say "actually, that's wrong,"
rung 1 is broken. Each rung adds precision the last one lacked, not a correction.


<!-- Note on SIMULATIONs: Both dialogues: named speakers, one point per turn, ~6-10 turns. Real reasoning,
not scripted Q&A where one side only asks and the other lectures. Cut pleasantries and
throat-clearing — every line either advances the argument or goes. Usually include one,
not both; use both only when going deep. -->

## Rediscover It (Simulated Conversation)
Two people who do NOT know the idea reason their way into it from the problem
alone. They must propose at least one wrong answer and discover why it fails — that
wrongness is the whole point, because it shows what the real idea is buying. End at the
moment it becomes the only move left, not with someone announcing its name. If either
speaker already knows the answer, you're writing a lecture with two mouths.

## Apply It (Simulated Conversation)
Pick the scenario that FORCES the tradeoffs to the surface — an incident
review, a design critique, a founder in front of a skeptical investor, a code review
where someone has to defend a choice. Never a generic teacher-explains-to-student.
The scenario is the design decision: choose one where the idea's cost, not just its
benefit, has to be paid out loud in front of someone who'll push back


## Question Ladder
Questions that drill DOWN to first principles ("but why is that true?") or build UP
to the full idea. Each question must attack the previous ANSWER — a question that
moves to a new subtopic is an FAQ, not a ladder. Bottom out somewhere you genuinely
can't push further, then reassemble the concept from what the descent uncovered.
Include short answers, or leave some as self-tests.

Map it as a DAG in ASCII — don't pick a shape up front, let the questions produce one.
An answer with one weak point yields a line; several independent ones, branches; and
when distant branches bottom out on the SAME thing, they converge. All three are the
same drawing. The load-bearing insight is the node with the most arrows into it, and
seeing them meet is what prose can't show. Terse nodes; say why each convergence
happens. Don't force a merge that isn't there — a ladder that stays a line is a line.

Example (backprop):

        How does a neural net learn?
       /            |               \
  What is a    Which direction     How big a
   loss?       reduces it?          step?
      \          /      \             /
       \        /        \           /
      Why differentiable?  Why is wiggling
              |            each weight slow?
               \                /
            A net is composed functions
                 f(g(h(x))) — layers stack
                        |
                    CHAIN RULE
                 ┌──────┴──────┐
          Local derivatives   Shared subterms
          are cheap           can be reused
                 └──────┬──────┘
                    BACKPROP

Both "why differentiable" and "why is wiggling slow" look unrelated — loss surface vs.
compute cost — but both land on composition. That shared node is the payoff.

## Feynman Gap-Check
Feynman's claim: if you can't explain it simply, you haven't understood it —
you've memorized its vocabulary. So this is a diagnostic, not a simplification. Explain
the whole thing plainly, and watch for the exact moment you reach for a term you can't
unpack, or a phrase like "and then it just works" / "for various reasons" / "somehow."
Each of those moments is a real gap — name 2-3 of them and say what would close it.
The gaps are the reader's to-do list: where understanding is borrowed, not earned.
Naming them beats sounding complete; a gap-free answer here means you didn't look.
```