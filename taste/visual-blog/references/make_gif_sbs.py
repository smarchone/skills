"""Side-by-side version of the 10x ledger GIF: Micromanage (left) vs Delegate goals (right),
running on the same project clock. Arrows grow upward as rows stack.
Usage: python make_gif_sbs.py <frames_dir>
"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
S = 2
PW, H = 600, 680          # one panel
W = PW * 2
C = dict(bg=(247, 248, 250), fg=(20, 28, 40), muted=(91, 102, 118), rule=(214, 220, 229),
         human=(47, 67, 201), hsoft=(227, 231, 251), agent=(11, 133, 116), asoft=(221, 242, 238),
         warn=(200, 65, 47), wsoft=(249, 225, 221), track=(230, 233, 238))
AV = '/System/Library/Fonts/Avenir Next.ttc'
MENLO = '/System/Library/Fonts/Menlo.ttc'
def F(path, size, idx=0): return ImageFont.truetype(path, int(size * S), index=idx)
F_TITLE = F(AV, 28, 0); F_NAME = F(AV, 14, 2); F_LABEL = F(AV, 17, 0)
F_MONO = F(MENLO, 11); F_MONO_S = F(MENLO, 10.5); F_SUB = F(MENLO, 12); F_PCT = F(AV, 20, 0)

BASE, BUDGET_Y = 610, 210
HX0, HX1, MX0, MX1, AX0, AX1 = 58, 236, 250, 350, 364, 542
HARROW, AARROW = 30, 570
PROJECTS = ['Billing retries', 'Search ranking', 'Onboarding emails', 'Audit log export',
            'Mobile dark mode', 'Rate limiter', 'Docs site', 'Flaky test triage']
MICRO = ['rename var in charge()', 'why is import failing?', 'no, use the other util',
         'rerun that test', 'revert line 42', 'which branch is this?']
ROW_H = {'micro': 150, 'goal': 46}
MICRO_FIT = 3   # rows that physically fit; later projects wait in the queue

def P(*v): return [round(x * S) for x in v]

hatch = Image.new('RGB', (PW * S, H * S), C['wsoft'])
hd = ImageDraw.Draw(hatch)
for k in range(-H * S, PW * S, 9 * S):
    hd.line([k, H * S, k + H * S, 0], fill=(232, 168, 158), width=2 * S)

def text(d, x, y, s, f, fill, anchor='la'): d.text((x * S, y * S), s, font=f, fill=fill, anchor=anchor)

def dashed(d, x0, y0, x1, y1, col, w=1.5, dash=7, gap=5):
    L = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L; p = 0
    while p < L:
        q = min(p + dash, L)
        d.line(P(x0 + ux * p, y0 + uy * p, x0 + ux * q, y0 + uy * q), fill=col, width=round(w * S))
        p += dash + gap

def arrow(d, x0, y0, x1, y1, col, w=2, head=9):
    d.line(P(x0, y0, x1, y1), fill=col, width=round(w * S))
    a = math.atan2(y1 - y0, x1 - x0)
    for s in (-1, 1):
        b = a + math.pi - s * 0.5
        d.line(P(x1, y1, x1 + head * math.cos(b), y1 + head * math.sin(b)), fill=col, width=round(w * S))

def panel(mode, ts, queued, sub, subcol):
    img = Image.new('RGB', (PW * S, H * S), C['bg']); d = ImageDraw.Draw(img)
    rh = ROW_H[mode]
    used = sum(rh * t for t in ts)
    pct = used / 400

    text(d, 30, 26, 'Micromanage' if mode == 'micro' else 'Delegate goals', F_TITLE, C['fg'])
    text(d, 30, 70, sub, F_SUB, subcol)
    if queued:
        text(d, 30, 92, f'{queued} more project{"s" if queued > 1 else ""} waiting on you', F_SUB, C['warn'])
    # attention meter
    mx0, mx1, my = 380, 570, 48
    text(d, mx0, 24, 'your attention', F_MONO, C['muted'])
    text(d, mx1, 20, f'{round(pct * 100)}%', F_PCT, C['warn'] if pct > 1 else C['human'], 'ra')
    d.rounded_rectangle(P(mx0, my, mx1, my + 9), radius=4.5 * S, fill=C['track'])
    full = (mx1 - mx0) / 1.25
    fw = min(pct, 1.25) * full
    if fw > 1:
        d.rounded_rectangle(P(mx0, my, mx0 + fw, my + 9), radius=4.5 * S, fill=C['warn'] if pct > 1 else C['human'])
    d.line(P(mx0 + full, my - 4, mx0 + full, my + 13), fill=C['fg'], width=2 * S)

    for (a, b, c_, e) in [(HX0, BUDGET_Y, HX0, BASE), (HX1, BUDGET_Y, HX1, BASE)]:
        dashed(d, a, b, c_, e, C['human'])

    y1 = BASE
    for i, t in enumerate(ts):
        if t <= 0: continue
        h = rh * t; y0 = y1 - h
        done = t >= 0.999
        over = (y1 - rh) < BUDGET_Y - 0.5
        name = PROJECTS[i]
        box = P(HX0 + 5, y0 + 3, HX1 - 5, y1 - 3)
        if box[3] - box[1] > 2:
            if over:
                m = Image.new('L', img.size, 0)
                ImageDraw.Draw(m).rounded_rectangle(box, radius=5 * S, fill=255)
                img.paste(hatch, (0, 0), m)
                d.rounded_rectangle(box, radius=5 * S, outline=C['warn'], width=round(1.5 * S))
            else:
                d.rounded_rectangle(box, radius=5 * S, fill=C['hsoft'])
        if mode == 'micro':
            if h > 8:
                for (a, b, c_, e) in [(AX0 + 5, y0 + 3, AX1 - 5, y0 + 3), (AX0 + 5, y1 - 3, AX1 - 5, y1 - 3),
                                      (AX0 + 5, y0 + 3, AX0 + 5, y1 - 3), (AX1 - 5, y0 + 3, AX1 - 5, y1 - 3)]:
                    dashed(d, a, b, c_, e, C['rule'], w=1.2, dash=4, gap=4)
            if done:
                col = C['warn'] if over else C['fg']
                text(d, HX0 + 14, y0 + 12, name, F_NAME, col)
                for j, s in enumerate(MICRO):
                    text(d, HX0 + 14, y0 + 38 + j * 17, s, F_MONO, C['warn'] if over else C['muted'])
                text(d, AX0 + 14, y0 + 12, name, F_NAME, C['muted'])
                text(d, AX0 + 14, y0 + 38, 'waiting on you…', F_MONO, C['muted'])
                for k in range(5):
                    yy = y0 + 32 + k * 22
                    if k % 2 == 0: arrow(d, MX0 + 6, yy, MX1 - 6, yy + 10, C['human'], w=1.5, head=7)
                    else: arrow(d, MX1 - 6, yy, MX0 + 6, yy + 10, C['agent'], w=1.5, head=7)
        else:
            abox = P(AX0 + 5, y0 + 3, AX1 - 5, y1 - 3)
            if abox[3] - abox[1] > 2:
                d.rounded_rectangle(abox, radius=5 * S, fill=C['asoft'])
            if h > 26:
                d.rounded_rectangle(P(MX0, y0 + 12, MX1, y1 - 12), radius=4 * S, fill=C['rule'])
            if done:
                text(d, HX0 + 14, y0 + 8, name, F_NAME, C['fg'])
                text(d, HX0 + 14, y0 + 28, 'why · shape · done-when', F_MONO_S, C['muted'])
                text(d, AX0 + 14, y0 + 8, name, F_NAME, C['fg'])
                text(d, AX0 + 14, y0 + 28, 'plan · code · tests · PR', F_MONO_S, C['muted'])
                text(d, (MX0 + MX1) / 2, (y0 + y1) / 2, 'goal + ctx', F_MONO_S, C['fg'], 'mm')
        y1 = y0

    dashed(d, HX0 - 8, BUDGET_Y, HX1 + 8, BUDGET_Y, C['human'], w=2)
    d.rectangle(P(HX1 - 118, BUDGET_Y - 19, HX1 + 2, BUDGET_Y - 4), fill=C['bg'])
    text(d, HX1, BUDGET_Y - 8, 'attention budget', F_MONO_S, C['human'], 'rs')

    d.line(P(14, BASE, PW - 14, BASE), fill=C['rule'], width=2 * S)
    top = min(BASE - 60, y1 - 26)
    arrow(d, HARROW, BASE + 2, HARROW, top, C['human'], w=2.5, head=11)
    arrow(d, AARROW, BASE + 2, AARROW, top, C['agent'], w=2.5, head=11)

    text(d, (HX0 + HX1) / 2, 632, 'Human', F_LABEL, C['human'], 'mm')
    text(d, (HX0 + HX1) / 2, 656, 'context in your head', F_MONO, C['muted'], 'mm')
    text(d, (MX0 + MX1) / 2, 632, 'shared' if mode == 'goal' else 'you, typing', F_MONO, C['muted'], 'mm')
    text(d, (AX0 + AX1) / 2, 632, 'Agent', F_LABEL, C['agent'], 'mm')
    text(d, (AX0 + AX1) / 2, 656, 'context in its window', F_MONO, C['muted'], 'mm')
    return img

def ease(t): return 1 - (1 - t) ** 3

GROW, HOLD, LEAD, END = 12, 8, 12, 70
SUB_M = "You hold the details. Agents wait."
SUB_G = 'You hold goals. Agents hold the work.'

def compose(left, right):
    img = Image.new('RGB', (W * S, H * S), C['bg'])
    img.paste(left, (0, 0)); img.paste(right, (PW * S, 0))
    ImageDraw.Draw(img).line(P(PW, 24, PW, H - 24), fill=C['rule'], width=2 * S)
    return img.resize((W, H), Image.LANCZOS)

frames = []
n = len(PROJECTS)
tg = [0.0] * n; tm = [0.0] * MICRO_FIT; queued = 0
def snap(end=False):
    sm = 'Over budget. Rows past the line get dropped.' if end else SUB_M
    sg = f'{n} projects in flight. Inside your budget.' if end else SUB_G
    frames.append(compose(panel('micro', list(tm), queued, sm, C['warn'] if end else C['muted']),
                          panel('goal', list(tg), 0, sg, C['agent'] if end else C['muted'])))

for _ in range(LEAD): snap()
for i in range(n):
    for f in range(1, GROW + 1):
        e = ease(f / GROW); tg[i] = e
        if i < MICRO_FIT: tm[i] = e
        snap()
    if i >= MICRO_FIT: queued += 1
    for _ in range(HOLD): snap()
for _ in range(END): snap(end=True)

for k, im in enumerate(frames):
    im.save(os.path.join(OUT, f'f{k:04d}.png'))
print(len(frames), 'frames')
