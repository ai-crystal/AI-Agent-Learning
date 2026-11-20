# -*- coding: utf-8 -*-
"""第 2 章：任务状态与恢复。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.figstyle import *

set_book("agent-engineering")


def f02_state():
    fig, ax = canvas(3.2)
    box(ax, 3, 68, 22, 12, "new", fc="#f8f7f3", ec=GRAY)
    box(ax, 33, 68, 22, 12, "running", fc="#e7edf4", ec=ACCENT2)
    box(ax, 63, 68, 24, 12, "waiting_approval", fc="#f7f3ec", ec=ACCENT, fs=7.0)
    box(ax, 33, 32, 22, 12, "tool_inflight", fc="#f7f3ec", ec=ACCENT2)
    box(ax, 3, 8, 22, 12, "cancelled", fc="#f1f1ef", ec=GRAY)
    box(ax, 63, 8, 24, 12, "done / failed", fc="#f1f5f0", ec=ACCENT3)
    arrow(ax, (25, 74), (33, 74), color=GRAY)
    arrow(ax, (55, 74), (63, 74), color=GRAY)
    arrow(ax, (44, 68), (44, 44), color=ACCENT2)
    arrow(ax, (63, 44), (55, 38), color=GRAY)
    arrow(ax, (44, 32), (14, 20), color=GRAY)
    arrow(ax, (75, 68), (75, 20), color=GRAY)
    ax.text(45, 88, "状态必须可恢复，动作必须先对账", fontsize=8.0, color=GRAY)
    save(fig, "ch02-state-machine.png")


if __name__ == "__main__":
    f02_state()
