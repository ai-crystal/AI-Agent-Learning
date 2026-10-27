# -*- coding: utf-8 -*-
"""统一的插图风格：所有示意图都用这套函数画，保证全书的线条、字号、配色一致。"""
import os
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon, Wedge
from matplotlib.lines import Line2D
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "images")
os.makedirs(OUT, exist_ok=True)
INK = "#1c1c1c"
GRAY = "#6b6b6b"
LIGHT = "#f2f1ed"
MID = "#d8d6cf"
ACCENT = "#a83232"
ACCENT2 = "#2f5d8a"
ACCENT3 = "#4a7a52"
WHITE = "#ffffff"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Microsoft YaHei", "SimHei", "Noto Sans SC"],
    "axes.unicode_minus": False,
    "figure.dpi": 200,
    "savefig.dpi": 200,
    "text.color": INK,
    "axes.edgecolor": GRAY,
    "axes.labelcolor": INK,
    "xtick.color": GRAY,
    "ytick.color": GRAY,
})

W = 6.6  # 英寸，对应正文宽度


def canvas(h=3.6, w=W, xlim=(0, 100), ylim=(0, 100)):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.02)
    return fig, ax


def box(ax, x, y, w, h, text="", fc=LIGHT, ec=INK, fs=8.6, bold=False, ls="-",
        lw=1.0, tc=INK, round=0.6, va="center", ha="center", alpha=1.0, zorder=2):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={round}",
                       fc=fc, ec=ec, lw=lw, ls=ls, alpha=alpha, zorder=zorder)
    ax.add_patch(p)
    if text:
        ax.text(x + w / 2 if ha == "center" else x + 1.2, y + h / 2, text,
                ha=ha, va=va, fontsize=fs, color=tc,
                fontweight="bold" if bold else "normal", zorder=zorder + 1,
                linespacing=1.5)
    return p


def arrow(ax, p1, p2, color=INK, lw=1.1, style="-|>", ls="-", rad=0.0,
          label="", lpos=0.55, fs=7.6, lcolor=None, zorder=1, shrink=2):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=10, lw=lw,
                        color=color, ls=ls, connectionstyle=f"arc3,rad={rad}",
                        shrinkA=shrink, shrinkB=shrink, zorder=zorder)
    ax.add_patch(a)
    if label:
        x = p1[0] + (p2[0] - p1[0]) * lpos
        y = p1[1] + (p2[1] - p1[1]) * lpos
        ax.text(x, y, label, fontsize=fs, color=lcolor or color, ha="center",
                va="center", zorder=zorder + 1,
                bbox=dict(fc="white", ec="none", pad=1.2))
    return a


def tag(ax, x, y, text, color=ACCENT, fs=7.6, ha="left", va="center", bold=True):
    ax.text(x, y, text, fontsize=fs, color=color, ha=ha, va=va,
            fontweight="bold" if bold else "normal")


def save(fig, name):
    import numpy as np
    from PIL import Image, ImageChops
    match = re.match(r"ch(\d{2})-", name)
    chapter = match.group(1) if match else "misc"
    chapter_dir = os.path.join(OUT, chapter)
    os.makedirs(chapter_dir, exist_ok=True)
    path = os.path.join(chapter_dir, name)
    fig.savefig(path, bbox_inches="tight", pad_inches=0.04, facecolor="white")
    plt.close(fig)
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg).convert("L")
    box = diff.point(lambda x: 255 if x > 6 else 0).getbbox()
    if box:
        pad = 8
        box = (max(0, box[0] - pad), max(0, box[1] - pad),
               min(im.width, box[2] + pad), min(im.height, box[3] + pad))
        im.crop(box).save(path)
    print("  ->", name)


def seq_label(ax, x, y, w, h, num, title, body="", fc=WHITE, ec=INK, fs=8.2):
    box(ax, x, y, w, h, "", fc=fc, ec=ec)
    ax.add_patch(Circle((x + 2.6, y + h - 2.6), 1.5, fc=ACCENT, ec="none", zorder=4))
    ax.text(x + 2.6, y + h - 2.6, str(num), color="white", fontsize=7.2,
            ha="center", va="center", fontweight="bold", zorder=5)
    ax.text(x + 2.6, y + h - 6.2, title, fontsize=fs, fontweight="bold",
            ha="left", va="center")
    if body:
        ax.text(x + 2.6, y + h - 10.4, body, fontsize=fs - 0.8, color="#333",
                ha="left", va="top", linespacing=1.55)
