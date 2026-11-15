# -*- coding: utf-8 -*-
"""第 9 章插图生成器。运行后输出到 book/images/09/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f09_codeact():
    fig, ax = canvas(3.5)
    ax.text(3, 95, "JSON 动作：一轮一件事", fontsize=10.15, fontweight="bold", color=ACCENT2)
    ax.text(55, 95, "代码动作：一段脚本做完", fontsize=10.15, fontweight="bold", color=ACCENT3)
    rounds = ['{"tool":"read","args":{...}}', '{"tool":"filter","args":{...}}',
              '{"tool":"sort","args":{...}}', '{"tool":"head","args":{...}}']
    y = 84
    for r in rounds:
        box(ax, 3, y, 42, 9, "", fc="white", ec="#b9b5ac")
        ax.text(5, y + 4.5, r, fontsize=6.84, va="center", color="#333")
        arrow(ax, (24, y), (24, y - 3.4), color=GRAY, lw=0.8)
        y -= 12.6
    ax.text(3, 14, "4 次模型调用 · 历史重发 4 次", fontsize=8.73, color=ACCENT2)
    ax.plot([50, 50], [10, 96], color="#e0ddd6", lw=1.0)
    code = ["df = read('a.csv')", "df = df[df.x > 3]", "df = df.sort_values('y')",
            "print(df.head(3))"]
    box(ax, 55, 52, 42, 30, "", fc="#f7f7f5", ec="#b9b5ac")
    for i, line in enumerate(code):
        ax.text(57, 76 - i * 6.0, line, fontsize=7.55, va="center", color="#222")
    arrow(ax, (76, 52), (76, 40), color=ACCENT3)
    box(ax, 55, 26, 42, 12, "执行一次，返回 3 行结果", fc="#f1f5f0", ec=ACCENT3, fs=7.2)
    ax.text(55, 14, "1 次模型调用 · 中间数据留在解释器里", fontsize=8.73, color=ACCENT3)
    save(fig, "ch09-codeact.png")

def f09_aci():
    fig, ax = canvas(3.8)
    box(ax, 2, 18, 26, 68, "", fc="#faf9f6", ec="#cfcbc2")
    ax.text(4, 81, "命令集", fontsize=9.44, fontweight="bold")
    cmds = ["open <file>", "search_file <kw>", "search_dir <kw>", "edit <a> <b>",
            "scroll_up / down"]
    for i, c in enumerate(cmds):
        ax.text(4, 73 - i * 7.6, c, fontsize=8.02, color="#333")
    ax.text(4, 28, "只暴露必要动作\n输出格式对模型友好", fontsize=8.02, color=GRAY,
            linespacing=1.6)
    ax.add_patch(Rectangle((36, 32), 56, 44, fc="white", ec="#b9b5ac", lw=0.9))
    ax.add_patch(Rectangle((36, 68), 56, 8, fc="#efece6", ec="#b9b5ac", lw=0.8))
    ax.text(38, 72, "src/cache.py　第 41–46 行", fontsize=8.02, color="#333", va="center")
    code = ["def get(k):", "    v = cache[k]", "    if v is None:",
            "        v = load(k)", "        cache[k] = v", "    return v"]
    for i, line in enumerate(code):
        yy = 63 - i * 5.0
        ax.text(37.4, yy, str(41 + i), fontsize=6.14, color="#aaa", va="center", ha="left")
        ax.text(40.5, yy, line, fontsize=6.84, color="#333", va="center")
    ax.add_patch(Rectangle((36.4, 63 - 4 * 5.0 - 2.2), 54, 4.4, fc="#f5e6e4", ec="none"))
    ax.text(40.5, 63 - 4 * 5.0, "        cache[k] = v", fontsize=6.84, color=ACCENT, va="center")
    box(ax, 36, 12, 56, 12, "反馈：第 45 行 KeyError，k 可能不存在", fc="#f1f5f0",
        ec=ACCENT3, fs=6.8)
    arrow(ax, (64, 32), (64, 25), color=ACCENT3)
    arrow(ax, (28, 60), (36, 60), color=ACCENT2)
    ax.text(32, 62.6, "执行", fontsize=7.79, color=ACCENT2, ha="center")
    arrow(ax, (30, 18), (30, 80), color=ACCENT2, ls="--")
    ax.text(31.4, 46, "改完再读", fontsize=7.55, color=ACCENT2, rotation=90, va="center")
    ax.text(2, 92, "SWE-agent 的循环：命令 → 观察 → 修改", fontsize=10.15, fontweight="bold")
    save(fig, "ch09-aci.png")

if __name__ == "__main__":
    for fn in [f09_codeact, f09_aci]:
        fn()
