# -*- coding: utf-8 -*-
"""第 16 章插图生成器。运行后输出到 book/images/16/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f16_attack():
    fig, ax = canvas(4.0)
    box(ax, 40, 38, 22, 28, "Agent\n模型 + 主循环\n有真实工具权限", fc="#f7f3ec", ec=ACCENT, fs=8.0)

    inputs = [("用户输入", 84, 62), ("网页 / 邮件 / 文档", 66, 58),
              ("工具返回", 48, 50), ("第三方 MCP", 30, 42)]
    for name, y, target_y in inputs:
        box(ax, 2, y - 5, 26, 10, name, fc="white", ec="#b9b5ac", fs=7.0)
        arrow(ax, (28, y), (40, target_y), color=ACCENT, lw=0.9)
    box(ax, 2, 7, 26, 10, "长期记忆", fc="#f1f4f7", ec=ACCENT2, fs=7.0)
    arrow(ax, (28, 12), (40, 38), color=ACCENT2, lw=0.9)

    outs = [("文件 / 命令", 66, 58), ("消息 / 邮件", 48, 52), ("页面渲染", 30, 46)]
    for name, y, source_y in outs:
        box(ax, 74, y - 5, 24, 10, name, fc="#f1f5f0", ec=ACCENT3, fs=7.0)
        arrow(ax, (62, source_y), (74, y), color=ACCENT3, lw=0.9)

    ax.text(2, 96, "入口：外部内容可能带来恶意指令", fontsize=9.4, fontweight="bold")
    ax.text(74, 96, "出口：副作用与数据外泄", fontsize=9.4, fontweight="bold")
    ax.text(50, 2, "关键防御：限制可读文件、可执行命令和可访问网络，而不是只靠提示词。",
            fontsize=8.1, color=GRAY, ha="center")
    save(fig, "ch16-attack.png")

if __name__ == "__main__":
    for fn in [f16_attack]:
        fn()
