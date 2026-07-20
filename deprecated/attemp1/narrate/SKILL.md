---
name: narrate
description: Fan out every installed explain-* lens against one target (a file path, URL, or inline idea/blog/concept) in parallel — one subagent per lens — each writing its own narrative to .explain/ as a markdown doc, plus an index. Use this whenever the user wants an idea, blog post, paper, codebase, or concept explained from MANY angles at once rather than one — e.g. "explain this every way you can", "narrate this from all angles", "give me all the explanations side by side", "run every explain lens on this", "I want the big-picture AND the story AND the first-principles version", or when they can't decide which explanation style fits and want to compare (a pitch vs a lesson vs a walkthrough). This is the multi-lens narrate fan-out; for a single specific style, use that one explain-* skill directly instead.
---

# narrate — one idea, many narratives

Each `explain-*` skill is a different way to narrate the same idea — one frames it as the big
picture and where it fits, one interrogates it down to its axioms Socratically, one rebuilds it from
first principles Feynman-style, one tells it as a story, one stages it as a situation, one walks it
across levels of expertise, one runs it as a simulation. No single narration is right for every
audience or goal; a pitch wants one shape, a lesson wants another. This skill runs every installed
narration lens against the same target in parallel and drops each one's output into `.explain/` as
its own file, so the user can read them side by side and pick the shape that fits.

## Steps

1. **Resolve the target.** The target is whatever the user pointed this at — a file path, a URL, or
   an inline idea/blog/concept in their request. If it's ambiguous or missing, ask what to point
   this at — don't guess. If it's an inline idea (not a path or URL), write it verbatim to
   `.explain/TARGET.md` first so every subagent narrates the same fixed statement rather than a
   paraphrase.

2. **Discover the skills.** Run `ls -d ~/.claude/skills/explain-*/ 2>/dev/null` and take the
   basename of each entry as a skill name. Do this fresh every run rather than assuming a fixed
   list — new `explain-*` skills may have been added since this skill was written, and the whole
   point is that every current lens gets included. Skip any entry that's a broken symlink.

3. **Make the output directory.** `mkdir -p .explain` in the current working directory (project-
   relative — a fresh `.explain/` per project/target, not a shared global location).

4. **Fan out.** In a single message, spawn one subagent per discovered skill (Agent tool,
   `subagent_type: general-purpose`, `run_in_background: false` so this skill can report a
   complete result at the end) — all in parallel, since that's the entire point of fanning out;
   spawning them one at a time would just be a slow version of the same work. Each subagent's prompt
   should be self-contained and include:
   - The target (path, URL, or `.explain/TARGET.md`) to read in full.
   - An instruction to invoke the Skill tool with that exact skill name against the target.
   - An instruction to write ONLY that skill's final output (no meta-commentary, no "here's what I
     did") to `.explain/<skill-name>.md` via the Write tool, overwriting if the file already exists.

5. **Verify.** Once all subagents return, check `.explain/` for one file per discovered skill. If
   any are missing, note which skill failed rather than silently ignoring it.

6. **Write an index.** Create `.explain/README.md` naming the target and listing each generated file
   with a one-line description of that lens's angle (pull the gist from the skill's own description,
   not a generic label) — and, where it helps, a hint of which audience or goal that narration fits
   (e.g. a pitch, a lesson, a design review). This is what makes the directory readable as a set of
   options rather than a pile of loose files.

7. **Report back** to the user with the list of files generated in `.explain/` and flag anything
   that failed.
