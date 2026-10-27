# -*- coding: utf-8 -*-
"""第 12 章插图生成器。运行后输出到 book/images/12/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f12_protocols():
    fig, ax = canvas(3.3)
    rows = [
        ("agent 与项目", "AGENTS.md：仓库的规矩、常用命令与禁区", 72, "#f5efe3"),
        ("agent 与 agent", "A2A：能力卡片、任务状态与协作消息", 44, "#f2ece2"),
        ("agent 与工具", "MCP：工具、资源、提示模板与 JSON-RPC 传输", 16, "#eef1ee"),
    ]
    for name, desc, y, fc in rows:
        box(ax, 8, y, 88, 18, "", fc=fc, ec="#c9c5bc")
        ax.text(11, y + 12, name, fontsize=10.0, fontweight="bold")
        ax.text(11, y + 5.2, desc, fontsize=8.2, color="#444")
    ax.text(4, 96, "三层约定：分别规定项目、协作和工具之间怎样交流", fontsize=10.0,
            fontweight="bold")
    ax.text(50, 5, "三者可以独立使用，不是从上到下依次调用的关系。",
            fontsize=8.4, color=GRAY, ha="center")
    save(fig, "ch12-protocols.png")

def f12_gateway():
    fig, ax = canvas(4.2)
    chans = [("聊天软件 A", 82), ("聊天软件 B", 66), ("命令行", 50)]
    for name, y in chans:
        box(ax, 2, y - 5.5, 17, 11, name, fc="white", ec="#b9b5ac", fs=7.2)
        arrow(ax, (19, y), (24, y), color=GRAY, lw=0.8, style="<|-|>",
              zorder=3, shrink=4)

    box(ax, 24, 40, 16, 50, "", fc="#f1f4f7", ec=ACCENT2)
    ax.text(32, 84, "网关", fontsize=9.6, fontweight="bold", ha="center")
    ax.text(32, 75, "去重\n鉴权\n会话路由\n回复原路返回", fontsize=7.3, color="#444",
            ha="center", va="top", linespacing=1.7)

    box(ax, 47, 52, 23, 38, "", fc="#f7f3ec", ec=ACCENT)
    ax.text(58.5, 83, "Agent 核心", fontsize=9.4, fontweight="bold", ha="center")
    ax.text(58.5, 73, "主循环 · 上下文\n模型 · 工具分发", fontsize=7.5, color="#444",
            ha="center", va="top", linespacing=1.7)
    arrow(ax, (40, 70), (47, 70), color=GRAY, style="<|-|>",
          zorder=3, shrink=4)

    box(ax, 76, 60, 22, 30, "", fc="#faf9f6", ec="#cfcbc2")
    ax.text(87, 84, "工作区", fontsize=9.0, fontweight="bold", ha="center")
    ax.text(87, 75, "记忆文件\n技能目录\n临时文件", fontsize=7.3, color="#444",
            ha="center", va="top", linespacing=1.7)
    arrow(ax, (70, 77), (76, 77), color=GRAY, style="<|-|>",
          zorder=3, shrink=4)

    box(ax, 24, 14, 16, 18, "调度 / 心跳\n定时触发任务", fc="#f1f5f0", ec=ACCENT3, fs=7.4)
    arrow(ax, (32, 32), (32, 40), color=ACCENT3)

    box(ax, 47, 14, 23, 22, "", fc="#f7eae4", ec=ACCENT)
    ax.text(58.5, 29, "权限、审批与审计", fontsize=7.8, fontweight="bold", ha="center")
    ax.text(58.5, 20.5, "低风险自动\n高风险先确认", fontsize=7.2, color="#444",
            ha="center", va="center", linespacing=1.6)
    arrow(ax, (58.5, 52), (58.5, 36), color=ACCENT)
    ax.text(63, 44, "动作请求", fontsize=7.2, color=ACCENT, ha="center")

    box(ax, 76, 14, 22, 22, "工具 / 系统\n文件 · 命令 · API", fc="#f1f5f0", ec=ACCENT3, fs=7.5)
    arrow(ax, (70, 25), (76, 25), color=ACCENT3, style="<|-|>",
          zorder=3, shrink=4)

    ax.text(50, 4, "调度器只触发任务；工具调用由 Agent 核心经过权限层发出。",
            fontsize=8.2, color=GRAY, ha="center")
    save(fig, "ch12-gateway.png")

if __name__ == "__main__":
    for fn in [f12_protocols, f12_gateway]:
        fn()
