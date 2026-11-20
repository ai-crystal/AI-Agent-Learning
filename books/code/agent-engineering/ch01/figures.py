# -*- coding: utf-8 -*-
"""第 1 章：Agent 工程化的五层。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.figstyle import *

set_book("agent-engineering")


def f01_layers():
    fig, ax = canvas(3.4)
    layers = [
        (76, "交互层", "用户 · 渠道 · 输入输出"),
        (59, "决策层", "模型 · 提示 · 上下文"),
        (42, "工具层", "API · 代码 · 浏览器"),
        (25, "状态层", "会话 · 计划 · 检查点"),
        (8, "运行层", "权限 · 预算 · 观测 · 发布"),
    ]
    for y, name, desc in layers:
        box(ax, 16, y, 68, 13, "", fc="#f8f7f3", ec="#b9b5ac")
        ax.text(19, y + 8, name, fontsize=10.0, fontweight="bold", va="center")
        ax.text(46, y + 8, desc, fontsize=8.0, color="#444", va="center")
    for y in (67, 50, 33, 16):
        arrow(ax, (50, y + 9), (50, y - 1), color=GRAY, lw=0.8)
    save(fig, "ch01-engineering-layers.png")


if __name__ == "__main__":
    f01_layers()
