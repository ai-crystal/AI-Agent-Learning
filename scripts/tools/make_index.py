# -*- coding: utf-8 -*-
"""根据 assets/.local/papers/ 里实际存在的文件生成 INDEX.md。"""
import os, re, sys, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from papers_list import PAPERS

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPERS_DIR = os.path.join(ROOT, "assets", ".local", "papers")

# 后来改名或补充的条目
RENAME = {
    "2302.12173": ("indirect-prompt-injection", "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection", "16"),
    "2306.05499": ("houyi-prompt-injection", "Prompt Injection attack against LLM-integrated Applications", "16"),
}
EXTRA = [
    ("lats__2310.04406.pdf", "Language Agent Tree Search Unifies Reasoning, Acting, and Planning", "6"),
    ("toolrl__2504.13958.pdf", "ToolRL: Reward is All Tool Learning Needs", "14"),
    ("hackaprompt__2311.16119.pdf", "Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs", "16"),
]
DOCS = [
    ("doc-anthropic-building-effective-agents.pdf", "Anthropic · Building Effective Agents（工程博客）", "11"),
    ("doc-anthropic-context-engineering.pdf", "Anthropic · Effective Context Engineering for AI Agents", "8"),
    ("doc-mcp-specification.pdf", "Model Context Protocol 规范", "5"),
    ("doc-openai-practical-guide-building-agents.pdf", "OpenAI · A Practical Guide to Building Agents", "11"),
    ("doc-agents-md.pdf", "AGENTS.md 约定", "12"),
    ("doc-a2a-protocol.pdf", "Agent2Agent（A2A）协议规范", "12"),
]
CH = {"1": "第 1 章　背景与失败模式", "2": "第 2 章　最小骨架", "3": "第 3 章　思维链及其家族",
      "4": "第 4 章　ReAct", "5": "第 5 章　工具调用", "6": "第 6 章　规划与反思",
      "7": "第 7 章　记忆", "8": "第 8 章　上下文工程", "9": "第 9 章　用代码行动",
      "10": "第 10 章　操作界面", "11": "第 11 章　Harness", "12": "第 12 章　协议与形态",
      "13": "第 13 章　多 Agent", "14": "第 14 章　训练", "15": "第 15 章　评测", "16": "第 16 章　安全"}
ORDER = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

items = {}
for pid, slug, title, ch in PAPERS:
    if pid in RENAME:
        slug, title, ch = RENAME[pid]
    items[f"{slug}__{pid}.pdf"] = (title, pid, ch)
for fn, t, ch in EXTRA + DOCS:
    items[fn] = (t, fn.split("__")[-1].replace(".pdf", "") if "__" in fn else "—", ch)

have = set(os.path.basename(p) for p in glob.glob(os.path.join(PAPERS_DIR, "*.pdf")))
for fn in sorted(have):
    if fn not in items:
        print("警告：没有登记的论文", fn)
listed = [f for f in items if f in have]
by = {}
for fn in listed:
    t, pid, ch = items[fn]
    by.setdefault(ch, []).append((fn, t, pid))

out = ["# 论文与资料清单", "",
       "书里引用的原始文献都在这里，共 %d 份（%d 篇论文 + %d 份规范与工程文档）。"
       % (len(have), len(have) - len(DOCS), len(DOCS)),
       "", "文件名格式是 `短名__arXiv编号.pdf`，按编号可以直接在 arXiv 上找到原文。"
       "想补充新论文，把编号加进 `scripts/tools/papers_list.py`，再运行 `python scripts/tools/fetch_papers.py`。", ""]
for ch in ORDER:
    if ch not in by:
        continue
    out += ["## " + CH[ch], "", "| 文件 | 标题 | 编号 |", "|------|------|------|"]
    for fn, t, pid in sorted(by[ch], key=lambda x: x[0]):
        out.append("| `%s` | %s | %s |" % (fn, t.replace("|", "／"), pid))
    out.append("")
open(os.path.join(PAPERS_DIR, "INDEX.md"), "w", encoding="utf-8").write("\n".join(out))
print("写入 INDEX.md，收录 %d 份，目录内共 %d 份 PDF" % (len(listed), len(have)))
