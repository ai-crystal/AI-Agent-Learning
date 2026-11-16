# 构建与发布

本目录放系列书共用的构建、检查、发布脚本和资源。书稿在各书的 `books/<slug>/` 中。

## 构建单本书

依赖 Python 3.10+、Google Chrome 或 Microsoft Edge。首次安装：

```bash
python -m pip install -r build/requirements.txt
```

每本书有自己的构建入口：

```text
books/ai-agent-foundations/build.bat
books/rag-context-rerank/build.bat
```

双击其中一个，只会处理对应书籍，不会重新编译整个系列。命令行等价操作：

```bash
# 第一本
python build/render_figures.py --book ai-agent-foundations
python build/build.py --book ai-agent-foundations
python build/checks/verify_pdf_text.py --book ai-agent-foundations

# 第二本（没有插图脚本时会自动跳过插图）
python build/render_figures.py --book rag-context-rerank
python build/build.py --book rag-context-rerank
python build/checks/verify_pdf_text.py --book rag-context-rerank
```

站点链接检查可独立运行：

```bash
python build/checks/verify_repo.py
```

构建流程会：

1. 读取每本书的 `front/`、`chapters/`、`appendix/`；
2. 把正文引用的 PNG 转成构建用 JPEG；
3. 用 Chrome 打印、回填目录页码、合并封面封底并写入书签；
4. 对字体做子集化；
5. 输出到对应书籍的 `output/<pdf>`，并执行 20 MiB 体积保护。超过上限时按 150/120/96 dpi 继续压缩内嵌图片，仍超限则构建失败。

## 目录约定

```text
books/<slug>/book.json       书名、副标题、PDF 文件名
books/<slug>/README.md       该书 landing page
books/<slug>/build.bat       只构建该书的入口
books/<slug>/front/          前言等前置辅文
books/<slug>/chapters/       chNN.md，唯一一份章节 Markdown
books/<slug>/appendix/       附录
books/<slug>/images/NN/      第 NN 章插图，正文用 ../images/NN/xxx.png
books/<slug>/code/chNN/      第 NN 章插图生成脚本
books/<slug>/code/common/    共用绘图库
books/<slug>/output/         该书的 PDF
build/                       系列共用构建、检查、KaTeX 与封面资源
build/build_book.bat         单书批处理的共用逻辑
_private/                    本地资料，不进入 Git
```

新增一本书：复制一个 `book.json` 和目录骨架，按同样的结构放入 `front/`、`chapters/`、`appendix/`。根目录 Docsify 侧栏加入书籍入口后，构建脚本会自动发现它。

封面和封底由 `build/build.py` 生成，系列 Docsify 封面由根目录 `_coverpage.md` 提供；书稿里的 `front/` 只放实际存在的前言等文本，不复制封面文字。

## 发布 GitHub Pages

1. 将仓库推送到 GitHub 的 `main` 分支。
2. 打开仓库 **Settings → Pages**。
3. Source 选择 **Deploy from a branch**。
4. 分支选择 `main`，目录选择 `/ (root)`，保存。
5. 访问 `https://<用户名>.github.io/<仓库名>/`。

根目录的 `index.html`、`_sidebar.md`、`_coverpage.md`、`README.md` 和 `.nojekyll` 构成系列 Docsify 站点；正文 Markdown 不会被复制。每次更新后重新构建、提交并推送，Pages 会刷新。

## 不上传的内容

`_private/` 已加入 `.gitignore`，用于本地写作记录、写作规范、下载的论文和原始大图。仓库只提交书稿、插图、绘图代码、站点和构建脚本。
