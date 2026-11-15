---
description: Simulated experience in a few lines. A situation, scattered dots, someone across the table, and you connecting them. Then a look at how engineers at higher levels would have connected the same dots. The lighter sibling of connect-the-dots.
disable-model-invocation: true
argument-hint: "[a role and a situation] [with <who>]"
---

> **Bundled command:** Relative references to `experience.md` are inlined in **## Bundled skill files** at the end of this file. Resolve those references from that section instead of reading from disk.

# Dots

Experience is what seniors/experts have and juniors can't buy. This is a way to get some of it: live through a
situation, connect the dots yourself, then see how someone further along would have done it.

## The constructs

- **Situation:** something going wrong in a role and domain, with a hidden truth behind it.
  - one truth: there is a cause to find
  - few truths: options to weigh and rank
  - no single truth: a position to defend
- **Dots:** observations that point to the truth, along with some that don't. They are fixed for the
  whole situation.
- **The person across the table:** a colleague, a mentor, a CTO, an interviewer. They set the stakes and
  the mood, but never the facts.
- **Connection:** the user's own work of linking dots into a cause, a choice or a stance.
- **Board:** the investigation made visible. The dots found so far and the links the user has drawn
  (only theirs), with open questions marked `?`. It grows as they go.
- **Closing:** a clear statement to the people who need it, in the user's own words.
- **Ghosts:** the same situation as an L3, an L5 and a Staff engineer would have played it. The gap
  between them is the lesson.
- **Habit to steal:** the one thing to carry into the next real situation.
- **Two axes:** competence (did they work out what happened?) and conduct (did they handle it?).

## The situation file

Before the first line, the situation, the dots and the hidden connection are written to a temp
file (`${TMPDIR:-/tmp}/dots/<slug>.md`), and the session keeps going back to it. Every reveal, the board
and the ghosts come from the file, not from memory, and nothing in it changes once play starts.

## The experience

How the conversation feels is in `experience.md`.

It feels like real work with a real person, not a quiz. The user does the thinking, and the dots open up
because of the questions they ask. In a chat window it's the quality of the questions that matters, not
how thorough they are. They leave seeing how someone a level up would have thought, carrying one habit,
and wanting another situation. Being judged is something they ask for, not something done to them.

---

## Bundled skill files

The files below are bundled from the skill directory. Infer any relative file or directory references above (e.g. `experience.md`, `packs/`) from these sections instead of reading from disk.

<!-- BEGIN BUNDLED FILE: experience.md -->
### `experience.md`

# Experience

The problem can be hard. The conversation never is.

- **One thing at a time.** Each turn is short: a line or two of talk, at most one dot.
- **Plain words.** It sounds like people talking. The role's own jargon is fine, filler and narration aren't.
- **Pictures carry the data.** A dot looks like what it is (a graph, a log, a table, a photo described)
  as a small ASCII visual, so the user reads it at a glance instead of parsing prose.
- **The board.** It comes back whenever things shift, so nothing has to be held in their head:

```
┌ board ──────────────────────────────────────────┐
│ [p99 2.4s since 10:40] ──?── [inventory deploy] │
│ [DB pool 50/50] ──because── [traffic 1.7x]      │
│ [orders flat]                                   │
└─────────────────────────────────────────────────┘
```
- **The hard part is the thinking.** The difficulty lives in the dots and how they connect, never in
  decoding what was said.
<!-- END BUNDLED FILE: experience.md -->
