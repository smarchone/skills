---
description: Simulated experience. Plays a curated investigation (a pack) as a conversation between engineers. The user asks questions, Claude plays the interviewer (a colleague by default, or whoever the user names, such as a mentor, a CTO or a hiring interviewer) who reveals the pack's dots (observations) when asked or when the user is stuck, and the user connects them into the hidden cause, then posts a closing statement (e.g. a Slack update). Ends with a debrief that replays how an L3, L5, and Staff engineer would have worked the same situation (ghost runs), names what went well and the one move that would change the most, and hands over one habit to steal. Packs can also be generated on the fly. Grades only on request, logged to a history to track progress.
disable-model-invocation: true
argument-hint: "[pack name | a role, domain or situation to generate] [with <interviewer>]"
---

> **Bundled command:** Relative references to `experience.md`, `packs/sre-01-slow-checkout.md` are inlined in **## Bundled skill files** at the end of this file. Resolve those references from that section instead of reading from disk.

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

---

## Bundled skill files

The files below are bundled from the skill directory. Infer any relative file or directory references above (e.g. `experience.md`, `packs/`) from these sections instead of reading from disk.

<!-- BEGIN BUNDLED FILE: experience.md -->
### `experience.md`

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
<!-- END BUNDLED FILE: experience.md -->

<!-- BEGIN BUNDLED FILE: packs/sre-01-slow-checkout.md -->
### `packs/sre-01-slow-checkout.md`

# Slow checkout, quiet errors

role: backend engineer (L2–L3) · domain: e-commerce checkout service · type: one-truth (RCA)

## Stakes

- **Default interviewer:** Sam, a colleague: a backend engineer on the same team, on-call with you today. Sam knows the
  checkout system well and has dashboard, log and trace access, but hasn't dug into this yet. Sam is
  pulling up whatever you ask for.
- **Pressure:** it's 10:55 on a Tuesday. Support tickets about a slow checkout are climbing. The eng
  manager has asked for an update in #checkout-incident "when you have something". Mood: focused, a
  little tense, not panicked.
- **Tone:** two peers on a call. Sam is friendly and quick, and says "I don't know" honestly.
- **Closing:** post an update in #checkout-incident covering what's happening, why, and what we're doing
  about it. The eng manager and support will read it.
- **The opening brief below is Sam's.** For another interviewer, keep its facts (D1, the 10:40 start, the
  tickets) and retell it in their tone.

## Situation

> hey, thanks for jumping on. checkout's been slow since ~10:40. p99 went from like 180ms to over 2
> seconds. weird thing is errors are barely up. support has ~40 tickets saying "payment spinner forever".
> i've only looked at the latency graph so far. where do you want to start?

## Dots

### D1 · Checkout latency · reveal: opening
Reached by: the opening brief.
```
checkout-api latency (p50 / p99), last 2h
p99 2.4s ┤                    ╭────────
         │                    │
p99 180ms┤────────────────────╯         p50: 40ms → 310ms
         └──────┬─────────────┬────────
              09:00        10:40
```

### D2 · Error rates · reveal: on-ask
Reached by: errors, 5xx, status codes, failures.
```
checkout-api responses     before    now
2xx                        99.8%     99.1%
5xx                         0.2%      0.9%   (mostly 503 "upstream timeout" at gateway)
4xx                         flat      flat
```
Sam: "so mostly it's just… slow. not failing much."

### D3 · Deploys today · reveal: on-ask
Reached by: deploys, what changed, recent changes, releases (backend).
```
10:15  inventory-svc  v2.31  "structured logging format"   ✓ healthy
--     checkout-api   no deploy since Monday
--     payments-gw    no deploy this week
```
Sam: "only inventory shipped. checkout calls inventory to reserve stock, so… maybe?"
*(This is the red herring. Only backend deploys are on this list. Mobile releases are tracked
elsewhere, see D8.)*

### D4 · Inventory service health · reveal: on-ask
Reached by: inventory latency, inventory errors, checking the inventory deploy.
```
inventory-svc  p99   38ms → 41ms     errors 0.1% flat
checkout → inventory call span p99: 45ms (unchanged)
```
Sam: "inventory looks totally fine actually."

### D5 · Database metrics · reveal: on-ask
Reached by: DB, database, CPU, queries, slow queries.
```
checkout-db (postgres)        before    now
CPU                            40%      58%
query p99                      11ms     12ms
active connections             ~22      50 (= checkout pool max)
```
Sam: "queries aren't slower. but connections are pinned at 50."

### D6 · Connection pool · reveal: on-ask
Reached by: connection pool, pool, threads, waiting, saturation; or following up on D5's connections.
```
checkout-api db pool (max 50)
in use   ██████████████████████████ 50/50   since 10:41
waiting  180 requests queued
acquire wait p99: 1.9s
```

### D7 · Request rate vs orders · reveal: nudge
Reached by: traffic, RPS, request rate, load, "is traffic up", orders, business metrics.
```
                    09:00–10:30    now
checkout RPS          ~400        ~680    ▲ 1.7x
orders / sec          ~364        ~370    ─ flat
```
Sam: "huh. way more requests, same number of orders."
*(The separating dot. The load is not real demand.)*

### D8 · Traffic by client · reveal: nudge
Reached by: splitting traffic by client, platform, app version or user agent; asking who is sending
the extra requests; asking about mobile or client releases.
```
checkout RPS by client       before    now     requests per order
web                           100      102          1.1
android 6.x                    80       82          1.1
iOS 4.11                      220      112          1.1
iOS 4.12                        0      384          3.8   ◀
```
Sam: "iOS is most of our checkout traffic. 4.12 is the new release. rollout went 20% → 50% at 10:35, i saw it in #mobile."

### D9 · iOS 4.12 release notes · reveal: on-ask (after D8 or when asking about mobile changes)
Reached by: 4.12 changes, mobile release notes, what changed in the app, retry policy.
```
iOS 4.12 — migrated to new networking layer (NetKit 3)
  • request timeout: 1.0s
  • retry on timeout: up to 3 times, immediate (no backoff)
  • staged rollout: 20% @ 10:00 → 50% @ 10:35
```

### D10 · Checkout logs · reveal: on-ask
Reached by: logs, warnings, exceptions, grep, access logs, idempotency keys.
```
10:47:12 WARN  Timeout acquiring connection from pool after 2000ms
10:47:12 WARN  Timeout acquiring connection from pool after 2000ms
10:47:13 INFO  POST /checkout idem=7f3a.. ua=iOS/4.12  2310ms
10:47:14 INFO  POST /checkout idem=7f3a.. ua=iOS/4.12  2280ms
10:47:15 INFO  POST /checkout idem=7f3a.. ua=iOS/4.12  2405ms
```
Sam: "same idempotency key three times in a row. that's one person's checkout."

### D11 · A slow trace · reveal: on-ask
Reached by: traces, tracing, a slow request, spans, where the time goes.
```
POST /checkout  2.31s
├─ auth                     4ms
├─ db.pool.acquire       1,920ms  ◀
├─ db.query (order)        12ms
├─ inventory.reserve       44ms
└─ payments.authorize     210ms
```

## Hidden connection

```
iOS 4.12 rollout to 50% (10:35)
  └─▶ new client: 1.0s timeout, 3 immediate retries, no backoff          [D8, D9]
        └─▶ each slow checkout becomes up to 4 requests                   [D10]
              └─▶ checkout RPS 1.7x while orders stay flat                 [D7]
                    └─▶ DB pool (50) saturated, requests wait ~1.9s        [D5, D6, D11]
                          └─▶ p99 2.4s > the client's 1.0s timeout → more retries
                                └─▶ feedback loop (a retry storm)          [D1]
```

- **Why 10:40, not 10:00:** at 20% rollout the pool still had headroom. At 50% the extra load
  tipped it into saturation, and from there the retries fed themselves.

- **Root cause:** a client retry policy (immediate retries, no backoff, timeout below server latency)
  amplifying load into a saturated connection pool, which feeds back on itself.
- **Mechanism vs cause:** pool saturation is the *mechanism*. The iOS 4.12 retry policy is the *cause*.
  Stopping at "pool is full, raise the pool size" is the classic L3 miss. It would push more load onto
  the DB and doesn't stop the storm.
- **Red herrings:** the inventory deploy (D3, ruled out by D4); DB CPU up (D5, a symptom of more
  load: query latency is flat).
- **Good mitigation:** pause or roll back the 4.12 rollout, or remote-config the client retries off.
  Optionally rate-limit or dedupe by idempotency key at the gateway. Long-term: backoff with jitter,
  a retry budget, and a client timeout above server p99.

## Level traits

- **L3:** starts from the service's own symptoms: errors (D2), then deploys (D3), and gets pulled
  toward the inventory deploy and checks it (D4). Goes to the DB (D5), finds the pool full (D6) and
  wants to raise the pool size. Needs a nudge ("why is the pool full, though?") to look at traffic
  (D7, D8). About 9 questions. First question: "what are the errors?"
- **L5:** looks at the shape first: slow but not failing means waiting, not breaking. Goes to traces or
  the pool (D11/D6), then asks the key question, "is load actually up, and is it real?" (D7). Splits by
  client (D8), reads the release notes (D9). About 5 questions. First question: "where's the time going
  in a slow request?"
- **Staff:** opens with "what changed anywhere that touches checkout today, including clients?" and
  "is traffic up?" in the same breath (D7). Goes straight to D8 → D9 and calls it a retry storm.
  **Proposes mitigation before full proof** ("let's pause the 4.12 rollout now, cheap and reversible,
  and confirm with logs while it drains"), then confirms with D10. About 3 questions. First question:
  "what changed — including mobile?"

## Grader

Two axes, graded separately and never blended.

**Competence:** did you work out what happened?

| Dimension | L3 | L5 | Staff |
|---|---|---|---|
| **Mechanism**: found the pool saturation / waiting | found it, maybe late | found it early via shape or traces | inferred it, confirmed quickly |
| **Cause**: got past mechanism to the retry amplification from iOS 4.12 | stopped at the pool, or needed nudges | found it via traffic → client split | went there first |
| **Evidence**: linked cause to effect with dots, not vibes | partial chain | full chain (D7/D8 + D6) | full chain + the feedback loop |
| **Red herrings**: dismissed with evidence | chased inventory, eventually dropped it | checked it once with D4, moved on | skipped it, or ruled it out in one line |
| **Efficiency**: questions to the cause, nudges used | 8+ or 2+ nudges | 4–7, ≤1 nudge | ≤4, no nudges |

**Conduct:** did you handle the situation?

| Dimension | L3 | L5 | Staff |
|---|---|---|---|
| **Mitigation**: proposed a safe, reversible action | "raise the pool size" (harmful) | roll back 4.12 | pause the rollout first, prove second, plus dedupe at gateway |
| **Closing update**: clear to the manager and support | symptom + guess ("DB pool is full, investigating") | cause + evidence + action | cause, action already taken, impact, next update time, in a few lines |

**Habit to steal:** when load goes up but the business doesn't, the traffic is lying. Find who's
sending the extra requests.

Alternate, if the user found the cause but went after the mechanism first: **"ask what changed, and
include the callers, not just your service."** If the user proved everything but never mitigated:
**"stop the bleeding before you finish the proof."**
<!-- END BUNDLED FILE: packs/sre-01-slow-checkout.md -->
