# ===== 一个能跑的最小 agent =====
# 整段代码只做四件事：定义工具、写系统提示、解析模型输出、跑循环。
import json   # 把 Action 里的 JSON 文本解析成 Python 字典
import re     # 用正则从模型输出里把 {...} 那段抠出来


# ---------- 1. 工具：一个会算数的函数 ----------
def calc(expr: str) -> str:
    """输入一个算术表达式，返回结果。
    返回值一律是字符串：它要被原样拼进上下文，作为模型
    下一步能读到的“观察结果”，而不是交给程序去用。
    """
    # eval() 可以执行任意 Python 代码，所以先用白名单把输入
    # 锁死：只允许数字、四则运算符、括号和空格。
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expr):
        return "错误：表达式包含非法字符"
    try:
        # 第二个参数把内置函数全部清空，即使输入里混进函数名
        # 也调不到任何东西；第三个参数是空的局部变量表。
        return str(eval(expr, {"__builtins__": {}}, {}))
    except Exception as e:
        # 除零、括号不配对等：把原因原样返回，模型下一轮
        # 看到这段文字，就知道该怎么改。
        return f"错误：{e}"


# 工具表。键是模型在 Action 里写的名字，值里两样东西：
#   fn   —— 真正被执行的函数
#   desc —— 给模型看的说明书（模型看不到代码，只能靠它猜用法）
TOOLS = {
    "calc": {
        "fn": calc,
        "desc": "计算一个算术表达式，例如 calc(expr='(12+8)*3')",
    },
}


# ---------- 2. 系统提示：规定输出格式 ----------
# 循环能不能转起来，全看这里定的格式。要点只有三条：
# 只允许两种输出；动作必须是合法 JSON；告诉它有哪些工具。
SYSTEM = """你是一个会用工具的助手。每一步只输出以下两种格式之一：

Thought: <你的推理>
Action: {"tool": "<工具名>", "args": {...}}

或者：

Thought: <你的推理>
Final Answer: <给用户的答复>

可用工具：
{tools}
"""
# 结尾的 {tools} 是占位符，请求前用字符串替换填进去（不能用
# format：提示词里本来就有 JSON 的花括号，会被当成占位符）


# ---------- 3. 解析：把一段文字变成“要做什么” ----------
def parse(text: str):
    """返回 (类型, 内容) 两元组：
       ("final", 答案文本)
       ("action", {"tool": ..., "args": {...}})
       ("error", 错误原因)
    """
    # 先看有没有最终答案。模型有可能既写了动作又写了答案，
    # 这时以答案为准，直接结束。
    if "Final Answer:" in text:
        return "final", text.split("Final Answer:", 1)[1].strip()

    # 用正则找 Action: 后面的那段 {...}。
    # re.S 让点号也能匹配换行，因为 JSON 可能写成多行。
    m = re.search(r"Action:\s*(\{.*\})", text, re.S)
    if m:
        try:
            return "action", json.loads(m.group(1))
        except json.JSONDecodeError:
            # 括号找到了，但里面不是合法 JSON：
            # 少逗号、引号没转义、多写了字，都会走到这里。
            return "error", "动作不是合法 JSON"

    # 两样都没找到，说明模型跑题了。
    return "error", "输出里既没有 Action 也没有 Final Answer"


# ---------- 4. 主循环：问 → 解析 → 执行 → 写回 ----------
def run(task: str, llm, max_steps: int = 6):
    # 把工具表摊平成几行文字，准备塞进系统提示的 {tools} 处
    tools_desc = "\n".join(
        f"- {k}: {v['desc']}" for k, v in TOOLS.items()
    )

    # 上下文从这里开始：一条系统提示、一条用户任务。
    # 之后每一轮都往这个列表里追加，模型看到的就是它全部。
    system_prompt = SYSTEM.replace("{tools}", tools_desc)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task},
    ]

    # 步数上限是保险丝：模型陷入死循环时，别让它无限烧钱
    for step in range(1, max_steps + 1):
        # ① 把整段上下文发给模型，拿到这一步的输出
        reply = llm(messages)

        # 模型说过的话也要进上下文，否则它下一轮不记得自己想过什么
        messages.append({"role": "assistant", "content": reply})

        # ② 看它想干什么
        kind, payload = parse(reply)

        # ③-1 它说做完了：把答案和历史一起返回
        if kind == "final":
            return payload, messages

        # ③-2 格式错了：把错误当成一条观察喂回去，让它自己改。
        # 注意 continue：格式错的时候不执行任何动作。
        if kind == "error":
            messages.append(
                {"role": "user", "content": f"格式错误：{payload}"}
            )
            continue

        # ③-3 要调工具：先按名字到表里查函数
        name = payload.get("tool")
        fn = TOOLS.get(name, {}).get("fn")

        if fn is None:
            # 名字对不上：不抛异常，而是把“没有这个工具”告诉模型，
            # 它会自己换一个。
            obs = f"错误：没有名为 {name} 的工具"
        else:
            try:
                # ** 把 {"expr": "18*7"} 展开成 calc(expr="18*7")
                obs = fn(**payload.get("args", {}))
            except TypeError as e:
                # 参数名写错、缺了必填项，同样作为观察返回
                obs = f"错误：参数不对（{e}）"

        # 工具结果以 user 身份写回上下文，模型下一轮就能看到
        messages.append(
            {"role": "user", "content": f"Observation: {obs}"}
        )

    # 循环正常走完，说明步数用光了
    return "达到步数上限，未完成", messages


# ---------- 5. 用一个假模型跑一遍 ----------
# 真实场景里 llm(messages) 是一次 API 请求；这里用一个
# 按顺序吐出台词的函数代替，方便离线观察循环怎么走。
script = [
    'Thought: 先算总价，再算单价。\n'
    'Action: {"tool": "calc", "args": {"expr": "18*7"}}',

    'Thought: 总价 126 元，现在算单价。\n'
    'Action: {"tool": "calc", "args": {"expr": "126/24"}}',

    'Thought: 单价 5.25 元，两问都有答案了。\n'
    'Final Answer: 7 箱共 126 元，平均每个 5.25 元。',
]

def mock_llm(messages):
    # 数一数上下文里有几条 assistant 消息，就知道当前是第几轮：
    # 第 1 轮返回 script[0]，第 2 轮返回 script[1]，依此类推。
    turn = len([m for m in messages if m["role"] == "assistant"])
    return script[turn]

# 跑起来：answer 是最终答案，history 是完整历史
answer, history = run("一箱苹果 24 个，每箱 18 元，买 7 箱要多少钱？"
                      "平均每个多少钱？", mock_llm)
print(answer)
