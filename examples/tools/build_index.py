#!/usr/bin/env python3
"""Write examples/index.html: a list of every example page, grouped by skill.

Example files are named <skill>--<topic>.html. Stdlib only.
Usage: examples/tools/build_index.py
"""
import glob, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXAMPLES = os.path.join(ROOT, "examples")
REPO = "https://github.com/smarchone/skills/blob/main/"


def skill_path(skill):
    hits = glob.glob(os.path.join(ROOT, "*", skill, "SKILL.md"))
    return os.path.relpath(hits[0], ROOT) if hits else None


def main():
    groups = {}
    for f in sorted(glob.glob(os.path.join(EXAMPLES, "*.html"))):
        name = os.path.basename(f)
        if name == "index.html":
            continue
        skill, _, topic = name[:-5].partition("--")
        m = re.search(r"<title>(.*?)</title>", open(f, encoding="utf-8").read(), re.S)
        title = html.unescape(m.group(1).strip()) if m else (topic or skill)
        groups.setdefault(skill, []).append((name, title))
    out = []
    for skill, pages in groups.items():
        sp = skill_path(skill)
        head = f'<a href="{REPO}{sp}">/{html.escape(skill)}</a>' if sp else f"/{html.escape(skill)}"
        items = "".join(f'<li><a href="{html.escape(n)}">{html.escape(t)}</a></li>' for n, t in pages)
        out.append(f"<section><h2>{head}</h2><ul>{items}</ul></section>")
    page = TEMPLATE.replace("{{BODY}}", "\n".join(out))
    open(os.path.join(EXAMPLES, "index.html"), "w", encoding="utf-8").write(page)


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Skill Examples</title>
  <style>
    :root { --bg:#000; --fg:#e8e8e8; --dim:#8a8a8a; --accent:#d97757; --line:#333; }
    body { background:var(--bg); color:var(--fg); margin:0; padding:24px 16px; }
    main { max-width:860px; margin:0 auto; font:15px/1.6 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
    h1 { font-size:1.2em; margin:0 0 4px; }
    p { color:var(--dim); margin:0 0 24px; }
    h2 { font-size:1em; color:var(--accent); margin:24px 0 4px; }
    h2 a { color:inherit; }
    ul { margin:0; padding-left:20px; }
    a { color:var(--fg); }
    a:hover { color:var(--accent); }
  </style>
</head>
<body>
<main>
<h1>Skill examples</h1>
<p>Real chat sessions using the skills in <a href="https://github.com/smarchone/skills">smarchone/skills</a>.</p>
{{BODY}}
</main>
</body>
</html>
"""

if __name__ == "__main__":
    main()
