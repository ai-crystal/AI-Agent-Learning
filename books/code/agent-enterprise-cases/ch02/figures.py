# -*- coding: utf-8 -*-
"""第 2 章：客服知识助手链路。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.figstyle import *

set_book("agent-enterprise-cases")


def f02_support():
    fig, ax = canvas(3.2)
    box(ax, 2, 58, 17, 20, "工单 / 用户", fc="white", ec=GRAY, fs=8.0)
    box(ax, 24, 58, 17, 20, "查订单", fc="#e7edf4", ec=ACCENT2, fs=8.0)
    box(ax, 46, 58, 17, 20, "检索政策", fc="#f7f3ec", ec=ACCENT, fs=8.0)
    box(ax, 68, 58, 17, 20, "生成 / 引用", fc="#f1f5f0", ec=ACCENT3, fs=7.4)
    box(ax, 24, 20, 39, 16, "需要审批 / 资料不足 → 转人工", fc="#f7f3ec", ec=ACCENT, fs=8.0)
    for x in (19, 41, 63):
        arrow(ax, (x, 68), (x + 5, 68), color=GRAY)
    arrow(ax, (56, 58), (56, 37), color=ACCENT)
    ax.text(45, 45, "高风险动作", fontsize=7.2, color=ACCENT)
    ax.text(50, 90, "订单事实与政策证据分开记录", fontsize=8.2, color=GRAY, ha="center")
    save(fig, "ch02-support-flow.png")


if __name__ == "__main__":
    f02_support()
