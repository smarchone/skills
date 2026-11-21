#!/usr/bin/env python3
"""Extract the visible conversation from an agent session log as a golden session file.

Reads the JSONL transcript the harness writes — Claude Code under ~/.claude/projects/, agy (Antigravity
CLI) under ~/.gemini/antigravity-cli/brain/<id>/ — so the turns come out exactly as written, not recalled. Keeps the conversation: the user's prompts, the assistant's replies, and the
questions it asked with the user's answers. Drops tool calls and their output, thinking, system
reminders, skill bodies and subagent traffic. Redacts the home dir, emails and token-shaped strings.

Usage:
  golden.py [SESSION] [--harness claude-code|agy] --repo DIR --why "..." [--why-suggested] --title "..." [--slug S] [--labels a,b] [--golden-turns 4,8]
            [--mode skill:x] [--until N] [--pr [--index]]

SESSION is a .jsonl path or a session id; omitted, it's the newest session for the current directory.
The harness comes from --harness, else the SESSION path, else claude-code inside Claude Code, else agy
when agy has a session for this directory.
Turns stop before the first /golden prompt (or the last prompt, if none) unless --until N. Writes
<repo>/<YYYY-MM>/<YYYY-MM-DD>-<slug>.md; --pr also opens a PR with it and squash-merges it; --index adds it to the repo's index.json in that PR. Stdlib only.
"""
import argparse, datetime, glob, json, os, re, subprocess, sys

HOME = os.path.expanduser("~")
AGY = os.path.join(HOME, ".gemini", "antigravity-cli")
HIDDEN = re.compile(r"<(system-reminder|local-command-stdout|local-command-caveat)>.*?</\1>\s*", re.S)
SECRETS = [
    re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    re.compile(r"\b(sk-[\w-]{16,}|gh[pousr]_\w{20,}|github_pat_\w{20,}|xox[abprs]-[\w-]{10,}|AKIA[0-9A-Z]{16}|AIza[\w-]{30,})"),
    re.compile(r"(?i)\b(bearer|token|api[_-]?key|secret|password)([\"']?\s*[:=]\s*[\"']?)[^\s\"']{8,}"),
]
ASK = ("AskUserQuestion", "ask_question")  # the only tool calls kept: a question the user answered
redactions = 0


def redact(s):
    global redactions
    s = s.replace(HOME, "~")
    for i, rx in enumerate(SECRETS):
        repl = (lambda m: m.group(1) + m.group(2) + "<redacted>") if i == 2 else "<redacted>"
        s, n = rx.subn(repl, s)
        redactions += n
    return s


def agy_log(cid):
    logs = os.path.join(AGY, "brain", cid, ".system_generated", "logs")
    return next((p for p in (os.path.join(logs, f) for f in ("transcript_full.jsonl", "transcript.jsonl")) if os.path.exists(p)), None)


def agy_workspaces():
    """conversation id -> workspace dir, from the prompt history agy keeps."""
    out = {}
    try:
        for l in open(os.path.join(AGY, "history.jsonl"), encoding="utf-8"):
            try:
                o = json.loads(l)
            except ValueError:
                continue
            if o.get("conversationId") and o.get("workspace"):
                out[o["conversationId"]] = o["workspace"]
    except OSError:
        pass
    return out


def find_agy_session(arg):
    if arg and os.path.exists(arg):
        return arg
    if arg:
        hits = [agy_log(arg)]
    else:
        cwd = os.path.realpath(os.getcwd())
        ids = [c for c, w in agy_workspaces().items() if os.path.realpath(w) == cwd]
        hits = sorted(filter(None, map(agy_log, ids)), key=os.path.getmtime)[-1:]
    hits = [h for h in hits if h]
    if not hits:
        sys.exit(f"agy session not found: {arg or os.getcwd()}")
    return hits[0]


def pick_harness(choice, arg):
    if choice:
        return choice
    if arg:
        return "agy" if os.path.realpath(arg).startswith(os.path.realpath(AGY)) or (not os.path.exists(arg) and agy_log(arg)) else "claude-code"
    if os.environ.get("CLAUDECODE"):
        return "claude-code"
    cwd = os.path.realpath(os.getcwd())
    return "agy" if any(os.path.realpath(w) == cwd for w in agy_workspaces().values()) else "claude-code"


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


def asked(inp):
    """One line for a question put to the user."""
    return "[asked: " + " / ".join(q.get("question", "") for q in inp.get("questions", [])) + "]"


def answer(content):
    """The user's pick in an AskUserQuestion result, which they did see and choose."""
    text = content if isinstance(content, str) else "\n".join(b.get("text", "") for b in content or [] if isinstance(b, dict))
    m = re.search(r'"[^"]*"="([^"]*)"', text)
    return f"[answered: {m.group(1)}]" if m else None


def collector():
    turns = []

    def add(role, text):
        if turns and turns[-1][0] == role:
            turns[-1][1].append(text)
        else:
            turns.append((role, [text]))
    return turns, add


def joined(turns):
    """Consecutive same-role pieces merged; [asked/answered: …] lines stack, prose gets a blank line."""
    join = lambda parts: "".join(("\n" if p.startswith("[") and q.startswith("[") else "\n\n") + q
                                 for p, q in zip([""] + parts, parts)).lstrip()
    return [(r, join(parts)) for r, parts in turns]


def load_claude(path):
    """Turns as [(role, text)] from a Claude Code session log, plus session metadata."""
    records = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    meta, asks = {}, set()
    turns, add = collector()

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
                elif b.get("type") == "tool_use" and b["name"] in ASK:
                    asks.add(b["id"])
                    add("assistant", asked(b.get("input", {})))
    return joined(turns), meta


def load_agy(path):
    """Turns as [(role, text)] from an agy transcript_full.jsonl, plus session metadata.

    Each line is one step. USER_INPUT holds the prompt inside <USER_REQUEST>; PLANNER_RESPONSE holds the
    reply text and tool_calls; ASK_QUESTION holds the user's answers as "A1: …" lines. Everything else
    (tool output, ephemeral/system messages, checkpoints) is dropped. Subagents log to their own dirs.
    """
    meta = {}
    turns, add = collector()
    cid = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(path)))))
    meta["session_id"] = cid
    meta["cwd"] = agy_workspaces().get(cid)
    try:
        meta["version"] = subprocess.run(["agy", "--version"], capture_output=True, text=True, timeout=10).stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        pass
    for l in open(path, encoding="utf-8", errors="replace"):
        try:
            o = json.loads(l)
        except ValueError:
            continue
        meta["started"] = meta.get("started") or o.get("created_at")
        kind = o.get("type")
        if kind == "USER_INPUT":
            content = o.get("content") or ""
            m = re.search(r"<USER_REQUEST>\s*(.*?)\s*</USER_REQUEST>", content, re.S)
            text = (m.group(1) if m else HIDDEN.sub("", content)).strip()
            if text:
                add("user", text)
        elif kind == "PLANNER_RESPONSE" and turns:
            meta["model"] = meta.get("model") or o.get("model")
            if (o.get("content") or "").strip():
                add("assistant", o["content"].strip())
            for t in o.get("tool_calls") or []:
                if t.get("name") in ASK:
                    args = t.get("args")
                    add("assistant", asked(args if isinstance(args, dict) else {}))
        elif kind == "ASK_QUESTION" and turns:
            picks = re.findall(r"^A\d+: (.*)$", o.get("content") or "", re.M)
            if picks:
                add("user", "[answered: " + " / ".join(picks) + "]")
    return joined(turns), meta


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
    ap.add_argument("--harness", choices=("claude-code", "agy"), help="whose log to read (default: auto)")
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
    ap.add_argument("--index", action="store_true", help="with --pr, also add the session to the repo's index.json")
    a = ap.parse_args()
    if not a.repo:
        sys.exit("no golden repo: pass --repo or set GOLDEN_REPO")

    harness = pick_harness(a.harness, a.session)
    path = find_agy_session(a.session) if harness == "agy" else find_session(a.session)
    turns, meta = (load_agy if harness == "agy" else load_claude)(path)
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
        "harness": harness, "harness_version": meta.get("version"), "model": meta.get("model"),
        "session_id": meta.get("session_id"), "source_path": redact(path), "started": meta.get("started"),
        "captured": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "cwd": redact(meta.get("cwd") or ""),
        "mode": a.mode, "turns": len(turns), "complete": True,
        "golden_turns": [int(x) for x in a.golden_turns.split(",") if x.strip()],
        "labels": [x.strip() for x in a.labels.split(",") if x.strip()], "thread": a.thread, "status": "raw",
    })

    out = os.path.join(a.repo, sid[:7], sid + ".md")
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
        files = [rel]
        index = os.path.join(a.repo, "index.json")
        if a.index and os.path.exists(index):  # the site lists only sessions in index.json
            entries = json.load(open(index, encoding="utf-8"))
            if rel not in entries:
                open(index, "w", encoding="utf-8").write(json.dumps(sorted(entries + [rel]), indent=2) + "\n")
            files.append("index.json")
        git("add", *files)
        git("commit", "-m", f"golden: {a.title}", "--", *files)
        git("push", "-u", "origin", branch)
        url = gh("pr", "create", "--base", base, "--head", branch, "--title", f"golden: {a.title}", "--body", a.why)
        gh("pr", "merge", url, "--squash", "--delete-branch")
        print(f"merged {url}", file=sys.stderr)


if __name__ == "__main__":
    main()
