# -*- coding: utf-8 -*-
"""第 6 章插图生成器。运行后输出到 book/images/06/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f06_plan_execute():
    fig, ax = canvas(4.0)
    ax.text(2, 95, "ReAct：边走边看", fontsize=10.62, fontweight="bold")
    xs = [4, 17, 30]
    y = 78
    for i, x in enumerate(xs):
        box(ax, x, y, 11, 9, "想", fc="#f5e6e4", ec=ACCENT, fs=7.4, round=0.4)
        box(ax, x, y - 14, 11, 9, "动", fc="#e4eaf0", ec=ACCENT2, fs=7.4, round=0.4)
        box(ax, x, y - 28, 11, 9, "看", fc="#e6ede4", ec=ACCENT3, fs=7.4, round=0.4)
        if i < 2:
            arrow(ax, (x + 11, y - 24), (xs[i + 1], y - 2), color="#b9b5ac", lw=0.8, rad=-0.15)
        else:
            arrow(ax, (x + 11, y - 24), (x + 11, 36), color="#b9b5ac", lw=0.8)
    ax.text(2, 44, "每一步都要判断下一步做什么", fontsize=8.50, color="#444")
    ax.text(2, 28, "上下文随步数线性增长", fontsize=8.50, color=ACCENT)
    ax.plot([46, 46], [8, 96], color="#e0ddd6", lw=1.0)
    ax.text(51, 95, "Plan-and-Execute：先看全局", fontsize=10.62, fontweight="bold")
    box(ax, 51, 72, 45, 17, "", fc="#f7f3ec", ec="#b9b5ac")
    ax.text(53, 85.4, "计划", fontsize=8.50, fontweight="bold")
    ax.text(53, 78.6, "1 查资料　2 算指标　3 写结论", fontsize=8.14, color="#333")
    for i in range(3):
        yy = 52 - i * 15
        box(ax, 51, yy, 45, 10, f"执行第 {i + 1} 步", fc="white", ec=ACCENT2, fs=7.4, round=0.4)
        ax.text(94.5, yy + 5, "√" if i < 2 else "…", fontsize=9.44, color=ACCENT3,
                ha="right", va="center")
    arrow(ax, (73, 72), (73, 62), color=GRAY)
    arrow(ax, (73, 52), (73, 37), color=GRAY)
    arrow(ax, (73, 37), (73, 22), color=GRAY)
    ax.text(51, 14, "计划只生成一次，每步只看当前步骤", fontsize=8.50, color="#444")
    ax.text(51, 6, "出问题时要能重规划", fontsize=8.50, color=ACCENT)
    save(fig, "ch06-plan-execute.png")

def f06_reflexion():
    fig, ax = canvas(3.6)
    box(ax, 4, 72, 36, 13, "执行任务（ReAct 循环）", fc="#f1f4f7", ec=ACCENT2, fs=8.0)
    box(ax, 58, 72, 34, 13, "评估结果（测试 / 答案核对）", fc="#f1f5f0", ec=ACCENT3, fs=7.4)
    box(ax, 58, 38, 34, 13, "写出反思：“第 3 步漏了边界”", fc="#f7f3ec", ec=ACCENT, fs=7.0)
    box(ax, 4, 38, 36, 13, "反思记忆（跨回合保留）", fc="#f7f3ec", ec=ACCENT, fs=8.0)
    arrow(ax, (40, 78.5), (58, 78.5), color=ACCENT3)
    ax.text(49, 81.6, "成功 / 失败", fontsize=8.02, ha="center", color=ACCENT3)
    arrow(ax, (75, 72), (75, 51), color=ACCENT)
    ax.text(76.6, 61.5, "失败才写", fontsize=8.02, color=ACCENT, rotation=90, va="center")
    arrow(ax, (58, 44.5), (40, 44.5), color=ACCENT)
    arrow(ax, (22, 51), (22, 72), color=ACCENT2)
    ax.text(23.6, 61.5, "下一回合带上", fontsize=8.02, color=ACCENT2, rotation=90, va="center")
    ax.text(50, 24, "没有参数更新，只有一段文字在起作用", fontsize=8.73, color=GRAY,
            ha="center")
    ax.text(4, 94, "Reflexion：把失败经验写成话，带到下一次尝试", fontsize=10.15, fontweight="bold")
    save(fig, "ch06-reflexion.png")

def f06_rewwo():
    fig, ax = canvas(3.4)
    box(ax, 2, 58, 28, 30, "", fc="#f7f3ec", ec="#b9b5ac")
    ax.text(4, 83, "规划器（模型 1 次）", fontsize=8.97, fontweight="bold")
    for i, t in enumerate(["#E1 = search[财报]", "#E2 = calc(#E1 × 0.8)", "#E3 = finish(#E2)"]):
        ax.text(4, 76 - i * 5.2, t, fontsize=7.79, color="#333")
    box(ax, 36, 58, 26, 30, "", fc="#f1f4f7", ec=ACCENT2)
    ax.text(38, 83, "执行器（不调用模型）", fontsize=8.97, fontweight="bold")
    ax.text(38, 74, "按顺序跑工具\n填入变量 → 结果", fontsize=8.02, color="#333", linespacing=1.7)
    box(ax, 68, 58, 28, 30, "", fc="#f1f5f0", ec=ACCENT3)
    ax.text(70, 83, "求解器（模型 1 次）", fontsize=8.97, fontweight="bold")
    ax.text(70, 74, "所有变量齐了\n一次写出答案", fontsize=8.02, color="#333", linespacing=1.7)
    arrow(ax, (30, 73), (36, 73), color=GRAY)
    arrow(ax, (62, 73), (68, 73), color=GRAY)
    ax.plot([2, 94], [48, 48], color="#e0ddd6", lw=0.9)
    ax.text(2, 40, "ReAct：每步一次模型调用，历史全部重发", fontsize=8.50, color=GRAY)
    ax.text(2, 31, "ReWOO：模型只调用两次，动作阶段不占上下文", fontsize=8.50, color=ACCENT)
    save(fig, "ch06-rewwo.png")

if __name__ == "__main__":
    for fn in [f06_plan_execute, f06_reflexion, f06_rewwo]:
        fn()
