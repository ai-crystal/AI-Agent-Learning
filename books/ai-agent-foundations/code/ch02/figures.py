# -*- coding: utf-8 -*-
"""第 2 章插图生成器。运行后输出到 book/images/02/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f02_loop():
    fig, ax = canvas(3.7)
    box(ax, 2, 68, 20, 16, "任务 / 用户", fc="white", ec="#b9b5ac", fs=8.4)
    box(ax, 30, 38, 30, 24, "上下文\n\n对话历史\n工具结果 · 当前任务", fc="#f4efe6", fs=8.2)
    box(ax, 72, 68, 26, 16, "模型", fc="#e7e9ec", fs=10.5, bold=True)
    box(ax, 72, 16, 26, 16, "工具 / 环境", fc="#e8ece6", fs=9.5, bold=True)

    # 箭头全部落在盒子边上；文字放在箭头旁，不压线、不压框。
    arrow(ax, (22, 76), (30, 58), color=GRAY)
    ax.text(21, 61, "新任务", fontsize=7.2, color=GRAY, ha="center")
    arrow(ax, (60, 56), (72, 72), color=ACCENT2)
    ax.text(66, 51, "完整历史", fontsize=7.2, color=ACCENT2, ha="center")
    arrow(ax, (85, 68), (85, 32), color=ACCENT2)
    ax.text(89, 50, "动作", fontsize=7.2, color=ACCENT2, ha="center")
    arrow(ax, (72, 24), (60, 44), color=ACCENT3)
    ax.text(65, 29, "工具结果", fontsize=7.2, color=ACCENT3, ha="center")
    arrow(ax, (72, 80), (22, 80), color=GRAY)
    ax.text(47, 85, "最终回答", fontsize=7.2, color=GRAY, ha="center")

    ax.text(50, 6, "每一轮：上下文 → 模型 → 工具 → 上下文；直到回答或触发停止条件",
            fontsize=8.2, color=GRAY, ha="center")
    save(fig, "ch02-loop.png")

def f02_trace():
    fig, ax = canvas(3.5)
    fig.subplots_adjust(top=0.90, bottom=0.16)
    rows = [
        (1, [("系统提示", 9), ("任务", 5)]),
        (2, [("系统提示", 9), ("任务", 5), ("思考", 6), ("动作", 3), ("观察", 4)]),
        (3, [("系统提示", 9), ("任务", 5), ("思考", 6), ("动作", 3), ("观察", 4),
             ("思考", 6), ("动作", 3), ("观察", 5)]),
        (4, [("系统提示", 9), ("任务", 5), ("思考", 6), ("动作", 3), ("观察", 4),
             ("思考", 6), ("动作", 3), ("观察", 5), ("回答", 4)]),
    ]
    cmap = {"系统提示": "#8f8f8f", "任务": "#c9c4b8", "思考": "#c98b8b",
            "动作": "#8fa8bd", "观察": "#93ab97", "回答": "#4a6f9c"}
    y = 80
    scale = 1.36
    for n, segs in rows:
        x = 16
        ax.text(13, y + 6, f"第 {n} 轮", fontsize=9.68, ha="right", va="center")
        for lab, w in segs:
            ax.add_patch(Rectangle((x, y), w * scale, 12, fc=cmap[lab], ec="white", lw=1.0))
            if w >= 6:
                ax.text(x + w * scale / 2, y + 6, lab, fontsize=8.26, color="white",
                        ha="center", va="center")
            x += w * scale
        ax.text(x + 2.0, y + 6, f"合计约 {sum(w for _, w in segs) * 30} token",
                fontsize=7.0, color=GRAY, va="center", ha="left")
        y -= 19
    handles = [Rectangle((0, 0), 1, 1, fc=c, ec="none") for c in
               ["#8f8f8f", "#c9c4b8", "#c98b8b", "#8fa8bd", "#93ab97", "#4a6f9c"]]
    ax.legend(handles, ["系统提示", "任务", "思考", "动作", "观察", "回答"],
              loc="lower left", bbox_to_anchor=(0.02, 0.0), ncol=6, frameon=False,
              fontsize=8.26, handlelength=1.0, columnspacing=1.0, handletextpad=0.4)
    ax.text(2, 96, "每一轮请求时，窗口里装的是什么", fontsize=10.62, fontweight="bold")
    save(fig, "ch02-trace.png")

if __name__ == "__main__":
    for fn in [f02_loop, f02_trace]:
        fn()
