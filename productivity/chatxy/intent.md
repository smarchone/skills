# Intent: /chatxy

## The ask

Simulate a conversation between **me** and a real person **X** about a topic **Y**: an interview, a
casual chat, mentoring, a client meeting, journalism. Profile X and Y so the conversation is contextually
rich and nontrivial. The conversation itself gives me the signals before the real one happens.

When it is an interview (X interviews me, or I interview X), also give a list of interesting,
nontrivial questions: just the questions that would lead to a high-quality conversation.

## Scenarios that shaped it

1. **The interview.** A VP will interview me for a senior engineer role. If they have a strong
   data-platform background, they'll grill me on that; if they have a cultural preference, that too.
2. **The casual chat.** I'm meeting someone tomorrow, just chatting. What will they bring up, and what is
   worth asking them?
3. **Journalism.** Bring the truth out of a mess of agendas, lies, and manipulation, for a reporter or a
   citizen researching for themselves.
4. **Mentoring, client meetings, learning a topic.**

## How we got here

It started as `/vibe`: a glanceable questionnaire whose wording carried the vibe, plus simulations. Two
runs taught us:

- **The simulation told more than the questions.** Questions are a compressed conversation; the
  conversation carries what they lose: how X reacts to a weak answer, where X digs, what X lets slide.
- **Questions from résumé lines are generic.** The first Sunny Shah run read his profile page back as
  questions; the user could get that without a skill. The fix that worked: read X's own words, write
  3-5 non-obvious inferences, and gate every question with a swap test and a résumé-echo test.

So `/vibe` was replaced by `/chatxy`, with the conversation as the main output.

## What we settled

- **Profile X, Y, and me.** X in depth (own words, record, behavior, inferences); Y for what is live and
  contested; me, because my side is only as sharp as what Claude knows about me.
- **Heavy in, light out.** Profiling stays hidden. No profile dump, sources section, verdicts, or
  commentary. The reader takes the signals from the conversation.
- **Never block on thin input.** Write it anyway, with one specific caveat line.
- **Grounded.** X never says anything that contradicts their record; inferred behavior stays plausible.
- **Questions only for interviews,** 5-7, gated. Fewer than three survive → say the profile is thin.
- **Pinned profile.** Every round is the same X unless I ask to change it.
