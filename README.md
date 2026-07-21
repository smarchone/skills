# skills

My agentic skill systems for Claude Code.

## Skills

| Skill | Group | Use when |
|---|---|---|
| [`/hex-feat`](code-simple/hex-feat/SKILL.md) | code-simple | Write a feature spec |
| [`/hex-domain`](code-simple/hex-domain/SKILL.md) | code-simple | Translate feature specs into domain models |
| [`/hex-code`](code-simple/hex-code/SKILL.md) | code-simple | Build the domain code from the specs |
| [`/hex-drift`](code-simple/hex-drift/SKILL.md) | code-simple | Audit the codebase against the specs |

The code-simple skills run in order: `/hex-feat → /hex-domain → /hex-code`, each stopping for
review. See [code-simple/README.md](code-simple/README.md).

| Skill | Group | Use when |
|---|---|---|
| [`/idea-establish`](productivity/idea-establish/SKILL.md) | productivity | The idea is vague |
| [`/idea-attack`](productivity/idea-attack/SKILL.md) | productivity | The idea needs stress-testing |
| [`/opine`](productivity/opine/SKILL.md) | productivity | Two views are stuck |
| [`/nail-on-the-head`](productivity/nail-on-the-head/SKILL.md) | productivity | Two concepts blur together |
| [`/intuition`](productivity/intuition/SKILL.md) | productivity | You want to understand, not memorize |

## Install

```sh
# code-simple
npx skills add smarchone/skills/code-simple/hex-feat
npx skills add smarchone/skills/code-simple/hex-domain
npx skills add smarchone/skills/code-simple/hex-code
npx skills add smarchone/skills/code-simple/hex-drift

# productivity
npx skills add smarchone/skills/productivity/idea-establish
npx skills add smarchone/skills/productivity/idea-attack
npx skills add smarchone/skills/productivity/opine
npx skills add smarchone/skills/productivity/nail-on-the-head
npx skills add smarchone/skills/productivity/intuition
```

