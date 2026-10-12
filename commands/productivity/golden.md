---
description: Saves the current conversation as a golden session — the visible messages (no reasoning or hidden prompts), extracted from the session log by a script, plus metadata — and merges it into your public golden repo as one PR. Use only when the user asks to save the session as golden.
---

# Golden

You're mid-conversation and it's gold. Capture it in seconds: one merged PR to the golden repo, the landing zone
for golden sessions. Transcripts are cheap; the user's **why** is the asset.

## Don't ask; suggest
- **Why** this session mattered: if the user gave one in the request, use their words verbatim. Otherwise
  write it yourself: one line, in the user's voice, naming the insight they'd want to find again, not a
  summary of the topic. Pass `--why-suggested` and show it in your reply so they can correct it later.
- **Repo**: the local clone at `$GOLDEN_REPO`. Unset → ask for the path once. That's the only question.
- The golden repo is **public**. Anything you commit is published, so treat redaction as the gate.

## Capture with the script
`scripts/golden.py` (next to this file, stdlib only) reads the session's own JSONL log under
`~/.claude/projects/`. The turns come out exactly as written, not recalled. It keeps only the visible
chat: the user's prompts, the replies they saw, a `[ran: …]` line per tool call, and `[asked: …]` /
`[answered: …]` for questions. It drops thinking, system reminders, skill bodies, tool output and
subagent traffic. It stops before the first `/golden` prompt, redacts the home dir, emails and
token-shaped strings, and writes `sessions/<YYYY-MM-DD>-<slug>/session.md` with the frontmatter below.

```sh
python3 <skill-dir>/scripts/golden.py --why "<user's words or your suggestion>" [--why-suggested] --title "<what the session found>" \
  --labels a,b --golden-turns 4,8 [--mode skill:x] [--thread slug] [--until N] [--pr]
```

1. **Run it without `--pr`.** It picks the newest session for the cwd; pass a session id or `.jsonl` path if that's wrong. Reuse labels already in the repo.
2. **Read the file before publishing.** Check the cut point. Look for secrets, private names or client details the regex missed, and replace them with `<redacted>`. Pick `golden_turns` from the numbered turns. Tell the user what you redacted.
3. **No log** (another harness, or the file is gone) → stop and tell the user. Never write the turns yourself.
4. **Publish**: rerun with `--pr`. It branches `golden/<id>` off the default branch, commits only the new `session.md`, opens a PR with the why as the body, and squash-merges it straight away. Undo a session with the PR's Revert button. Return the PR link.

## Frontmatter
```yaml
---
schema: 1
id: <YYYY-MM-DD>-<slug>
title: <one line: what the session found>
why: "<the user's words verbatim, or your suggestion>"
why_source: <user | suggested>
harness: <the agent's name>
harness_version: <x.y.z, if known>
model: <model id>
session_id: <native id, if known>
source_path: <the .jsonl it came from, with ~>
started: <ISO ts, if known>
captured: <ISO ts>
cwd: <with ~>
mode: <skill or persona that shaped it, if any>
turns: <n>
complete: <true | false>
golden_turns: [<turns where the insight landed>]
labels: [<reuse labels already in the repo before inventing new ones>]
thread: <slug of the idea arc, if it continues an earlier session>
status: raw
---
```
