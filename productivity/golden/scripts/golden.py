#!/usr/bin/env python3
"""Extract the visible conversation from a Claude Code session log as a golden session.md.

Reads the JSONL transcript Claude Code writes under ~/.claude/projects/, so the turns come out exactly
as written, not recalled. Keeps what the user saw: their prompts, the assistant's replies, and one
`[ran: ...]` line per tool call. Drops thinking, system reminders, skill bodies, tool output and
subagent traffic. Redacts the home dir, emails and token-shaped strings.

Usage:
  golden.py [SESSION] --repo DIR --why "..." [--why-suggested] --title "..." [--slug S] [--labels a,b] [--golden-turns 4,8]
            [--mode skill:x] [--until N] [--pr]

SESSION is a .jsonl path or a session id; omitted, it's the newest session for the current directory.
Turns stop before the first /golden prompt (or the last prompt, if none) unless --until N. Writes
<repo>/sessions/<date>-<slug>/session.md; --pr also opens a PR with it and squash-merges it. Stdlib only.
"""
import argparse, datetime, glob, json, os, re, subprocess, sys

HOME = os.path.expanduser("~")
HIDDEN = re.compile(r"<(system-reminder|local-command-stdout|local-command-caveat)>.*?</\1>\s*", re.S)
SECRETS = [
    re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    re.compile(r"\b(sk-[\w-]{16,}|gh[pousr]_\w{20,}|github_pat_\w{20,}|xox[abprs]-[\w-]{10,}|AKIA[0-9A-Z]{16}|AIza[\w-]{30,})"),
    re.compile(r"(?i)\b(bearer|token|api[_-]?key|secret|password)([\"']?\s*[:=]\s*[\"']?)[^\s\"']{8,}"),
]
INTERNAL = {"ToolSearch", "TodoWrite", "TaskCreate", "TaskUpdate"}  # bookkeeping the user doesn't read as a step
redactions = 0


def redact(s):
    global redactions
    s = s.replace(HOME, "~")
    for i, rx in enumerate(SECRETS):
        repl = (lambda m: m.group(1) + m.group(2) + "<redacted>") if i == 2 else "<redacted>"
        s, n = rx.subn(repl, s)
        redactions += n
    return s


def find_session(arg):
    if arg and os.path.exists(arg):
        return arg
    if arg:
        hits = glob.glob(os.path.join(HOME, ".claude", "projects", "*", arg + ".jsonl"))
    else:
        project = re.sub(r"[^A-Za-z0-9]", "-", os.getcwd())
        hits = sorted(glob.glob(os.path.join(HOME, ".claude", "projects", project, "*.jsonl")), key=os.path.getmtime)[-1:]
    if not hits:
        sys.exit(f"session not found: {arg or os.getcwd()}")
    return hits[0]


def prompt_text(content):
    """The prompt as the user typed it, or None for records that aren't a prompt."""
    if isinstance(content, list):
        if any(b.get("type") == "tool_result" for b in content):
            return None
        content = "\n".join(b.get("text", "") for b in content if b.get("type") == "text")
    m = re.search(r"<command-name>(.*?)</command-name>", content, re.S)
    if m:
        args = re.search(r"<command-args>(.*?)</command-args>", content, re.S)
        return (m.group(1).strip() + " " + (args.group(1).strip() if args else "")).strip()
    content = HIDDEN.sub("", content).strip()
    if not content or content.startswith("[Request interrupted"):
        return None
    return content


def ran(name, inp):
    """One line for a tool call, in the words the user saw in the terminal."""
    if name == "AskUserQuestion":
        return "[asked: " + " / ".join(q.get("question", "") for q in inp.get("questions", [])) + "]"
    for key in ("description", "query", "url", "file_path", "pattern", "skill", "command", "prompt"):
        v = inp.get(key)
        if isinstance(v, str) and v.strip():
            return f"[ran: {name} — {v.strip().splitlines()[0][:120]}]"
    return f"[ran: {name}]"


def answer(content):
    """The user's pick in an AskUserQuestion result, which they did see and choose."""
    text = content if isinstance(content, str) else "\n".join(b.get("text", "") for b in content or [] if isinstance(b, dict))
    m = re.search(r'"[^"]*"="([^"]*)"', text)
    return f"[answered: {m.group(1)}]" if m else None


def load(path):
    """Turns as [(role, text)], consecutive same-role pieces merged, plus session metadata."""
    records = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    meta, asks, turns = {}, set(), []

    def add(role, text):
        if turns and turns[-1][0] == role:
            turns[-1][1].append(text)
        else:
            turns.append((role, [text]))

    for o in records:
        if o.get("isSidechain") or o.get("isCompactSummary"):
            continue
        for k, mk in (("version", "version"), ("cwd", "cwd"), ("sessionId", "session_id"), ("timestamp", "started")):
            meta[mk] = meta.get(mk) or o.get(k)
        msg = o.get("message") or {}
        if o.get("type") == "user" and not o.get("isMeta"):
            content = msg.get("content", "")
            if isinstance(content, list):
                for b in content:
                    if b.get("type") == "tool_result" and b.get("tool_use_id") in asks and (a := answer(b.get("content"))):
                        add("user", a)
            p = prompt_text(content)
            if p is not None:
                add("user", p)
        elif o.get("type") == "assistant" and turns:
            meta["model"] = meta.get("model") or msg.get("model")
            for b in msg.get("content", []):
                if b.get("type") == "text" and b["text"].strip():
                    add("assistant", b["text"].strip())
                elif b.get("type") == "tool_use" and b["name"] not in INTERNAL:
                    if b["name"] == "AskUserQuestion":
                        asks.add(b["id"])
                    add("assistant", ran(b["name"], b.get("input", {})))
    join = lambda parts: "".join(("\n" if p.startswith("[") and q.startswith("[") else "\n\n") + q
                                 for p, q in zip([""] + parts, parts)).lstrip()
    return [(r, join(parts)) for r, parts in turns], meta


def frontmatter(f):
    def val(v):
        if isinstance(v, list):
            return "[" + ", ".join(str(x) for x in v) + "]"
        if isinstance(v, bool):
            return str(v).lower()
        return json.dumps(v) if isinstance(v, str) and (":" in v or v[:1] in "[{\"'#&*!|>%@`") else str(v)
    return "---\n" + "".join(f"{k}: {val(v)}\n" for k, v in f.items() if v not in (None, "")) + "---\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("session", nargs="?")
    ap.add_argument("--repo", default=os.environ.get("GOLDEN_REPO"), help="golden repo clone (default $GOLDEN_REPO)")
    ap.add_argument("--why", required=True)
    ap.add_argument("--why-suggested", action="store_true", help="the why was drafted by the agent, not the user")
    ap.add_argument("--title", required=True)
    ap.add_argument("--slug")
    ap.add_argument("--labels", default="")
    ap.add_argument("--golden-turns", default="")
    ap.add_argument("--mode")
    ap.add_argument("--thread")
    ap.add_argument("--until", type=int, help="keep turns 1..N instead of cutting at the save request")
    ap.add_argument("--pr", action="store_true", help="open a PR with this file and merge it")
    a = ap.parse_args()
    if not a.repo:
        sys.exit("no golden repo: pass --repo or set GOLDEN_REPO")

    path = find_session(a.session)
    turns, meta = load(path)
    if a.until:
        turns = turns[:a.until]
    else:  # stop before the first request to save; no /golden in the log → before the last prompt
        asks = [i for i, (r, t) in enumerate(turns) if r == "user"]
        cut = next((i for i in asks if re.match(r"/(\S+:)?golden\b", turns[i][1])), asks[-1] if asks else len(turns))
        turns = turns[:cut]
    if not turns:
        sys.exit("no turns to save")

    now = datetime.datetime.now(datetime.timezone.utc)
    slug = a.slug or re.sub(r"[^a-z0-9]+", "-", a.title.lower()).strip("-")[:48].rstrip("-")
    sid = f"{now:%Y-%m-%d}-{slug}"
    body = "".join(f"### {i} · **{r}:**\n\n{redact(t)}\n\n" for i, (r, t) in enumerate(turns, 1))
    fm = frontmatter({
        "schema": 1, "id": sid, "title": a.title, "why": a.why,
        "why_source": "suggested" if a.why_suggested else "user",
        "harness": "claude-code", "harness_version": meta.get("version"), "model": meta.get("model"),
        "session_id": meta.get("session_id"), "source_path": redact(path), "started": meta.get("started"),
        "captured": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "cwd": redact(meta.get("cwd") or ""),
        "mode": a.mode, "turns": len(turns), "complete": True,
        "golden_turns": [int(x) for x in a.golden_turns.split(",") if x.strip()],
        "labels": [x.strip() for x in a.labels.split(",") if x.strip()], "thread": a.thread, "status": "raw",
    })

    out = os.path.join(a.repo, "sessions", sid, "session.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(fm + "\n" + body.rstrip() + "\n")
    print(f"wrote {out} ({len(turns)} turns, {redactions} redactions)", file=sys.stderr)

    if a.pr:  # one squash-merged PR per session, so GitHub's Revert button undoes it
        git = lambda *c: subprocess.run(["git", "-C", a.repo, *c], check=True)
        gh = lambda *c: subprocess.run(["gh", *c], cwd=a.repo, check=True, capture_output=True, text=True).stdout.strip()
        rel, branch = os.path.relpath(out, a.repo), f"golden/{sid}"
        base = gh("repo", "view", "--json", "defaultBranchRef", "-q", ".defaultBranchRef.name")
        git("fetch", "origin", base)
        git("switch", "-c", branch, f"origin/{base}")
        git("add", rel)
        git("commit", "-m", f"golden: {a.title}", "--", rel)
        git("push", "-u", "origin", branch)
        url = gh("pr", "create", "--base", base, "--head", branch, "--title", f"golden: {a.title}", "--body", a.why)
        gh("pr", "merge", url, "--squash", "--delete-branch")
        print(f"merged {url}", file=sys.stderr)


if __name__ == "__main__":
    main()
