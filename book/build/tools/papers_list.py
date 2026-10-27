# -*- coding: utf-8 -*-
"""书稿引用论文清单：(arxiv_id, 文件名, 中文题名, 对应章节)"""

PAPERS = [
    # ---------- 第 1 章 背景 ----------
    ("2005.14165", "gpt3-few-shot-learners", "Language Models are Few-Shot Learners (GPT-3)", "1"),
    ("2203.02155", "instructgpt-rlhf", "Training language models to follow instructions with human feedback", "1"),
    ("2205.00445", "mrkl-systems", "MRKL Systems: A modular, neuro-symbolic architecture", "1"),
    ("2201.11903", "chain-of-thought", "Chain-of-Thought Prompting Elicits Reasoning in LLMs", "3"),
    # ---------- 第 3 章 推理 ----------
    ("2203.11171", "self-consistency", "Self-Consistency Improves Chain of Thought Reasoning", "3"),
    ("2305.10601", "tree-of-thoughts", "Tree of Thoughts: Deliberate Problem Solving with LLMs", "3"),
    ("2308.09687", "graph-of-thoughts", "Graph of Thoughts: Solving Elaborate Problems with LLMs", "3"),
    ("2211.12588", "program-of-thoughts", "Program of Thoughts Prompting", "3"),
    ("2501.12948", "deepseek-r1", "DeepSeek-R1: Incentivizing Reasoning Capability via RL", "3"),
    # ---------- 第 4 章 ReAct ----------
    ("2210.03629", "react", "ReAct: Synergizing Reasoning and Acting in Language Models", "4"),
    ("2305.18323", "rewoo", "ReWOO: Decoupling Reasoning from Observations", "4"),
    ("2305.04091", "plan-and-solve", "Plan-and-Solve Prompting", "4"),
    ("2303.17651", "self-refine", "Self-Refine: Iterative Refinement with Self-Feedback", "6"),
    ("2303.11366", "reflexion", "Reflexion: Language Agents with Verbal Reinforcement Learning", "6"),
    # ---------- 第 5 章 工具 ----------
    ("2302.04761", "toolformer", "Toolformer: Language Models Can Teach Themselves to Use Tools", "5"),
    ("2112.09332", "webgpt", "WebGPT: Browser-assisted question-answering with human feedback", "5"),
    ("2305.15334", "gorilla", "Gorilla: Large Language Model Connected with Massive APIs", "5"),
    ("2307.16789", "toolllm", "ToolLLM: Facilitating LLMs to Master 16000+ Real-world APIs", "5"),
    ("2312.04511", "llm-compiler", "An LLM Compiler for Parallel Function Calling", "5"),
    # ---------- 第 6 章 规划 ----------
    ("2205.10625", "least-to-most", "Least-to-Most Prompting Enables Complex Reasoning", "6"),
    ("2210.02406", "decomposed-prompting", "Decomposed Prompting: A Modular Approach", "6"),
    # ---------- 第 7 章 记忆 ----------
    ("2005.11401", "rag", "Retrieval-Augmented Generation for Knowledge-Intensive NLP", "7"),
    ("2310.08560", "memgpt", "MemGPT: Towards LLMs as Operating Systems", "7"),
    ("2504.19413", "mem0", "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory", "7"),
    ("2304.03442", "generative-agents", "Generative Agents: Interactive Simulacra of Human Behavior", "7"),
    ("2309.02427", "coala", "Cognitive Architectures for Language Agents (CoALA)", "7"),
    # ---------- 第 8 章 上下文 ----------
    ("2307.03172", "lost-in-the-middle", "Lost in the Middle: How Language Models Use Long Contexts", "8"),
    ("2307.13854", "webarena", "WebArena: A Realistic Web Environment for Building Autonomous Agents", "10"),
    # ---------- 第 9 章 代码 ----------
    ("2107.03374", "codex-eval", "Evaluating Large Language Models Trained on Code", "9"),
    ("2402.01030", "codeact", "Executable Code Actions Elicit Better LLM Agents (CodeAct)", "9"),
    ("2405.15793", "swe-agent", "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", "9"),
    ("2305.16291", "voyager", "Voyager: An Open-Ended Embodied Agent with LLMs", "9"),
    ("2407.16741", "openhands", "OpenHands: An Open Platform for AI Software Developers", "9"),
    # ---------- 第 10 章 GUI ----------
    ("2207.01206", "webshop", "WebShop: Towards Scalable Real-World Web Interaction", "10"),
    ("2306.06070", "mind2web", "Mind2Web: Towards a Generalist Agent for the Web", "10"),
    ("2404.07972", "osworld", "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks", "10"),
    # ---------- 第 13 章 多 agent ----------
    ("2303.17760", "camel", "CAMEL: Communicative Agents for Mind Exploration", "13"),
    ("2308.08155", "autogen", "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", "13"),
    ("2308.00352", "metagpt", "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework", "13"),
    ("2307.07924", "chatdev", "ChatDev: Communicative Agents for Software Development", "13"),
    # ---------- 第 14 章 训练 ----------
    ("2203.14465", "star", "STaR: Bootstrapping Reasoning With Reasoning", "14"),
    ("2503.09516", "search-r1", "Search-R1: Training LLMs to Reason and Leverage Search Engines with RL", "14"),
    ("2504.11536", "retool", "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs", "14"),
    # ---------- 第 15 章 评测 ----------
    ("2308.03688", "agentbench", "AgentBench: Evaluating LLMs as Agents", "15"),
    ("2311.12983", "gaia", "GAIA: A Benchmark for General AI Assistants", "15"),
    ("2310.06770", "swe-bench", "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", "15"),
    ("2406.12045", "tau-bench", "τ-bench: A Benchmark for Tool-Agent-User Interaction", "15"),
    ("2412.14161", "the-agent-company", "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks", "15"),
    # ---------- 第 16 章 安全 ----------
    ("2302.12173", "prompt-injection-attacks", "Ignore Previous Prompt: Attack Techniques For Language Models", "16"),
    ("2306.05499", "indirect-prompt-injection", "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications", "16"),
    ("2309.15817", "toolemu", "Identifying the Risks of LM Agents with an LM-Emulated Sandbox (ToolEmu)", "16"),
    ("2406.13352", "agentdojo", "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks", "16"),
    # ---------- 综述与背景 ----------
    ("2308.11432", "survey-autonomous-agents", "A Survey on Large Language Model based Autonomous Agents", "1"),
    ("2309.07864", "rise-and-potential", "The Rise and Potential of LLM Based Agents: A Survey", "2"),
    ("2303.08774", "gpt4-technical-report", "GPT-4 Technical Report", "1"),
]
