# -*- coding: utf-8 -*-
"""第 6—10 章的插图。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
from figstyle import *


# ---------------- 图 6-1 ----------------
def f06_plan_execute():
    fig, ax = canvas(4.0)
    ax.text(2, 95, "ReAct：边走边看", fontsize=10.62, fontweight="bold")
    xs = [4, 17, 30]
    y = 78
    for i, x in enumerate(xs):
        box(ax, x, y, 11, 9, "想", fc="#f5e6e4", ec=ACCENT, fs=7.4, round=0.4)
        box(ax, x, y - 14, 11, 9, "动", fc="#e4eaf0", ec=ACCENT2, fs=7.4, round=0.4)
        box(ax, x, y - 28, 11, 9, "看", fc="#e6ede4", ec=ACCENT3, fs=7.4, round=0.4)
        if i < 2:
            arrow(ax, (x + 11, y - 24), (xs[i + 1], y - 2), color="#b9b5ac", lw=0.8, rad=-0.15)
        else:
            arrow(ax, (x + 11, y - 24), (x + 11, 36), color="#b9b5ac", lw=0.8)
    ax.text(2, 44, "每一步都要判断下一步做什么", fontsize=8.50, color="#444")
    ax.text(2, 28, "上下文随步数线性增长", fontsize=8.50, color=ACCENT)
    ax.plot([46, 46], [8, 96], color="#e0ddd6", lw=1.0)
    ax.text(51, 95, "Plan-and-Execute：先看全局", fontsize=10.62, fontweight="bold")
    box(ax, 51, 72, 45, 17, "", fc="#f7f3ec", ec="#b9b5ac")
    ax.text(53, 85.4, "计划", fontsize=8.50, fontweight="bold")
    ax.text(53, 78.6, "1 查资料　2 算指标　3 写结论", fontsize=8.14, color="#333")
    for i in range(3):
        yy = 52 - i * 15
        box(ax, 51, yy, 45, 10, f"执行第 {i + 1} 步", fc="white", ec=ACCENT2, fs=7.4, round=0.4)
        ax.text(94.5, yy + 5, "√" if i < 2 else "…", fontsize=9.44, color=ACCENT3,
                ha="right", va="center")
    arrow(ax, (73, 72), (73, 62), color=GRAY)
    arrow(ax, (73, 52), (73, 37), color=GRAY)
    arrow(ax, (73, 37), (73, 22), color=GRAY)
    ax.text(51, 14, "计划只生成一次，每步只看当前步骤", fontsize=8.50, color="#444")
    ax.text(51, 6, "出问题时要能重规划", fontsize=8.50, color=ACCENT)
    save(fig, "ch06-plan-execute.png")


# ---------------- 图 6-2 ----------------
def f06_reflexion():
    fig, ax = canvas(3.6)
    box(ax, 4, 72, 36, 13, "执行任务（ReAct 循环）", fc="#f1f4f7", ec=ACCENT2, fs=8.0)
    box(ax, 58, 72, 34, 13, "评估结果（测试 / 答案核对）", fc="#f1f5f0", ec=ACCENT3, fs=7.4)
    box(ax, 58, 38, 34, 13, "写出反思：“第 3 步漏了边界”", fc="#f7f3ec", ec=ACCENT, fs=7.0)
    box(ax, 4, 38, 36, 13, "反思记忆（跨回合保留）", fc="#f7f3ec", ec=ACCENT, fs=8.0)
    arrow(ax, (40, 78.5), (58, 78.5), color=ACCENT3)
    ax.text(49, 81.6, "成功 / 失败", fontsize=8.02, ha="center", color=ACCENT3)
    arrow(ax, (75, 72), (75, 51), color=ACCENT)
    ax.text(76.6, 61.5, "失败才写", fontsize=8.02, color=ACCENT, rotation=90, va="center")
    arrow(ax, (58, 44.5), (40, 44.5), color=ACCENT)
    arrow(ax, (22, 51), (22, 72), color=ACCENT2)
    ax.text(23.6, 61.5, "下一回合带上", fontsize=8.02, color=ACCENT2, rotation=90, va="center")
    ax.text(50, 24, "没有参数更新，只有一段文字在起作用", fontsize=8.73, color=GRAY,
            ha="center")
    ax.text(4, 94, "Reflexion：把失败经验写成话，带到下一次尝试", fontsize=10.15, fontweight="bold")
    save(fig, "ch06-reflexion.png")


# ---------------- 图 6-3 ----------------
def f06_rewwo():
    fig, ax = canvas(3.4)
    box(ax, 2, 58, 28, 30, "", fc="#f7f3ec", ec="#b9b5ac")
    ax.text(4, 83, "规划器（模型 1 次）", fontsize=8.97, fontweight="bold")
    for i, t in enumerate(["#E1 = search[财报]", "#E2 = calc(#E1 × 0.8)", "#E3 = finish(#E2)"]):
        ax.text(4, 76 - i * 5.2, t, fontsize=7.79, color="#333")
    box(ax, 36, 58, 26, 30, "", fc="#f1f4f7", ec=ACCENT2)
    ax.text(38, 83, "执行器（不调用模型）", fontsize=8.97, fontweight="bold")
    ax.text(38, 74, "按顺序跑工具\n填入变量 → 结果", fontsize=8.02, color="#333", linespacing=1.7)
    box(ax, 68, 58, 28, 30, "", fc="#f1f5f0", ec=ACCENT3)
    ax.text(70, 83, "求解器（模型 1 次）", fontsize=8.97, fontweight="bold")
    ax.text(70, 74, "所有变量齐了\n一次写出答案", fontsize=8.02, color="#333", linespacing=1.7)
    arrow(ax, (30, 73), (36, 73), color=GRAY)
    arrow(ax, (62, 73), (68, 73), color=GRAY)
    ax.plot([2, 94], [48, 48], color="#e0ddd6", lw=0.9)
    ax.text(2, 40, "ReAct：每步一次模型调用，历史全部重发", fontsize=8.50, color=GRAY)
    ax.text(2, 31, "ReWOO：模型只调用两次，动作阶段不占上下文", fontsize=8.50, color=ACCENT)
    save(fig, "ch06-rewwo.png")


# ---------------- 图 7-1 ----------------
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


# ---------------- 图 7-2 ----------------
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


# ---------------- 图 7-3 ----------------
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


# ---------------- 图 7-4 ----------------
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


# ---------------- 图 8-1 ----------------
def f08_lost_middle():
    fig, ax = plt.subplots(figsize=(W * 0.82, 3.1))
    x = np.linspace(0, 100, 200)
    y = 0.62 + 0.33 * ((x - 50) / 50) ** 2 + 0.02 * np.sin(x / 6)
    ax.plot(x, y, color=ACCENT2, lw=1.8)
    ax.axvspan(30, 70, color="#f2ece2", alpha=0.7, zorder=0)
    ax.text(50, 0.665, "中间位置\n信息容易被淹没", fontsize=9.20, ha="center", color="#7a6a55",
            linespacing=1.6)
    ax.text(6, 0.955, "开头", fontsize=8.97, color=GRAY)
    ax.text(88, 0.955, "结尾", fontsize=8.97, color=GRAY)
    ax.set_xlabel("关键信息在上下文中的位置", fontsize=10.15)
    ax.set_ylabel("模型找到它的概率", fontsize=10.15)
    ax.set_xticks([]); ax.set_ylim(0.55, 1.0)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "ch08-lost-middle.png")


# ---------------- 图 8-2 ----------------
def f08_ops():
    fig, ax = canvas(3.4)
    panels = [
        ("写入", "把状态写到上下文之外", "例：把“已确认”“待解决”写成 note.md", 4, 54),
        ("选择", "从大量信息里挑一部分", "例：检索 top-5、只留最近 8 轮、截断输出", 52, 54),
        ("压缩", "把多轮内容压成更短的表示", "例：把前二十轮摘要成两百字", 4, 5),
        ("隔离", "把子任务放到另一个窗口", "例：子 agent 只回传结论", 52, 5),
    ]
    for name, desc, ex, x, y in panels:
        box(ax, x, y, 44, 37, "", fc="#faf9f6", ec="#cfcbc2")
        ax.text(x + 3, y + 29, name, fontsize=10.86, fontweight="bold")
        ax.text(x + 3, y + 21, desc, fontsize=8.50, color="#333")
        ax.text(x + 3, y + 12, ex, fontsize=7.67, color="#777")
    ax.text(4, 96, "上下文工程的四类动作", fontsize=10.62, fontweight="bold")
    save(fig, "ch08-ops.png")


# ---------------- 图 8-3 ----------------
def f08_budget():
    fig, ax = plt.subplots(figsize=(W * 0.9, 2.4))
    segs = [("系统提示与工具定义", 15, "#8f8f8f"),
            ("任务与约束", 5, "#c9c4b8"),
            ("近期历史", 38, ACCENT2),
            ("检索内容", 25, ACCENT3),
            ("余量（留给工具返回）", 17, "#d9c9a8")]
    left = 0
    for name, w, c in segs:
        ax.barh(0, w, left=left, color=c, height=0.42, edgecolor="white", lw=1.2)
        ax.text(left + w / 2, 0, f"{w}%", ha="center", va="center", fontsize=9.68,
                color="white" if c not in ("#c9c4b8", "#d9c9a8") else "#333",
                fontweight="bold")
        left += w
    ax.set_xlim(0, 100); ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([]); ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("一次调用的上下文预算", fontsize=10.15)
    ax.tick_params(labelsize=7.6)
    ax.spines["left"].set_visible(False)
    handles = [Rectangle((0, 0), 1, 1, fc=c, ec="none") for _, _, c in segs]
    ax.legend(handles, [n for n, _, _ in segs], loc="upper center",
              bbox_to_anchor=(0.5, -0.42), ncol=3, frameon=False, fontsize=8.73,
              handlelength=1.0, columnspacing=1.2, handletextpad=0.5)
    fig.tight_layout()
    save(fig, "ch08-budget.png")


# ---------------- 图 9-1 ----------------
def f09_codeact():
    fig, ax = canvas(3.5)
    ax.text(3, 95, "JSON 动作：一轮一件事", fontsize=10.15, fontweight="bold", color=ACCENT2)
    ax.text(55, 95, "代码动作：一段脚本做完", fontsize=10.15, fontweight="bold", color=ACCENT3)
    rounds = ['{"tool":"read","args":{...}}', '{"tool":"filter","args":{...}}',
              '{"tool":"sort","args":{...}}', '{"tool":"head","args":{...}}']
    y = 84
    for r in rounds:
        box(ax, 3, y, 42, 9, "", fc="white", ec="#b9b5ac")
        ax.text(5, y + 4.5, r, fontsize=6.84, va="center", color="#333")
        arrow(ax, (24, y), (24, y - 3.4), color=GRAY, lw=0.8)
        y -= 12.6
    ax.text(3, 14, "4 次模型调用 · 历史重发 4 次", fontsize=8.73, color=ACCENT2)
    ax.plot([50, 50], [10, 96], color="#e0ddd6", lw=1.0)
    code = ["df = read('a.csv')", "df = df[df.x > 3]", "df = df.sort_values('y')",
            "print(df.head(3))"]
    box(ax, 55, 52, 42, 30, "", fc="#f7f7f5", ec="#b9b5ac")
    for i, line in enumerate(code):
        ax.text(57, 76 - i * 6.0, line, fontsize=7.55, va="center", color="#222")
    arrow(ax, (76, 52), (76, 40), color=ACCENT3)
    box(ax, 55, 26, 42, 12, "执行一次，返回 3 行结果", fc="#f1f5f0", ec=ACCENT3, fs=7.2)
    ax.text(55, 14, "1 次模型调用 · 中间数据留在解释器里", fontsize=8.73, color=ACCENT3)
    save(fig, "ch09-codeact.png")


# ---------------- 图 9-2 ----------------
def f09_aci():
    fig, ax = canvas(3.8)
    box(ax, 2, 18, 26, 68, "", fc="#faf9f6", ec="#cfcbc2")
    ax.text(4, 81, "命令集", fontsize=9.44, fontweight="bold")
    cmds = ["open <file>", "search_file <kw>", "search_dir <kw>", "edit <a> <b>",
            "scroll_up / down"]
    for i, c in enumerate(cmds):
        ax.text(4, 73 - i * 7.6, c, fontsize=8.02, color="#333")
    ax.text(4, 28, "只暴露必要动作\n输出格式对模型友好", fontsize=8.02, color=GRAY,
            linespacing=1.6)
    ax.add_patch(Rectangle((36, 32), 56, 44, fc="white", ec="#b9b5ac", lw=0.9))
    ax.add_patch(Rectangle((36, 68), 56, 8, fc="#efece6", ec="#b9b5ac", lw=0.8))
    ax.text(38, 72, "src/cache.py　第 41–46 行", fontsize=8.02, color="#333", va="center")
    code = ["def get(k):", "    v = cache[k]", "    if v is None:",
            "        v = load(k)", "        cache[k] = v", "    return v"]
    for i, line in enumerate(code):
        yy = 63 - i * 5.0
        ax.text(37.4, yy, str(41 + i), fontsize=6.14, color="#aaa", va="center", ha="left")
        ax.text(40.5, yy, line, fontsize=6.84, color="#333", va="center")
    ax.add_patch(Rectangle((36.4, 63 - 4 * 5.0 - 2.2), 54, 4.4, fc="#f5e6e4", ec="none"))
    ax.text(40.5, 63 - 4 * 5.0, "        cache[k] = v", fontsize=6.84, color=ACCENT, va="center")
    box(ax, 36, 12, 56, 12, "反馈：第 45 行 KeyError，k 可能不存在", fc="#f1f5f0",
        ec=ACCENT3, fs=6.8)
    arrow(ax, (64, 32), (64, 25), color=ACCENT3)
    arrow(ax, (28, 60), (36, 60), color=ACCENT2)
    ax.text(32, 62.6, "执行", fontsize=7.79, color=ACCENT2, ha="center")
    arrow(ax, (30, 18), (30, 80), color=ACCENT2, ls="--")
    ax.text(31.4, 46, "改完再读", fontsize=7.55, color=ACCENT2, rotation=90, va="center")
    ax.text(2, 92, "SWE-agent 的循环：命令 → 观察 → 修改", fontsize=10.15, fontweight="bold")
    save(fig, "ch09-aci.png")


# ---------------- 图 10-1 ----------------
def _mock_page(ax, x, y, w, h, marks=False):
    ax.add_patch(Rectangle((x, y), w, h, fc="white", ec="#b9b5ac", lw=0.9))
    ax.add_patch(Rectangle((x, y + h - 4.5), w, 4.5, fc="#e8e5de", ec="none"))
    ax.text(x + 1.6, y + h - 2.2, "● ● ●", fontsize=4.96, color="#a8a49b", va="center")
    ax.add_patch(Rectangle((x + 1.6, y + h - 12), w * 0.55, 4.2, fc="#f7f6f2",
                           ec="#c9c5bc", lw=0.7))
    ax.add_patch(Rectangle((x + 1.6 + w * 0.58, y + h - 12), w * 0.22, 4.2, fc="#dfe6ee",
                           ec="#b9c6d4", lw=0.7))
    ax.text(x + 1.6 + w * 0.69, y + h - 9.9, "搜索", fontsize=4.96, color="#4a5a6a",
            va="center", ha="center")
    ax.add_patch(Rectangle((x + 1.6, y + h - 18), w * 0.5, 2.6, fc="#ddd9d0", ec="none"))
    for i in range(3):
        ax.add_patch(Rectangle((x + 1.6, y + h - 23 - i * 3.2), w * (0.8 - i * 0.12), 1.4,
                               fc="#eeebe5", ec="none"))
    ax.add_patch(Rectangle((x + 1.6, y + 3), w * 0.3, 4.4, fc="#dfe6ee", ec="#b9c6d4", lw=0.7))
    ax.text(x + 1.6 + w * 0.15, y + 5.2, "提交", fontsize=4.96, color="#4a5a6a",
            ha="center", va="center")
    if marks:
        boxes = [(x + 1.2, y + h - 12.6, w * 0.59, 5.4),
                 (x + 1.2 + w * 0.55, y + h - 12.6, w * 0.27, 5.4),
                 (x + 1.2, y + 2.4, w * 0.33, 5.4)]
        for i, (mx, my, mw, mh) in enumerate(boxes):
            ax.add_patch(Rectangle((mx, my), mw, mh, fc="none", ec=ACCENT, lw=1.0))
            ax.add_patch(Circle((mx + 1.4, my + mh + 1.4), 1.6, fc=ACCENT, ec="none", zorder=5))
            ax.text(mx + 1.4, my + mh + 1.4, str(i + 1), color="white", fontsize=5.90,
                    ha="center", va="center", zorder=6)


def f10_observation():
    fig, ax = canvas(3.4)
    ax.text(2, 96, "① 像素", fontsize=10.15, fontweight="bold")
    _mock_page(ax, 2, 56, 26, 34)
    ax.text(2, 49, "看得见布局，看不清小字", fontsize=8.02, color="#444")
    ax.text(36, 96, "② 结构化文本", fontsize=10.15, fontweight="bold")
    box(ax, 36, 52, 26, 38, "", fc="#f7f7f5", ec="#b9b5ac")
    lines = ["[1] input 搜索框", "[2] button 搜索", "[3] h1 标题",
             "[4] a 链接 详情", "[5] button 提交"]
    for i, l in enumerate(lines):
        ax.text(37.4, 84 - i * 6.4, l, fontsize=6.84, color="#333")
    ax.text(36, 45, "信息全，但节点多，需要裁剪", fontsize=8.02, color="#444")
    ax.text(70, 96, "③ 编号 + 截图", fontsize=10.15, fontweight="bold")
    _mock_page(ax, 70, 52, 26, 38, marks=True)
    ax.text(70, 45, "既能看懂，也能点准", fontsize=8.02, color="#444")
    ax.text(2, 22, "同一个页面，三种观察方式给出的信息完全不同。\n混合表示把“理解语义”和“定位像素”拆成两件事。",
            fontsize=8.50, color=GRAY, linespacing=1.7)
    save(fig, "ch10-observation.png")


# ---------------- 图 10-2 ----------------
def f10_bench():
    fig, ax = plt.subplots(figsize=(W * 0.86, 3.0))
    names = ["WebArena", "OSWorld", "GAIA"]
    human = [78.2, 72.4, 92.0]
    agent = [14.4, 12.2, 15.0]
    x = np.arange(len(names))
    w = 0.32
    b1 = ax.bar(x - w / 2, human, w, label="人类", color="#c9c4b8")
    b2 = ax.bar(x + w / 2, agent, w, label="agent（发布时的最好成绩）", color=ACCENT)
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.8, f"{b.get_height():.0f}%",
                    ha="center", fontsize=9.20)
    ax.set_xticks(x); ax.set_xticklabels(names, fontsize=9.91)
    ax.set_ylim(0, 105); ax.set_ylabel("任务成功率", fontsize=10.15)
    ax.tick_params(labelsize=7.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=8.97, loc="upper left", ncol=2)
    ax.grid(axis="y", color="#eeece7", lw=0.6); ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "ch10-bench.png")


if __name__ == "__main__":
    for fn in [f06_plan_execute, f06_reflexion, f06_rewwo, f07_layers, f07_rag,
               f07_memgpt, f08_lost_middle, f08_ops, f08_budget, f09_codeact,
               f09_aci, f10_observation, f10_bench, f07_impl]:
        fn()
