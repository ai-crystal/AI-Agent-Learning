# 构建与发布

本目录只放构建、检查、发布相关脚本和资源，站点正文在仓库根目录，书稿在 `book/`。

## 构建 PDF

依赖 Python 3.10+、Google Chrome 或 Microsoft Edge。首次安装：

```bash
python -m pip install -r book/build/requirements.txt
```

重新生成全部插图并构建 PDF：

```bash
python book/build/render_figures.py
python book/build/build.py
python book/build/checks/verify_pdf_text.py
python book/build/checks/verify_repo.py
```

Windows 也可以双击 `book/build/build_pdf.bat`。

构建流程会：

1. 读取 `book/front/`、`book/chapters/`、`book/appendix/`，合并成一份书稿；
2. 把正文引用的 PNG 转成构建用 JPEG，避免 PDF 直接嵌入原图；
3. 用 Chrome 打印、回填目录页码、合并封面封底并写入书签；
4. 对字体做子集化；
5. 输出 `output/book.pdf`，并执行 20 MiB 体积保护。超过上限时自动按 150/120/96 dpi 继续压缩内嵌图片，仍超限则构建失败。

## 目录约定

```text
book/front/           前言等前置辅文
book/chapters/        ch00.md … ch16.md，唯一一份章节 Markdown
book/appendix/        附录
book/images/NN/       第 NN 章插图，正文用 ../images/NN/xxx.png
book/code/chNN/       第 NN 章插图生成脚本
book/code/common/     共用绘图库
book/build/           构建脚本、检查脚本、KaTeX 与封面资源
output/book.pdf       构建产物
_private/             本地资料，不进入 Git
```

封面和封底由 `build.py` 生成，Docsify 的封面由根目录 `_coverpage.md` 提供；为避免重复，`book/front/` 只放实际存在的前言，不复制封面文字。

## 发布 GitHub Pages

1. 将仓库推送到 GitHub 的 `main` 分支。
2. 打开仓库 **Settings → Pages**。
3. Source 选择 **Deploy from a branch**。
4. 分支选择 `main`，目录选择 `/ (root)`，保存。
5. 访问 `https://<用户名>.github.io/<仓库名>/`。

根目录的 `index.html`、`_sidebar.md`、`_coverpage.md`、`README.md` 和 `.nojekyll` 构成 Docsify 站点；正文 Markdown 不会被复制，侧栏直接读取 `book/chapters/`。每次更新后重新构建 PDF、提交并推送，Pages 会立即刷新。

## 不上传的内容

`_private/` 已加入 `.gitignore`，用于本地写作记录、写作规范、下载的论文和原始大图。仓库只提交书稿、插图、绘图代码、站点和构建脚本。
