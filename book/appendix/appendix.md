# 附录 A 术语表

书里出现的英文术语按首字母排序，中文解释尽量落在“它在 agent 里具体指什么”，而不是词典定义。

A2A
: Agent2Agent，一套让不同来源的 agent 互相发现、委派任务、交换结果的协议。核心概念是 agent card 和 task 状态机。

ACI
: Agent-Computer Interface，agent 与计算机之间的接口设计。SWE-agent 用它指那套专门为模型设计的命令集，也泛指一切“模型怎么操作环境”的设计。

Agent loop
: agent 的主循环：组装上下文、调用模型、解析动作、执行、把结果写回上下文。

Agentic RL
: 用强化学习训练 agent 行为（工具调用、多步规划、长任务），区别于只训练单轮回答的 RLHF。

Chunking
: 把长文档切成小块以便检索。块的大小和重叠长度直接影响检索质量。

Compaction
: 上下文压缩。当上下文接近上限时，把较早的内容摘要或丢弃，腾出空间。

Context engineering
: 上下文工程。系统地决定每次调用时窗口里放什么、怎么排序、怎么替换，区别于只优化单句提示的提示工程。

CoT
: Chain-of-Thought，思维链。让模型在给出答案前写出中间推理步骤。

Function calling
: 函数调用。模型以结构化格式（通常是 JSON）输出要调用的工具名和参数，由宿主程序执行。

GRPO
: Group Relative Policy Optimization。一种强化学习算法，用同一问题的多次采样结果做组内比较来估计优势，不需要单独的价值网络。

Guardrail
: 护栏。在模型输出或工具执行前后加的检查，用于拦截不合规内容或危险动作。

Harness
: 模型之外承载 agent 的那套系统：循环、工具执行、上下文管理、权限、沙箱、日志、错误恢复。

Human-in-the-loop
: 人在回路。在关键节点引入人工确认或决策。

In-context learning
: 上下文学习。不改参数，只在提示里给例子，让模型照着做。

MCP
: Model Context Protocol，模型上下文协议。把工具、资源、提示模板标准化，使一个服务端可以被多个 agent 宿主复用。

Memory
: 记忆。在 agent 语境下通常指上下文之外的持久存储，包括情景记忆、语义记忆、程序记忆。

Pass@k / Pass^k
: 前者是跑 k 次至少成功一次的概率，衡量能力上限；后者是 k 次全部成功的概率，衡量稳定性。

Prompt injection
: 提示注入。把指令藏在 agent 会读到的数据里，诱导它执行非预期操作。间接注入指藏在网页、邮件、文档里的情况。

RAG
: Retrieval-Augmented Generation，检索增强生成。先从外部知识库检索相关片段，再让模型基于这些片段回答。

ReAct
: 一种把推理（Thought）和行动（Action）交替进行的范式，是现代 agent 循环的原型。

Reasoning model
: 推理模型。在回答前会生成长段内部思考的模型，通常用强化学习训练。

RLHF
: Reinforcement Learning from Human Feedback，基于人类反馈的强化学习。常见做法用人类偏好训练奖励模型，再做强化学习；完整指令对齐流程通常还包含监督微调（SFT）。

RLVR
: Reinforcement Learning with Verifiable Rewards。用可自动验证的奖励（答案对不对、测试过不过）做强化学习。

Rollout
: 在强化学习里指用当前策略完整跑一次任务，得到一条轨迹。

Sandbox
: 沙箱。限制代码执行范围的环境，通常隔离文件系统、网络和资源。

Scratchpad
: 草稿区。模型写中间推理的文本区域，通常不直接展示给用户。

Self-consistency
: 自洽性。采样多条推理路径，对最终答案投票。

Skill
: 技能。广义上指可复用的能力；在 Agent Skills 开放格式中，最小形态是含 `SKILL.md` 的目录，用名称、描述和操作流程告诉兼容宿主何时以及怎样完成工作，脚本、参考资料和模板可选。

SFT
: Supervised Fine-Tuning，监督微调。用输入—目标输出样本训练模型，让它模仿示范回答或轨迹。

Sub-agent
: 子 agent。由主 agent 派生的独立执行单元，有独立的上下文，只把结论返回。

System prompt
: 系统提示。每次调用都放在最前面的指令，定义角色、规则和输出格式。

Token
: 模型处理文本的基本单位，可能对应字、词或词片段；具体换算取决于模型的分词器，不能固定按“一个汉字多少 token”精确计算。

Tool
: 工具。模型可以请求调用的外部函数或动作，通常有名称、描述和参数 Schema；模型提出请求，宿主程序负责校验和执行。

Trajectory
: 轨迹。一次任务中所有的思考、动作、观察的完整记录。

Tree of Thoughts
: 思维树。把推理组织成树状搜索，允许分支、评估和回溯。

Verifier
: 验证器。判断一个结果是否正确的程序或模型，常用于评测和 RL 奖励。

JSON Schema
: 描述 JSON 数据形状和约束的规则格式，可规定字段、类型、必填项和枚举等；结构合法不代表内容真实。

Structured Outputs
: 结构化输出。广义指模型按 JSON、XML、代码等约定结构生成；在一些模型 API 中也特指基于 JSON Schema 的约束输出能力。

SDK
: Software Development Kit，软件开发工具包。模型 SDK 通常封装 API 请求、响应和数据类型，不一定包含完整 Agent 循环。

LangChain / LangGraph
: 前者提供较高层的模型、工具集成和 Agent 抽象；后者提供更低层的状态与流程编排、持久化和恢复能力。当前 LangChain 的 Agent 抽象构建在 LangGraph 之上，LangGraph 也可独立使用。

DOM
: Document Object Model，文档对象模型。浏览器把 HTML 元素组织成的树，GUI agent 可从中读取控件语义和位置。

CI
: Continuous Integration，持续集成。代码提交后自动运行构建、检查或测试的流程，也可用来运行 Agent 回归评测。


# 附录 B 延伸阅读

下面按章节列出相关的原始文献，括号里是论文在 arXiv 上的编号。这些论文按编号都能在 arXiv 上找到，随书资料里也存了一份。

读论文的建议是：先读摘要和图 1，判断它解决的问题你是否关心；再读方法部分，看它具体的做法；实验部分可以只挑和你场景接近的那一组看。不必按顺序读完，也不必读完每一篇。

**第 1 章 背景**

- *Language Models are Few-Shot Learners*（2005.14165），GPT-3 的论文，理解“规模带来的能力”的起点。
- *Training language models to follow instructions with human feedback*（2203.02155），InstructGPT，解释模型为什么会“听指令”。
- *MRKL Systems*（2205.00445），早期把工具路由和语言模型结合的构想。
- *A Survey on Large Language Model based Autonomous Agents*（2308.11432），一篇覆盖面很广的综述，适合建立整体印象。

**第 3 章 思维链**

- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*（2201.11903）
- *Self-Consistency Improves Chain of Thought Reasoning*（2203.11171）
- *Tree of Thoughts*（2305.10601）
- *Graph of Thoughts*（2308.09687）
- *Program of Thoughts Prompting*（2211.12588）
- *DeepSeek-R1*（2501.12948），看推理模型是怎么训练出来的。

**第 4 章 ReAct**

- *ReAct: Synergizing Reasoning and Acting in Language Models*（2210.03629）
- *ReWOO: Decoupling Reasoning from Observations*（2305.18323）
- *Plan-and-Solve Prompting*（2305.04091）

**第 5 章 工具**

- *Toolformer*（2302.04761）
- *WebGPT*（2112.09332）
- *Gorilla*（2305.15334）
- *ToolLLM*（2307.16789）
- *An LLM Compiler for Parallel Function Calling*（2312.04511）
- *Model Context Protocol* 规范

**第 6 章 规划与反思**

- *Least-to-Most Prompting*（2205.10625）
- *Decomposed Prompting*（2210.02406）
- *Self-Refine*（2303.17651）
- *Reflexion*（2303.11366）
- *Language Agent Tree Search*（2310.04406）

**第 7 章 记忆**

- *Retrieval-Augmented Generation*（2005.11401）
- *MemGPT*（2310.08560）
- *Mem0*（2504.19413）
- *Generative Agents*（2304.03442）
- *Cognitive Architectures for Language Agents*（2309.02427）

**第 8 章 上下文**

- *Lost in the Middle*（2307.03172）
- Anthropic 的工程文章 *Effective Context Engineering for AI Agents*
- [Agent Skills 开放格式与规范](https://agentskills.io/specification)
- [Claude Skills 使用说明](https://support.claude.com/en/articles/12512180-using-skills-in-claude)、[skills.sh 文档](https://skills.sh/docs)

**第 9 章 代码行动**

- *Evaluating Large Language Models Trained on Code*（2107.03374），Codex。
- *Executable Code Actions Elicit Better LLM Agents*（2402.01030），CodeAct。
- *SWE-agent*（2405.15793）
- *Voyager*（2305.16291）
- *OpenHands*（2407.16741）

**第 10 章 界面操作**

- *WebShop*（2207.01206）
- *Mind2Web*（2306.06070）
- *WebArena*（2307.13854）
- *OSWorld*（2404.07972）

**第 11 章 Harness**

- Anthropic 的工程文章 *Building Effective Agents*
- OpenAI 的 *A Practical Guide to Building Agents*

**第 12 章 生态与形态**

- *Agent2Agent* 协议规范
- *AGENTS.md* 的约定
- *Model Context Protocol* 规范
- [LangChain 官方概览](https://docs.langchain.com/oss/python/langchain/overview)
- [LangGraph 官方概览](https://docs.langchain.com/oss/python/langgraph/overview)
- [LlamaIndex Framework](https://developers.llamaindex.ai/python/framework/)

以上平台与框架链接于 2026 年 10 月核对；具体 API 和政策仍应查最新官方文档。

**第 13 章 多 Agent**

- *CAMEL*（2303.17760）
- *AutoGen*（2308.08155）
- *MetaGPT*（2308.00352）
- *ChatDev*（2307.07924）

**第 14 章 训练**

- *STaR*（2203.14465）
- *Search-R1*（2503.09516）
- *ReTool*（2504.11536）
- *ToolRL*（2504.13958）

**第 15 章 评测**

- *AgentBench*（2308.03688）
- *GAIA*（2311.12983）
- *SWE-bench*（2310.06770）
- *τ-bench*（2406.12045）
- *TheAgentCompany*（2412.14161）

**第 16 章 安全**

- *Not what you've signed up for*（2302.12173），间接提示注入的早期系统研究。
- *Prompt Injection attack against LLM-integrated Applications*（2306.05499）
- *Identifying the Risks of LM Agents with an LM-Emulated Sandbox*（2309.15817）
- *AgentDojo*（2406.13352）
- *Ignore This Title and HackAPrompt*（2311.16119），大规模提示攻击竞赛的总结。

# 附录 C 自己搭一个实验环境

搭建最小实验环境通常需要三样东西：Python、一个模型 API（或本地模型）、一个能限制命令和代码的执行环境。本地学习可以用配置适当的容器；“限定工作目录 + 命令白名单”只能降低一部分风险，**不能当作不受信代码的安全沙箱**，因为路径逃逸、子进程、网络和系统权限仍要处理。

如果想复现书里的实验，建议按这个顺序做：

先写一个只能调一个工具的循环（第二章那个最小实现），把它跑通，理解上下文是怎么增长的。然后加上文件读写和命令执行，观察 agent 在没有约束时会怎么“乱来”。接着加上上下文压缩，让它在跑五十步之后还能记住目标。最后加上权限层，看看哪些动作需要确认。

每加一层，都记一下它在哪些任务上变好了、哪些变差了。这个过程本身就是全书内容的压缩版。

至于模型的选择，看你的预算和任务类型。开放性的复杂任务用能力最强的模型，窄而重复的任务用便宜的小模型，两者都可以通过同一个接口切换。不要一开始就纠结选型，先让循环跑起来，再看瓶颈在哪里。
