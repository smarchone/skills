# Agents

## Before creating a PR

`commands/` is generated from the skills. If you touched any `SKILL.md`, sync it and commit the result
with your change:

```sh
python3 tools/skills2commands.py          # rebuild commands/
python3 tools/skills2commands.py --check  # must print "commands/ is up to date"
```

Never edit `commands/` by hand.
