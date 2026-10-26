# 从语言模型到智能体

> 从下一个词预测，到能在真实世界里连续工作数小时的智能体。

作者：许春晓（Dr. Dezeming）

这是一本面向零前端、零后端、零机器学习基础读者的 AI Agent 技术书。全书从语言模型的能力边界讲起，逐步走到 ReAct、工具调用、记忆、上下文工程、代码与 GUI、Harness、多 Agent、训练、评测与安全。

**[开始阅读：前言](book/00-front.md)**　·　**[下载完整 PDF](./从语言模型到智能体.pdf)**

[![封面](assets/logo/cover.jpg)](./从语言模型到智能体.pdf)

## 在线阅读

GitHub 会直接渲染各章 Markdown 和书内插图。可以按顺序读，也可以从感兴趣的一章开始。

| 章节 | 内容 |
| --- | --- |
| [前言](book/00-front.md) | 本书想解决什么问题、给谁看 |
| [第 0 章](book/00b-primer.md) | 预备：进程、HTTP、JSON、API、CLI、沙箱、数据库、Token 等 |
| [第 1 章](book/01-ch01.md) | 预测下一个词，然后呢 |
| [第 2 章](book/02-ch02.md) | 一个 Agent 的最小骨架 |
| [第 3 章](book/03-ch03.md) | 让它先想再说：思维链及其家族 |
| [第 4 章](book/04-ch04.md) | ReAct：把推理和行动缠在一起 |
| [第 5 章](book/05-ch05.md) | 工具：从提示技巧到模型能力 |
| [第 6 章](book/06-ch06.md) | 规划、反思与自我修正 |
| [第 7 章](book/07-ch07.md) | 记忆：让 Agent 记住发生过什么 |
| [第 8 章](book/08-ch08.md) | 上下文工程 |
| [第 9 章](book/09-ch09.md) | 用代码行动 |
| [第 10 章](book/10-ch10.md) | 操作界面：浏览器与计算机 |
| [第 11 章](book/11-ch11.md) | Harness：模型外面那层壳 |
| [第 12 章](book/12-ch12.md) | 协议、平台与常驻 Agent |
| [第 13 章](book/13-ch13.md) | 多 Agent：协作的收益与代价 |
| [第 14 章](book/14-ch14.md) | 把 Agent 能力训练进模型 |
| [第 15 章](book/15-ch15.md) | 怎么知道它行不行 |
| [第 16 章](book/16-ch16.md) | 安全、可靠与还没解决的问题 |
| [附录](book/17-appendix.md) | 术语表、延伸阅读、实验环境 |

## 完整 PDF

仓库根目录的 [从语言模型到智能体.pdf](./从语言模型到智能体.pdf) 是排版后的完整版本，包含封面、目录页码、书签和全部插图。

在 GitHub 上打开该文件后，右上角有 **Download** 按钮；也可以把仓库克隆到本地后直接阅读。PDF 当前约 6.7 MB，构建流程会把体积上限控制在 **20 MiB** 以内。

## 仓库内容

```text
book/                 各章 Markdown；book/figures/ 是正文直接引用的插图
figures/              matplotlib 插图生成脚本
assets/katex/         离线公式渲染资源
assets/logo/          封面与封底图片
examples/             最小 agent 的可运行示例
tools/                构建自检、链接检查和 PDF 体积保护
build.py              Markdown -> HTML -> PDF
style.css             PDF 排版样式
从语言模型到智能体.pdf   可直接下载阅读的完整书稿
```

为了保持仓库轻量，以下内容**不进入 Git**：`build/` 编译中间产物、`papers/` 论文 PDF、`logo/` 原始大图、`assets/package/` 重复的 npm 包，以及 Python 缓存和本地环境文件。需要重新抓取论文时使用 `tools/fetch_papers.py`。

## 本地构建

需要 Python 3.10+、Google Chrome 或 Microsoft Edge。首次安装依赖：

```bash
python -m pip install -r requirements.txt
```

重新生成插图并编译 PDF：

```bash
python figures/figs_a.py
python figures/figs_b.py
python figures/figs_c.py
python build.py
```

Windows 也可以直接双击 `一键生成PDF.bat`。构建完成后会运行文字层自检，并自动执行 PDF 体积保护。

单独检查：

```bash
python tools/verify_pdf_text.py
python tools/pdf_size_guard.py --check
python tools/verify_repo.py
```

## 两个构建约束

**字体必须是静态字体。** 正文用宋体（SimSun），标题和强调用微软雅黑（Microsoft YaHei），代码用 Consolas。Chrome 无法正确嵌入 `*VF` 变量字体，会出现 Type3 字形和标题乱码；`tools/verify_pdf_text.py` 会检查这个问题。

**PDF 不得超过 20 MiB。** `build.py` 保存 PDF 后会调用 `tools/pdf_size_guard.py`。未超限时不做任何处理；超限时按 150/120/96 dpi 逐级重采样内嵌图片，仍无法压到 20 MiB 就中止并保留原文件。需要更低分辨率时，优先降低 `figures/` 里的图片生成 dpi，而不是删正文。

## 更新与发布

仓库维护步骤见 [PUBLISHING.md](PUBLISHING.md)。每次推送后，GitHub 的 **Actions → book-check** 会自动检查章节图片、相对链接和 PDF 体积。
