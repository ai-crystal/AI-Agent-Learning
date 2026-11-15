# -*- coding: utf-8 -*-
"""第 14 章插图生成器。运行后输出到 book/images/14/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f14_rl():
    fig, ax = canvas(3.6)
    box(ax, 4, 70, 26, 14, "环境 / 任务", fc="#f1f5f0", ec=ACCENT3, fs=8.2)
    box(ax, 40, 70, 24, 14, "策略模型", fc="#e7e9ec", ec="#8f8f8f", fs=8.4)
    box(ax, 74, 70, 22, 14, "验证器\n（测试 / 答案）", fc="#f1f4f7", ec=ACCENT2, fs=7.6)
    box(ax, 74, 32, 22, 14, "优势估计\n（组内比较）", fc="#f7f3ec", ec=ACCENT, fs=7.6)
    box(ax, 40, 32, 24, 14, "参数更新", fc="#f7f3ec", ec=ACCENT, fs=8.2)
    box(ax, 4, 32, 26, 14, "轨迹与奖励记录", fc="#faf9f6", ec="#cfcbc2", fs=7.4)
    arrow(ax, (30, 77), (40, 77), color=GRAY, label="观察", fs=6.6, lpos=0.5)
    arrow(ax, (64, 77), (74, 77), color=ACCENT2, label="动作序列", fs=6.6, lpos=0.5)
    arrow(ax, (85, 70), (85, 46), color=ACCENT2)
    arrow(ax, (74, 39), (64, 39), color=ACCENT)
    arrow(ax, (40, 39), (30, 39), color="#b9b5ac")
    arrow(ax, (52, 46), (52, 70), color=ACCENT, label="新策略再采样", fs=6.6, lpos=0.5)
    ax.text(50, 16, "训练的好坏，取决于奖励信号能不能真的分辨对错", fontsize=8.73,
            color=GRAY, ha="center")
    ax.text(2, 94, "Agentic RL 的循环：采样 → 判定 → 更新", fontsize=10.15, fontweight="bold")
    save(fig, "ch14-rl-loop.png")

def f14_grpo():
    fig, ax = canvas(3.2)
    box(ax, 2, 44, 16, 14, "同一道题", fc="#e7e9ec", fs=8.2)
    scores = [1, 0, 0, 1, 0, 1, 0, 1]
    ys = [88, 78, 68, 58, 48, 38, 28, 18]
    for i, (s, y) in enumerate(zip(scores, ys)):
        c = ACCENT3 if s else "#b9b5ac"
        box(ax, 26, y, 12, 7, f"样本 {i + 1}", fc="white", ec=c, fs=6.2, round=0.3)
        arrow(ax, (18, 51), (26, y + 3.5), color="#dcd9d1", lw=0.7)
        ax.text(41, y + 3.5, "成功  1" if s else "失败  0", fontsize=7.6, color=c, va="center")
    ax.plot([46, 46], [14, 98], color="#e0ddd6", lw=0.8)
    ax.text(49, 92, "组内均值 0.5", fontsize=8.97, va="center")
    ax.text(49, 82, "高于均值 → 优势为正\n低于均值 → 优势为负", fontsize=8.26, color="#444",
            va="top", linespacing=1.7)
    ax.text(49, 56, "不需要额外的价值网络\n（省掉 critic）", fontsize=8.26, color=ACCENT,
            va="top", linespacing=1.7)
    save(fig, "ch14-grpo.png")

def f14_retool():
    fig, ax1 = plt.subplots(figsize=(W * 0.82, 3.0))
    steps = np.arange(0, 420, 20)
    call = 0.08 + 0.65 / (1 + np.exp(-(steps - 160) / 55))
    acc = 0.27 + 0.40 / (1 + np.exp(-(steps - 170) / 70))
    ax1.plot(steps, call * 100, color=ACCENT, lw=1.6, label="代码调用率")
    ax1.plot(steps, acc * 100, color=ACCENT2, lw=1.6, label="解题准确率")
    ax1.set_xlabel("训练步数", fontsize=10.15)
    ax1.set_ylabel("百分比", fontsize=10.15)
    ax1.set_ylim(0, 100)
    ax1.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax1.spines[s].set_visible(False)
    ax1.legend(frameon=False, fontsize=9.20, loc="lower right")
    ax1.grid(axis="y", color="#eeece7", lw=0.6); ax1.set_axisbelow(True)
    ax1.annotate("学会在需要精确计算时\n才调用解释器", xy=(230, 55), xytext=(60, 78),
                 fontsize=8.50, color=GRAY,
                 arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.7))
    fig.tight_layout()
    save(fig, "ch14-retool.png")

if __name__ == "__main__":
    for fn in [f14_rl, f14_grpo, f14_retool]:
        fn()
