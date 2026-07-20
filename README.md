# skills

My agentic skill systems for Claude Code.

## Skills

| Skill | Group | Use when |
|---|---|---|
| [`/feature`](code/feature/SKILL.md) | code | Write a feature spec |
| [`/model`](code/model/SKILL.md) | code | Fold features into the docs |
| [`/domain`](code/domain/SKILL.md) | code | Build the domain code from the specs |
| [`/idea-establish`](productivity/idea-establish/SKILL.md) | productivity | The idea is vague |
| [`/idea-attack`](productivity/idea-attack/SKILL.md) | productivity | The idea needs stress-testing |
| [`/opine`](productivity/opine/SKILL.md) | productivity | Two views are stuck |
| [`/nail-on-the-head`](productivity/nail-on-the-head/SKILL.md) | productivity | Two concepts blur together |
| [`/intuition`](productivity/intuition/SKILL.md) | productivity | You want to understand, not memorize |

The code skills run in order: `/feature → /model → /domain`, each stopping for
review. See [code/README.md](code/README.md).

## Install

```sh
# code
npx skills add smarchone/skills/code/feature
npx skills add smarchone/skills/code/model
npx skills add smarchone/skills/code/domain

# productivity
npx skills add smarchone/skills/productivity/idea-establish
npx skills add smarchone/skills/productivity/idea-attack
npx skills add smarchone/skills/productivity/opine
npx skills add smarchone/skills/productivity/nail-on-the-head
npx skills add smarchone/skills/productivity/intuition
```

