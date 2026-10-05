# systems

Skills for studying a technology, company, or system the way a senior engineer would — where it came from, how it changed, who uses it, and whether to own it.

## Skills

| Skill | Use when | What it does |
|---|---|---|
| [`/origin-story`](origin-story/SKILL.md) | You want to know why something exists | Tells the origin story of a technology, company, or idea |
| [`/evolve`](evolve/SKILL.md) | You want to know how it got here | Traces business and tech evolution, each architecture shift as a before → after picture |
| [`/rebuild`](rebuild/SKILL.md) | You want to understand why it's built this way | Rebuilds it from a naïve version in stages, each forced by the last one's failure, showing what it looks like and how it operates |
| [`/adoption`](adoption/SKILL.md) | You want to know who uses it and how | Groups company usage by pattern, shows how it fits each backend, and who moved off it |
| [`/build-vs-buy`](build-vs-buy/SKILL.md) | You're deciding whether to build or buy | Analyzes unit economics, opportunity cost, scale break-even, and migration architecture |

Read in order for a full picture: `/origin-story → /evolve → /rebuild → /adoption → /build-vs-buy`.

## Install

```sh
npx skills add smarchone/skills/systems/origin-story
npx skills add smarchone/skills/systems/evolve
npx skills add smarchone/skills/systems/rebuild
npx skills add smarchone/skills/systems/adoption
npx skills add smarchone/skills/systems/build-vs-buy
```
