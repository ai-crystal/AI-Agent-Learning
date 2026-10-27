# -*- coding: utf-8 -*-
"""第 15 章插图生成器。运行后输出到 book/images/15/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f15_pyramid():
    fig, ax = canvas(2.6)
    # 底层测单点能力，越往上越接近真实系统的使用表现。
    tiers = [
        ("模型能力", "单题问答 · 数学 · 代码片段", 6, 18, "#eef1ee"),
        ("任务完成", "完整任务 + 真实环境", 28, 18, "#f4eae4"),
        ("系统工程", "成功率 · 成本 · 延迟 · 介入率", 50, 18, "#f5e0dd"),
    ]
    for name, desc, y, h, fc in tiers:
        shrink = (y - 6) * 0.55
        pts = [[4 + shrink, y], [96 - shrink, y],
               [88 - shrink, y + h], [12 + shrink, y + h]]
        ax.add_patch(Polygon(pts, closed=True, fc=fc, ec="#c9c5bc", lw=0.9))
        ax.text(50, y + h * 0.66, name, fontsize=10.0, fontweight="bold", ha="center")
        ax.text(50, y + h * 0.27, desc, fontsize=7.8, color="#444", ha="center")
    save(fig, "ch15-pyramid.png")

def f15_bench():
    fig, ax = plt.subplots(figsize=(W * 0.84, 3.15))
    labels = ["GAIA", "WebArena", "OSWorld"]
    agents = [15.0, 14.41, 12.24]
    humans = [92.0, 78.24, 72.36]
    x = np.arange(len(labels))
    width = 0.32
    bars1 = ax.bar(x - width / 2, agents, width, color=ACCENT, label="Agent（论文发布时）")
    bars2 = ax.bar(x + width / 2, humans, width, color="#b8b2a8", label="人类（论文设置）")
    for bars in (bars1, bars2):
        for bar in bars:
            value = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, value + 2,
                    f"{value:g}%", ha="center", fontsize=8.7, color=INK)
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9.2)
    ax.set_ylim(0, 108); ax.set_ylabel("成功率 / 得分（%）", fontsize=9.6)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=8.2, loc="upper right", ncol=2)
    ax.text(0.0, -0.24, "各论文发布时的设置；任务与评分不同，不能横向排名",
            transform=ax.transAxes, fontsize=8.1, color=GRAY)
    fig.tight_layout()
    save(fig, "ch15-bench.png")

def f15_passk():
    fig, ax = plt.subplots(figsize=(W * 0.8, 2.9))
    k = np.arange(1, 11)
    p = 0.7
    ax.plot(k, 1 - (1 - p) ** k, "o-", color=ACCENT2, lw=1.6, ms=4, label="pass@k（至少一次成功）")
    ax.plot(k, p ** k, "s-", color=ACCENT, lw=1.6, ms=4, label="pass^k（每次都成功）")
    ax.set_xlabel("重复运行次数 k", fontsize=10.15)
    ax.set_ylabel("概率", fontsize=10.15)
    ax.set_xticks(k); ax.set_ylim(0, 1.05)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=8.97, loc="center right")
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    ax.text(0.03, 0.06, "单次成功率 70% 的同一个 agent", transform=ax.transAxes,
            fontsize=8.50, color=GRAY)
    fig.tight_layout()
    save(fig, "ch15-passk.png")

if __name__ == "__main__":
    for fn in [f15_pyramid, f15_bench, f15_passk]:
        fn()
