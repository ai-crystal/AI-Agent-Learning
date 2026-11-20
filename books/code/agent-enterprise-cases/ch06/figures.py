# -*- coding: utf-8 -*-
"""第 6 章：跨系统流程与幂等。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.figstyle import *

set_book("agent-enterprise-cases")


def f06_workflow():
    fig, ax = canvas(3.2)
    steps = [
        (2, "合同", "CRM"),
        (21, "信用", "风控"),
        (40, "发货", "ERP"),
        (59, "开票", "财务"),
        (78, "通知", "消息"),
    ]
    for x, name, system in steps:
        box(ax, x, 50, 17, 24, "", fc="#f8f7f3", ec="#b9b5ac")
        ax.text(x + 8.5, 66, name, fontsize=9.0, fontweight="bold", ha="center")
        ax.text(x + 8.5, 58, system, fontsize=7.0, color="#444", ha="center")
    for x in (19, 38, 57, 76):
        arrow(ax, (x, 62), (x + 2, 62), color=GRAY)
    box(ax, 10, 16, 78, 14, "幂等键 + 外部 ID + 状态对账：超时先查，不直接重发", fc="#f1f5f0", ec=ACCENT3, fs=7.8)
    arrow(ax, (50, 50), (50, 32), color=ACCENT3)
    save(fig, "ch06-workflow.png")


if __name__ == "__main__":
    f06_workflow()
