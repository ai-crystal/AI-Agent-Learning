# -*- coding: utf-8 -*-
"""第 7 章插图生成器。运行后输出到 book/images/07/。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, FancyArrowPatch
from common.figstyle import *
def f07_layers():
    fig, ax = canvas(4.0)
    layers = [
        ("工作记忆", "当前的对话与工具结果，受窗口限制", "秒到分钟", "#e9e4dc", 74),
        ("情景记忆", "发生过的事件，带时间与情境", "天到月", "#efe6e0", 58),
        ("语义记忆", "从事件里提炼出的事实与偏好", "月到年", "#f2ece2", 42),
        ("程序记忆", "怎么做一件事：技能、脚本、流程", "长期", "#f5efe3", 26),
    ]
    for name, desc, life, fc, y in layers:
        box(ax, 10, y, 60, 13, "", fc=fc, ec="#b9b5ac")
        ax.text(12.5, y + 8.4, name, fontsize=10.38, fontweight="bold")
        ax.text(12.5, y + 4.0, desc, fontsize=8.26, color="#444")
        ax.text(74, y + 6.5, life, fontsize=8.02, color=GRAY, va="center")
    for y1, y2 in [(74, 58), (58, 42), (42, 26)]:
        arrow(ax, (88, y1 + 2), (88, y2 + 13), color=ACCENT, lw=0.9)
    ax.text(89.6, 66, "抽象", fontsize=8.26, color=ACCENT, va="center")
    ax.text(89.6, 50, "沉淀", fontsize=8.26, color=ACCENT, va="center")
    arrow(ax, (83, 30), (83, 84), color=ACCENT2, lw=0.9, ls="--")
    ax.text(84.6, 57, "检索 / 写入", fontsize=8.02, color=ACCENT2, rotation=90, va="center")
    ax.text(4, 95, "四种记忆：越往下越持久，越往上越即时", fontsize=10.15, fontweight="bold")
    save(fig, "ch07-layers.png")

def f07_rag():
    fig, ax = canvas(3.8)
    ax.text(3, 94, "建索引", fontsize=9.91, fontweight="bold", color=ACCENT2)
    ax.text(52, 94, "查询", fontsize=9.91, fontweight="bold", color=ACCENT3)
    box(ax, 3, 74, 20, 12, "文档", fc="white", ec="#b9b5ac", fs=7.8)
    box(ax, 3, 56, 20, 12, "切块", fc="white", ec="#b9b5ac", fs=7.8)
    box(ax, 3, 38, 20, 12, "向量化", fc="white", ec="#b9b5ac", fs=7.8)
    box(ax, 3, 20, 20, 12, "向量库", fc="#f1f4f7", ec=ACCENT2, fs=7.8)
    for y in (74, 56, 38):
        arrow(ax, (13, y), (13, y - 6), color=GRAY)
    box(ax, 52, 74, 20, 12, "问题", fc="white", ec="#b9b5ac", fs=7.8)
    box(ax, 52, 56, 20, 12, "向量化", fc="white", ec="#b9b5ac", fs=7.8)
    box(ax, 52, 38, 20, 12, "检索 top-k", fc="#f1f5f0", ec=ACCENT3, fs=7.6)
    box(ax, 52, 20, 20, 12, "重排 + 拼接", fc="#f1f5f0", ec=ACCENT3, fs=7.4)
    arrow(ax, (62, 74), (62, 68), color=GRAY)
    arrow(ax, (62, 56), (62, 50), color=GRAY)
    arrow(ax, (62, 38), (62, 32), color=GRAY)
    arrow(ax, (23, 26), (52, 43), color=ACCENT2, rad=0.12)
    ax.text(35, 29, "相似度检索", fontsize=8.02, color=ACCENT2)
    box(ax, 78, 20, 19, 12, "模型", fc="#e7e9ec", ec="#8f8f8f", fs=8.2)
    arrow(ax, (72, 26), (78, 26), color=GRAY)
    ax.text(52, 8, "检索到的不等于相关的", fontsize=8.50, color=ACCENT)
    save(fig, "ch07-rag.png")

def f07_memgpt():
    fig, ax = canvas(3.8)
    box(ax, 4, 18, 44, 68, "", fc="#f8f7f3", ec="#b9b5ac")
    ax.text(6, 82, "主上下文（窗口）", fontsize=9.68, fontweight="bold")
    box(ax, 8, 68, 36, 9, "系统指令", fc="white", ec="#b9b5ac", fs=7.4, round=0.3)
    box(ax, 8, 50, 36, 14, "核心记忆\n（用户、项目、约束）", fc="#f7f3ec", ec=ACCENT, fs=7.0, round=0.3)
    box(ax, 8, 26, 36, 18, "FIFO 队列\n最近的对话与工具结果", fc="white", ec="#b9b5ac", fs=7.0, round=0.3)
    box(ax, 8, 30, 30, 2.2, "", fc="#e8e5de", ec="none")
    ax.text(56, 82, "外部存储", fontsize=9.68, fontweight="bold")
    box(ax, 56, 56, 40, 20, "回忆存储\n完整对话历史\n（可检索）", fc="#f1f4f7", ec=ACCENT2, fs=7.2)
    box(ax, 56, 28, 40, 20, "归档存储\n长期事实与文档\n（可检索）", fc="#f1f5f0", ec=ACCENT3, fs=7.2)
    arrow(ax, (48, 66), (56, 66), color=ACCENT2, lw=0.9)
    ax.text(52, 68.6, "换出", fontsize=7.55, color=ACCENT2, ha="center")
    arrow(ax, (56, 58), (48, 58), color=ACCENT2, lw=0.9)
    ax.text(52, 53.6, "换入", fontsize=7.55, color=ACCENT2, ha="center")
    arrow(ax, (48, 36), (56, 36), color=ACCENT3, lw=0.9)
    ax.text(52, 38.6, "写入", fontsize=7.55, color=ACCENT3, ha="center")
    ax.text(4, 10, "搬什么由模型决定，搬动本身由函数执行", fontsize=8.50, color=GRAY)
    save(fig, "ch07-memgpt.png")

def f07_impl():
    fig, ax = canvas(3.8)
    box(ax, 3, 26, 66, 60, "", fc="#f8f7f3", ec="#b9b5ac")
    ax.text(5, 82, "长期记忆库  事实 · 偏好 · 技能", fontsize=8.97, fontweight="bold")
    box(ax, 8, 34, 46, 42, "", fc="#f2ece2", ec="#c9b8a6")
    ax.text(10, 71, "会话存储  完整对话，可按关键词与向量检索", fontsize=8.02)
    box(ax, 12, 42, 32, 24, "", fc="#e9e4dc", ec="#b9b5ac")
    ax.text(14, 61, "工作记忆  当前对话与工具结果", fontsize=8.02)
    box(ax, 15, 46, 24, 10, "常驻区\n用户 · 项目 · 硬约束", fc="white", ec=ACCENT, fs=6.6)

    arrow(ax, (76, 20), (76, 74), color=ACCENT2, lw=0.9)
    ax.text(77.6, 48, "写入：抽取 → 去重 → 落库", fontsize=7.79, color=ACCENT2, rotation=90,
            va="center")
    arrow(ax, (70, 78), (70, 30), color=ACCENT3, lw=0.9, ls="--")
    ax.text(64.5, 54, "检索：按需取回", fontsize=7.79, color=ACCENT3, rotation=90, va="center")
    ax.annotate("", xy=(52, 46), xytext=(60, 20),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.8,
                                connectionstyle="arc3,rad=-0.2"))
    ax.text(3, 16, "搬运规则由程序控制，判断“什么重要”交给模型。", fontsize=8.50, color=GRAY)
    save(fig, "ch07-impl.png")

if __name__ == "__main__":
    for fn in [f07_layers, f07_rag, f07_memgpt, f07_impl]:
        fn()
