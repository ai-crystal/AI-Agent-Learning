# -*- coding: utf-8 -*-
"""第 8 章插图生成器。运行后输出到 book/images/08/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f08_lost_middle():
    fig, ax = plt.subplots(figsize=(W * 0.82, 3.1))
    x = np.linspace(0, 100, 200)
    y = 0.62 + 0.33 * ((x - 50) / 50) ** 2 + 0.02 * np.sin(x / 6)
    ax.plot(x, y, color=ACCENT2, lw=1.8)
    ax.axvspan(30, 70, color="#f2ece2", alpha=0.7, zorder=0)
    ax.text(50, 0.665, "中间位置\n信息容易被淹没", fontsize=9.20, ha="center", color="#7a6a55",
            linespacing=1.6)
    ax.text(6, 0.955, "开头", fontsize=8.97, color=GRAY)
    ax.text(88, 0.955, "结尾", fontsize=8.97, color=GRAY)
    ax.set_xlabel("关键信息在上下文中的位置", fontsize=10.15)
    ax.set_ylabel("模型找到它的概率", fontsize=10.15)
    ax.set_xticks([]); ax.set_ylim(0.55, 1.0)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "ch08-lost-middle.png")

def f08_ops():
    fig, ax = canvas(3.4)
    panels = [
        ("写入", "把状态写到上下文之外", "例：把“已确认”“待解决”写成 note.md", 4, 54),
        ("选择", "从大量信息里挑一部分", "例：检索 top-5、只留最近 8 轮、截断输出", 52, 54),
        ("压缩", "把多轮内容压成更短的表示", "例：把前二十轮摘要成两百字", 4, 5),
        ("隔离", "把子任务放到另一个窗口", "例：子 agent 只回传结论", 52, 5),
    ]
    for name, desc, ex, x, y in panels:
        box(ax, x, y, 44, 37, "", fc="#faf9f6", ec="#cfcbc2")
        ax.text(x + 3, y + 29, name, fontsize=10.86, fontweight="bold")
        ax.text(x + 3, y + 21, desc, fontsize=8.50, color="#333")
        ax.text(x + 3, y + 12, ex, fontsize=7.67, color="#777")
    ax.text(4, 96, "上下文工程的四类动作", fontsize=10.62, fontweight="bold")
    save(fig, "ch08-ops.png")

def f08_budget():
    fig, ax = plt.subplots(figsize=(W * 0.9, 2.4))
    segs = [("系统提示与工具定义", 15, "#8f8f8f"),
            ("任务与约束", 5, "#c9c4b8"),
            ("近期历史", 38, ACCENT2),
            ("检索内容", 25, ACCENT3),
            ("余量（留给工具返回）", 17, "#d9c9a8")]
    left = 0
    for name, w, c in segs:
        ax.barh(0, w, left=left, color=c, height=0.42, edgecolor="white", lw=1.2)
        ax.text(left + w / 2, 0, f"{w}%", ha="center", va="center", fontsize=9.68,
                color="white" if c not in ("#c9c4b8", "#d9c9a8") else "#333",
                fontweight="bold")
        left += w
    ax.set_xlim(0, 100); ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([]); ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("一次调用的上下文预算", fontsize=10.15)
    ax.tick_params(labelsize=7.6)
    ax.spines["left"].set_visible(False)
    handles = [Rectangle((0, 0), 1, 1, fc=c, ec="none") for _, _, c in segs]
    ax.legend(handles, [n for n, _, _ in segs], loc="upper center",
              bbox_to_anchor=(0.5, -0.42), ncol=3, frameon=False, fontsize=8.73,
              handlelength=1.0, columnspacing=1.2, handletextpad=0.5)
    fig.tight_layout()
    save(fig, "ch08-budget.png")

if __name__ == "__main__":
    for fn in [f08_lost_middle, f08_ops, f08_budget]:
        fn()
