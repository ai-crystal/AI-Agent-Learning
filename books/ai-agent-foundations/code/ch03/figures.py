# -*- coding: utf-8 -*-
"""第 3 章插图生成器。运行后输出到 book/images/03/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f03_gsm8k():
    fig, ax = plt.subplots(figsize=(W * 0.76, 3.2))
    labels = ["标准提示", "思维链", "思维链\n+ 自洽性投票"]
    vals = [17.9, 56.9, 74.4]
    bars = ax.bar(labels, vals, color=["#c9c4b8", "#7f9c86", ACCENT], width=0.52)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.6, f"{v}%", ha="center",
                fontsize=11.21, fontweight="bold")
    ax.set_ylim(0, 88)
    ax.set_ylabel("GSM8K 准确率", fontsize=10.62)
    ax.tick_params(labelsize=8.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#e8e8e4", lw=0.6); ax.set_axisbelow(True)
    ax.text(0.03, 0.9, "PaLM 540B，同一个模型", transform=ax.transAxes,
            fontsize=9.44, color=GRAY)
    fig.tight_layout()
    save(fig, "ch03-gsm8k.png")

def f03_selfconsistency():
    fig, ax = canvas(3.4)
    box(ax, 2, 42, 15, 14, "问题", fc="#e7e9ec", fs=9)
    paths = [("路径 1", "42", True), ("路径 2", "42", True), ("路径 3", "38", False),
             ("路径 4", "42", True), ("路径 5", "40", False)]
    ys = [78, 66, 54, 42, 30]
    for (lab, a, good), y in zip(paths, ys):
        c = ACCENT3 if good else "#b9b5ac"
        box(ax, 24, y, 26, 8, "", fc="white", ec="#b9b5ac", fs=7.4, round=0.4)
        ax.text(26.5, y + 4, lab, fontsize=8.73, va="center")
        ax.text(46.5, y + 4, f"→ {a}", fontsize=10.15, va="center", ha="right",
                color=c, fontweight="bold" if good else "normal")
        arrow(ax, (17, 49), (24, y + 4), color="#c9c4b8", lw=0.8)
        arrow(ax, (50, y + 4), (66, 49), color="#c9c4b8", lw=0.8)
    box(ax, 66, 38, 14, 22, "投票", fc="#e8ece6", fs=8.6)
    arrow(ax, (80, 49), (85, 49), color=ACCENT3)
    ax.text(87, 49, "42", fontsize=20.06, color=ACCENT3, fontweight="bold", va="center")
    ax.text(2, 96, "采样 5 条路径，3 条落在同一个答案上", fontsize=10.38, fontweight="bold")
    save(fig, "ch03-selfconsistency.png")

def f03_tot():
    fig, ax = canvas(3.9)
    box(ax, 36, 86, 24, 9, "起始状态", fc="#e7e9ec", fs=8.4)
    kids = [(4, "3+8=11", "0.2", False), (36, "8-3=5", "0.6", True), (68, "3×8=24", "0.8", True)]
    for x, t, s, keep in kids:
        box(ax, x, 62, 24, 9, t, fc="white" if keep else "#f2f2f0",
            ec="#b9b5ac" if keep else "#d3d0c8", fs=8.0, ls="-" if keep else "--")
        arrow(ax, (48, 86), (x + 12, 71), color="#c9c4b8", lw=0.8)
        ax.text(x + 12, 58.5, f"评估 {s}", fontsize=8.50, ha="center",
                color=ACCENT if keep else GRAY)
    # 剪枝
    ax.text(25.4, 68.2, "×", fontsize=15.34, color=ACCENT, ha="center", va="center")
    ax.text(30, 74, "剪掉", fontsize=8.26, color=ACCENT, ha="right")
    # 展开
    box(ax, 34, 38, 22, 9, "5 → 无解", fc="#f2f2f0", ec="#d3d0c8", fs=7.8, ls="--")
    arrow(ax, (44, 62), (44, 47), color=GRAY, ls=":")
    box(ax, 64, 38, 28, 9, "24 × 1 = 24，达成", fc="#e8ece6", ec=ACCENT3, fs=7.6)
    arrow(ax, (78, 62), (78, 47), color=ACCENT3)
    ax.text(66, 27, "目标达成，停止搜索", fontsize=8.50, color=ACCENT3)
    arrow(ax, (46, 38), (34, 60), color=ACCENT, ls="--", rad=0.3)
    ax.text(20, 46, "走不通\n回退换分支", fontsize=8.26, color=ACCENT, linespacing=1.5)
    ax.text(2, 97, "在中间状态上分支、评估、回溯", fontsize=10.38, fontweight="bold")
    save(fig, "ch03-tot.png")

if __name__ == "__main__":
    for fn in [f03_gsm8k, f03_selfconsistency, f03_tot]:
        fn()
