#!/usr/bin/env python3
"""
Renders the two column-one features as SVG:

  assets/crossword-{light,dark}.svg   from content/puzzle.yaml
  assets/cartoon-{light,dark}.svg     hand-drawn, edit DRAW() below

    python tools/crossword.py        # sets the puzzle (edit WORDS there)
    python tools/build_features.py   # draws it

The grid is geometry, not a screenshot, so it stays crisp at any width and
follows the reader's theme. Clues live in the README as real text.
"""

import re
import sys
from pathlib import Path
from urllib.request import urlretrieve

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_masthead import THEMES, FONTS, Face, ensure_fonts, box, rule  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
PUZZLE = ROOT / "content" / "puzzle.yaml"

ITALIC = ("ss-italic.ttf",
          "ofl/sourceserif4/SourceSerif4-Italic%5Bopsz,wght%5D.ttf")

CELL = 34
PAD = 5

CAPTION = "Do not encourage it."


def round_floats(svg):
    return re.sub(r"-?\d+\.\d+", lambda m: f"{float(m.group()):.1f}", svg)


def wrap(svg_body, w, h, bg, label):
    return round_floats(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="{label}">'
        f'<rect width="{w}" height="{h}" fill="{bg}"/>{svg_body}</svg>')


# ------------------------------------------------------------------ crossword
def crossword(theme_name, data):
    t = THEMES[theme_name]
    cell_fill = "#cfcbbf" if theme_name == "light" else "#26272a"
    num = Face(FONTS / "an.ttf", wght=500)

    w = data["cols"] * CELL + PAD * 2
    h = data["rows"] * CELL + PAD * 2
    o = []
    for c in data["cells"]:
        x = PAD + c["x"] * CELL
        y = PAD + c["y"] * CELL
        o.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" '
                 f'fill="{cell_fill}" stroke="{t["ink"]}" stroke-width="1"/>')
        if "n" in c:
            o.append(num.path(str(c["n"]), 10, x + 4, y + 13, t["ink"], opacity=0.75))
    # NB: c["a"] holds the answer letter — deliberately not drawn.
    return wrap("".join(o), w, h, t["bg"], f'Crossword no. {data["number"]:02d}')


# -------------------------------------------------------------------- cartoon
def printer(x, y, s, ink, sw=2.0):
    """One desktop 3D printer, drawn at scale s from its bottom-left corner."""
    def X(v):
        return x + v * s

    def Y(v):
        return y - v * s

    L = []

    def line(x1, y1, x2, y2, width=sw):
        L.append(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" '
                 f'stroke="{ink}" stroke-width="{width * s}" stroke-linecap="square"/>')

    def rect(x1, y1, w_, h_, width=sw, fill="none"):
        L.append(f'<rect x="{X(x1)}" y="{Y(y1 + h_)}" width="{w_ * s}" height="{h_ * s}" '
                 f'fill="{fill}" stroke="{ink}" stroke-width="{width * s}"/>')

    rect(0, 0, 100, 14)          # plinth
    line(4, 14, 4, 96)           # left upright
    line(96, 14, 96, 96)         # right upright
    line(4, 96, 96, 96)          # top rail
    line(4, 74, 96, 74)          # gantry
    rect(40, 67, 20, 13)         # carriage
    L.append(f'<polygon points="{X(50)},{Y(60)} {X(45)},{Y(67)} {X(55)},{Y(67)}" fill="{ink}"/>')
    rect(14, 26, 72, 5)          # bed
    return "".join(L)


def spool(cx, cy, r, ink, sw):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{ink}" stroke-width="{sw}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * 0.28}" fill="none" stroke="{ink}" '
            f'stroke-width="{sw}"/>')


def cartoon(theme_name):
    t = THEMES[theme_name]
    W, H = 480, 330
    ink = t["ink"]
    ital = Face(FONTS / ITALIC[0], wght=400, opsz=20)

    o = [box(8, 8, W - 16, H - 16, t["rule"], 0.75)]

    # the printer, and the small printer it has just finished printing
    o.append(printer(150, 258, 1.55, ink))
    o.append(printer(214, 210, 0.30, ink, sw=3.2))

    # filament, fed in over the top rail
    o.append(spool(408, 120, 30, ink, 2.4))
    o.append(f'<path d="M 396 92 C 380 58, 300 52, 268 108" fill="none" stroke="{ink}" '
             f'stroke-width="2.2" stroke-linecap="round"/>')

    # bench line
    o.append(rule(40, 262, 440, ink, 2.4))

    o.append(ital.path(CAPTION, 19, W / 2, 300, t["muted"], anchor="middle"))
    return wrap("".join(o), W, H, t["bg"], "The cartoon")


# ----------------------------------------------------------------------- main
def main():
    ensure_fonts()
    dest = FONTS / ITALIC[0]
    if not dest.exists():
        print(f"fetching {ITALIC[0]} ...")
        urlretrieve("https://raw.githubusercontent.com/google/fonts/main/" + ITALIC[1], dest)

    if not PUZZLE.exists():
        sys.exit("content/puzzle.yaml missing — run tools/crossword.py first.")
    data = yaml.safe_load(PUZZLE.read_text(encoding="utf-8"))

    OUT.mkdir(exist_ok=True)
    for name in THEMES:
        (OUT / f"crossword-{name}.svg").write_text(crossword(name, data))
        (OUT / f"cartoon-{name}.svg").write_text(cartoon(name))
    print(f"crossword no. {data['number']:02d} — {data['cols']}x{data['rows']}, "
          f"{len(data['across'])} across, {len(data['down'])} down")

    # clue list, ready to paste into the README
    print("\n--- clues ---")
    for heading, key in (("ACROSS", "across"), ("DOWN", "down")):
        print(f"\n**{heading}**\n")
        for c in data[key]:
            print(f"<sub>**{c['n']}.** {c['clue']}</sub>  ")


if __name__ == "__main__":
    main()
