# BRIEF.md template

```
# Brief · <project>

source: <research doc | session> · <date>

pain:
- <why this needs to exist, in the user's words>

ideas:
- <decided behaviors and concepts: what it does, how it feels>

prior art:
- <existing product / repo / tool> · <link> · <why not just use it>
  (or: ⚠ not checked)

main components:
- <the pieces and their contracts (inputs → outputs, schemas)>

directions:
- pilot / first cut: <scope, size, success test>
- next steps: <open choices the research ended on>
- later: <explicitly deferred items>

constraints:
- <hard limits every design must respect: cost, legal, rate limits, run mode, scale>

axes:
- <axis>: <option A> | <option B> | <option C>   ← where designs differ
```

Example axis lines (from a feed-surveillance project):

```
- storage: one yaml | folder per person | global event log | markdown notes
- memory: none (stateless runs) | per person | global, replayable
- fetch unit: per person | per source (1 rss call covers many people)
- logic: scripts | agent skills | hybrid (scripts fetch, agent judges)
- compounding: manual roster edits | auto-propose from events | views feed back
```
