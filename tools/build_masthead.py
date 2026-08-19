#!/usr/bin/env python3
"""
Renders the Basement Gazette front-page furniture as SVG, with all type
converted to outlines so GitHub renders it without needing the fonts.

    python tools/build_masthead.py

Writes assets/masthead-light.svg and assets/masthead-dark.svg.
"""

import re
from datetime import date
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"
OUT = ROOT / "assets"

# ---------------------------------------------------------------- palette
# Sampled straight off shvmkpr.in so the README matches the site exactly.
THEMES = {
    "light": dict(bg="#d8d4ca", ink="#16161a", red="#9d262f", muted="#6f6b60", rule="#16161a"),
    "dark":  dict(bg="#1b1c1e", ink="#e7e1cb", red="#d6786e", muted="#8a857a", rule="#e7e1cb"),
}

W = 1200
H = 384
M = 40  # page margin

# ---------------------------------------------------------------- masthead copy
ISSUE = "VOL. I \u00b7 NO. 5"
PLACE = f"JAIPUR \u00b7 {date.today().strftime('%A, %-d %B %Y').upper()}"
EDITION = "GITHUB EDITION"
EST = "EST. 2026"
TITLE = "The Basement Gazette"
KICKER = "SOFTWARE \u00b7 HARDWARE \u00b7 THINGS HALF-BUILT"
NAV = ["FRONT PAGE", "WORKSHOP", "MOTORING", "LAB NOTES", "MARKETS",
       "CLASSIFIEDS", "OP-ED", "ARCHIVE", "ABOUT"]
NAV_ACTIVE = 0
WEATHER = [("WEATHER", "label"), ("Hazy, hot", "body"), ("39\u00b0 / 28\u00b0", "body")]
PRICE = [("FREE", "label"), ("\u2605\u2605\u2605 Late Edition", "body"), ("Circulation 11", "body")]
TICKER = [("JRVS", "12", "up", "10"), ("CHLK", "9", "up", "6"),
          ("SQON", "3", "flat", ""), ("EBIK", "0", "down", "-2")]


# ---------------------------------------------------------------- type engine
class Face:
    """A font at one weight, able to emit SVG path data for a string."""

    def __init__(self, path, wght=None, opsz=None):
        font = TTFont(path)
        axes = {}
        if wght is not None:
            axes["wght"] = wght
        if opsz is not None:
            axes["opsz"] = opsz
        if axes and "fvar" in font:
            font = instancer.instantiateVariableFont(font, axes)
        self.font = font
        self.upem = font["head"].unitsPerEm
        self.glyphs = font.getGlyphSet()
        self.cmap = font.getBestCmap()
        self.hmtx = font["hmtx"]

    def _name(self, ch):
        return self.cmap.get(ord(ch))

    def width(self, text, size, tracking=0.0):
        total = 0.0
        for ch in text:
            gn = self._name(ch)
            if gn:
                total += self.hmtx[gn][0] * size / self.upem
            elif ch == " ":
                total += size * 0.28
        if len(text) > 1:
            total += tracking * (len(text) - 1)
        return total

    def path(self, text, size, x, y, fill, tracking=0.0, anchor="start", opacity=None):
        if anchor == "middle":
            x -= self.width(text, size, tracking) / 2
        elif anchor == "end":
            x -= self.width(text, size, tracking)
        scale = size / self.upem
        cursor = x
        d = []
        for ch in text:
            gn = self._name(ch)
            if gn is None:
                cursor += size * 0.28 + tracking
                continue
            pen = SVGPathPen(self.glyphs)
            tp = TransformPen(pen, Transform(scale, 0, 0, -scale, cursor, y))
            self.glyphs[gn].draw(tp)
            seg = pen.getCommands()
            if seg:
                d.append(seg)
            cursor += self.hmtx[gn][0] * scale + tracking
        if not d:
            return ""
        op = f' opacity="{opacity}"' if opacity else ""
        return f'<path d="{" ".join(d)}" fill="{fill}"{op}/>'


# ---------------------------------------------------------------- primitives
def rule(x1, y, x2, color, w=1, opacity=None):
    op = f' opacity="{opacity}"' if opacity else ""
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{w}"{op}/>'


def vrule(x, y1, y2, color, w=1, opacity=None):
    op = f' opacity="{opacity}"' if opacity else ""
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="{w}"{op}/>'


def box(x, y, w, h, color, sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{color}" stroke-width="{sw}"/>'


def star(x, y, color, r=5.5):
    import math
    pts = []
    for i in range(10):
        rad = r if i % 2 == 0 else r * 0.42
        a = -math.pi / 2 + i * math.pi / 5
        pts.append(f"{x + rad * math.cos(a):.1f},{y + rad * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{color}"/>'


def tri(x, y, color, up=True, s=5):
    pts = f"{x},{y-s} {x-s},{y+s} {x+s},{y+s}" if up else f"{x},{y+s} {x-s},{y-s} {x+s},{y-s}"
    return f'<polygon points="{pts}" fill="{color}"/>'


# ---------------------------------------------------------------- composition
def build(theme_name):
    t = THEMES[theme_name]
    black = Face(FONTS / "mc.ttf")                       # nameplate
    cond = Face(FONTS / "an.ttf", wght=500)              # furniture
    cond_b = Face(FONTS / "an.ttf", wght=700)            # tickers, labels
    serif = Face(FONTS / "ss.ttf", wght=400, opsz=20)    # weather / price boxes

    o = [f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>']

    # --- top bar -------------------------------------------------------
    y = 30
    o.append(cond.path(ISSUE, 13, M, y, t["muted"], tracking=1.6))
    o.append(cond.path(PLACE, 13, W / 2, y, t["muted"], tracking=1.6, anchor="middle"))
    o.append(cond.path(EST, 13, W - M, y, t["muted"], tracking=1.6, anchor="end"))
    ex = W - M - cond.width(EST, 13, 1.6) - 48
    o.append(cond.path(EDITION, 13, ex, y, t["ink"], tracking=1.6, anchor="end"))
    o.append(rule(ex - cond.width(EDITION, 13, 1.6), y + 6, ex, t["ink"], 0.75))
    o.append(rule(M, 48, W - M, t["rule"], 0.75, opacity=0.45))

    # --- weather + price boxes ----------------------------------------
    for bx, rows, align in ((M, WEATHER, "start"), (W - M - 210, PRICE, "end")):
        o.append(box(bx, 68, 210, 96, t["rule"], 0.75))
        ax = bx + 16 if align == "start" else bx + 194
        o.append(cond_b.path(rows[0][0], 12, ax, 94, t["ink"], tracking=2.2, anchor=align))
        o.append(serif.path(rows[1][0], 16, ax, 122, t["ink"], anchor=align))
        o.append(serif.path(rows[2][0], 16, ax, 146, t["ink"], anchor=align))
        if rows is PRICE:  # ★★★ has no glyph in the serif — draw it
            sx = ax - serif.width(rows[1][0], 16) - 20
            for k in range(3):
                o.append(star(sx - k * 13, 117, t["ink"]))

    # --- nameplate ------------------------------------------------------
    o.append(black.path(TITLE, 82, W / 2, 152, t["ink"], anchor="middle"))
    # hairlines flanking the nameplate, as on the site
    half = black.width(TITLE, 82) / 2
    o.append(rule(M + 226, 158, W / 2 - half - 18, t["rule"], 0.75, opacity=0.45))
    o.append(rule(W / 2 + half + 18, 158, W - M - 226, t["rule"], 0.75, opacity=0.45))

    o.append(cond.path(KICKER, 14, W / 2, 196, t["muted"], tracking=6, anchor="middle"))
    o.append(rule(M, 218, W - M, t["rule"], 0.75, opacity=0.45))

    # --- nav ------------------------------------------------------------
    widths = [cond.width(n, 15, 1.8) for n in NAV]
    gap = (W - 2 * M - 40 - sum(widths)) / (len(NAV) - 1)
    x = M + 20
    for i, (n, wd) in enumerate(zip(NAV, widths)):
        o.append(cond.path(n, 15, x, 252, t["red"] if i == NAV_ACTIVE else t["ink"], tracking=1.8))
        x += wd + gap
    o.append(rule(M, 272, W - M, t["rule"], 0.75, opacity=0.45))

    # --- markets ---------------------------------------------------------
    o.append(cond.path("MARKETS \u00b7 COMMITS THIS SESSION AGAINST THE LAST", 12, M, 300,
                       t["muted"], tracking=2.4))
    colw = (W - 2 * M) / len(TICKER)
    for i, (sym, val, dirn, chg) in enumerate(TICKER):
        cx = M + i * colw
        if i:
            vrule(cx - 14, 314, 352, t["rule"], 0.75)
            o.append(vrule(cx - 14, 314, 352, t["rule"], 0.75, opacity=0.35))
        o.append(cond_b.path(sym, 19, cx, 340, t["ink"], tracking=0.6))
        vx = cx + cond_b.width(sym, 19, 0.6) + 14
        o.append(serif.path(val, 19, vx, 340, t["ink"]))
        ax = vx + serif.width(val, 19) + 18
        if dirn == "flat":
            o.append(rule(ax - 4, 336, ax + 10, t["muted"], 1.5))
        else:
            o.append(tri(ax + 3, 334, t["red"], up=(dirn == "up")))
            o.append(cond_b.path(chg, 15, ax + 14, 340, t["red"], tracking=0.4))

    # --- bottom double rule ------------------------------------------------
    o.append(rule(M, 366, W - M, t["rule"], 2.5))
    o.append(rule(M, 373, W - M, t["rule"], 0.75, opacity=0.6))

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
           f'height="{H}" role="img" aria-label="The Basement Gazette — GitHub Edition">'
           + "".join(x for x in o if x) + "</svg>")
    # outlines carry far more precision than a 1200px banner needs
    return re.sub(r"-?\d+\.\d+", lambda m: f"{float(m.group()):.1f}", svg)


FONT_SOURCES = {
    "mc.ttf": "ofl/manufacturingconsent/ManufacturingConsent-Regular.ttf",
    "an.ttf": "ofl/archivonarrow/ArchivoNarrow%5Bwght%5D.ttf",
    "ss.ttf": "ofl/sourceserif4/SourceSerif4%5Bopsz,wght%5D.ttf",
}


def ensure_fonts():
    """Pull the three faces from the Google Fonts repo if they aren't here yet."""
    from urllib.request import urlretrieve
    base = "https://raw.githubusercontent.com/google/fonts/main/"
    FONTS.mkdir(exist_ok=True)
    for name, rel in FONT_SOURCES.items():
        dest = FONTS / name
        if not dest.exists():
            print(f"fetching {name} ...")
            urlretrieve(base + rel, dest)


if __name__ == "__main__":
    ensure_fonts()
    OUT.mkdir(exist_ok=True)
    for name in THEMES:
        p = OUT / f"masthead-{name}.svg"
        p.write_text(build(name))
        print(f"wrote {p.relative_to(ROOT)}  ({p.stat().st_size // 1024} KB)")
