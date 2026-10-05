#!/usr/bin/env python3
"""Render a Claude Code session or a shared Gemini chat as a readable HTML page.

Reads the JSONL transcript Claude Code writes under ~/.claude/projects/, or the
conversation data behind a Gemini share link, not a terminal capture or scraped
page, so text comes out exactly as the model wrote it. Markdown
(tables, lists, code) is rendered in the browser; without network it falls
back to the raw Markdown, still exact.

Usage:
  examples/tools/session2html.py SESSION [-o OUT.html] [--turns 1-2] [--title T] [--no-tools]

SESSION is a path to a .jsonl file, a session id (looked up under
~/.claude/projects/*/), or a Gemini share link (https://share.gemini.google/...
or https://gemini.google.com/share/...). --turns keeps only those user turns (1-based, e.g. "1,3"
or "1-2"). Stdlib only.
"""
import argparse, glob, html, json, os, re, sys
import urllib.parse, urllib.request

HOME = os.path.expanduser("~")
STRIP_TAGS = re.compile(r"<(system-reminder|local-command-stdout|local-command-caveat)>.*?</\1>\s*", re.S)


def find_session(arg):
    if os.path.exists(arg):
        return arg
    hits = glob.glob(os.path.join(HOME, ".claude", "projects", "*", arg + ".jsonl"))
    if not hits:
        sys.exit(f"session not found: {arg}")
    return hits[0]


def redact(s):
    return s.replace(HOME, "~")


def user_text(content):
    """Return the visible prompt text, or None for non-prompt user records."""
    if isinstance(content, list):
        if any(b.get("type") == "tool_result" for b in content):
            return None
        content = "\n".join(b.get("text", "") for b in content if b.get("type") == "text")
    m = re.search(r"<command-name>(.*?)</command-name>", content, re.S)
    if m:
        args = re.search(r"<command-args>(.*?)</command-args>", content, re.S)
        return (m.group(1).strip() + " " + (args.group(1).strip() if args else "")).strip()
    content = STRIP_TAGS.sub("", content).strip()
    if not content or content.startswith("[Request interrupted"):
        return None
    return content


def tool_summary(name, inp):
    for key in ("description", "query", "command", "file_path", "url", "pattern", "prompt"):
        if isinstance(inp.get(key), str):
            v = inp[key].splitlines()[0] if inp[key] else ""
            return f"{name}({v[:100]})"
    return f"{name}()"


def result_text(content):
    if isinstance(content, list):
        content = "\n".join(b.get("text", "") for b in content if b.get("type") == "text")
    return str(content or "")


def load(path):
    """Group records into turns: [{prompt, items:[(kind, data)], ms}]."""
    turns, meta, results = [], {}, {}
    records = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    for o in records:
        if o.get("type") == "user" and isinstance(o.get("message", {}).get("content"), list):
            for b in o["message"]["content"]:
                if b.get("type") == "tool_result":
                    results[b.get("tool_use_id")] = result_text(b.get("content"))
    for o in records:
        if o.get("isSidechain"):
            continue
        t = o.get("type")
        for k in ("version", "cwd"):
            meta[k] = meta.get(k) or o.get(k)
        if t == "user" and not o.get("isMeta"):
            p = user_text(o["message"].get("content", ""))
            if p is not None:
                turns.append({"prompt": p, "items": [], "ms": None})
        elif t == "assistant" and turns:
            msg = o["message"]
            meta["model"] = meta.get("model") or msg.get("model")
            for b in msg.get("content", []):
                if b.get("type") == "text" and b["text"].strip():
                    turns[-1]["items"].append(("text", b["text"]))
                elif b.get("type") == "tool_use":
                    turns[-1]["items"].append(("tool", (tool_summary(b["name"], b.get("input", {})), results.get(b["id"], ""))))
        elif t == "system" and o.get("subtype") == "turn_duration" and turns:
            turns[-1]["ms"] = o.get("durationMs")
    return turns, meta


UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}


def is_gemini(arg):
    return re.match(r"https?://(share\.gemini\.google|gemini\.google\.com)/", arg) is not None


def load_gemini(url):
    """Fetch a shared Gemini chat through the same RPC the share page calls."""
    resp = urllib.request.urlopen(urllib.request.Request(url, headers=UA))
    page, final = resp.read().decode("utf-8"), resp.geturl()
    m = re.search(r"/share/([0-9a-f]+)", final)
    if not m:
        sys.exit(f"not a Gemini share page: {final}")
    share_id = m.group(1)
    wiz = json.loads(re.search(r"window\.WIZ_global_data = (\{.*?\});", page, re.S).group(1))
    query = urllib.parse.urlencode({"rpcids": "ujx1Bf", "source-path": f"/share/{share_id}", "bl": wiz["cfb2h"],
                                    "f.sid": wiz["FdrFJe"], "hl": "en", "_reqid": "100001", "rt": "c"})
    freq = json.dumps([[["ujx1Bf", json.dumps([None, share_id, [1]]), None, "generic"]]])
    req = urllib.request.Request(f"https://gemini.google.com/_/BardChatUi/data/batchexecute?{query}",
                                 data=urllib.parse.urlencode({"f.req": freq}).encode(),
                                 headers={**UA, "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
    raw = urllib.request.urlopen(req).read().decode("utf-8")
    line = next((l for l in raw.splitlines() if l.startswith('[["wrb.fr"')), None)
    if line is None or json.loads(line)[0][2] is None:
        sys.exit("Gemini returned no conversation (link private, deleted, or the RPC changed)")
    conv = json.loads(json.loads(line)[0][2])[0]
    turns = []
    for t in conv[1]:
        reply = t[3][0][0][1][0]
        turns.append({"prompt": t[2][0][0], "items": [("text", reply)], "ms": None})
    info = conv[2] or []
    model = info[7][2] if len(info) > 7 and info[7] and len(info[7]) > 2 else ""
    meta = {"app": "Gemini", "version": "", "model": model, "cwd": "", "title": info[1] if len(info) > 1 else None}
    return turns, meta


def parse_turns(spec, n):
    keep = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        keep.update(range(int(a), int(b or a) + 1))
    return [i for i in range(1, n + 1) if i in keep]


def fmt_ms(ms):
    s = round(ms / 1000)
    return f"{s // 60}m {s % 60}s" if s >= 60 else f"{s}s"


def render(turns, meta, title, tools):
    e = lambda s: html.escape(redact(s))
    head = [f'{meta.get("app", "Claude Code")} {meta.get("version") or ""}'.strip(), meta.get("model"), meta.get("cwd")]
    out = ["<header>" + "".join(f"<div>{e(h)}</div>" for h in head if h) + "</header>"]
    for t in turns:
        p = t["prompt"]
        if len(p) > LONG_PROMPT:  # e.g. a pasted skill: collapse behind its first line
            first = p.strip().splitlines()[0]
            out.append(f'<section class="turn"><details class="prompt"><summary>❯ {e(first)} '
                       f'<span class="dim">({len(p):,} chars)</span></summary>{e(p)}</details>')
        else:
            out.append(f'<section class="turn"><div class="prompt">❯ {e(p)}</div>')
        for kind, data in t["items"]:
            if kind == "text":
                out.append(f'<div class="md"><pre class="raw">{e(data)}</pre></div>')
            elif tools:
                summary, res = data
                res = res if len(res) <= 4000 else res[:4000] + "\n… (truncated)"
                out.append(f'<details class="tool"><summary>⏺ {e(summary)}</summary><pre>{e(res)}</pre></details>')
        if t["ms"]:
            out.append(f'<div class="done">✻ Done in {fmt_ms(t["ms"])}</div>')
        out.append("</section>")
    return TEMPLATE.replace("{{TITLE}}", html.escape(title)).replace("{{BODY}}", "\n".join(out))


LONG_PROMPT = 1500

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}}</title>
  <style>
    :root { --bg:#000; --fg:#e8e8e8; --dim:#8a8a8a; --accent:#d97757; --line:#333; --code:#141414; }
    body { background:var(--bg); color:var(--fg); margin:0; padding:24px 16px; }
    main { max-width:860px; margin:0 auto; font:14px/1.6 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
    header { color:var(--dim); border:1px solid var(--line); border-radius:6px; padding:8px 12px; margin-bottom:24px; }
    .turn { margin-bottom:32px; }
    .prompt { background:#1c1c1c; padding:8px 12px; border-radius:6px; white-space:pre-wrap; overflow-wrap:anywhere; }
    .prompt summary { cursor:pointer; }
    .dim { color:var(--dim); }
    .md { overflow-wrap:anywhere; }
    .md pre.raw { white-space:pre-wrap; font:inherit; margin:16px 0; }
    .md h1, .md h2, .md h3, .md h4 { font-size:1em; color:var(--accent); margin:1.4em 0 .4em; }
    .md table { border-collapse:collapse; width:100%; margin:12px 0; display:block; overflow-x:auto; }
    .md th, .md td { border:1px solid var(--line); padding:6px 8px; text-align:left; vertical-align:top; }
    .md th { background:#141414; }
    .md code { background:var(--code); padding:1px 4px; border-radius:3px; }
    .md pre { background:var(--code); padding:10px 12px; border-radius:6px; overflow-x:auto; }
    .md pre code { background:none; padding:0; }
    .md a { color:var(--accent); }
    .md hr { border:0; border-top:1px solid var(--line); }
    .tool { color:var(--dim); margin:8px 0; }
    .tool pre { white-space:pre-wrap; overflow-wrap:anywhere; max-height:320px; overflow:auto; background:var(--code); padding:8px; }
    .done { color:var(--dim); margin-top:12px; }
    .back { display:inline-block; color:var(--accent); font-size:1.15em; font-weight:600; text-decoration:none; margin:0 0 12px; }
    .back:hover { text-decoration:underline; }
    .back.bottom { margin:24px 0 0; }
  </style>
</head>
<body>
<main>
<a class="back" href="index.html">← Examples</a>
{{BODY}}
<a class="back bottom" href="index.html">← Examples</a>
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/15.0.7/marked.min.js"></script>
<script>
  if (window.marked) {
    const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    marked.use({ gfm: true, renderer: { html: t => esc(typeof t === "string" ? t : t.text) } });
    document.querySelectorAll(".md").forEach(el => {
      el.innerHTML = marked.parse(el.querySelector("pre.raw").textContent);
    });
  }
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("session")
    ap.add_argument("-o", "--out")
    ap.add_argument("--turns", help='user turns to keep, 1-based: "1-2" or "1,3"')
    ap.add_argument("--title")
    ap.add_argument("--no-tools", action="store_true", help="hide tool calls")
    a = ap.parse_args()
    turns, meta = load_gemini(a.session) if is_gemini(a.session) else load(find_session(a.session))
    if a.turns:
        turns = [turns[i - 1] for i in parse_turns(a.turns, len(turns))]
    title = a.title or meta.get("title") or (turns[0]["prompt"][:60] if turns else "Claude session")
    page = render(turns, meta, title, not a.no_tools)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(page)
    else:
        sys.stdout.write(page)


if __name__ == "__main__":
    main()
