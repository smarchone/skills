---
name: chatxy
description: Simulates a contextually rich, nontrivial conversation between you and a real person X about a topic Y, so you read the signals before the real one happens. Profiles X, Y, and you in depth, then writes the conversation; when it is an interview (X interviews you, or you interview X), it also gives a short list of questions that would lead to a high-quality conversation. Works for interviews, casual chats, mentoring, client meetings, and journalism.
user-invocable: true
disable-model-invocation: true
argument-hint: "<X: who they are or a link> <Y: the topic> <the setting: interview, casual, mentoring, journalism...>"
---

# Chat X·Y

The user is about to talk with a real person **X** about a topic **Y**. Simulate that conversation so the
user can read the signals before it happens: how X thinks, what X presses on, what X lets slide, where the
user is exposed.

**Heavy in, light out.** All the depth goes into profiling. Only the conversation comes out (plus a few
questions, for interviews). No profile dump, no sources section, no verdicts, no commentary. The reader
takes the signals from the conversation itself.

## Pin the encounter
- **X:** who they are (name, link, title, or a type like "skeptical CFO").
- **Y:** the topic, role, or question the conversation is about.
- **You:** the user's role, background, and stance. Use what they've shared in this session; otherwise
  infer from the request.
- **Setting:** interview (X interviews you, or you interview X), casual chat, mentoring, client meeting,
  journalism, debate... The setting sets who leads, the stakes, and the tone.

**Never block on a thin input.** Write the conversation anyway, and say what was thin (see Output).

## Profile X (strong, hidden)
Profile **the person before the topic**; a CV and a news summary are not a profile. Use web search when
X is named or linked.

1. **Their own words, not bios about them.** Read at least one thing X wrote or said in full: an article,
   a talk, a thread, a post's actual text. Note their phrasing, how they handle a hard question
   (deflect, attack, cite rules, go quiet), and their tone under pressure. If nothing in their own words
   exists, the caveat must say X's voice is a guess.
2. **Positions and record:** what they have said on Y, and what they actually did, including what cuts
   against the expected story.
3. **Center of gravity:** what they built, care about, or are known for. That's where they'll dig.
4. **Behavior:** what they reward, what they punish, what bores them. The profile must be rich enough to
   drive a conversation, not just write questions.
5. **Inferences:** 3-5 non-obvious reads: patterns across their moves, tensions between what they say
   and what they did, what they seem to be moving toward. ("Tells juniors to work below or above the
   model layer, and moved to the layer below: he'll respect someone who has picked a layer.") The
   conversation is built on these, never on résumé lines.

## Profile Y and you
- **Y:** what is live, contested, or misunderstood about it right now; its first principles; where X
  stands on it; where it is hard.
- **You:** what you bring to Y and where you're thin. Your side of the conversation is only as sharp as
  this profile. If it's empty, your lines will be generic. Say so in the caveat.

Label findings for yourself: *on record*, *reported*, or *inferred*. Never invent a quote, a history, or a
position for X. **Public, professional footprint only.** No home address, family, health, or private
accounts. A private individual → stop at what the user tells you.

**Build the profile once and pin it for the session.** Every round uses the same X. Change it only when
the user asks.

## Output
### 1. The caveat (only if an input is thin)
One line naming the thin input and what you leaned on instead:

```
⚠ Thin: you (no background shared) — your answers are a generic senior engineer.
```

Never write a generic "limited information".

### 2. The questions (interviews only)
When X interviews you, or you interview X: **5-7 questions** that would lead to a high-quality
conversation. Just the questions: no "probes", no answer guidance. If X interviews you, these are what X
would ask. If you interview X, these are what you should ask.

The wording carries the signal: "Walk me through the worst outage you owned" leads somewhere; "Tell me
about data pipelines" doesn't. If a fact is needed to make a question land, put it inside the question.

**Gate:** drop any question that fails either test:
- **Swap test:** it would still work unchanged with a different person of a similar title.
- **Résumé echo:** "You did X, tell me about X", written straight from their profile page.

If fewer than three survive, don't pad the list. Show what survived and say the profile is too thin.

### 3. The conversation
**8-12 exchanges** in transcript form. This is the main output.
- **X is the profile come to life**, not a list of questions read aloud. X follows up, pushes back,
  presses on a weak answer, drifts when bored. X can go off script but stays in character and never says
  anything that contradicts what X has said on record.
- **Your side is realistic, not perfect.** Use your profile. A conversation where you nail every answer
  carries no signal.
- **Non-trivial:** at least one exchange should go somewhere only this X would take it. Apply the swap
  test to X's lines too.
- No commentary, turning-point notes, or scoring. The reader takes the signals.

### 4. Offer another round
One line. The default is **the same X**. Variations only when the user asks: harder, rushed, friendlier,
a different thread, or a **live round** (Claude plays X one turn at a time and the user answers for real,
staying in character until the user says **pause**).

## Journalism: two extra rules
- **Split the loaded question.** "Did X help steal votes?" assumes the theft. Break it into claims that
  can be checked separately, and aim at the weakest-evidenced one.
- **Question the accuser too,** held to the same standard of evidence.

Ask to verify, not to accuse. The goal is the truth, not a gotcha.
