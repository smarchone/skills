---
name: golden
description: Saves the current conversation as a golden session — the visible messages (no reasoning or hidden prompts), extracted from the session log by a script, plus metadata — and merges it into your public golden repo as one PR. Use only when the user asks to save the session as golden.
---

# Golden

You're mid-conversation and it's gold. Capture it in seconds as one merged PR to the golden repo.
Transcripts are cheap; the user's **why** is the asset.

## Don't ask
- **Why** it mattered: the user's words from the request, verbatim. None given → write one line in their
  voice naming the insight they'd want to find again (not the topic), pass `--why-suggested`, and show it.
- **Repo**: `$GOLDEN_REPO`. Unset → ask for the path. That's the only question.

## Capture
`scripts/golden.py` (next to this file) reads the session's JSONL log, so turns come out exactly as
written, not recalled. It keeps what the user saw: prompts, replies, `[ran: …]` per tool call,
`[asked: …]` / `[answered: …]`. It drops reasoning, system prompts, tool output and subagents, stops
before the first `/golden` prompt, redacts home dir, emails and tokens, and writes
`<YYYY-MM>/<YYYY-MM-DD>-<slug>.md` with the frontmatter below.

```sh
python3 <skill-dir>/scripts/golden.py --why "…" [--why-suggested] --title "<what the session found>" \
  --labels a,b --golden-turns 4,8 [--mode skill:x] [--thread slug] [--until N] [--pr]
```

1. **Run without `--pr`.** Defaults to the newest session for the cwd; pass an id or `.jsonl` path otherwise. Reuse labels already in the repo.
2. **Read it before publishing.** The repo is **public**. Check the cut point, redact what the regex missed (secrets, private names, client details) as `<redacted>`, pick `golden_turns`, and tell the user what you redacted.
3. **Publish** with `--pr`: a `golden/<id>` branch with only that file, a PR with the why as body, squash-merged at once (Revert undoes it). Return the PR link.

No log or no script (another harness, or running as a command) → stop and say so. Never write the turns yourself.

## Frontmatter
The script fills it; you supply title, why, labels, golden turns, mode and thread.
```yaml
---
schema: 1
id: <YYYY-MM-DD>-<slug>
title: <one line: what the session found>
why: "<the user's words verbatim, or your suggestion>"
why_source: <user | suggested>
harness: <the agent's name>
harness_version: <x.y.z>
model: <model id>
session_id: <native id>
source_path: <the .jsonl it came from, with ~>
started: <ISO ts>
captured: <ISO ts>
cwd: <with ~>
mode: <skill or persona that shaped it, if any>
turns: <n>
complete: true
golden_turns: [<turns where the insight landed>]
labels: [<reuse labels already in the repo before inventing new ones>]
thread: <slug of the idea arc, if it continues an earlier session>
status: raw
---
```
