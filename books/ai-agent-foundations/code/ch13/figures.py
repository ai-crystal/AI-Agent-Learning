# -*- coding: utf-8 -*-
"""第 13 章插图生成器。运行后输出到 book/images/13/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f13_metagpt():
    fig, ax = canvas(3.6)
    stages = [("需求", "一句想法"), ("产品经理", "PRD"), ("架构师", "设计文档"),
              ("工程师", "代码"), ("测试", "用例与报告")]
    w, gap = 17.0, 3.2
    for i, (role, art) in enumerate(stages):
        x = 2 + i * (w + gap)
        box(ax, x, 54, w, 30, "", fc="white", ec="#b9b5ac")
        ax.text(x + w / 2, 78, role, fontsize=8.97, fontweight="bold", ha="center")
        ax.text(x + w / 2, 66, art, fontsize=8.02, color="#444", ha="center")
        if i < 4:
            arrow(ax, (x + w, 69), (x + w + gap, 69), color=GRAY, lw=0.9)
    arrow(ax, (88, 54), (88, 44), color=ACCENT3, lw=0.9)
    box(ax, 40, 30, 48, 12, "可执行反馈：代码跑不通 → 打回重写", fc="#f1f5f0", ec=ACCENT3, fs=7.2)
    arrow(ax, (40, 36), (30, 54), color=ACCENT, lw=0.9, rad=0.2)
    ax.text(2, 92, "MetaGPT 用 SOP 把“聊天”换成“有格式的产物”", fontsize=10.15, fontweight="bold")
    ax.text(2, 20, "产物越结构化，下游越好用，也越容易自动检查。", fontsize=8.50, color=GRAY)
    save(fig, "ch13-metagpt.png")

def f13_patterns():
    fig, ax = canvas(3.9)
    def node(x, y, r, label, fc="white", ec=INK, fs=6.2):
        ax.add_patch(Circle((x, y), r, fc=fc, ec=ec, lw=0.9))
        ax.text(x, y, label, fontsize=fs, ha="center", va="center")
    # 1 主管
    ax.text(13, 95, "主管", fontsize=9.68, fontweight="bold", ha="center")
    node(13, 76, 4.2, "主", fc="#f7f3ec", ec=ACCENT)
    for dx in (-9, 0, 9):
        node(13 + dx, 60, 3.4, "工")
        arrow(ax, (13, 72), (13 + dx, 64), color="#b9b5ac", lw=0.8, style="<|-|>")
    ax.text(13, 48, "一个大脑分派", fontsize=7.55, ha="center", color=GRAY)
    # 2 交接
    ax.text(37, 95, "交接", fontsize=9.68, fontweight="bold", ha="center")
    node(29, 72, 3.4, "A"); node(37, 72, 3.4, "B"); node(45, 72, 3.4, "C")
    arrow(ax, (32.4, 72), (33.6, 72), color="#b9b5ac", lw=0.8)
    arrow(ax, (40.4, 72), (41.6, 72), color="#b9b5ac", lw=0.8)
    ax.text(37, 62, "上游交给下游", fontsize=7.55, ha="center", color=GRAY)
    node(37, 50, 3.4, "用", fc="#f1f4f7", ec=ACCENT2)
    # 3 辩论
    ax.text(61, 95, "辩论", fontsize=9.68, fontweight="bold", ha="center")
    node(54, 72, 3.4, "A"); node(68, 72, 3.4, "B")
    arrow(ax, (57.4, 73.4), (64.6, 73.4), color="#b9b5ac", lw=0.8, style="<|-|>")
    arrow(ax, (64.6, 70.6), (57.4, 70.6), color="#b9b5ac", lw=0.8)
    ax.text(61, 62, "互评后收敛", fontsize=7.55, ha="center", color=GRAY)
    node(61, 50, 3.4, "答", fc="#f1f5f0", ec=ACCENT3)
    arrow(ax, (57.6, 68.2), (59.6, 53), color="#b9b5ac", lw=0.8)
    # 4 群聊
    ax.text(85, 95, "群聊", fontsize=9.68, fontweight="bold", ha="center")
    for (dx, dy) in [(-6, 68), (0, 72), (6, 68), (0, 62)]:
        node(85 + dx, dy, 3.0, "·")
    ax.text(85, 52, "共享一个对话", fontsize=7.55, ha="center", color=GRAY)
    # 5 层级
    ax.text(13, 40, "层级", fontsize=9.68, fontweight="bold", ha="center")
    node(13, 26, 3.6, "总", fc="#f7f3ec", ec=ACCENT)
    node(6, 12, 3.0, "组"); node(20, 12, 3.0, "组")
    arrow(ax, (11, 23), (7, 15), color="#b9b5ac", lw=0.8)
    arrow(ax, (15, 23), (19, 15), color="#b9b5ac", lw=0.8)
    ax.text(37, 30, "层数增加后，协调与失败归因更复杂；\n需要谨慎控制层数。",
            fontsize=8.26, color="#444", linespacing=1.7)
    save(fig, "ch13-patterns.png")

def f13_cost():
    fig, ax = plt.subplots(figsize=(W * 0.8, 3.0))
    n = np.array([1, 2, 3, 4, 5, 6])
    cost = 1.0 * n ** 2.1
    benefit = 1 - np.exp(-1.1 * (n - 1)) * 0.9
    benefit = np.array([0.28, 0.62, 0.72, 0.73, 0.70, 0.66])
    ax.plot(n, cost / cost.max(), "o-", color=ACCENT, lw=1.6, ms=4, label="成本")
    ax.plot(n, benefit, "s-", color=ACCENT2, lw=1.6, ms=4, label="收益")
    ax.axvspan(1.6, 3.4, color="#f2ece2", alpha=0.6, zorder=0)
    ax.text(2.5, 0.86, "需实测的区间", fontsize=8.8, ha="center", color="#7a6a55")
    ax.set_xlabel("agent 数量", fontsize=10.15)
    ax.set_ylabel("归一化相对值（示意）", fontsize=9.6)
    ax.set_xticks(n); ax.set_ylim(0, 1.05)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=9.20, loc="center right")
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    ax.text(0.0, -0.24, "概念示意，非实测；独立并行任务的成本可接近线性",
            transform=ax.transAxes, fontsize=8.0, color=GRAY)
    fig.tight_layout()
    save(fig, "ch13-cost.png")

if __name__ == "__main__":
    for fn in [f13_metagpt, f13_patterns, f13_cost]:
        fn()
