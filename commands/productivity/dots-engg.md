---
description: A 5-minute simulated engineering experience. Drop into a real-world situation with locked facts, investigate by asking questions, commit to a closing call, and see your run next to a Staff engineer simulation over the exact same facts.
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

3. **Investigate:**
   - Follow `experience.md`: one thing at a time, ASCII visuals for data, and redraw the `┌ board ──┐` whenever things shift.
   - **Hard rule — locked facts:** Never invent new clues, metrics, or root causes mid-run. If the user asks about something not in the pack, give a realistic non-clue (*"looks normal," "no data on that," "unchanged"*).
   - **Don't rush or spoil:** Let the user drive the pace. Never pull unasked dots, never connect the dots for them, and don't repeatedly ask *"are you ready to close?"* while they are still investigating.
   - If the user is spinning in circles after 4+ turns with no new dot, offer one light nudge in-character.

4. **Close (hard gate — never skip):**
   - Move to Close only when the user states their cause/call or says they're ready.
   - Show the empty closing frame (see `experience.md`) and **end your turn immediately**.
   - **Wait for the user's actual closing statement.** Never skip it, never pretend they posted it, and never output the Debrief in the same turn. If they ask a clarification before posting, answer it briefly in-character and wait again for their closing statement.

5. **Debrief (Your Run vs. Staff Simulation):**
   - Keep it scannable and cognitively light—short lines, white space, no walls of text.
   - **Side-by-side table:** Compare **Your Run** vs. **Staff Simulation** across the key phases/moves (`Phase | Your Run | Staff Simulation | Why It Matters`), strictly bound to **the exact same locked facts** (the Staff engineer cannot ask a question whose answer isn't supported by the pack). Keep cells crisp (1–2 lines).
   - **No hindsight shaming:** Never label reasonable triage or deeper RCA questions as "detours" or wasted turns. Frame differences around *sequencing* and *what unlocks the next decision*.
   - **Mitigation vs. root-cause ownership:** Distinguish what's needed for the **immediate call** (scoped to the closing prompt) from **follow-up root-cause fixes** (what an owner owns afterward), so deeper RCA instincts are recognized rather than penalized.
   - **Staff closing statement:** Show how the Staff engineer would close, in a short blockquote.
   - **The single shift & habit to steal:** 1–2 lines on the one move or framing shift that changed the most, plus one crisp **Habit to steal** in a blockquote.
   - Do not give numeric scores or level grades unless the user explicitly asks.

## Pack format (for generated packs)

Write generated packs to `${TMPDIR:-/tmp}/dots-engg/<slug>.md` with:
- Title, internal situation model (`one-truth (analysis)` | `few-truths (judgment)` | `no-single-truth (opinion)`), role/stakes, and who is across the table
- Opening brief + initial dot(s)
- Locked facts / dots (each with what reveals it, plus 1–2 realistic red herrings or constraints)
- The underlying tension, root cause, or trade-off (kept hidden until debrief)
- Closing prompt
