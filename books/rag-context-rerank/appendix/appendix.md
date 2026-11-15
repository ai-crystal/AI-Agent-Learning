# 附录 A 术语与练习

## 术语表

RAG
: Retrieval-Augmented Generation，检索增强生成。先从外部知识源检索片段，再把片段作为证据交给模型生成答案。

Chunk
: 文档切分后的可检索单元。一个 chunk 应尽量表达一个完整意思，同时保留来源、章节和版本等元数据。

Embedding
: 把文本映射成向量。向量距离用来近似语义相关性，不等同于事实正确或答案有用。

ANN
: Approximate Nearest Neighbor，近似最近邻检索。用少量召回率换取大规模向量检索的速度和内存。

BM25
: 一种基于词频和逆文档频率的稀疏检索算法，擅长精确词、编号和专有名词匹配。

RRF
: Reciprocal Rank Fusion，倒数排名融合。按多个检索器的名次而不是原始分数合并结果，减少分数尺度不一致的问题。

Reranker
: 重排序模型。对召回候选逐对或逐条重新打分，通常比向量召回更贵，但能利用查询和文档的细粒度交互。

Recall@k
: 前 k 个结果中包含相关文档的比例。它衡量“有没有找到”，不衡量最终答案。

nDCG
: 归一化折损累计增益。考虑相关文档的位置，越靠前的高相关结果贡献越大。

Groundedness
: 答案是否由提供的证据支持。一个流畅、正确但引用不到证据的答案，在 RAG 评测中仍然不算合格。

## 练习

1. 取一份有标题层级的产品手册，分别用固定长度和标题感知方式切块。为十个小问题比较 Recall@5，并记录失败案例。
2. 找一组包含编号、否定句和表格的文档，比较 BM25、向量检索和混合检索的候选差异。不要只看总分，逐条看漏掉了什么。
3. 让重排序器把 30 个候选压到 8 个，记录延迟、token 成本和最终答案的依据率。
4. 为一个 8k 上下文窗口设计预算表：系统指令、用户问题、证据、输出各占多少 token？超过预算时先删除什么？
5. 构造一个“没有答案”的问题，检查系统是否会拒答，而不是把最相似的片段硬说成答案。

## 延伸阅读

- *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*（arXiv:2005.11401）
- *Dense Passage Retrieval for Open-Domain Question Answering*（arXiv:2004.04906）
- *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*（arXiv:2004.12832）
- *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*（arXiv:1908.10084）
- *Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs*（arXiv:1603.09320）
- *Lost in the Middle: How Language Models Use Long Contexts*（arXiv:2307.03172）
