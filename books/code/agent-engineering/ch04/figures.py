# -*- coding: utf-8 -*-
"""第 4 章：权限检查链。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.figstyle import *

set_book("agent-engineering")


def f04_permission():
    fig, ax = canvas(3.0)
    steps = [
        (2, "身份", "用户 / 租户 / 角色"),
        (21, "资源", "订单 / 文件 / API"),
        (40, "动作", "读 / 写 / 支付"),
        (59, "审批", "高风险人工"),
    ]
    for x, name, desc in steps:
        box(ax, x, 55, 17, 20, "", fc="#f8f7f3", ec="#b9b5ac")
        ax.text(x + 8.5, 68, name, fontsize=9.2, fontweight="bold", ha="center")
        ax.text(x + 8.5, 61, desc, fontsize=6.8, color="#444", ha="center", va="center")
    for x in (19, 38, 57):
        arrow(ax, (x, 65), (x + 2, 65), color=GRAY)
    box(ax, 2, 20, 74, 14, "审计：谁在何时对什么资源做了什么", fc="#f1f5f0", ec=ACCENT3, fs=8.2)
    arrow(ax, (39, 55), (39, 34), color=ACCENT3)
    save(fig, "ch04-permission-chain.png")


if __name__ == "__main__":
    f04_permission()
