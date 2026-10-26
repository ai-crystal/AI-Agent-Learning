# -*- coding: utf-8 -*-
"""第 11—16 章的插图。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
from figstyle import *


# ---------------- 图 11-1 ----------------
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


# ---------------- 图 11-2 ----------------
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


# ---------------- 图 12-1 ----------------
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


# ---------------- 图 12-2 ----------------
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


# ---------------- 图 13-1 ----------------
def f13_metagpt():
    fig, ax = canvas(3.6)
    stages = [("需求", "一句想法"), ("产品经理", "PRD"), ("架构师", "设计文档"),
              ("工程师", "代码"), ("测试", "用例与报告")]
    w, gap = 17.0, 3.2
    for i, (role, art) in enumerate(stages):
        x = 2 + i * (w + gap)
        box(ax, x, 54, w, 30, "", fc="white", ec="#b9b5ac")
        ax.text(x + w / 2, 78, role, fontsize=8.97, fontweight="bold", ha="center")
        ax.text(x + w / 2, 66, art, fontsize=8.02, color="#444", ha="center")
        if i < 4:
            arrow(ax, (x + w, 69), (x + w + gap, 69), color=GRAY, lw=0.9)
    arrow(ax, (88, 54), (88, 44), color=ACCENT3, lw=0.9)
    box(ax, 40, 30, 48, 12, "可执行反馈：代码跑不通 → 打回重写", fc="#f1f5f0", ec=ACCENT3, fs=7.2)
    arrow(ax, (40, 36), (30, 54), color=ACCENT, lw=0.9, rad=0.2)
    ax.text(2, 92, "MetaGPT 用 SOP 把“聊天”换成“有格式的产物”", fontsize=10.15, fontweight="bold")
    ax.text(2, 20, "产物越结构化，下游越好用，也越容易自动检查。", fontsize=8.50, color=GRAY)
    save(fig, "ch13-metagpt.png")


# ---------------- 图 13-2 ----------------
def f13_patterns():
    fig, ax = canvas(3.9)
    def node(x, y, r, label, fc="white", ec=INK, fs=6.2):
        ax.add_patch(Circle((x, y), r, fc=fc, ec=ec, lw=0.9))
        ax.text(x, y, label, fontsize=fs, ha="center", va="center")
    # 1 主管
    ax.text(13, 95, "主管", fontsize=9.68, fontweight="bold", ha="center")
    node(13, 76, 4.2, "主", fc="#f7f3ec", ec=ACCENT)
    for dx in (-9, 0, 9):
        node(13 + dx, 60, 3.4, "工")
        arrow(ax, (13, 72), (13 + dx, 64), color="#b9b5ac", lw=0.8, style="<|-|>")
    ax.text(13, 48, "一个大脑分派", fontsize=7.55, ha="center", color=GRAY)
    # 2 交接
    ax.text(37, 95, "交接", fontsize=9.68, fontweight="bold", ha="center")
    node(29, 72, 3.4, "A"); node(37, 72, 3.4, "B"); node(45, 72, 3.4, "C")
    arrow(ax, (32.4, 72), (33.6, 72), color="#b9b5ac", lw=0.8)
    arrow(ax, (40.4, 72), (41.6, 72), color="#b9b5ac", lw=0.8)
    ax.text(37, 62, "上游交给下游", fontsize=7.55, ha="center", color=GRAY)
    node(37, 50, 3.4, "用", fc="#f1f4f7", ec=ACCENT2)
    # 3 辩论
    ax.text(61, 95, "辩论", fontsize=9.68, fontweight="bold", ha="center")
    node(54, 72, 3.4, "A"); node(68, 72, 3.4, "B")
    arrow(ax, (57.4, 73.4), (64.6, 73.4), color="#b9b5ac", lw=0.8, style="<|-|>")
    arrow(ax, (64.6, 70.6), (57.4, 70.6), color="#b9b5ac", lw=0.8)
    ax.text(61, 62, "互评后收敛", fontsize=7.55, ha="center", color=GRAY)
    node(61, 50, 3.4, "答", fc="#f1f5f0", ec=ACCENT3)
    arrow(ax, (57.6, 68.2), (59.6, 53), color="#b9b5ac", lw=0.8)
    # 4 群聊
    ax.text(85, 95, "群聊", fontsize=9.68, fontweight="bold", ha="center")
    for (dx, dy) in [(-6, 68), (0, 72), (6, 68), (0, 62)]:
        node(85 + dx, dy, 3.0, "·")
    ax.text(85, 52, "共享一个对话", fontsize=7.55, ha="center", color=GRAY)
    # 5 层级
    ax.text(13, 40, "层级", fontsize=9.68, fontweight="bold", ha="center")
    node(13, 26, 3.6, "总", fc="#f7f3ec", ec=ACCENT)
    node(6, 12, 3.0, "组"); node(20, 12, 3.0, "组")
    arrow(ax, (11, 23), (7, 15), color="#b9b5ac", lw=0.8)
    arrow(ax, (15, 23), (19, 15), color="#b9b5ac", lw=0.8)
    ax.text(37, 30, "层数增加后，协调与失败归因更复杂；\n需要谨慎控制层数。",
            fontsize=8.26, color="#444", linespacing=1.7)
    save(fig, "ch13-patterns.png")


# ---------------- 图 13-3 ----------------
def f13_cost():
    fig, ax = plt.subplots(figsize=(W * 0.8, 3.0))
    n = np.array([1, 2, 3, 4, 5, 6])
    cost = 1.0 * n ** 2.1
    benefit = 1 - np.exp(-1.1 * (n - 1)) * 0.9
    benefit = np.array([0.28, 0.62, 0.72, 0.73, 0.70, 0.66])
    ax.plot(n, cost / cost.max(), "o-", color=ACCENT, lw=1.6, ms=4, label="成本")
    ax.plot(n, benefit, "s-", color=ACCENT2, lw=1.6, ms=4, label="收益")
    ax.axvspan(1.6, 3.4, color="#f2ece2", alpha=0.6, zorder=0)
    ax.text(2.5, 0.86, "需实测的区间", fontsize=8.8, ha="center", color="#7a6a55")
    ax.set_xlabel("agent 数量", fontsize=10.15)
    ax.set_ylabel("归一化相对值（示意）", fontsize=9.6)
    ax.set_xticks(n); ax.set_ylim(0, 1.05)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=9.20, loc="center right")
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    ax.text(0.0, -0.24, "概念示意，非实测；独立并行任务的成本可接近线性",
            transform=ax.transAxes, fontsize=8.0, color=GRAY)
    fig.tight_layout()
    save(fig, "ch13-cost.png")


# ---------------- 图 14-1 ----------------
def f14_rl():
    fig, ax = canvas(3.6)
    box(ax, 4, 70, 26, 14, "环境 / 任务", fc="#f1f5f0", ec=ACCENT3, fs=8.2)
    box(ax, 40, 70, 24, 14, "策略模型", fc="#e7e9ec", ec="#8f8f8f", fs=8.4)
    box(ax, 74, 70, 22, 14, "验证器\n（测试 / 答案）", fc="#f1f4f7", ec=ACCENT2, fs=7.6)
    box(ax, 74, 32, 22, 14, "优势估计\n（组内比较）", fc="#f7f3ec", ec=ACCENT, fs=7.6)
    box(ax, 40, 32, 24, 14, "参数更新", fc="#f7f3ec", ec=ACCENT, fs=8.2)
    box(ax, 4, 32, 26, 14, "轨迹与奖励记录", fc="#faf9f6", ec="#cfcbc2", fs=7.4)
    arrow(ax, (30, 77), (40, 77), color=GRAY, label="观察", fs=6.6, lpos=0.5)
    arrow(ax, (64, 77), (74, 77), color=ACCENT2, label="动作序列", fs=6.6, lpos=0.5)
    arrow(ax, (85, 70), (85, 46), color=ACCENT2)
    arrow(ax, (74, 39), (64, 39), color=ACCENT)
    arrow(ax, (40, 39), (30, 39), color="#b9b5ac")
    arrow(ax, (52, 46), (52, 70), color=ACCENT, label="新策略再采样", fs=6.6, lpos=0.5)
    ax.text(50, 16, "训练的好坏，取决于奖励信号能不能真的分辨对错", fontsize=8.73,
            color=GRAY, ha="center")
    ax.text(2, 94, "Agentic RL 的循环：采样 → 判定 → 更新", fontsize=10.15, fontweight="bold")
    save(fig, "ch14-rl-loop.png")


# ---------------- 图 14-2 ----------------
def f14_grpo():
    fig, ax = canvas(3.2)
    box(ax, 2, 44, 16, 14, "同一道题", fc="#e7e9ec", fs=8.2)
    scores = [1, 0, 0, 1, 0, 1, 0, 1]
    ys = [88, 78, 68, 58, 48, 38, 28, 18]
    for i, (s, y) in enumerate(zip(scores, ys)):
        c = ACCENT3 if s else "#b9b5ac"
        box(ax, 26, y, 12, 7, f"样本 {i + 1}", fc="white", ec=c, fs=6.2, round=0.3)
        arrow(ax, (18, 51), (26, y + 3.5), color="#dcd9d1", lw=0.7)
        ax.text(41, y + 3.5, "成功  1" if s else "失败  0", fontsize=7.6, color=c, va="center")
    ax.plot([46, 46], [14, 98], color="#e0ddd6", lw=0.8)
    ax.text(49, 92, "组内均值 0.5", fontsize=8.97, va="center")
    ax.text(49, 82, "高于均值 → 优势为正\n低于均值 → 优势为负", fontsize=8.26, color="#444",
            va="top", linespacing=1.7)
    ax.text(49, 56, "不需要额外的价值网络\n（省掉 critic）", fontsize=8.26, color=ACCENT,
            va="top", linespacing=1.7)
    save(fig, "ch14-grpo.png")


# ---------------- 图 14-3 ----------------
def f14_retool():
    fig, ax1 = plt.subplots(figsize=(W * 0.82, 3.0))
    steps = np.arange(0, 420, 20)
    call = 0.08 + 0.65 / (1 + np.exp(-(steps - 160) / 55))
    acc = 0.27 + 0.40 / (1 + np.exp(-(steps - 170) / 70))
    ax1.plot(steps, call * 100, color=ACCENT, lw=1.6, label="代码调用率")
    ax1.plot(steps, acc * 100, color=ACCENT2, lw=1.6, label="解题准确率")
    ax1.set_xlabel("训练步数", fontsize=10.15)
    ax1.set_ylabel("百分比", fontsize=10.15)
    ax1.set_ylim(0, 100)
    ax1.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax1.spines[s].set_visible(False)
    ax1.legend(frameon=False, fontsize=9.20, loc="lower right")
    ax1.grid(axis="y", color="#eeece7", lw=0.6); ax1.set_axisbelow(True)
    ax1.annotate("学会在需要精确计算时\n才调用解释器", xy=(230, 55), xytext=(60, 78),
                 fontsize=8.50, color=GRAY,
                 arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.7))
    fig.tight_layout()
    save(fig, "ch14-retool.png")


# ---------------- 图 15-1 ----------------
def f15_pyramid():
    fig, ax = canvas(2.6)
    # 底层测单点能力，越往上越接近真实系统的使用表现。
    tiers = [
        ("模型能力", "单题问答 · 数学 · 代码片段", 6, 18, "#eef1ee"),
        ("任务完成", "完整任务 + 真实环境", 28, 18, "#f4eae4"),
        ("系统工程", "成功率 · 成本 · 延迟 · 介入率", 50, 18, "#f5e0dd"),
    ]
    for name, desc, y, h, fc in tiers:
        shrink = (y - 6) * 0.55
        pts = [[4 + shrink, y], [96 - shrink, y],
               [88 - shrink, y + h], [12 + shrink, y + h]]
        ax.add_patch(Polygon(pts, closed=True, fc=fc, ec="#c9c5bc", lw=0.9))
        ax.text(50, y + h * 0.66, name, fontsize=10.0, fontweight="bold", ha="center")
        ax.text(50, y + h * 0.27, desc, fontsize=7.8, color="#444", ha="center")
    save(fig, "ch15-pyramid.png")


# ---------------- 图 15-2 ----------------
def f15_bench():
    fig, ax = plt.subplots(figsize=(W * 0.84, 3.15))
    labels = ["GAIA", "WebArena", "OSWorld"]
    agents = [15.0, 14.41, 12.24]
    humans = [92.0, 78.24, 72.36]
    x = np.arange(len(labels))
    width = 0.32
    bars1 = ax.bar(x - width / 2, agents, width, color=ACCENT, label="Agent（论文发布时）")
    bars2 = ax.bar(x + width / 2, humans, width, color="#b8b2a8", label="人类（论文设置）")
    for bars in (bars1, bars2):
        for bar in bars:
            value = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, value + 2,
                    f"{value:g}%", ha="center", fontsize=8.7, color=INK)
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9.2)
    ax.set_ylim(0, 108); ax.set_ylabel("成功率 / 得分（%）", fontsize=9.6)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=8.2, loc="upper right", ncol=2)
    ax.text(0.0, -0.24, "各论文发布时的设置；任务与评分不同，不能横向排名",
            transform=ax.transAxes, fontsize=8.1, color=GRAY)
    fig.tight_layout()
    save(fig, "ch15-bench.png")


# ---------------- 图 15-3 ----------------
def f15_passk():
    fig, ax = plt.subplots(figsize=(W * 0.8, 2.9))
    k = np.arange(1, 11)
    p = 0.7
    ax.plot(k, 1 - (1 - p) ** k, "o-", color=ACCENT2, lw=1.6, ms=4, label="pass@k（至少一次成功）")
    ax.plot(k, p ** k, "s-", color=ACCENT, lw=1.6, ms=4, label="pass^k（每次都成功）")
    ax.set_xlabel("重复运行次数 k", fontsize=10.15)
    ax.set_ylabel("概率", fontsize=10.15)
    ax.set_xticks(k); ax.set_ylim(0, 1.05)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=8.97, loc="center right")
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    ax.text(0.03, 0.06, "单次成功率 70% 的同一个 agent", transform=ax.transAxes,
            fontsize=8.50, color=GRAY)
    fig.tight_layout()
    save(fig, "ch15-passk.png")


# ---------------- 图 16-1 ----------------
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
    for fn in [f11_arch, f11_permission, f12_protocols, f12_gateway, f13_metagpt,
               f13_patterns, f13_cost, f14_rl, f14_grpo, f14_retool, f15_pyramid,
               f15_bench, f15_passk, f16_attack]:
        fn()
