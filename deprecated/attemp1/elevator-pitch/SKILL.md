---
name: elevator-pitch
description: Distills a blog post, codebase, repo, paper, or abstract concept down to a plain-English elevator pitch — what it actually does, what problem it solves, and in what situation someone would reach for it. Strips away jargon, acronyms, and feature lists in favor of the core "why would I care." Use this whenever the user asks to "boil down," "distill," "explain in plain English," give the "elevator pitch," "tl;dr" (the good kind, not a summary), or asks "what does this actually do / what problem does this solve / who is this for" about an article, a repo, a library, a paper, or an idea they describe. Also reach for it when someone pastes a dense README or technical doc and just wants to know if it's relevant to them.
---

# Elevator Pitch

An elevator pitch is not a summary. A summary compresses everything that's there. A pitch throws
almost everything away and keeps only the one thing that matters: why would a person who has never
heard of this care, and when would they reach for it.

The failure mode this skill exists to prevent is producing a shorter version of the source material
that still requires the reader to already understand the domain. If the reader needs to know what
"idempotent," "middleware," or "attention mechanism" means to get your pitch, you haven't pitched
anything — you've just summarized with a smaller word count.

## Answer three questions before writing a single sentence

Don't start drafting prose. First pin down the answers to these, even just as scratch notes:

1. **What does this actually do?** One plain sentence. No product name jargon, no internal
   terminology. If you had to describe the action/outcome to someone over the phone with no
   visual aids, what would you say?
2. **What problem does it solve, and for whom?** Not "it improves X" — what was broken, slow,
   expensive, or impossible before this existed, and who specifically felt that pain?
3. **When does someone actually reach for this?** The concrete situation or trigger moment. Not
   "when you need X" in the abstract, but the moment in someone's day/project where the problem
   bites hard enough that they'd go looking for a fix.

If you can't answer #3 concretely, you probably don't understand the thing well enough yet — go back
and read more before writing the pitch. A pitch that's vague about the situation ("useful for
developers who want to be more efficient") is a sign the research step was skipped, not a sign the
source material was thin.

## Reading the source

How you gather the answers above depends on what you're pitching:

**Blog posts / articles.** Read the whole thing — don't stop at the intro or the abstract, since
the actual insight is often buried in the middle after the throat-clearing. If given a URL, fetch
and read it. Look past the author's own framing for the underlying claim: authors often bury the
lede in academic hedging or narrative setup. Ask yourself "what's the one idea here that would
change how someone acts or thinks, if they only remembered one thing a week later?"

**Codebases / repos.** Don't just paraphrase the README — READMEs are often written by people too
close to the project to see it from the outside, and inherit the same jargon problem you're trying
to fix. Instead, look at: what does running this thing actually produce or enable? What would the
user otherwise have had to do by hand, or pay for, or build themselves? Check entry points, the
top-level example/quickstart if one exists, and issues or the first few lines of the repo
description for clues about who uses this and why. If it's a library, ask "what capability does
importing this give me that I didn't have five minutes ago?"

**Concepts / papers / ideas described to you directly.** Here you don't have a document to mine —
the user's own explanation IS the source, and it may already contain their own jargon. Ask
clarifying questions if the core mechanism or the problem being solved isn't clear yet; don't
guess and produce a vague pitch. It's fine to reflect back "so the problem this solves is X,
right?" before writing the final version.

**Anything else.** The same three questions apply regardless of medium. If the source type doesn't
fit neatly into the categories above, don't force it — just make sure you've actually understood
the thing (not skimmed it) before condensing it.

## Calibrate the audience: smart generalist

Write for a sharp person who is not in this field, not for a total beginner and not for a peer
expert. That means:

- Don't explain what a website, an app, or "code" is — the reader has that context.
- Do explain what a specific technical mechanism, acronym, or piece of jargon *does in plain terms*
  the first time it would otherwise appear — or better, just don't use the term at all if a plain
  description works just as well.
- A useful test: could you say this pitch out loud to a sharp friend from a completely different
  field, at a party, and have them immediately get why it matters — without them needing to ask
  "wait, what's that?"

Jargon creeps back in more often through acronyms and internal/product-specific names than through
obviously technical words — watch for those specifically, since they're easy to miss because they
feel like plain language to anyone already familiar with the source.

## Choosing the shape of the pitch

Two shapes work, and which one fits depends on the material, not on a fixed rule:

**A pure pitch paragraph** (3-5 tight sentences, no headers) works when the pitch is single-threaded
— one problem, one audience, one situation. It reads more naturally and is easier to actually repeat
to someone else, which is the whole point of an elevator pitch.

**A structured mini-brief** (one-liner / problem it solves / when to use it, each 1-2 sentences)
works better when there are genuinely multiple distinct problems solved, multiple different
audiences, or multiple trigger situations that would get muddled into a run-on sentence if forced
into one paragraph.

Default to the paragraph. Only reach for the structured version when the paragraph is starting to
sprawl or you notice yourself listing more than one "and it's also useful for..." clause.

Either way, keep the whole thing short enough to read in about 15-30 seconds. If it's taking a full
minute to read, it has drifted from pitch back toward summary — cut, don't just compress the wording.

## Failure modes to catch before showing the pitch

- **Feature list instead of problem.** "It has X, Y, and Z" is a spec sheet, not a pitch. Every
  feature you mention should be in service of explaining the problem or the situation, not just
  listed because it exists.
- **Vague benefit language.** "Makes things easier," "improves efficiency," "streamlines the
  process" — these are true of almost anything and tell the reader nothing concrete. Replace with
  the specific before/after: what exactly was hard, and what's true now instead.
- **Explaining HOW instead of WHAT/WHY.** The mechanism is usually not the pitch. Someone deciding
  whether to care needs the problem and the payoff first; the mechanism only matters if they're
  already convinced it's relevant to them.
- **Jargon smuggled back in.** Re-read your own draft as if you were the smart-generalist reader.
  Any acronym, internal name, or term of art that survived without a plain-language gloss should be
  cut or explained.

## Examples

**Codebase, paragraph form:**
> This is a payments API that lets a developer accept credit cards by adding a few lines of code,
> instead of negotiating bank contracts and building compliance infrastructure themselves. It solves
> the problem of payment processing normally being a multi-month, specialist-heavy slog for a small
> team that just wants to charge a customer's card. Reach for it the moment your product needs to
> move money between a customer and your business and you don't want to hire someone whose whole job
> is banking compliance.

**Research paper, structured form (multiple distinct use situations):**
> **One-liner:** A way to compress a neural network so it runs on a phone instead of a data center,
> with barely any drop in accuracy.
> **Problem it solves:** Good models are normally too big and slow to run on a device in someone's
> pocket, forcing apps to send data to a server and wait for a response.
> **When to use it:** Any time an app needs to run recognition or prediction instantly, offline, or
> without sending the user's data off their device — voice assistants, camera features, anything
> where a round trip to a server is too slow or too invasive.

**Blog post, paragraph form:**
> This post argues that most teams' code review process optimizes for catching typos and style
> nits while missing the bugs that actually cause outages, because reviewers default to skimming
> for surface issues instead of tracing what the change actually does at runtime. It matters for
> any team that's been burned by a reviewed, approved change still breaking production — the fix
> isn't more review, it's reviewing differently.
