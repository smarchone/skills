#!/usr/bin/env python3
"""Convert every <group>/<skill>/SKILL.md into a slash command at commands/<group>/<skill>.md.

Groups are kept as subfolders, so `productivity/intuition` becomes `/productivity:intuition`
once commands/ is copied into ~/.claude/commands or a project's .claude/commands.

Skill-only frontmatter keys (name, user-invocable) are dropped; everything else — description,
argument-hint, disable-model-invocation — carries over. The body is copied as-is: Claude Code
appends the arguments to a command that has no $ARGUMENTS placeholder.

Usage:
  python3 tools/skills2commands.py          # (re)generate commands/
  python3 tools/skills2commands.py --check  # exit 1 if commands/ is out of date
"""

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "commands"
SKILL_ONLY_KEYS = {"name", "user-invocable"}


def convert(text: str) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return text
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    kept, skipping = [], False
    for line in lines[1:end]:
        # A top-level key starts at column 0; indented lines continue the previous key.
        if line[:1] not in (" ", "\t", "\n", "\r"):
            skipping = line.split(":", 1)[0].strip() in SKILL_ONLY_KEYS
        if not skipping:
            kept.append(line)
    return "".join(["---\n", *kept, "---\n", *lines[end + 1 :]])


def build(out: Path) -> list[Path]:
    written = []
    for skill in sorted(ROOT.glob("*/*/SKILL.md")):
        group, name = skill.parent.parent.name, skill.parent.name
        if group in {"commands", "docs"}:
            continue
        target = out / group / f"{name}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(convert(skill.read_text()))
        written.append(target)
    return written


def snapshot(d: Path) -> dict[str, str]:
    return {str(p.relative_to(d)): p.read_text() for p in sorted(d.rglob("*.md"))} if d.exists() else {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if commands/ is out of date")
    args = ap.parse_args()

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            build(Path(tmp))
            if snapshot(Path(tmp)) != snapshot(OUT):
                print("commands/ is out of date; run: python3 tools/skills2commands.py", file=sys.stderr)
                return 1
        print("commands/ is up to date")
        return 0

    shutil.rmtree(OUT, ignore_errors=True)
    for path in build(OUT):
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
