---
name: golden
description: Saves the current conversation as a golden session — the text of every turn plus metadata — and opens a PR to your private golden repo. Use only when the user asks to save the session as golden.
---

# Golden

You're mid-conversation and it's gold. Capture it in seconds: a PR to a **private** repo, the landing
zone for golden sessions. Transcripts are cheap; the user's **why** is the asset.

## Ask at most one thing
- **Why** this session mattered: take it from the user's request. Missing → ask once, in one line. Nothing else is a question; fill the rest yourself.
- **Repo**: the local clone at `$GOLDEN_REPO`. Unset → ask for the path once.
- Check `gh repo view --json visibility` says `PRIVATE`. If not, stop. Never write anywhere public.

## Capture
Write the conversation from your own context window. Don't go looking for the harness's session files.
1. **Write it out verbatim.** Every turn as `**user:**` / `**assistant:**`, numbered, in the words actually
   used. Don't summarize or tidy. Text only; a tool call becomes one line: `[ran: <what>]`.
2. **Stop before the request to save.** Leave out that turn and anything after it.
3. **Be honest about gaps.** Earlier turns compacted or dropped from context → write what you have, mark the
   gap as `[… turns n–m not in context …]`, and set `complete: false`.
4. **Redact**: keys, tokens, emails → `<redacted>`; home dir → `~`. Say what you redacted.
5. **Write** `sessions/<YYYY-MM-DD>-<slug>/session.md`: frontmatter below, then the turns.
6. **PR.** Branch `golden/<id>`, commit, push, `gh pr create` with the why as the body. Return the PR link.

## Frontmatter
```yaml
---
schema: 1
id: <YYYY-MM-DD>-<slug>
title: <one line: what the session found>
why: "<the user's words, verbatim>"
harness: <the agent's name>
harness_version: <x.y.z, if known>
model: <model id>
session_id: <native id, if known>
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
