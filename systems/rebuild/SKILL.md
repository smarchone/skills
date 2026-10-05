---
name: rebuild
description: Rebuilds a system, tool, or idea from first principles in stages — each stage forced by the last one's failure, with what it looks like on disk/in code and how it operates — for a senior engineer. Two modes, sketch (simplified) and faithful (close to the real implementation, failure modes included).
user-invocable: true
disable-model-invocation: true
---

# Rebuild

Rebuild a **system, tool, or idea** from scratch for a **curious senior engineer**, one stage at a time,
starting from the naïve version anyone would build. Each stage is forced by a failure of the previous one.
At every stage the reader sees what the system **looks like** (files, structures, code) and how it
**operates** (a write or read traced step by step, with numbers). Afterwards they should be able to
re-derive the real design themselves: "of course it needs a manifest list, otherwise planning is O(files)".
Example: Iceberg from scratch: files in a folder → file formats → a table format → snapshots → catalog/metastore.
Scope: systems, tools, and ideas with a buildable core. For the real history, point to `/evolve`;
for why it was born, `/origin-story`; for how it feels at scale, `/feel`.

**Priority: quality of learning.** Use as many stages as the derivation needs; don't merge or drop a
stage to save length. Every stage must teach one forcing failure and one structural idea.

## Modes
The user picks one: `/rebuild <subject> sketch` or `/rebuild <subject> faithful`. Not stated → `sketch`,
and say so in the header line.

| | `sketch` | `faithful` |
|---|---|---|
| Goal | Grasp the core design fast | Know how the real thing works and fails |
| Structures | Simplified; toy names allowed; details merged | Real formats, field names, file layouts, protocols (close, not 100%) |
| Traces | Happy path | Happy path **and** failure paths: crashes mid-write, conflicts, retries, partial state, cleanup |
| Failure modes | Only the one that forces the next stage | Each stage lists how it can fail and how the real system handles it |
| Simplifications | Allowed; each one flagged in the stage | Avoided; any left are flagged |

## Voice & Style
- **Audience:** Senior. Skip basics. They know what a B-tree is; they want to see why *this* system needs *this* structure.
- **Format:** Stages, each with an artifact (directory tree, JSON/struct, short code sketch, trace). Skimmable.
- **Tone:** Concrete: file counts, bytes, ms, request counts, $. No hype.

## Step 1: Research first
Always research before writing. The rebuild teaches the real design, so facts must come from sources,
not memory. Budget ~10-20 searches/fetches (more for `faithful`).
- **Source priority:**
  1. The spec or format docs (e.g. the Iceberg table spec), and the design docs / RFCs / improvement proposals.
  2. Source code of the reference implementation (the commit path, the planner, the on-disk writer).
  3. Papers, and engineering blogs by the system's authors or heavy operators.
  4. Conference talks; postmortems and issue threads for failure modes.
- Note the current version and anything recently changed or in flight (e.g. a new format version).
- Verify field names, limits, and protocol steps against the primary source, not search snippets.
- Research grounds the content; don't add citations. Still unsure after research → mark *(unverified)*.

## Step 2: Pin the target
- Subject is too broad ("databases") → ask for one system, or offer 2-3 concrete picks.
- Name the **end state** you're rebuilding toward, with a version (e.g. "Iceberg v2 tables with a REST catalog").
- Write down the **requirements** the end state satisfies (e.g. ACID appends, concurrent writers, time travel,
  schema evolution, fast planning at 1M files). Each stage earns one or more. If a requirement never gets
  earned, the rebuild is incomplete.
- Fix one running **workload** used in every stage (e.g. "events table, 10 GB/day, 200 files/day, 3 writers,
  analysts query last 7 days"). Every number derives from it.

## Integrity
- In `sketch`, structures may be simplified; facts stated about the real system may not.
- Numbers must be consistent with the workload. Show the key derivation in one line:
  `200 files/day × 365 = 73K files → 73K LIST/HEAD calls to plan one query`.
- Where the real system took a detour, or made a choice you wouldn't derive, say so in **Real vs rebuilt**;
  don't bend the stages to match history.

## Step 3: Write the overview conversation
Before the stages, a simulated conversation previews the whole rebuild. Its job is learning: by the end
the reader holds the shape of the design and knows what to look for in each stage. Length is whatever that
takes; don't cut it short, and don't pad it.
- Two invented people: **Dev** (a senior engineer new to the system, the reader's stand-in) and **Vet**
  (someone who has built or run it). Not real people.
- **Walk the forcing chain.** For each stage: the idea Dev proposes, the failure Vet points at (with a number
  from the workload), and the stage that fixes it, referenced as "(→ Stage n)".
- **Make Dev think, don't just tell.** Vet often answers with a question or a scenario ("Two writers finish
  at the same second. Whose file list wins?") and lets Dev reason to the next idea. Dev predicts before Vet
  confirms or corrects.
- **Wrong ideas are the lesson.** Dev proposes the plausible-but-wrong ideas a senior engineer would actually
  try (a lock file, listing faster, a database for everything). Vet shows exactly where each breaks. Several,
  not one.
- **Surface the misconception.** Name the intuition a senior engineer brings that's wrong for this system
  (e.g. "a rename is atomic on S3"), and correct it.
- **Point at what to watch for** in each key stage ("in Stage 4, notice that a commit writes three files but
  only one of them matters"). Hint at the fix; leave the full design for the stages to derive.
- **Anchor with analogies** Dev already knows (git commits, a B-tree root, a WAL), and say where the analogy breaks.
- **Checkpoints.** Every few stages Dev restates the design so far in their own words; Vet sharpens it.
- In `faithful`, Vet also flags the failure modes worth watching ("Stage 5 is where two writers race").
- End with Dev restating the whole chain in one line, and Vet naming the one idea everything rests on.

## Step 4: Build in stages
Start naïve; end at the end state. Each stage is the **smallest change** that fixes the previous stage's
failure. Don't introduce a structure before a failure demands it.

**Stage rules:**
- **Break it first.** Open with the concrete failure(s) of the previous stage: a scenario, the numbers, what the user sees.
  Stage 0 has none: it's "the simplest thing that could work".
- **Pause.** From stage 1 on, one question the reader should try before reading the fix
  ("Two writers commit at once. What do you need?").
- **Show it.** What it looks like: directory tree, file contents, struct/JSON, or code. Real-looking, small.
  Mark what's new since the last stage: `*…*` in prose/JSON, a `+` prefix in trees and listings, `# new` in code.
- **Run it.** How it operates: trace one write and/or one read as numbered steps, with I/O counts or latency.
  In `faithful`, also trace at least one failure path.
- **Name it.** Only now give the real system's name for what was just built (*"this is a manifest file"*).
- **Cost.** What the fix made worse, or the new limit. This is the next stage's failure.

## Output
Use this structure and order:

````text
# Rebuilding <subject> from scratch
<1-line: what it is> · end state: <system + version> · mode: <sketch | faithful> · <n> stages

## Target
- **Requirements:** (the bar the final stage must clear)
- **Workload:** (1-2 lines; every number below derives from it)

## Roadmap
<stage 0 name> → <stage 1 name> → … → <end state>   (one-line strip)

## Overview (simulated)
**Dev:** …
**Vet:** … (→ Stage n)
…
**Dev:** <the chain in one line>

## Stage <n> · <name>
**Breaks because:** the failure(s) of stage n-1, with numbers (1-2 bullets).
> **Pause:** <question to try before reading on>   (omit at stage 0)

**Looks like:**
```
<directory tree / file contents / struct / code sketch; new parts marked>
```
**Operates like:**
1. <step of a write or read, with I/O count / bytes / ms>
2. …
**Failure modes:** (faithful only)
| What fails | What happens | How the real system handles it |
|------------|--------------|--------------------------------|
**Simplified:** <what this stage glosses over vs the real thing> (sketch: when anything is; faithful: only if unavoidable)
**Real name:** <what the real system calls this> (or "none, a toy step")
**Earns:** <requirement(s) now satisfied> · **Costs:** <what got worse → the next failure> (1-2 bullets)

(One block per stage. Each stage's "Looks like" builds on the previous one.)

## Real vs rebuilt
| Piece | Our rebuild | Real <system> | Why the difference |
|-------|-------------|---------------|--------------------|
(what the real system does that the rebuild skipped or did differently, and why)

## Recall card
```
<subject> in ~8 lines: the chain of forcing failures
(naïve → breaks on X → add Y → breaks on Z → …), and the one structure that makes it all work.
```
````

## Follow-ups
Offer 2-3 next steps: the other mode, zooming into one stage ("trace a concurrent commit conflict byte by
byte"), turning the rebuild into runnable code (one stage per file, in the user's language), or rebuilding a
sibling system (Delta, Hudi) and diffing the forks.
