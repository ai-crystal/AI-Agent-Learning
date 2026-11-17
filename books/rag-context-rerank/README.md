# RAG 与上下文工程

**系列第二本 · 进阶**

> 把外部知识接进模型，再把合适的证据放进有限的上下文。

作者：Dr. Dezeming

[开始阅读：前言](front/preface.md)　·　<a href="../../output/rag-context-rerank.pdf" target="_blank" rel="noopener" data-router-ignore>下载完整 PDF</a>

第一本《从语言模型到智能体》回答的是“模型怎样从预测下一个词走到行动循环”；这一本换一个方向：当答案不在模型参数里，或者不能只靠参数回答时，系统怎样找到资料、判断资料是否相关、把证据组织进上下文，并对最终答案负责。

## 目录

### 第一部分 问题与链路

- [第 1 章 RAG 的问题边界](chapters/ch01.md)
- [第 2 章 一条完整的 RAG 链路](chapters/ch02.md)

### 第二部分 找到资料

- [第 3 章 文档解析与切块](chapters/ch03.md)
- [第 4 章 向量、嵌入与近似检索](chapters/ch04.md)
- [第 5 章 混合检索与查询改写](chapters/ch05.md)
- [第 6 章 重排序：把候选变成证据](chapters/ch06.md)

### 第三部分 把证据放进上下文

- [第 7 章 上下文组装与引用](chapters/ch07.md)
- [第 8 章 多轮对话与上下文管理](chapters/ch08.md)

### 第四部分 证明它真的有用

- [第 9 章 RAG 的评测](chapters/ch09.md)
- [第 10 章 生产系统与 Agentic RAG](chapters/ch10.md)

## 完整 PDF

<a href="../../output/rag-context-rerank.pdf" target="_blank" rel="noopener" data-router-ignore>下载 `output/rag-context-rerank.pdf`</a>

## 这本书不做什么

它不把 RAG 描述成某个产品的配置项，也不承诺“接上向量库就能回答准确”。书里的检索分数、延迟和成本示例除特别说明外都是教学估算，用来解释机制；真实系统必须在自己的语料和请求上测量。
