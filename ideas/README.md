# ideas

[WIP] Skills for shaping and stress-testing an idea before anything gets built.

## Workflow

```text
/idea-establish  -->  /idea-attack  -->  /opine
(vague → clear)       (stress-test)      (resolve stuck disagreements)
```

## Skills

| Skill | Use when | What it does |
|---|---|---|
| [`/idea-establish`](idea-establish/SKILL.md) | The idea is vague | Asks for the missing pieces until the idea is established |
| [`/idea-attack`](idea-attack/SKILL.md) | The idea needs stress-testing | Attacks assumptions, searches prior art, hunts failure modes, returns effort-value suggestions |
| [`/opine`](opine/SKILL.md) | Two views are stuck | Weighs pro and opposing views and finds a path to converge — compromise, proof, experiment, or reframing |

## Install

```sh
npx skills add smarchone/skills/ideas/idea-establish
npx skills add smarchone/skills/ideas/idea-attack
npx skills add smarchone/skills/ideas/opine
```
