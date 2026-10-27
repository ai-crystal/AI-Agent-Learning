# -*- coding: utf-8 -*-
"""第 11 章插图生成器。运行后输出到 book/images/11/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f11_arch():
    fig, ax = canvas(4.4)
    ax.text(50, 98, "模型之外的那套系统", fontsize=10.62, fontweight="bold", ha="center")
    box(ax, 2, 80, 18, 12, "用户 / 通道\n消息 · 文件 · 审批", fc="white", ec="#b9b5ac", fs=7.0)
    box(ax, 26, 78, 44, 16, "", fc="#f7f3ec", ec=ACCENT2, lw=1.2)
    ax.text(48, 90.5, "主循环", fontsize=10.15, fontweight="bold", ha="center")
    steps = ["组装上下文", "调用模型", "解析动作", "分发执行"]
    for i, s in enumerate(steps):
        x = 27.5 + i * 10.6
        box(ax, x, 80, 9.6, 7, s, fc="white", ec="#b9b5ac", fs=6.4, round=0.3)
        if i < 3:
            arrow(ax, (x + 9.6, 83.5), (x + 10.6, 83.5), color=GRAY, lw=0.7)
    box(ax, 76, 80, 22, 12, "模型", fc="#e7e9ec", ec="#8f8f8f", fs=9.5, bold=True)
    arrow(ax, (20, 86), (26, 86), color=GRAY)
    arrow(ax, (70, 86), (76, 86), color=GRAY, style="<|-|>")

    row2 = [(2, "上下文管理器", "预算 · 压缩 · 检索 · 去重"),
            (28, "工具层", "校验 · 执行 · 截断 · 记录"),
            (54, "权限与沙箱", "分级 · 审批 · 隔离 · 审计"),
            (80, "状态与检查点", "会话 · 计划 · 恢复")]
    for x, name, desc in row2:
        w = 18 if x == 80 else 22
        box(ax, x, 56, w, 14, "", fc="white", ec="#cfcbc2")
        ax.text(x + w / 2, 65.5, name, fontsize=8.5, fontweight="bold", ha="center")
        ax.text(x + w / 2, 60, desc, fontsize=6.9, color="#555", ha="center")

    # 主循环通过一条总线连接四个子系统；箭头严格对准各盒子的中心。
    centers = [13, 39, 65, 89]
    ax.plot([48, 48], [78, 74], color="#b9b5ac", lw=0.8)
    ax.plot([centers[0], centers[-1]], [74, 74], color="#b9b5ac", lw=0.8)
    for x in centers:
        arrow(ax, (x, 74), (x, 70), color="#b9b5ac", lw=0.8)

    box(ax, 2, 32, 44, 14, "", fc="#faf9f6", ec="#cfcbc2")
    ax.text(24, 39, "可观测性\n轨迹 · 指标 · 失败分类 · 成本", fontsize=8.2, ha="center")
    box(ax, 52, 32, 46, 14, "", fc="#faf9f6", ec="#cfcbc2")
    ax.text(75, 39, "评测与回放\n用例集 · 回归 · A/B", fontsize=8.2, ha="center")
    for x in (13, 39, 65, 89):
        arrow(ax, (x, 56), (x, 46), color="#b9b5ac", lw=0.8)
    ax.text(50, 20, "主循环负责决策流程；上下两排提供状态、执行、保护与验证能力。",
            fontsize=8.3, color=GRAY, ha="center")
    save(fig, "ch11-arch.png")

def f11_permission():
    fig, ax = canvas(3.5)
    tiers = [
        ("读取", "读文件、搜索、查询", "自动放行", "#eef1ee"),
        ("写入", "改文件、建分支、写数据库", "沙箱内自动，出沙箱确认", "#f4f0e6"),
        ("对外", "发消息、提交 PR、付费调用", "每次确认", "#f7eae4"),
        ("不可逆", "删除、转账、改权限", "二次确认 + 预演", "#f5e0dd"),
    ]
    for i, (name, ex, how, fc) in enumerate(tiers):
        x = 2 + i * 24.5
        box(ax, x, 40, 22, 42, "", fc=fc, ec="#c9c5bc")
        ax.text(x + 11, 74, name, fontsize=10.86, fontweight="bold", ha="center")
        ax.text(x + 11, 62, ex, fontsize=7.79, color="#444", ha="center", va="center",
                wrap=False)
        ax.text(x + 11, 48, how, fontsize=7.79, color=ACCENT, ha="center", va="center")
    ax.annotate("", xy=(97, 30), xytext=(3, 30),
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=1.0))
    ax.text(50, 24, "确认的强度随影响范围上升", fontsize=8.73, color=ACCENT, ha="center")
    ax.text(2, 92, "动作分级：按影响范围决定要不要人工确认", fontsize=9.91,
            fontweight="bold")
    save(fig, "ch11-permission.png")

if __name__ == "__main__":
    for fn in [f11_arch, f11_permission]:
        fn()
