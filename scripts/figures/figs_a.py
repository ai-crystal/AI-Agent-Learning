# -*- coding: utf-8 -*-
"""第 1—5 章的插图。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch
from figstyle import *


# ---------------- 图 1-1 ----------------
def f01_error_decay():
    fig, ax = plt.subplots(figsize=(W, 3.4))
    n = np.arange(1, 51)
    for p, c, lab in [(0.99, ACCENT3, "单步正确率 0.99"),
                      (0.95, ACCENT2, "0.95"),
                      (0.90, ACCENT, "0.90")]:
        ax.plot(n, p ** n, color=c, lw=1.6, label=lab)
    ax.axvline(20, color=GRAY, lw=0.7, ls=":")
    ax.annotate("20 步时约 36%", xy=(20, 0.95 ** 20), xytext=(23.5, 0.62),
                fontsize=9.44, color=ACCENT2,
                arrowprops=dict(arrowstyle="-", color=ACCENT2, lw=0.7))
    ax.set_xlabel("任务需要的步数", fontsize=10.62)
    ax.set_ylabel("全部做对的概率", fontsize=10.62)
    ax.set_xlim(1, 50); ax.set_ylim(0, 1.02)
    ax.legend(frameon=False, fontsize=9.44, loc="upper right")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8)
    ax.grid(axis="y", color="#e8e8e4", lw=0.6)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "ch01-error-decay.png")


# ---------------- 图 1-2 ----------------
def f01_autonomy():
    fig, ax = canvas(4.1)
    levels = [
        ("完全自主", "目标由模型自己提出，人只做事后审计", "#ebdfdd"),
        ("长期自主", "持续运行，只在异常时找人", "#f0e4e0"),
        ("自主规划", "自己拆步骤、调工具，关键节点确认", "#f4eae4"),
        ("有限选择", "在几个预设动作里选一个", "#f7f0ea"),
        ("固定流程", "模型只做分类或抽取，路径由代码写死", "#faf6f0"),
    ]
    h, gap = 14.0, 3.0
    for i, (name, desc, fc) in enumerate(levels):
        y = 5 + i * (h + gap)
        x = 20 + i * 1.2
        w = 52 + i * 3.2
        box(ax, x, y, w, h, "", fc=fc, ec="#bdb9b0", lw=0.9, round=0.5)
        ax.text(x + 2.6, y + h - 4.4, name, fontsize=10.62, fontweight="bold")
        ax.text(x + 2.6, y + 4.6, desc, fontsize=8.73, color="#444")
    ax.annotate("", xy=(16, 93), xytext=(16, 6),
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=1.2))
    ax.text(12, 50, "自主性增强", rotation=90, fontsize=9.44, color=ACCENT,
            ha="center", va="center")
    ax.text(96.5, 50, "人需要介入的频率下降", rotation=90, fontsize=8.50,
            color=GRAY, ha="center", va="center")
    save(fig, "ch01-autonomy.png")


# ---------------- 图 1-3 ----------------
def f01_stack():
    fig, ax = canvas(4.5)
    layers = [
        ("系统形态", "单 agent · 多 agent · 常驻服务 · 嵌入式助手", "#e9e4dc"),
        ("Harness", "主循环 · 权限 · 沙箱 · 状态 · 可观测性", "#eae2df"),
        ("工具与接口", "函数调用 · MCP · 代码执行 · 浏览器 / GUI", "#efe6e0"),
        ("记忆与上下文", "检索 · 压缩 · 分层记忆 · 子 agent 隔离", "#f2ece2"),
        ("推理与行动范式", "CoT · ReAct · 规划 · 反思", "#f5efe3"),
        ("模型能力", "预训练知识 · 指令遵循 · 工具使用 · 长思考", "#f7f2e6"),
    ]
    top, h, gap = 92, 12.6, 1.6
    for i, (name, desc, fc) in enumerate(layers):
        y = top - (i + 1) * h - i * gap
        box(ax, 8, y, 66, h, "", fc=fc, ec="#b9b5ac", lw=0.9, round=0.5)
        ax.text(10.6, y + h * 0.68, name, fontsize=10.62, fontweight="bold", va="center")
        ax.text(10.6, y + h * 0.28, desc, fontsize=8.38, color="#444", va="center")
    total_h = 6 * h + 5 * gap
    y0 = top - total_h
    for x, lab in [(78, "评测"), (89, "安全")]:
        box(ax, x, y0, 9, total_h, "", fc="#f6f2ea", ec="#b9b5ac", lw=0.9)
        ax.text(x + 4.5, y0 + total_h / 2, lab, rotation=90, fontsize=9.68,
                ha="center", va="center", fontweight="bold")
    ax.annotate("", xy=(5.4, 92), xytext=(5.4, y0),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.9))
    ax.text(3.2, (92 + y0) / 2, "能力", rotation=90, fontsize=8.50, color=GRAY,
            ha="center", va="center")
    save(fig, "ch01-stack.png")


# ---------------- 图 2-1 ----------------
def f02_loop():
    fig, ax = canvas(3.7)
    box(ax, 2, 68, 20, 16, "任务 / 用户", fc="white", ec="#b9b5ac", fs=8.4)
    box(ax, 30, 38, 30, 24, "上下文\n\n对话历史\n工具结果 · 当前任务", fc="#f4efe6", fs=8.2)
    box(ax, 72, 68, 26, 16, "模型", fc="#e7e9ec", fs=10.5, bold=True)
    box(ax, 72, 16, 26, 16, "工具 / 环境", fc="#e8ece6", fs=9.5, bold=True)

    # 箭头全部落在盒子边上；文字放在箭头旁，不压线、不压框。
    arrow(ax, (22, 76), (30, 58), color=GRAY)
    ax.text(21, 61, "新任务", fontsize=7.2, color=GRAY, ha="center")
    arrow(ax, (60, 56), (72, 72), color=ACCENT2)
    ax.text(66, 51, "完整历史", fontsize=7.2, color=ACCENT2, ha="center")
    arrow(ax, (85, 68), (85, 32), color=ACCENT2)
    ax.text(89, 50, "动作", fontsize=7.2, color=ACCENT2, ha="center")
    arrow(ax, (72, 24), (60, 44), color=ACCENT3)
    ax.text(65, 29, "工具结果", fontsize=7.2, color=ACCENT3, ha="center")
    arrow(ax, (72, 80), (22, 80), color=GRAY)
    ax.text(47, 85, "最终回答", fontsize=7.2, color=GRAY, ha="center")

    ax.text(50, 6, "每一轮：上下文 → 模型 → 工具 → 上下文；直到回答或触发停止条件",
            fontsize=8.2, color=GRAY, ha="center")
    save(fig, "ch02-loop.png")


# ---------------- 图 2-2 ----------------
def f02_trace():
    fig, ax = canvas(3.5)
    fig.subplots_adjust(top=0.90, bottom=0.16)
    rows = [
        (1, [("系统提示", 9), ("任务", 5)]),
        (2, [("系统提示", 9), ("任务", 5), ("思考", 6), ("动作", 3), ("观察", 4)]),
        (3, [("系统提示", 9), ("任务", 5), ("思考", 6), ("动作", 3), ("观察", 4),
             ("思考", 6), ("动作", 3), ("观察", 5)]),
        (4, [("系统提示", 9), ("任务", 5), ("思考", 6), ("动作", 3), ("观察", 4),
             ("思考", 6), ("动作", 3), ("观察", 5), ("回答", 4)]),
    ]
    cmap = {"系统提示": "#8f8f8f", "任务": "#c9c4b8", "思考": "#c98b8b",
            "动作": "#8fa8bd", "观察": "#93ab97", "回答": "#4a6f9c"}
    y = 80
    scale = 1.36
    for n, segs in rows:
        x = 16
        ax.text(13, y + 6, f"第 {n} 轮", fontsize=9.68, ha="right", va="center")
        for lab, w in segs:
            ax.add_patch(Rectangle((x, y), w * scale, 12, fc=cmap[lab], ec="white", lw=1.0))
            if w >= 6:
                ax.text(x + w * scale / 2, y + 6, lab, fontsize=8.26, color="white",
                        ha="center", va="center")
            x += w * scale
        ax.text(x + 2.0, y + 6, f"合计约 {sum(w for _, w in segs) * 30} token",
                fontsize=7.0, color=GRAY, va="center", ha="left")
        y -= 19
    handles = [Rectangle((0, 0), 1, 1, fc=c, ec="none") for c in
               ["#8f8f8f", "#c9c4b8", "#c98b8b", "#8fa8bd", "#93ab97", "#4a6f9c"]]
    ax.legend(handles, ["系统提示", "任务", "思考", "动作", "观察", "回答"],
              loc="lower left", bbox_to_anchor=(0.02, 0.0), ncol=6, frameon=False,
              fontsize=8.26, handlelength=1.0, columnspacing=1.0, handletextpad=0.4)
    ax.text(2, 96, "每一轮请求时，窗口里装的是什么", fontsize=10.62, fontweight="bold")
    save(fig, "ch02-trace.png")


# ---------------- 图 3-1 ----------------
def f03_gsm8k():
    fig, ax = plt.subplots(figsize=(W * 0.76, 3.2))
    labels = ["标准提示", "思维链", "思维链\n+ 自洽性投票"]
    vals = [17.9, 56.9, 74.4]
    bars = ax.bar(labels, vals, color=["#c9c4b8", "#7f9c86", ACCENT], width=0.52)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.6, f"{v}%", ha="center",
                fontsize=11.21, fontweight="bold")
    ax.set_ylim(0, 88)
    ax.set_ylabel("GSM8K 准确率", fontsize=10.62)
    ax.tick_params(labelsize=8.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#e8e8e4", lw=0.6); ax.set_axisbelow(True)
    ax.text(0.03, 0.9, "PaLM 540B，同一个模型", transform=ax.transAxes,
            fontsize=9.44, color=GRAY)
    fig.tight_layout()
    save(fig, "ch03-gsm8k.png")


# ---------------- 图 3-2 ----------------
def f03_selfconsistency():
    fig, ax = canvas(3.4)
    box(ax, 2, 42, 15, 14, "问题", fc="#e7e9ec", fs=9)
    paths = [("路径 1", "42", True), ("路径 2", "42", True), ("路径 3", "38", False),
             ("路径 4", "42", True), ("路径 5", "40", False)]
    ys = [78, 66, 54, 42, 30]
    for (lab, a, good), y in zip(paths, ys):
        c = ACCENT3 if good else "#b9b5ac"
        box(ax, 24, y, 26, 8, "", fc="white", ec="#b9b5ac", fs=7.4, round=0.4)
        ax.text(26.5, y + 4, lab, fontsize=8.73, va="center")
        ax.text(46.5, y + 4, f"→ {a}", fontsize=10.15, va="center", ha="right",
                color=c, fontweight="bold" if good else "normal")
        arrow(ax, (17, 49), (24, y + 4), color="#c9c4b8", lw=0.8)
        arrow(ax, (50, y + 4), (66, 49), color="#c9c4b8", lw=0.8)
    box(ax, 66, 38, 14, 22, "投票", fc="#e8ece6", fs=8.6)
    arrow(ax, (80, 49), (85, 49), color=ACCENT3)
    ax.text(87, 49, "42", fontsize=20.06, color=ACCENT3, fontweight="bold", va="center")
    ax.text(2, 96, "采样 5 条路径，3 条落在同一个答案上", fontsize=10.38, fontweight="bold")
    save(fig, "ch03-selfconsistency.png")


# ---------------- 图 3-3 ----------------
def f03_tot():
    fig, ax = canvas(3.9)
    box(ax, 36, 86, 24, 9, "起始状态", fc="#e7e9ec", fs=8.4)
    kids = [(4, "3+8=11", "0.2", False), (36, "8-3=5", "0.6", True), (68, "3×8=24", "0.8", True)]
    for x, t, s, keep in kids:
        box(ax, x, 62, 24, 9, t, fc="white" if keep else "#f2f2f0",
            ec="#b9b5ac" if keep else "#d3d0c8", fs=8.0, ls="-" if keep else "--")
        arrow(ax, (48, 86), (x + 12, 71), color="#c9c4b8", lw=0.8)
        ax.text(x + 12, 58.5, f"评估 {s}", fontsize=8.50, ha="center",
                color=ACCENT if keep else GRAY)
    # 剪枝
    ax.text(25.4, 68.2, "×", fontsize=15.34, color=ACCENT, ha="center", va="center")
    ax.text(30, 74, "剪掉", fontsize=8.26, color=ACCENT, ha="right")
    # 展开
    box(ax, 34, 38, 22, 9, "5 → 无解", fc="#f2f2f0", ec="#d3d0c8", fs=7.8, ls="--")
    arrow(ax, (44, 62), (44, 47), color=GRAY, ls=":")
    box(ax, 64, 38, 28, 9, "24 × 1 = 24，达成", fc="#e8ece6", ec=ACCENT3, fs=7.6)
    arrow(ax, (78, 62), (78, 47), color=ACCENT3)
    ax.text(66, 27, "目标达成，停止搜索", fontsize=8.50, color=ACCENT3)
    arrow(ax, (46, 38), (34, 60), color=ACCENT, ls="--", rad=0.3)
    ax.text(20, 46, "走不通\n回退换分支", fontsize=8.26, color=ACCENT, linespacing=1.5)
    ax.text(2, 97, "在中间状态上分支、评估、回溯", fontsize=10.38, fontweight="bold")
    save(fig, "ch03-tot.png")


# ---------------- 图 4-1 ----------------
def f04_loop():
    fig, ax = canvas(3.5)
    w, h = 26, 18

    def step(x, y, kind, text, fc, ec):
        box(ax, x, y, w, h, "", fc=fc, ec=ec, lw=0.9)
        ax.text(x + w / 2, y + 12.2, kind, fontsize=7.4, color=ec,
                ha="center", va="center", fontweight="bold")
        ax.text(x + w / 2, y + 5.7, text, fontsize=7.6, color=INK,
                ha="center", va="center")

    # 第一行从左向右，第二行从右向左，组成一条连续的蛇形轨迹。
    step(4, 66, "Thought 1", "先查这本书的作者", "#f7f3ec", ACCENT)
    step(37, 66, "Action 1", 'search["书名"]', "#f1f4f7", ACCENT2)
    step(70, 66, "Observation 1", "作者 = A（百科）", "#f1f5f0", ACCENT3)
    step(70, 30, "Thought 2", "再查 A 的合作者", "#f7f3ec", ACCENT)
    step(37, 30, "Action 2", 'search["A 的合作者"]', "#f1f4f7", ACCENT2)
    step(4, 30, "Observation 2", "合作者 = B", "#f1f5f0", ACCENT3)

    arrow(ax, (30, 75), (37, 75), color=GRAY)
    arrow(ax, (63, 75), (70, 75), color=GRAY)
    arrow(ax, (83, 66), (83, 48), color=ACCENT3)
    arrow(ax, (70, 39), (63, 39), color=GRAY)
    arrow(ax, (37, 39), (30, 39), color=GRAY)

    ax.text(50, 57, "观察结果写回上下文", fontsize=7.8, color=ACCENT3,
            ha="center", va="center")
    ax.text(50, 14, "Thought 与 Action 由模型生成；Observation 由环境返回。任务未完成就继续下一轮。",
            fontsize=8.0, color=GRAY, ha="center")
    save(fig, "ch04-loop.png")


# ---------------- 图 4-2 ----------------
def f04_compare():
    fig, ax = canvas(3.5)
    cols = [
        ("CoT", [("想", "拆开问题"), ("想", "算第一步"), ("想", "算第二步"), ("答", "42")],
         "推理全在模型内部\n没有外部校验"),
        ("Act", [("动", "search"), ("动", "lookup"), ("动", "finish")],
         "只有动作\n不知道为什么要做"),
        ("ReAct", [("想", "先查作者"), ("动", "search"), ("观", "作者 A"),
                   ("想", "再查合作者"), ("动", "search"), ("答", "B")],
         "推理与观察交替\n错误能被外部否定"),
    ]
    style = {"想": (ACCENT, "#f5e6e4"), "动": (ACCENT2, "#e4eaf0"),
             "观": (ACCENT3, "#e6ede4"), "答": (ACCENT3, "#e6ede4")}
    for name, seq, note in cols:
        x = {"CoT": 3, "Act": 36, "ReAct": 69}[name]
        ax.text(x + 14, 94, name, fontsize=11.80, fontweight="bold", ha="center")
        y = 82
        for kind, text in seq:
            c, fc = style[kind]
            box(ax, x, y, 28, 8, f"{kind}　{text}", fc=fc, ec=c, fs=7.2, round=0.4)
            y -= 10.2
        ax.text(x + 14, y - 2, note, fontsize=8.26, ha="center", color="#444",
                va="top", linespacing=1.6)
    save(fig, "ch04-compare.png")


# ---------------- 图 5-1 ----------------
def f05_toolformer():
    fig, ax = canvas(3.2)
    steps = [
        ("插入候选调用", "印度的首都是\n[QA(印度的首都?)]"),
        ("执行并写入结果", "印度的首都是\n[QA] → 新德里"),
        ("比较后续文本的\n预测概率", "有结果时 loss 更低\n→ 保留这次调用"),
        ("微调模型", "学会在何时\n调用哪个工具"),
    ]
    w, gap = 21.0, 4.0
    for i, (t, ex) in enumerate(steps):
        x = 2 + i * (w + gap)
        box(ax, x, 38, w, 36, "", fc="white", ec="#b9b5ac")
        ax.add_patch(Circle((x + 4.2, 69), 2.8, fc=ACCENT, ec="none", zorder=4))
        ax.text(x + 4.2, 69, str(i + 1), color="white", fontsize=8.97, ha="center",
                va="center", fontweight="bold", zorder=5)
        ax.text(x + 8.4, 69, t, fontsize=8.61, va="center", linespacing=1.4)
        ax.text(x + 2.8, 51, ex, fontsize=8.26, color="#333", va="center", linespacing=1.6)
        if i < 3:
            arrow(ax, (x + w, 56), (x + w + gap, 56), lw=1.0)
    ax.text(2, 84, "自监督地构造带工具调用的训练数据", fontsize=10.62, fontweight="bold")
    ax.text(2, 20, "判据是“这次调用有没有让后续文本更容易预测”，不需要人工标注对错",
            fontsize=8.73, color=ACCENT)
    save(fig, "ch05-toolformer.png")


# ---------------- 图 5-2 ----------------
def f05_function_call():
    fig, ax = canvas(3.9)
    xs = {"程序": 14, "模型": 50, "工具": 86}
    for k, x in xs.items():
        box(ax, x - 9, 88, 18, 8, k, fc="#e7e9ec", fs=8.8, bold=True)
        ax.plot([x, x], [4, 88], color="#ccc", lw=0.8, ls=(0, (4, 3)))
    msgs = [
        (14, 50, 80, "① 工具清单 + 对话", ACCENT2, "above"),
        (50, 14, 70, "② tool_calls", ACCENT, "above"),
        (14, 86, 60, "③ 执行", ACCENT3, "above"),
        (86, 14, 50, "④ 结果", ACCENT3, "above"),
        (14, 50, 40, "⑤ role=tool 消息", ACCENT2, "above"),
        (50, 14, 30, "⑥ 回答或继续调用", ACCENT, "above"),
    ]
    for x1, x2, y, lab, c, _ in msgs:
        arrow(ax, (x1, y), (x2, y), color=c, lw=1.0)
        ax.text((x1 + x2) / 2, y + 2.8, lab, fontsize=8.26, ha="center", color=c)
    ax.text(50, 12, "每一轮往返 = 两次模型调用", fontsize=8.73, ha="center", color=GRAY)
    save(fig, "ch05-function-call.png")


# ---------------- 图 5-3 ----------------
def f05_mcp():
    fig, ax = canvas(3.5)
    box(ax, 3, 10, 44, 78, "", fc="#f8f7f3", ec="#b9b5ac")
    ax.text(5, 83, "宿主（agent 应用）", fontsize=10.15, fontweight="bold")
    box(ax, 7, 56, 36, 18, "客户端 A", fc="white", ec=ACCENT2, fs=8.2)
    box(ax, 7, 32, 36, 18, "客户端 B", fc="white", ec=ACCENT2, fs=8.2)
    box(ax, 7, 15, 36, 10, "模型 + 主循环", fc="#e7e9ec", ec="#8f8f8f", fs=7.8)
    arrow(ax, (25, 50), (25, 56), color=GRAY)
    arrow(ax, (25, 26), (25, 32), color=GRAY)
    for y, name, items in [(64, "文件系统服务端", "tools: read / write / list\nresources: file://…"),
                           (36, "数据库服务端", "tools: query\nresources: schema")]:
        box(ax, 62, y, 35, 22, "", fc="white", ec=ACCENT3)
        ax.text(64, y + 16, name, fontsize=9.20, fontweight="bold")
        ax.text(64, y + 5, items, fontsize=7.79, color="#444", va="center", linespacing=1.6)
    arrow(ax, (43, 66), (62, 72), color=ACCENT2, label="JSON-RPC", fs=6.8, lpos=0.5)
    arrow(ax, (43, 42), (62, 46), color=ACCENT2)
    ax.text(50, 96, "传输层：标准输入输出 或 HTTP", fontsize=8.50, color=GRAY, ha="center")
    save(fig, "ch05-mcp.png")


if __name__ == "__main__":
    for fn in [f01_error_decay, f01_autonomy, f01_stack, f02_loop, f02_trace,
               f03_gsm8k, f03_selfconsistency, f03_tot, f04_loop, f04_compare,
               f05_toolformer, f05_function_call, f05_mcp]:
        fn()
