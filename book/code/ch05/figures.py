# -*- coding: utf-8 -*-
"""第 5 章插图生成器。运行后输出到 book/images/05/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f05_toolformer():
    fig, ax = canvas(3.2)
    steps = [
        ("插入候选调用", "印度的首都是\n[QA(印度的首都?)]"),
        ("执行并写入结果", "印度的首都是\n[QA] → 新德里"),
        ("比较后续文本的\n预测概率", "有结果时 loss 更低\n→ 保留这次调用"),
        ("微调模型", "学会在何时\n调用哪个工具"),
    ]
    w, gap = 21.0, 4.0
    for i, (t, ex) in enumerate(steps):
        x = 2 + i * (w + gap)
        box(ax, x, 38, w, 36, "", fc="white", ec="#b9b5ac")
        ax.add_patch(Circle((x + 4.2, 69), 2.8, fc=ACCENT, ec="none", zorder=4))
        ax.text(x + 4.2, 69, str(i + 1), color="white", fontsize=8.97, ha="center",
                va="center", fontweight="bold", zorder=5)
        ax.text(x + 8.4, 69, t, fontsize=8.61, va="center", linespacing=1.4)
        ax.text(x + 2.8, 51, ex, fontsize=8.26, color="#333", va="center", linespacing=1.6)
        if i < 3:
            arrow(ax, (x + w, 56), (x + w + gap, 56), lw=1.0)
    ax.text(2, 84, "自监督地构造带工具调用的训练数据", fontsize=10.62, fontweight="bold")
    ax.text(2, 20, "判据是“这次调用有没有让后续文本更容易预测”，不需要人工标注对错",
            fontsize=8.73, color=ACCENT)
    save(fig, "ch05-toolformer.png")

def f05_function_call():
    fig, ax = canvas(3.9)
    xs = {"程序": 14, "模型": 50, "工具": 86}
    for k, x in xs.items():
        box(ax, x - 9, 88, 18, 8, k, fc="#e7e9ec", fs=8.8, bold=True)
        ax.plot([x, x], [4, 88], color="#ccc", lw=0.8, ls=(0, (4, 3)))
    msgs = [
        (14, 50, 80, "① 工具清单 + 对话", ACCENT2, "above"),
        (50, 14, 70, "② tool_calls", ACCENT, "above"),
        (14, 86, 60, "③ 执行", ACCENT3, "above"),
        (86, 14, 50, "④ 结果", ACCENT3, "above"),
        (14, 50, 40, "⑤ role=tool 消息", ACCENT2, "above"),
        (50, 14, 30, "⑥ 回答或继续调用", ACCENT, "above"),
    ]
    for x1, x2, y, lab, c, _ in msgs:
        arrow(ax, (x1, y), (x2, y), color=c, lw=1.0)
        ax.text((x1 + x2) / 2, y + 2.8, lab, fontsize=8.26, ha="center", color=c)
    ax.text(50, 12, "每一轮往返 = 两次模型调用", fontsize=8.73, ha="center", color=GRAY)
    save(fig, "ch05-function-call.png")

def f05_mcp():
    fig, ax = canvas(3.5)
    box(ax, 3, 10, 44, 78, "", fc="#f8f7f3", ec="#b9b5ac")
    ax.text(5, 83, "宿主（agent 应用）", fontsize=10.15, fontweight="bold")
    box(ax, 7, 56, 36, 18, "客户端 A", fc="white", ec=ACCENT2, fs=8.2)
    box(ax, 7, 32, 36, 18, "客户端 B", fc="white", ec=ACCENT2, fs=8.2)
    box(ax, 7, 15, 36, 10, "模型 + 主循环", fc="#e7e9ec", ec="#8f8f8f", fs=7.8)
    arrow(ax, (25, 50), (25, 56), color=GRAY)
    arrow(ax, (25, 26), (25, 32), color=GRAY)
    for y, name, items in [(64, "文件系统服务端", "tools: read / write / list\nresources: file://…"),
                           (36, "数据库服务端", "tools: query\nresources: schema")]:
        box(ax, 62, y, 35, 22, "", fc="white", ec=ACCENT3)
        ax.text(64, y + 16, name, fontsize=9.20, fontweight="bold")
        ax.text(64, y + 5, items, fontsize=7.79, color="#444", va="center", linespacing=1.6)
    arrow(ax, (43, 66), (62, 72), color=ACCENT2, label="JSON-RPC", fs=6.8, lpos=0.5)
    arrow(ax, (43, 42), (62, 46), color=ACCENT2)
    ax.text(50, 96, "传输层：标准输入输出 或 HTTP", fontsize=8.50, color=GRAY, ha="center")
    save(fig, "ch05-mcp.png")

if __name__ == "__main__":
    for fn in [f05_toolformer, f05_function_call, f05_mcp]:
        fn()
