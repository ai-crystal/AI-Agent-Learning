# -*- coding: utf-8 -*-
"""第 4 章插图生成器。运行后输出到 book/images/04/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f04_loop():
    fig, ax = canvas(3.5)
    w, h = 26, 18

    def step(x, y, kind, text, fc, ec):
        box(ax, x, y, w, h, "", fc=fc, ec=ec, lw=0.9)
        ax.text(x + w / 2, y + 12.2, kind, fontsize=7.4, color=ec,
                ha="center", va="center", fontweight="bold")
        ax.text(x + w / 2, y + 5.7, text, fontsize=7.6, color=INK,
                ha="center", va="center")

    # 第一行从左向右，第二行从右向左，组成一条连续的蛇形轨迹。
    step(4, 66, "Thought 1", "先查这本书的作者", "#f7f3ec", ACCENT)
    step(37, 66, "Action 1", 'search["书名"]', "#f1f4f7", ACCENT2)
    step(70, 66, "Observation 1", "作者 = A（百科）", "#f1f5f0", ACCENT3)
    step(70, 30, "Thought 2", "再查 A 的合作者", "#f7f3ec", ACCENT)
    step(37, 30, "Action 2", 'search["A 的合作者"]', "#f1f4f7", ACCENT2)
    step(4, 30, "Observation 2", "合作者 = B", "#f1f5f0", ACCENT3)

    arrow(ax, (30, 75), (37, 75), color=GRAY)
    arrow(ax, (63, 75), (70, 75), color=GRAY)
    arrow(ax, (83, 66), (83, 48), color=ACCENT3)
    arrow(ax, (70, 39), (63, 39), color=GRAY)
    arrow(ax, (37, 39), (30, 39), color=GRAY)

    ax.text(50, 57, "观察结果写回上下文", fontsize=7.8, color=ACCENT3,
            ha="center", va="center")
    ax.text(50, 14, "Thought 与 Action 由模型生成；Observation 由环境返回。任务未完成就继续下一轮。",
            fontsize=8.0, color=GRAY, ha="center")
    save(fig, "ch04-loop.png")

def f04_compare():
    fig, ax = canvas(3.5)
    cols = [
        ("CoT", [("想", "拆开问题"), ("想", "算第一步"), ("想", "算第二步"), ("答", "42")],
         "推理全在模型内部\n没有外部校验"),
        ("Act", [("动", "search"), ("动", "lookup"), ("动", "finish")],
         "只有动作\n不知道为什么要做"),
        ("ReAct", [("想", "先查作者"), ("动", "search"), ("观", "作者 A"),
                   ("想", "再查合作者"), ("动", "search"), ("答", "B")],
         "推理与观察交替\n错误能被外部否定"),
    ]
    style = {"想": (ACCENT, "#f5e6e4"), "动": (ACCENT2, "#e4eaf0"),
             "观": (ACCENT3, "#e6ede4"), "答": (ACCENT3, "#e6ede4")}
    for name, seq, note in cols:
        x = {"CoT": 3, "Act": 36, "ReAct": 69}[name]
        ax.text(x + 14, 94, name, fontsize=11.80, fontweight="bold", ha="center")
        y = 82
        for kind, text in seq:
            c, fc = style[kind]
            box(ax, x, y, 28, 8, f"{kind}　{text}", fc=fc, ec=c, fs=7.2, round=0.4)
            y -= 10.2
        ax.text(x + 14, y - 2, note, fontsize=8.26, ha="center", color="#444",
                va="top", linespacing=1.6)
    save(fig, "ch04-compare.png")

if __name__ == "__main__":
    for fn in [f04_loop, f04_compare]:
        fn()
