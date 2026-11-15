# -*- coding: utf-8 -*-
"""第 10 章插图生成器。运行后输出到 book/images/10/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def _mock_page(ax, x, y, w, h, marks=False):
    ax.add_patch(Rectangle((x, y), w, h, fc="white", ec="#b9b5ac", lw=0.9))
    ax.add_patch(Rectangle((x, y + h - 4.5), w, 4.5, fc="#e8e5de", ec="none"))
    ax.text(x + 1.6, y + h - 2.2, "● ● ●", fontsize=4.96, color="#a8a49b", va="center")
    ax.add_patch(Rectangle((x + 1.6, y + h - 12), w * 0.55, 4.2, fc="#f7f6f2",
                           ec="#c9c5bc", lw=0.7))
    ax.add_patch(Rectangle((x + 1.6 + w * 0.58, y + h - 12), w * 0.22, 4.2, fc="#dfe6ee",
                           ec="#b9c6d4", lw=0.7))
    ax.text(x + 1.6 + w * 0.69, y + h - 9.9, "搜索", fontsize=4.96, color="#4a5a6a",
            va="center", ha="center")
    ax.add_patch(Rectangle((x + 1.6, y + h - 18), w * 0.5, 2.6, fc="#ddd9d0", ec="none"))
    for i in range(3):
        ax.add_patch(Rectangle((x + 1.6, y + h - 23 - i * 3.2), w * (0.8 - i * 0.12), 1.4,
                               fc="#eeebe5", ec="none"))
    ax.add_patch(Rectangle((x + 1.6, y + 3), w * 0.3, 4.4, fc="#dfe6ee", ec="#b9c6d4", lw=0.7))
    ax.text(x + 1.6 + w * 0.15, y + 5.2, "提交", fontsize=4.96, color="#4a5a6a",
            ha="center", va="center")
    if marks:
        boxes = [(x + 1.2, y + h - 12.6, w * 0.59, 5.4),
                 (x + 1.2 + w * 0.55, y + h - 12.6, w * 0.27, 5.4),
                 (x + 1.2, y + 2.4, w * 0.33, 5.4)]
        for i, (mx, my, mw, mh) in enumerate(boxes):
            ax.add_patch(Rectangle((mx, my), mw, mh, fc="none", ec=ACCENT, lw=1.0))
            ax.add_patch(Circle((mx + 1.4, my + mh + 1.4), 1.6, fc=ACCENT, ec="none", zorder=5))
            ax.text(mx + 1.4, my + mh + 1.4, str(i + 1), color="white", fontsize=5.90,
                    ha="center", va="center", zorder=6)

def f10_observation():
    fig, ax = canvas(3.4)
    ax.text(2, 96, "① 像素", fontsize=10.15, fontweight="bold")
    _mock_page(ax, 2, 56, 26, 34)
    ax.text(2, 49, "看得见布局，看不清小字", fontsize=8.02, color="#444")
    ax.text(36, 96, "② 结构化文本", fontsize=10.15, fontweight="bold")
    box(ax, 36, 52, 26, 38, "", fc="#f7f7f5", ec="#b9b5ac")
    lines = ["[1] input 搜索框", "[2] button 搜索", "[3] h1 标题",
             "[4] a 链接 详情", "[5] button 提交"]
    for i, l in enumerate(lines):
        ax.text(37.4, 84 - i * 6.4, l, fontsize=6.84, color="#333")
    ax.text(36, 45, "信息全，但节点多，需要裁剪", fontsize=8.02, color="#444")
    ax.text(70, 96, "③ 编号 + 截图", fontsize=10.15, fontweight="bold")
    _mock_page(ax, 70, 52, 26, 38, marks=True)
    ax.text(70, 45, "既能看懂，也能点准", fontsize=8.02, color="#444")
    ax.text(2, 22, "同一个页面，三种观察方式给出的信息完全不同。\n混合表示把“理解语义”和“定位像素”拆成两件事。",
            fontsize=8.50, color=GRAY, linespacing=1.7)
    save(fig, "ch10-observation.png")

def f10_bench():
    fig, ax = plt.subplots(figsize=(W * 0.86, 3.0))
    names = ["WebArena", "OSWorld", "GAIA"]
    human = [78.2, 72.4, 92.0]
    agent = [14.4, 12.2, 15.0]
    x = np.arange(len(names))
    w = 0.32
    b1 = ax.bar(x - w / 2, human, w, label="人类", color="#c9c4b8")
    b2 = ax.bar(x + w / 2, agent, w, label="agent（发布时的最好成绩）", color=ACCENT)
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.8, f"{b.get_height():.0f}%",
                    ha="center", fontsize=9.20)
    ax.set_xticks(x); ax.set_xticklabels(names, fontsize=9.91)
    ax.set_ylim(0, 105); ax.set_ylabel("任务成功率", fontsize=10.15)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=8.97, loc="upper left", ncol=2)
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "ch10-bench.png")

if __name__ == "__main__":
    for fn in [f10_observation, f10_bench]:
        fn()
