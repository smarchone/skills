---
name: todo
description: >-
  Encode an existing repo (code, skills, specs, intent notes) as a compact TODO file at its root: a plain-text decision workspace where the human iterates on the idea. Captures the pitch, layout, nouns, rules and flows that are decided, plus what's next, open and later. Use when the user asks for a TODO, a "workspace to iterate on the idea", a compact picture of a repo for making decisions, or to refresh one.
argument-hint: "[path to repo, default: current] [focus]"
disable-model-invocation: true
---

# todo

Write `TODO` (no extension) at the repo root: the one file the human opens to think and decide. Not a task
list, not docs. It holds what is **decided** (so it can be argued with) and what is **not yet** (so it can be
decided). The human edits it by hand; you keep it true to the repo.

## Process

1. **Read the source itself.** Code, skills, packs, configs, and any intent/notes/README. Notes say what was
   meant; files say what is true. Where they disagree, the file wins and the gap becomes an open question.
2. **Find the shape:** the one-line idea and for whom · the layout that matters · the 4–8 nouns everything else
   is a dial on · the rules that make it what it is · the main flow(s) · what's half-done, unsettled, or parked.
3. **Merge, don't list.** If two files say the same rule, write it once. If they contradict, write the version
   the repo uses and put the contradiction under `open questions`.
4. **Write** the file below. Show the user the sections in 4–6 lines and say what you couldn't settle.

## The file

Plain text, lowercase, terse. ASCII for structure. Sections in this order; drop any that would be empty.

```
<name> -- <what it is, one line>.
<who it's for / what they get. 1–2 lines. the stance it takes.>
<scope today: single player, chat only, ...>

<layout>/                      -- only the parts a decision touches
  - file.md        -- its one job
  sub/             -- its one job

nouns (everything else is a dial on one of them):
  <noun>    <one line: what it is · its values>

<main flow on one line: a -> b ⇄ c -> d>


rules (the decisions, encoded):

<short claim, sharp enough to argue with>.
  <1–2 lines: what it means in practice, or why.>

<flows / commands, if the repo has them>:
  /<cmd>
    - step
    - step


now:
  - [ ] <next concrete move, with sub-items when it has parts>
open questions:
  - <a real fork the human must choose; name both sides>
later:
  - <parked ideas, one line each>
```

## Taste

- **Decisions, not descriptions.** "one ask, one dot." beats "the system reveals information gradually."
- **Say it once.** No section restates another. No summary at the end.
- **Repo's own words.** Use the names in the files; never invent a term the repo doesn't use.
- **Stay at altitude.** No field lists, internals or recipes. A line stays only if it changes a decision.
- **Open means open.** Don't resolve forks for the human; state both sides in one line.
- **80–150 lines.** Longer means it's becoming docs, so cut.

## Updating

One living file. If `TODO` exists, read it first: keep the human's words and edits, check every name against the
repo, and amend in place. Settled questions move from `open questions` into `rules`; done items leave `now`. Never
write a second file.
