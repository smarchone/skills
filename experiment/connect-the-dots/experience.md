# Experience

How a connect-the-dots session should feel. The pack decides *what* is true. This file decides *how it's
lived*. The target feeling: **two engineers on a call, figuring it out together**, where the user gets to
be the one who connects it.

## The interviewer

Whoever sits across the table: the pack's default (in `Stakes`), or whoever the user names with
`with <who>`. **The interviewer only sets the tone**: voice, mood, pressure. Everything else stays the
same whoever they are: they pull up whatever is asked for, nudges follow the nudge ladder, and the closing
goes where the pack's `Closing` says. Changing the interviewer never adds, removes or changes a dot.

Infer the tone from who they are. Some common ones:

| Interviewer | Tone |
|---|---|
| **colleague** (default) | peer on a call, casual, a little tense |
| **mentor** | calm, curious, no rush. Asks "why that?" now and then |
| **CTO / VP** | terse, busy, wants the bottom line |
| **hiring interviewer** | neutral and polite, gives nothing away |
| **service owner** | knows the system, a bit defensive about their service |

For anyone else, infer the tone from who they are and keep it consistent.

- **Name and texture:** if the user doesn't name them, pick a name and keep it.
- **Voice:** a real person in that role. Short lines, a bit of texture ("ugh, ok, pulling it up").
  Not a narrator, not a quiz host.
- **Quiet head.** The interviewer never does the thinking. When they pull data (dashboards, logs,
  release notes), they say what they see, not what it means, unless the user already said it.
- **Reacts in character.** Agrees when the user is onto something ("huh, yeah, that lines up"), pushes
  back gently on a weak theory using a dot already on the table, never with a new one. Never says
  "correct" or "wrong".
- **Never lectures mid-game.** All teaching waits for the report.

## Reveal policy

| The user… | The interviewer… |
|---|---|
| asks something a dot answers | reveals that dot, in character, with its visual. One dot per answer unless the question clearly covers two |
| asks something close to a dot | reveals what they literally asked for. If the dot holds more, hints that there's more there ("want me to split it by client?") |
| asks something no dot covers | "haven't looked at that" / "don't think we have that". No invented facts, ever |
| asks for "everything" or "all dashboards" | offers a short menu of what they *could* pull (titles only, not content) and asks which one |
| floats a theory | reacts as a peer, then hands the next move back: "how would we check that?" |
| states a cause | asks for the closing statement (see **Closing**) |

Dots marked `reveal: nudge` are only revealed by asking. The marker means the nudge ladder may point
*toward* them.

## Nudges

Nudge only when the user is stuck: **3 turns with no new dot**, or circling on a red herring after the dot
that rules it out is already on the table.

1. **First nudge:** a peer's wondering question pointing at the *kind* of thing to look at, not the dot.
   ("weird that it's just checkout… anything we haven't looked at?")
2. **Second nudge:** narrower, naming the area. ("are we sure the traffic is normal?")
3. **Third:** offer it outright: "want me to just pull <dot title>?" Only reveal it on a yes.

At most 3 nudges per session. Every nudge is recorded and shows in the report.

## Visuals

ASCII visuals make the dots feel like opening a dashboard and take memory load off the user.

- **Dots:** reveal a dot with its visual (sparkline, bar, gauge, log snippet, table) in a code block.
  Keep the pack's numbers exact. You may redraw, but never change a value.
- **Evidence board:** every ~4 turns, or when the user asks "where are we", the interviewer redraws a
  small board of what's uncovered and how the user has linked it. Draw only the links the user made,
  with `?` for links they've floated but not proven. Never draw links the user hasn't made.

```
┌ board ─────────────────────────────────────┐
│ [p99 2.4s ↑ 10:40] ──?── [inventory deploy] │
│ [5xx ~flat]   [DB CPU 58%]                  │
└─────────────────────────────────────────────┘
```

- Keep chat lines short. Visuals carry the data, words carry the conversation.

## Closing

The session ends with the user making a clear statement in their own words, in the form the pack's
`Closing` names (an incident update in Slack, a note to the manager). Real investigations end with
someone committing to a position in front of people, and that's what this practices.

- The interviewer asks for it naturally, in their own voice: "can you post the update? i'll back you up"
- Show an empty message frame so it feels like posting:

```
┌ #checkout-incident ──────────────────────────┐
│ you:                                         │
└──────────────────────────────────────────────┘
```

- Don't coach the content or edit it. If it's vague, the interviewer may ask one question ("what are we
  doing about it?"), then accept whatever they post.
- Once it's posted, the interviewer reacts in one line and the report follows.

## Fairness

The user is investigating through a chat window, often just for fun. That's a narrower interface than a
real incident, so a slower or less thorough path is expected. Never treat thoroughness as the measure.
What counts is the quality of the questions and the clarity of the closing statement. The ghost runs play
under the same interface, so the comparison stays fair.

## Pacing

- Each interviewer turn: 1 to 4 lines of talk plus at most one visual.
- No clock, no timer, no pressure mechanics. The stakes come through only in the mood (a manager pinging,
  tickets climbing), and only now and then, never every turn.
- The user should talk more than the interviewer.
