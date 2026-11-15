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
IGNORED_EXTRAS = {"SKILL.md", "intent.md"}


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


def collect_extras(skill_dir: Path) -> list[tuple[Path, str]]:
    """Return sorted (relative_path, content) pairs for extra .md files in skill_dir."""
    extras = []
    for path in sorted(skill_dir.rglob("*.md")):
        rel = path.relative_to(skill_dir)
        if rel.name in IGNORED_EXTRAS:
            continue
        extras.append((rel, path.read_text()))
    return extras


def _insert_bundle_notice(body: str, rel_paths: list[str]) -> str:
    """Insert a short notice at the top of the command body pointing to bundled files."""
    notice = (
        "> **Bundled command:** Relative references to "
        f"`{'`, `'.join(rel_paths)}` are inlined in **## Bundled skill files** at the end of this file. "
        "Resolve those references from that section instead of reading from disk.\n\n"
    )
    lines = body.splitlines(keepends=True)
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is not None:
            insert_at = end + 1
            if insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            return "".join([*lines[:insert_at], notice, *lines[insert_at:]])
    return notice + body


def bundle_extras(body: str, extras: list[tuple[Path, str]]) -> str:
    """Append bundled skill files to the command body when present."""
    if not extras:
        return body
    rel_paths = [rel.as_posix() for rel, _ in extras]
    parts = [
        _insert_bundle_notice(body, rel_paths).rstrip("\n"),
        "\n\n---\n\n## Bundled skill files\n\n"
        "The files below are bundled from the skill directory. "
        "Infer any relative file or directory references above (e.g. `experience.md`, `packs/`) "
        "from these sections instead of reading from disk.\n",
    ]
    for rel, content in extras:
        rel_str = rel.as_posix()
        parts.append(
            f"\n<!-- BEGIN BUNDLED FILE: {rel_str} -->\n"
            f"### `{rel_str}`\n\n"
            f"{content.strip()}\n"
            f"<!-- END BUNDLED FILE: {rel_str} -->\n"
        )
    return "".join(parts)


def build(out: Path) -> list[Path]:
    written = []
    for skill in sorted(ROOT.glob("*/*/SKILL.md")):
        group, name = skill.parent.parent.name, skill.parent.name
        if group in {"commands", "docs"}:
            continue
        target = out / group / f"{name}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        converted = convert(skill.read_text())
        extras = collect_extras(skill.parent)
        target.write_text(bundle_extras(converted, extras))
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
