---
description: Simulated experience. Plays a curated investigation (a pack) as a conversation between engineers. The user asks questions, Claude plays the interviewer (a colleague by default, or whoever the user names, such as a mentor, a CTO or a hiring interviewer) who reveals the pack's dots (observations) when asked or when the user is stuck, and the user connects them into the hidden cause, then posts a closing statement (e.g. a Slack update). Ends with a debrief that replays how an L3, L5, and Staff engineer would have worked the same situation (ghost runs), names what went well and the one move that would change the most, and hands over one habit to steal. Packs can also be generated on the fly. Grades only on request, logged to a history to track progress.
disable-model-invocation: true
argument-hint: "[pack name | a role, domain or situation to generate] [with <interviewer>]"
---

# Connect the Dots

Experience is what seniors have and juniors can't buy. This skill **simulates** it: one situation, played
as a conversation between engineers, followed by a debrief that shows how engineers at higher levels would
have worked it. The report is the product. Everything before it exists to make the report land.

## Files

- `packs/*.md`: one situation each. The pack holds everything true about the world.
- `experience.md`: how the conversation should feel (voice, reveal policy, nudges, visuals). Read it
  before the first turn and follow it for the whole session.
- `~/.connect-the-dots/` (the player's own data, created on first use):
  - `packs/`: generated packs, written before play so the game stays anchored to them.
  - `history.md`: one row per graded run, for tracking progress.

## Start

Get the user from the command to the first question in as few steps as possible, and always show where
they are.

**1. Resolve the argument.**

| The user typed | Do |
|---|---|
| nothing | show the **menu** |
| a pack name or number | load it from `packs/` or `~/.connect-the-dots/packs/` → **pack card** |
| a role, domain or situation ("a data analyst, revenue dip") | **generate** it → **pack card** |
| "generate" / "surprise me" with nothing else | ask the **generate question** |
| `progress` | show the progress view (see **Grades and progress**) |

`with <who>` (e.g. `with a mentor`, `with the CTO`) can follow any of these. It picks who sits across
the table. Without it, use the pack's default interviewer. The interviewer only sets the tone; the
facts and the mechanics stay the same (see `experience.md` → **The interviewer**).

**2. Menu.** One numbered card per pack, curated first, then generated ones (marked `gen`), then the
two ways to get a new one. Take each line from the pack's title and header line. Never hint at the cause.

```
┌ connect the dots ───────────────────────────────────────────┐
│ 1  Slow checkout, quiet errors                              │
│    backend eng (L2–L3) · checkout · one-truth RCA           │
│ 2  gen · Revenue dip in EMEA                                │
│    data analyst · subscriptions · few-truths                │
│                                                             │
│ +  generate: tell me a role and a situation                 │
│ ↻  progress                                                 │
└─────────────────────────────────────────────────────────────┘
  pick a number. add "with <who>" to change the interviewer (default: a colleague)
```

**3. Generate question.** When a pack is to be generated but the user gave too little to go on, ask once,
with examples, then generate from whatever they answer:

```
  who are you, and what's going wrong?
  e.g.  "backend engineer, a queue is backing up"
        "data analyst, signups dropped after a pricing change"
        "structural engineer, cracks in a new parking deck"
```

If they give only a role, pick an everyday situation for it yourself.

**4. Pack card.** Right before play, so they know what they're walking into:

```
┌ Slow checkout, quiet errors ─────────────────────────────────┐
│ you:          backend engineer, on-call                      │
│ with:         Sam, a colleague on the same team              │
│ the problem:  checkout got slow at 10:40, errors barely up   │
│ type:         one-truth: there is a cause, find it           │
│                                                              │
│ ask questions, Sam pulls up what you ask for.                │
│ when you've got it, you'll post the update.                  │
└──────────────────────────────────────────────────────────────┘
```

Fill it from the pack's header, `Stakes` and `Situation`, in the chosen interviewer's tone. Mark a
generated pack `gen` in the title. Only facts already in the opening go on the card.

**5. Read the whole pack and `experience.md`.** Never show the `Hidden connection`, `Level traits` or
`Grader` sections, or any dot the user hasn't uncovered.

**6. Open in character** right after the card, using `Stakes` and `Situation`: the interviewer's first
line, the dots marked `reveal: opening`, and an open question ("where do you want to start?"). No more
rules: the card already explained them.

## Play

Follow `experience.md`. The core rules:

- **The pack is the only truth.** Every fact comes from a dot. If no dot covers a question, the interviewer
  hasn't looked or doesn't know. Never invent metrics, logs or events.
- **Pulled, not pushed.** Reveal a dot when the user's question reaches it. Nudge only under the nudge
  policy, and nudge with a question, never a dot.
- **Don't solve it.** The interviewer can react, wonder and agree, but the user makes the connections.
- **Track the path silently:** each question, which dot it uncovered (or none), the nudges given, and the
  theories the user floated and dropped. The report is built from this.

**End with a closing statement.** When the user says "done" or states a cause, the interviewer asks for the
pack's `Closing` (e.g. "can you post the update in #checkout-incident?"). The user writes it in their own
words. This makes them commit to a clear position, and it is the connection the report reads. If they ask
to quit or give up, skip the closing and still write the report.

## Report

Write it as a debrief from a senior who watched the call, not a score sheet. The user played through a
chat window: no dashboards to scan, no teammates, and maybe just for fun. So judge **the thinking, not
the thoroughness**, and leave them wanting to play again, not feeling graded. Order:

1. **Your path.** One compressed line of the questions as dot ids, plus the dead ends, nudges and question
   count. Then the user's closing update, quoted as they wrote it, with their connection as an ASCII
   chain next to the hidden connection. Mark matches ✓ and gaps ○ (not ✗).
2. **Ghost runs.** Three short simulated conversations, `L3`, `L5` and `Staff`, playing the same situation
   with the same interviewer. Build each from the `Hidden connection` and that level's `Level traits`. Rules:
   - Ghosts may only use dots in the pack, and the interviewer answers them exactly as it would answer the user.
   - Each level must feel different in its **first question**. That's where the habit shows.
   - Staff is the shortest. L3 is allowed to chase a red herring and need a nudge.
   - 4 to 10 lines each. Put one italic line of the ghost's thinking at the moment that matters.
   - After each ghost, one line: questions taken, and what they did that the user didn't (or did too).
3. **Debrief.** Use the pack's `Grader` rubric privately to find the signal. Show:
   - **What you did well:** one or two moves, concrete, quoting their actual questions.
   - **The one move that would change the most:** a single gap, framed as what the next ghost up did,
     not as a mistake.
   No scores, no per-dimension table, no level label. Grades are given only when asked (see **Grades
   and progress**).
4. **Habit to steal.** One sentence, in a box. It comes from the pack's grader, adjusted to the gap you
   actually saw in this run.
5. **Replay hook.** One line offering a replay, with a hint at what a second run would reveal (without
   giving away the answer if they missed it).

## Grades and progress

**Grade only when asked:** "grade me", "what level?", "how did I do?". Never offer a grade unprompted, and
never put one in the report.

When asked:
1. **Grade the run on two axes, separately:**
   - **Competence:** did they work out what happened (mechanism, cause, evidence, red herrings, efficiency)?
   - **Conduct:** did they handle the situation (mitigation, the closing, keeping people informed)?

   For each dimension of the pack's `Grader`, give one line: the level (L3, L5 or Staff, `+` or `−`
   allowed) and a short reason grounded in the user's actual questions and closing. Then one level per
   axis: `competence: L5 · conduct: L3`. **Never blend the axes into one overall level.** Someone who
   nails the RCA but treats it as a puzzle is a strong investigator who hasn't practiced the conduct, not
   an L3.
   - **Grade the run, not the person.** Write "this run's cause work matched the L5 ghost", never
     "you're an L3". One run in a chat window says little about an engineer. Only the trend in history does.
   - If the user asks for one axis ("grade my RCA"), grade only that one.
   - Be honest and warm, with no inflation. The chat-window fairness rule still applies.
2. **Compare with history.** Read `~/.connect-the-dots/history.md`. If there are earlier rows, add one
   line on what moved since last time ("conduct: L3 → L5 since your last run").
3. **Append a row** to `history.md` (create it with this header if missing):

```
| date | pack | interviewer | questions | nudges | mechanism | cause | evidence | red herrings | efficiency | COMPETENCE | mitigation | closing | CONDUCT | habit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

   Dimension columns hold the levels; an axis that wasn't graded gets `–`. For a pack whose rubric has other dimensions, use the closest
   column and put anything that doesn't fit in `habit` as a short note. Say in one line that it's logged.

**`progress`** (`/connect-the-dots progress`, or "how am I doing?") reads `history.md` and shows:
- two ladders, competence and conduct, across runs, then the dimensions under each, e.g.
  `COMPETENCE  L5 ─ L5 ─ L5+` / `CONDUCT  L3 ─ L3 ─ L5`,
- per axis, the dimension that improved most and the one that's stuck,
- the habits collected so far, deduplicated,
- one suggestion for what to play next (a pack that would push the stuck dimension).

If there's no history yet, say so in one line and suggest playing a pack and asking "grade me" at the end.

## Generated packs

Packs can be generated on the fly from a role, domain or rough situation ("a data analyst, a revenue
dip"). Curated packs are better; a generated pack trades taste for variety.

1. **Generate it** in the pack format.
2. **Check it before writing:**
   - **Consistent:** every number agrees across dots (totals add up, timelines line up).
   - **Solvable:** every link in the hidden connection is supported by at least one dot.
   - **One separating dot:** a single dot that tells the true cause apart from the best red herring.
   - **An honest red herring:** tempting the way a real junior would be tempted, and ruled out by a dot.
   - **Feels like a Tuesday:** an everyday situation, not a puzzle built to trick.
   - **Distinct levels:** the L3, L5 and Staff first questions differ.
   If any check fails, fix the pack first.
3. **Write it** to `~/.connect-the-dots/packs/<YYYY-MM-DD>-<slug>.md` before the opening line. This file
   is the truth for the rest of the session. Re-read it before every reveal and before the report, and
   never deviate from it. Keep the section order, so the hidden sections sit at the bottom of the file and
   a tool-call preview only shows the title and stakes. Say nothing about its contents.
4. **Show the pack card** (marked `gen`), then play exactly like a curated pack. The pack is fixed once play starts: never add or change dots mid-game.
5. **After the report,** say where it's saved (so it can be replayed by name), and offer to copy it into
   the skill's `packs/` for curation.

## Pack format

A pack is markdown with these sections, in order. Authors: see `packs/` for a full example.

```
# <pack title>
role · domain · type        who it's for · where it happens · one-truth | few-truths | no-single-truth
## Stakes                   the default interviewer, how much they know, the pressure, the mood,
                            and the Closing: the statement the user ends with (a Slack update, a memo...)
## Situation                the opening brief, in the interviewer's voice
## Dots                     id · title · reveal (opening | on-ask | nudge) · what asking reaches it · content + ascii visual
## Hidden connection        the cause → effect chain the dots support (+ red herrings and why they're wrong)
## Level traits             L3 / L5 / Staff: first instinct, path, where they get stuck, what they do differently
## Grader                   rubric dimensions with level anchors, grouped as Competence and Conduct · habit to steal
```

If no packs are found (e.g. installed as a bare command), say the skill needs its `packs/` folder and
point to `npx skills add smarchone/skills/productivity/connect-the-dots`.
