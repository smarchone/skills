---
name: explain-simulation
disable-model-invocation: true
description: >-
  Explains a blog post, article, file, codebase, design doc, or abstract idea by
  simulating a concise, realistic conversation between people who'd actually need
  to discuss it — an incident-review team, stakeholders in an alignment meeting,
  engineers in a design critique, a founder facing a skeptical investor — not a
  generic teacher-explains-to-student dialogue. The scenario matches the
  content: whatever setting would force the key facts and tradeoffs to the
  surface. Use whenever the user asks to "explain this as a conversation,"
  "simulate a meeting about this," "turn this into a dialogue," "make this a
  scene," "roleplay a discussion of this," or wants an idea made vivid through
  dialogue. This is NOT explain-socrates (a Q/R dialogue stress-testing an
  argument) and NOT explain-stories (a Setup/Conflict/Resolution/Lesson
  narrative, not real-time dialogue) — the product is a live conversation whose
  participants have their own stakes, and the explanation emerges from them
  working something out.
---

# Explain: Simulation

A lecture states facts. A meeting *produces* them — someone asks a question because they genuinely
don't know the answer, someone else pushes back because it affects their part of the system, and the
key facts come out as a side effect of people trying to get something done. That "as a side effect"
quality is the entire value of this skill. A conversation that exists only to inform the reader reads
like a textbook wearing a costume — two characters saying "as you know, Bob" to each other. A
conversation where the participants have real, separate reasons to be in the room reads like
something that actually happened, and readers remember it.

The failure mode to avoid is picking a bland, one-size-fits-all frame (generic "expert explains to
curious learner") and copy-pasting the target's content into alternating lines. If the scenario you
picked wouldn't change even if you swapped in a completely different topic, you haven't done the
work — the scenario has to be *load-bearing* for this specific content.

## Read the target first

Read the whole thing before writing anything — fetch the complete URL, read the full file, or take
the full pasted text/idea as given. Don't work from a title, a skim, or your own prior knowledge of
the topic. You need to know what's actually being claimed, decided, or built before you can figure out
who would realistically be arguing about it.

## Step 1 — Find the thing worth arguing about

Every target has some point of friction: a decision that could have gone another way, a claim a
skeptic would poke at, a mechanism that's easy to get wrong, a tradeoff someone had to accept, a
step that isn't obvious until you've been burned by skipping it. Find that point before picking a
scenario — it's what the conversation needs to be *about*. A target with no friction at all (a plain
factual list, a simple announcement) can still work, but be honest with yourself about whether a
dialogue is actually earning its keep versus a bulleted summary would do the same job faster.

## Step 2 — Pick the scenario the friction belongs to

Ask: in the real world, who would actually need to hash this out, and in what setting? The scenario
should be the natural habitat of the friction you found in Step 1 — not a container bolted on
afterward. Some examples of the kind of match you're looking for (illustrative, not a checklist):

- A prod bug fix or postmortem → an incident review or on-call handoff, where the friction is "why
  did this actually break and why does the fix hold."
- A product or feature idea → a stakeholder alignment meeting or a founder pitching a skeptical
  investor, where the friction is "why should we believe this is worth doing."
- A design doc or architecture choice → a design review or code critique, where the friction is
  "why this approach and not the obvious alternative."
- An essay or blog post making a claim → an editorial meeting, a podcast interview, or a hallway
  argument between two people who read it differently, where the friction is "is this actually
  true, and what would change your mind."
- A piece of code → two engineers pairing on it, where the friction is "why does this line matter,
  what happens if you delete it."

Pick (or invent) whatever setting best matches the *specific* friction you found — these are
starting points for your own judgment, not a lookup table. The scenario is doing its job if
swapping in a different topic would force you to pick a different scenario too.

## Step 3 — Cast people with stakes, not roles

Give each participant a reason to be in the room that isn't "explain things to the reader." A name
and a one-clause job/stake is usually enough — "Priya, the on-call engineer who got paged," "Marcus,
an investor who's been burned by this exact pitch before," "Devon, who wrote the original code and
is defensive about it." Two to four participants is normally right; use as many as the scenario
actually needs, not more. Every participant should want something out of the conversation (an
answer, a decision, to be proven right, to protect their own work) — that want is what drives their
lines, not a need to relay information.

Ground every line in specifics pulled from the target — real numbers, quotes, function names,
claims — rather than a vague paraphrase. A generic dialogue that could be reskinned onto any topic
means you weren't actually reasoning about *this* target.

## Step 4 — Write it, and stop when it's landed

Length should be driven by clarity, not a target line count — some targets land in six lines, others
genuinely need twenty. The discipline is: every line either asks the question a real reader would be
stuck on, reveals a fact, corrects a wrong assumption, or advances the room toward whatever it's
there to decide. Cut anything that's just scene-setting filler or a character restating what was
just said.

Include at least one moment of real friction inside the dialogue itself — a wrong guess, a pushback,
a "wait, that doesn't add up" — and let it get resolved on the page. This is what separates a
simulation from a Q&A wearing dialogue formatting: understanding should visibly change over the
course of the conversation, not just get stated once cleanly.

End when the friction from Step 1 has actually been worked through — not with a moral or a summary
line tacked on. The conversation itself is the deliverable; if it needs a "and that's why X matters"
coda to land, the dialogue didn't do its job and is worth another pass.

## Format

```
**Scene:** [one line — where this is happening and why, right now]

**[Name], [stake/role]:** ...
**[Name], [stake/role]:** ...
...
```

Keep the scene-setting line to one sentence. Don't add stage directions or narration beyond that
line unless a physical action is genuinely load-bearing (someone pulling up a dashboard, pointing at
a diff) — the words people say should carry the explanation.

## Edge cases worth handling deliberately

- **Can't access the target** (broken URL, missing file, empty paste): say so plainly and stop —
  don't simulate a conversation about content you never actually read.
- **Target has no real friction** (a plain changelog entry, a simple factual announcement): say so,
  and either produce a much shorter dialogue than usual or suggest that a plain summary would serve
  the reader better than forcing a scene.
- **Target is dense or covers several independent points**: don't cram every point into one
  meeting — either pick the single most load-bearing point of friction, or, if the user clearly
  wants full coverage, use one scene per major point rather than one overstuffed scene.
- **User names a scenario explicitly** ("simulate a standup," "make it an investor pitch"): use
  their framing rather than picking your own, even if you'd have chosen differently — but still
  apply Step 3's discipline (real stakes, real friction) inside it.

## A short worked example

**Target:** a design doc proposing a move from synchronous request/response to an async job queue
for a report-generation endpoint, justified by "reports can take up to 90 seconds and we're seeing
timeout errors."

**Scene:** Design review, 15 minutes before the doc gets signed off.

**Priya, backend lead proposing the change:** The core problem is we're holding an HTTP connection
open for up to 90 seconds. Anything client-side with a 30-second timeout just fails.

**Devon, on-call for the endpoint:** So make the timeout longer. Why add a whole queue?

**Priya:** Because it's not just timeouts — every one of those open connections holds a worker the
whole time it's running. At peak we've had reports queue up behind each other because there weren't
enough workers free.

**Devon:** Okay, that part I didn't know. So the queue isn't really about the 90 seconds, it's about
not tying up a worker for the whole 90 seconds.

**Priya:** Right. Client gets a job ID back immediately, worker's free again in milliseconds, and we
poll or push a webhook when the report's actually done.

**Devon:** What happens if the poll never comes — client walks away, job's still running?

**Priya:** Job finishes either way, result sits in the queue's result store for an hour. We're not
losing work, just decoupling "is it done" from "is the connection open."

**Devon:** That's the sentence that should be in the doc, honestly — "decoupling is-it-done from
is-the-connection-open." I'd have signed off on this eventually but I was picturing the wrong
problem.
