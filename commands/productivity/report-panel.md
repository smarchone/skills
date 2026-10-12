---
description: Turn a talk, video, article, or launch into a short report a CEO, PM, and Architect can each read in their own segment: what the product is, how it fits together, and what it means for each of them.
disable-model-invocation: true
argument-hint: "<source url or file> [for whom] [output path]"
---

# Report panel

Someone watched (or skipped) a talk, demo, or launch and wants the **product experience** pulled out
of it: what was shown, how the pieces fit, and what it means. The same source gets read by
different people for different reasons, so the report gives each one a segment of their own.
In the AI age the moat is experience and trust, not the model. Read the source with that lens.

## Get the source
- Read the actual source, not what you know about the title. Video → transcript; if captions are
  missing, try other caption tracks or languages, and use the description and chapter timestamps.
- Say how good the source is in one line at the top: transcript quality, names you corrected,
  parts that were Q&A or off-topic. Numbers from a rough source are *directional*.
- The given source is the job. Don't go fetching other pages without asking.

## The report
Clear and concise. Every segment answers a question the others don't; if two say the same thing,
cut one. Mark anything you inferred rather than heard with **⚑**.

````text
# <Product>: <one-line angle>
**Source:** <title, speakers, link, length> · **For:** <reader>
> Source note: <quality caveats, in one line>

## CEO note
What's happening · why it matters (where the moat is) · the real constraint ·
opportunity / threat / watch · one-line bottom line.

## The product
**Capabilities:** table of capability · what it does · where it sits · status (per source).
**How it fits:** an ASCII diagram of the pieces, then the loop in one line (a → b → c → back to a).

## PM view
The experience vision (where work starts, how the user's role changes, what goes away) ·
impact claimed, with numbers · novel approaches (the ones that change the experience, not features)
· gaps and open questions.

## Architect view
Layers (component · key property) · key design decisions (chosen · gives up) ·
hard problems, stated or ⚑ inferred · extension points.
````

Who reads it decides the order and the weight: lead with that reader's segment. The user names
other roles (designer, investor, SRE) → add or swap a segment.

## Don't
- **Add mental models, analogies, or frameworks of your own.** They tend to restate what's already
  in the report and don't change a decision. Stick to what the source says and what it implies.
- Pad with a TL;DR that repeats the CEO note.

## Follow-ups
The user asks for a new segment → add it in its place, keep the rest, and fold in any existing
section that belongs to it rather than making two. Asked to remove one → remove it cleanly.
