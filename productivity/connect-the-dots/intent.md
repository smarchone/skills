# Intent: /connect-the-dots

Not a reference file. My notes on what this is and where it could go.

## The idea

**Simulated experience.** Learning means being prepared for situations. Give someone a situation and
isolated dots, let them investigate by asking questions, then show them how experts at each level would
have connected the same dots. The debrief is the product.

## Shape

- **Pack:** role · domain · type · stakes · situation · dots · hidden connection · level traits · grader.
- **Truth types:** one truth (definite analysis) · few truths (rank, weigh, choose) · no single truth (expert judgment).
- **Interviewer:** who sits across the table (colleague, mentor, CTO, hiring interviewer…). It only sets
  the tone (voice, mood, pressure). The pack owns the facts, and the mechanics stay the same.
- **Closing:** the user ends by committing to a clear statement (a Slack update, three lines to the CTO).
- **Debrief, not grade:** your path → ghost runs (L3 / L5 / Staff as simulated conversations) → what
  went well + the one move that would change most → habit to steal. Grades only on request.
- **Fairness:** a chat window limits the investigation. Judge the thinking, not the thoroughness.
- **Two axes, never blended:** competence (did you work out what happened?) and conduct (did you handle
  the situation: mitigate, communicate?). Nailing the RCA as a puzzle shouldn't read as L3. Grade the
  run, not the person.
- **Taste matters most:** curate by hand first, then encode the taste as rules.

## Abstractions

**The engine:** a handful of nouns. Everything else is a dial on one of them, or a mode.

```
  MODE         practice (relaxed, leaderboard)  |  interview (hidden pack)
  ────────────────────────────────────────────────────────────────────
  DOMAIN·ROLE  SRE · auditor · analyst · structural eng · ...
     │
  SITUATION    truth: one | few | none   ·  adversary: noise, irrelevant, lying dots
     │
  DOTS         form: text · log · chart · visual  ·  reveal: opening | on-ask | nudge
     │
  INTERVIEWER  colleague · mentor · CTO · hiring interviewer  →  tone only
     │
  CONNECTION   what the user linked, why, in what order  →  CLOSING (their statement)
     │
  GRADER       vs hidden connection + rubric  →  DEBRIEF   (grade only on ask → HISTORY)
               two axes: COMPETENCE (what happened?) · CONDUCT (handled it?)
```

**Truth types × time:** the variants for other personas.

```
               PAST (what happened?)          FUTURE (what will happen?)
  ONE TRUTH    RCA · diagnosis · audit        pre-mortem · safety review     → find it
  FEW TRUTHS   rank competing causes          choose between options         → weigh it
  NO TRUTH     "why did the metric drop?"     forecast · investment thesis   → defend it
  + adversary dial: someone hides the truth (fraud, due diligence)
```

**Pack × interviewer:** the interviewer never changes a fact.

```
  PACK (what's true)               INTERVIEWER (who's across the table)
  facts, dots, hidden truth        voice, mood, pressure
  owns the facts and the closing   owns the tone, nothing else
            └──────── session = pack × interviewer ────────┘
  same outage, same dots: colleague → casual and tense · mentor → calm, "why that?" · CTO → terse, bottom line
```

**A session:**

```
  open (stakes + brief) → ask ⇄ reveal dots (nudge if stuck) → "post the update" → debrief
                                                                                    │
                                                                    "grade me" → grade → history.md
```

**Experience constructs (how it's lived):**

- **Quiet head:** interviewer pulls data and reacts in character, never does the thinking, never says "correct/wrong", never lectures mid-game.
- **Reveal policy:** 1 dot per ask (exact pack numbers) · close ask → reveal literal + hint · off-pack → honest non-clue, never invent · "everything" → menu of titles only.
- **Nudge ladder:** only after 3 turns with no new dot (or circling a ruled-out red herring) → 1. peer wonder → 2. name area → 3. offer dot (max 3).
- **Visuals & board:** ASCII visuals carry the data; `┌ board ──┐` redraws every ~4 turns (only user's links: `──?──` floated, `──because──` connected).
- **Closing frame & pacing:** empty message frame (`┌ #channel ──┐`) for the closing statement; 1–4 lines of talk + ≤1 visual per turn; user talks more than interviewer.

**One pack, two modes:**

```
  PACK ─┬─ public → practice  (play, replay, beat the next ghost)
        └─ hidden → interview (one shot, graded)
```

**The debrief (the product):**

```
  YOUR PATH    D2 → D3 → D4 → D5 → D6 → (nudge) → D7 → ✓   9 questions
  L3 ghost     D2 → D3 → D4 → D5 → D6 → (nudge) → D7 → D8   ~9
  L5 ghost     D11 → D7 → D8 → D9 ✓                          ~5
  STAFF ghost  "what changed, incl. mobile?" → D7 → D8 ✓     ~3
                                  ▲
  did well: ruled out inventory with data (D4)  ·  one move: ask "is the load real?" before the DB
  ┌ HABIT TO STEAL ──────────────────────────────────────────┐
  │ when load goes up but the business doesn't, the traffic  │
  │ is lying                                                 │
  └──────────────────────────────────────────────────────────┘
  loop: play → see the ghost one level up → replay
```

**Progress:** grades only when asked, kept for reflection.

```
  ~/.connect-the-dots/history.md   one row per graded run
  /connect-the-dots progress
    COMPETENCE  L3 ─ L5 ─ L5 ─ L5+   ▲ cause most improved
    CONDUCT     L3 ─ L3 ─ L3 ─ L3    ─ mitigation stuck → try a pack that needs mitigating first
    habits: "the traffic is lying" · "stop the bleeding first"
```

**Packs:** curated or generated, always anchored to a file.

```
  curated:    hand-curate → playtest → "why did #3 land?" → TASTE.md
  generated:  generate → self-check → write ~/.connect-the-dots/packs/ → play from the file → offer to curate
```

## v1 (built)

- One SRE pack, chat only, ASCII visuals. No lying dots, no clock.
- `with <interviewer>`: colleague by default; mentor, CTO, hiring interviewer, service owner, or anyone
  (inferred). Sets the tone only; dots are revealed when asked, nudges come when you're stuck.
- Ends with you posting the closing: a clear statement in your own words.
- Debrief by default. Grades only on request, logged to `~/.connect-the-dots/history.md`; `progress`
  shows the trend.
- Packs generated on the fly: self-checked, written to `~/.connect-the-dots/packs/`, played from the
  file so nothing drifts, replayable by name.

## Later

- **Modes:** practice (relaxed, leaderboard) · interview (a hidden pack, a new kind of interview).
- **Harder:** noise, irrelevant dots, lying dots, adversaries, a clock, cost per question, level ladders.
- **Dots:** visual dots. Dynamic dots that change their surface each run (makes interviews leak-resistant).
- **Connection as a graph** the user draws (dots on a canvas, a "because" on each edge), then defends in conversation.
- **Ghosts from real experts:** record seniors playing packs. Captured judgment is the moat.
- **Taste as a skill:** TASTE.md (separating dot, tempting red herring, ghost gap > score gap, feels like a
  Tuesday, replay reveals more) → generate, lint, playtest with an expert.
- **Other domains:** financial analyst, data analyst, economist, structural or nuclear engineer, doctor,
  auditor. Variants beyond root-cause analysis: pre-mortem, forecast, diagnosis, forensic audit, due diligence.
- **Platform (distant):** authors create packs, practitioners pick from a catalog.

## First test

Five juniors, one situation, no instructions. Do they ask for situation #2?


--
initial prompt:

learning and building experience via investigation.
this should increase quality thinking.


simplest form: RCA scenarios for junior engineers
- given situations and isolated dots (observations), drive conversation with engineers to help them find the root cause.
- this will help build critical thinking and prepare engineers for situations and THAT's what learning actually is (to prepare for situations).
- the learning experience can be tuned - signals and noise ratio, pressure from authority and stakes (emotional aspect), skill/level ladder etc...


experience:
- build situation with hidden root cause and grading crietieria
- conversation
  - situation-brief
  - observations (dumped once vs given out on time basis)
  - conversation 
  - final report


I feel this doesnt have to be just for engineers.
I wonder how it would feel like for other domains? eg: Financial analyst, Data analyst, economist, structural engineer, nuclear engineer,
I think it doesnt only have to be Root Cause Analysis.
help me discuss other variants for target personas.

connect-the-dots -- variants -- personas
