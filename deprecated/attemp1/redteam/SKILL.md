---
name: redteam
description: Fan out every installed attack-* lens against one target (a file path, URL, or inline idea/blog/doc) in parallel — one subagent per lens — each writing its attack to .attack/ as a markdown doc, then synthesize a single prioritized verdict. Use this whenever the user wants an idea, plan, design, business case, or argument stress-tested from MANY adversarial angles at once — e.g. "red-team this", "attack this from every angle", "poke all the holes you can", "where does this fall apart", "pressure-test this idea", "run every attack lens on this", or when they want convergence (which weaknesses multiple independent attacks all find). This is the multi-lens adversarial fan-out; for a single specific attack style, use that one attack-* skill directly instead.
---

# redteam — every attacker, one target

Each `attack-*` skill assaults the same idea from a different direction — one maps its negative
space to find where the boundary is fuzzy, one audits the unstated assumptions and blindspots it
stands on, one plays adversary and hunts the scenarios that kill it. Any single lens can be shrugged
off as "one perspective"; the point of running them all is convergence — a weakness that three
independent attacks each found on their own is almost certainly real. This skill runs every
installed attack lens against the target in parallel, drops each attack into `.attack/` as its own
file, and then does the one thing no individual lens can: a synthesis that says which findings
converge and what to fix first.

## Steps

1. **Resolve the target.** The target is whatever the user pointed this at — a file path, a URL, or
   an inline idea/doc in their request. If it's ambiguous or missing, ask what to point this at —
   don't guess. If it's an inline idea (not a path or URL), write it verbatim to `.attack/TARGET.md`
   first so every subagent attacks the same fixed statement rather than a paraphrase.

2. **Discover the skills.** Run `ls -d ~/.claude/skills/attack-*/ 2>/dev/null` and take the
   basename of each entry as a skill name. Do this fresh every run rather than assuming a fixed
   list — new `attack-*` skills may have been added since this skill was written, and the whole
   point is that every current attacker joins the assault. Skip any entry that's a broken symlink.

3. **Make the output directory.** `mkdir -p .attack` in the current working directory (project-
   relative — a fresh `.attack/` per project/target, not a shared global location).

4. **Fan out.** In a single message, spawn one subagent per discovered skill (Agent tool,
   `subagent_type: general-purpose`, `run_in_background: false` so this skill can report a
   complete result at the end) — all in parallel, since the attacks are independent by design and
   must not see each other's findings; independence is what makes convergence in step 6 meaningful.
   Each subagent's prompt should be self-contained and include:
   - The target (path, URL, or `.attack/TARGET.md`) to read in full.
   - An instruction to invoke the Skill tool with that exact skill name against the target.
   - An instruction to write ONLY that skill's final output (no meta-commentary, no "here's what I
     did") to `.attack/<skill-name>.md` via the Write tool, overwriting if the file already exists.

5. **Verify.** Once all subagents return, check `.attack/` for one file per discovered skill. If any
   are missing, note which skill failed rather than silently ignoring it.

6. **Synthesize.** Read every generated attack file yourself and write `.attack/VERDICT.md`. This
   is the payoff of the fan-out, so do it as real analysis, not a table of contents:
   - **Convergent findings first:** weaknesses that two or more lenses independently flagged, even
     under different names (attack-gaps' "assumes the API stays stable" and attack-red's "kill it
     by deprecating the API" are the same finding wearing different clothes — merge them and cite
     both files). These are the highest-confidence problems and the reader should meet them first.
   - **Strongest lens-specific findings:** the best finding from each lens that no other lens
     could have produced, so nothing important is buried just because it didn't converge.
   - **What survived:** what every attack failed to dent — an idea that just took three independent
     assaults deserves to know which parts held; this is also what makes the verdict read as
     judgment rather than hostility.
   - **Fix-first list:** 3-5 items, ordered by leverage, each pointing back at the finding it
     resolves. Keep the verdict compact — it links to the per-lens files for depth.

7. **Write an index.** Create `.attack/README.md` naming the target, pointing at VERDICT.md as the
   place to start, and listing each per-lens file with a one-line description of that lens's angle
   (pull the gist from the skill's own description, not a generic label).

8. **Report back** to the user with the verdict's convergent findings in brief, the list of files
   generated in `.attack/`, and anything that failed.
