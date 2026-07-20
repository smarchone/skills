---
name: explain-big-picture
disable-model-invocation: true
description: >-
  Explains a concept, idea, technology, blog post, or file by placing it in its
  surrounding ecosystem — what it depends on, what depends on it, what it's
  commonly used alongside — and in time: the vision it points at and the
  trajectory of plausible outcomes it could land on. This is a zoom-OUT
  explanation (opposite of explain-feynman's zoom-IN to first principles): it
  shows where the target sits relative to everything around it and where it's
  headed, not its own internals. The ecosystem and trajectory framing always come
  from general knowledge, even when the source never discusses its own context.
  Use whenever the user asks "where does this fit," "how does this fit into the
  bigger picture," "what does this depend on," "what's this part of," "zoom out
  on this," "what's the context here," "what does this connect to," "where is
  this headed," "what's the vision / endgame here," "what could this land on,"
  or wants to understand something in relation to the broader stack, field, or
  future it lives in.
---

# Explain: Big Picture

A concept explained in isolation is a fact. A concept explained in its ecosystem is understanding —
because knowing what something depends on tells you how it breaks when a dependency changes, and
knowing what depends on it tells you why it matters enough to exist. Most explanations describe the
inside of a box; this skill describes the wiring around it — and then follows the wires forward:
every idea points somewhere (a vision) and is in motion toward some set of plausible outcomes (a
trajectory). The zoom-out is in space *and* in time.

## Read the target, but build the context yourself

Read the full target so you understand exactly what it is and does. But the ecosystem framing itself
should always come from your own general knowledge of the space — don't just repeat back what the
source says about its own context, even if it says something. The value of this skill is the outside
view: what someone who knows the surrounding landscape would tell you that the source, focused on
itself, doesn't say.

## Produce a report with these sections

### 1. Where This Sits

Describe the target as a layer in a chain, not a standalone thing:

- **Depends on / built on top of:** name 2-4 concrete things (prior technologies, ideas, or
  preconditions) this target requires or assumes in order to exist or function, and briefly say why
  each one is load-bearing rather than incidental.
- **What relies on it / what it enables:** name 2-4 concrete things downstream — technologies,
  practices, or outcomes — that use this target as a foundation, and briefly say what they'd lose or
  have to do differently without it.

Write this so the reader comes away with a mental picture like "downstream of X and Y, upstream of
Z" — a chain, not a scattered list. If the target is a technical thing, this is often a real
dependency graph. If it's a broader idea (a strategy, a methodology, a social trend), "depends on"
becomes "presupposes" and "enables" becomes "makes possible" — the same shape of reasoning, looser
mechanics.

### 2. Commonly Paired With

Name 2-4 things the target is typically found running or discussed alongside — not a dependency
(neither strictly needs the other), but things that travel together often enough that seeing one
usually means the other is nearby. Say briefly *why* they tend to co-occur — a shared root cause,
solving complementary problems, or one making the other more attractive to adopt. This is the
difference between "what this needs" (section 1) and "what it tends to run into in the wild"
(this section).

### 3. Concrete Examples in the Wild

Give 2-3 short (2-3 sentence) real examples — actual products, companies, papers, or situations —
where you can see the target operating together with its dependencies and pairings from sections 1
and 2. The point of this section is to make the ecosystem placement tangible rather than abstract:
a reader should be able to picture an actual system, not just a list of related nouns. If the target
is genuinely obscure enough that well-known real examples don't exist, say so and use a plausible,
clearly-labeled illustrative scenario instead of forcing a real example that doesn't quite fit.

### 4. The Vision — Where This Points

Every idea, technology, or argument implies a destination: the state of the world if it fully
succeeds on its own terms. Name it in a few sentences. If the source states its vision outright,
report that — but also say whether the stated vision and the *implied* one match, because they
often don't (a tool pitched as "just a faster X" whose design only makes sense as a replacement
for the whole category is a common pattern worth calling out). If the source never states one,
infer the most reasonable vision from what the thing is built to do, and mark it as your inference.
The vision is the fixed reference point that makes the next section readable: trajectories are only
meaningful relative to where the thing is trying to go.

### 5. Trajectory — The Landing Space

An established idea is in motion, and it lands somewhere — but rarely on exactly its vision. The
job here is to explore the space of plausible landings, not to predict one. Sketch **2-4 distinct
landing zones**, each a genuinely different end-state, such as: becomes invisible infrastructure
(the default nobody discusses), settles into a durable niche, gets absorbed as a feature of
something bigger, gets superseded by a successor that keeps its core insight, or fades with its
moment. For each landing, give:

- **The landing:** one sentence describing the end-state.
- **What drives it there:** the force or condition that makes this landing likely — adoption
  economics, a dependency from section 1 shifting, a pairing from section 2 winning or losing.
- **A signal to watch:** one concrete, observable early indicator that the idea is heading for
  this landing rather than the others.

This section is structured speculation, so keep it honest: derive the landings from the real forces
mapped in sections 1-3 (a trajectory disconnected from the ecosystem is just a vibe), draw on what
historically happened to comparable things, and don't rank the landings with false confidence —
if one is clearly most likely, say so and why; if it's genuinely open, say that instead.

### 6. The Big Picture, in One Paragraph

Close by synthesizing sections 1-5 into a single paragraph that answers "where does this actually
sit, where is it headed, and why." This should read like what you'd say if someone asked you to
place the target on a whiteboard diagram of its whole field in ten seconds — one dot for where it
is, one arrow for where it's going.

## Calibrate to the target

A specific technology (a library, protocol, algorithm) usually has a real, checkable dependency
graph — be concrete and technical in section 1. A broader idea (a business model, a cultural shift,
a management practice) has softer, more interpretive dependencies — lean on "presupposes" and
"makes possible" rather than forcing a rigid technical-sounding structure onto something that isn't
one. Either way, resist the urge to pad any section with weak or generic connections just to hit a
number — two sharp, specific dependencies beat four vague ones.

The same calibration applies in time. A mature, settled target (TCP, double-entry bookkeeping) may
have already landed — if so, section 5 collapses to naming the landing that happened and, at most,
what could still dislodge it. A brand-new idea has a wide-open landing space and thin evidence, so
lean harder on comparable historical cases and label the speculation as such. Match the confidence
of the trajectory to the amount of motion actually left in the thing.
