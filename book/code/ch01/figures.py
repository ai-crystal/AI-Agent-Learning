# -*- coding: utf-8 -*-
"""第 1 章插图生成器。运行后输出到 book/images/01/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f01_error_decay():
    fig, ax = plt.subplots(figsize=(W, 3.4))
    n = np.arange(1, 51)
    for p, c, lab in [(0.99, ACCENT3, "单步正确率 0.99"),
                      (0.95, ACCENT2, "0.95"),
                      (0.90, ACCENT, "0.90")]:
        ax.plot(n, p ** n, color=c, lw=1.6, label=lab)
    ax.axvline(20, color=GRAY, lw=0.7, ls=":")
    ax.annotate("20 步时约 36%", xy=(20, 0.95 ** 20), xytext=(23.5, 0.62),
                fontsize=9.44, color=ACCENT2,
                arrowprops=dict(arrowstyle="-", color=ACCENT2, lw=0.7))
    ax.set_xlabel("任务需要的步数", fontsize=10.62)
    ax.set_ylabel("全部做对的概率", fontsize=10.62)
    ax.set_xlim(1, 50); ax.set_ylim(0, 1.02)
    ax.legend(frameon=False, fontsize=9.44, loc="upper right")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8)
    ax.grid(axis="y", color="#e8e8e4", lw=0.6)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "ch01-error-decay.png")

def f01_autonomy():
    fig, ax = canvas(4.1)
    levels = [
        ("完全自主", "目标由模型自己提出，人只做事后审计", "#ebdfdd"),
        ("长期自主", "持续运行，只在异常时找人", "#f0e4e0"),
        ("自主规划", "自己拆步骤、调工具，关键节点确认", "#f4eae4"),
        ("有限选择", "在几个预设动作里选一个", "#f7f0ea"),
        ("固定流程", "模型只做分类或抽取，路径由代码写死", "#faf6f0"),
    ]
    h, gap = 14.0, 3.0
    for i, (name, desc, fc) in enumerate(levels):
        y = 5 + i * (h + gap)
        x = 20 + i * 1.2
        w = 52 + i * 3.2
        box(ax, x, y, w, h, "", fc=fc, ec="#bdb9b0", lw=0.9, round=0.5)
        ax.text(x + 2.6, y + h - 4.4, name, fontsize=10.62, fontweight="bold")
        ax.text(x + 2.6, y + 4.6, desc, fontsize=8.73, color="#444")
    ax.annotate("", xy=(16, 93), xytext=(16, 6),
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=1.2))
    ax.text(12, 50, "自主性增强", rotation=90, fontsize=9.44, color=ACCENT,
            ha="center", va="center")
    ax.text(96.5, 50, "人需要介入的频率下降", rotation=90, fontsize=8.50,
            color=GRAY, ha="center", va="center")
    save(fig, "ch01-autonomy.png")

def f01_stack():
    fig, ax = canvas(4.5)
    layers = [
        ("系统形态", "单 agent · 多 agent · 常驻服务 · 嵌入式助手", "#e9e4dc"),
        ("Harness", "主循环 · 权限 · 沙箱 · 状态 · 可观测性", "#eae2df"),
        ("工具与接口", "函数调用 · MCP · 代码执行 · 浏览器 / GUI", "#efe6e0"),
        ("记忆与上下文", "检索 · 压缩 · 分层记忆 · 子 agent 隔离", "#f2ece2"),
        ("推理与行动范式", "CoT · ReAct · 规划 · 反思", "#f5efe3"),
        ("模型能力", "预训练知识 · 指令遵循 · 工具使用 · 长思考", "#f7f2e6"),
    ]
    top, h, gap = 92, 12.6, 1.6
    for i, (name, desc, fc) in enumerate(layers):
        y = top - (i + 1) * h - i * gap
        box(ax, 8, y, 66, h, "", fc=fc, ec="#b9b5ac", lw=0.9, round=0.5)
        ax.text(10.6, y + h * 0.68, name, fontsize=10.62, fontweight="bold", va="center")
        ax.text(10.6, y + h * 0.28, desc, fontsize=8.38, color="#444", va="center")
    total_h = 6 * h + 5 * gap
    y0 = top - total_h
    for x, lab in [(78, "评测"), (89, "安全")]:
        box(ax, x, y0, 9, total_h, "", fc="#f6f2ea", ec="#b9b5ac", lw=0.9)
        ax.text(x + 4.5, y0 + total_h / 2, lab, rotation=90, fontsize=9.68,
                ha="center", va="center", fontweight="bold")
    ax.annotate("", xy=(5.4, 92), xytext=(5.4, y0),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.9))
    ax.text(3.2, (92 + y0) / 2, "能力", rotation=90, fontsize=8.50, color=GRAY,
            ha="center", va="center")
    save(fig, "ch01-stack.png")

if __name__ == "__main__":
    for fn in [f01_error_decay, f01_autonomy, f01_stack]:
        fn()
