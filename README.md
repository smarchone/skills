# Skills

## Conversations worth sharing.

See them run: https://smarchone.github.io/skills/

## The problem

- Every new topic, you type the same "explain it like…" prompts to Claude again.
- The angle that makes it click is luck. Most chats never get there.
- When one does, it's lost in your terminal history. Nobody else ever reads it.

## Reports

You name the topic. The skill already knows how to research it and how to lay it out, so you don't
re-explain the format every time. Each one is shaped for a different kind of reading.

| Skill | Read it when you want |
|---|---|
| [`/few-shot`](productivity/few-shot/SKILL.md) | To learn a tool from a few sharp examples, then predict one yourself |
| [`/report-panel`](productivity/report-panel/SKILL.md) | A talk or launch, with a segment each for the CEO, PM and Architect |
| [`/intuition`](productivity/intuition/SKILL.md) | A blog post or concept from several angles |
| [`/origin-story`](systems/origin-story/SKILL.md) | Why a technology exists and what broke first |

## Panels

Not a report, a conversation. In [`/intuition-panel`](productivity/intuition-panel/SKILL.md), a CEO, PM and Architect
react in a line or two each while you brainstorm, so the idea gets pushed from three sides at once.

## Golden conversations

Reports and panels make sessions worth keeping. [`/golden`](productivity/golden/SKILL.md) saves one, meaning the visible
chat plus *why* it mattered, to your public golden repo as one PR. Over time that repo becomes a
curated library of conversations you can share.

**report or panel → a session worth keeping → `/golden` → shared library**

## Start here

```sh
npx skills add smarchone/skills/productivity/few-shot
npx skills add smarchone/skills/productivity/intuition-panel
npx skills add smarchone/skills/productivity/golden
```

More skills, grouped: [Productivity](productivity/README.md) (understanding things faster),
[Systems](systems/README.md) (studying a system like a senior engineer), [Ideas](ideas/README.md) (stress-testing an idea before you build it).

## Install

```sh
npx skills add smarchone/skills/<group>/<skill>
```

Each group README lists the exact install commands.

### As slash commands

`commands/` mirrors every skill as a Claude Code command, grouped the same way
(`/productivity:intuition`, `/systems:rebuild`, ...). Install them for every project (use `.claude/commands`
for just one); rerun to update:

```sh
npx degit smarchone/skills/commands ~/.claude/commands --force
```

Regenerate after editing a skill:

```sh
python3 tools/skills2commands.py          # rebuild commands/
python3 tools/skills2commands.py --check  # verify it is in sync
```
