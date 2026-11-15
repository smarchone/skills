---
name: dots-engg
description: A 5-minute simulated engineering experience. Drop into a real-world situation with locked facts, investigate by asking questions, commit to a closing call, and see your run next to a Staff engineer simulation over the exact same facts.
user-invocable: true
disable-model-invocation: true
argument-hint: "[topic or 'new' to generate a fresh scenario]"
---

# dots-engg

A 5-minute crucible for software engineers. You live through a realistic situation—debugging a weird outage, making an architecture call under deadline, or defending an engineering stance—then see how a Staff engineer would have worked **the exact same facts**.

## Flow

1. **Pick or generate a pack (before the first line of play):**
   - **Default (`/dots-engg`):** Pick a curated pack from `packs/` in this skill directory (avoid repeating one already played in this conversation; mix analysis, judgment, and opinion scenarios naturally without announcing the type).
   - **On demand (`/dots-engg <topic>` or `new`):** Generate a fresh pack and write it to `${TMPDIR:-/tmp}/dots-engg/<slug>.md` *before* starting. Play strictly from that file so facts never drift.
   - **Promote (`save`):** After a great generated run, offer to copy the temp pack into `packs/` in this skill directory so it becomes curated.

2. **Open (1 short message):**
   - Set the stakes, who is across the table (colleague, EM, VP, etc.), and the opening observation as a compact ASCII visual if it has data.
   - End with a natural prompt: *"Where do you want to start?"* or *"What do you want to check first?"*

3. **Investigate (3–8 turns):**
   - Follow `experience.md`: one thing at a time, ASCII visuals for data, and redraw the `┌ board ──┐` whenever things shift.
   - **Hard rule — locked facts:** Never invent new clues, metrics, or root causes mid-run. If the user asks about something not in the pack, give a realistic non-clue (*"looks normal," "no data on that," "unchanged"*).
   - If the user is spinning in circles after 4+ turns, offer one light nudge in-character.

4. **Close:**
   - When the user is ready (or after ~6–8 turns), show an empty closing frame (see `experience.md`) and ask for their **closing statement**—2–4 lines they would actually post or commit to.

5. **Debrief (Your Run vs. Staff Simulation):**
   - **Your path:** Brief recap of your key questions and your closing call.
   - **Staff engineer simulation:** Simulate how a Staff engineer would have navigated **the exact same locked facts** in 3–4 sharp moves, ending with their closing statement. Let the Staff voice emerge naturally from the scenario—no pre-scripted answers, but **strictly bound to the pack's facts** (the Staff engineer cannot ask a question whose answer isn't supported by the pack).
   - **The gap & habit to steal:** 1–2 lines on the single move that changed the most, plus one crisp **Habit to steal** in a blockquote.
   - Do not give numeric scores or level grades unless the user explicitly asks.

## Pack format (for generated packs)

Write generated packs to `${TMPDIR:-/tmp}/dots-engg/<slug>.md` with:
- Title, internal situation model (`one-truth (analysis)` | `few-truths (judgment)` | `no-single-truth (opinion)`), role/stakes, and who is across the table
- Opening brief + initial dot(s)
- Locked facts / dots (each with what reveals it, plus 1–2 realistic red herrings or constraints)
- The underlying tension, root cause, or trade-off (kept hidden until debrief)
- Closing prompt
