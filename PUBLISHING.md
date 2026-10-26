# 发布到 GitHub

这个仓库已经按“GitHub 网页直接读 Markdown + 根目录直接下载 PDF”的方式整理，根目录只有 `book/`、`assets/`、`scripts/` 三个内容目录。下面是首次发布和后续更新步骤。

## 1. 在 GitHub 创建空仓库

登录 GitHub，点 **New repository**：

- 仓库名示例：`llm-to-agent-book`
- 可见性按需要选择 Public 或 Private
- **不要**勾选 Add a README、Add .gitignore 或 Choose a license

创建后复制仓库地址，例如：

```text
https://github.com/你的用户名/llm-to-agent-book.git
```

## 2. 在本项目目录推送

项目已经完成本地 Git 初始化和首次提交。打开终端：

```bat
cd /d E:\Study\AIAgent技术
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

如果提示 `remote origin already exists`，说明之前加过远程地址，改用：

```bat
git remote set-url origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

GitHub 不再接受账户密码作为 Git 密码。弹窗登录失败时，可以使用 Git Credential Manager，或创建一个 Personal Access Token（Fine-grained token，至少给目标仓库 Contents 读写权限），在要求密码时粘贴 token。

如果本机还没有配置提交身份：

```bat
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

## 3. 推送后在哪里看

1. 打开仓库主页，README 就是在线阅读入口。
2. 点“在线阅读”表格里的章节，GitHub 会直接渲染 Markdown、公式和 `book/figures/` 里的插图。
3. 点根目录的 `从语言模型到智能体.pdf`，在 GitHub 的 PDF 查看器右上角点 **Download**。

GitHub 网页渲染是即时的，不需要额外部署。若浏览器仍显示旧内容，强制刷新一次（`Ctrl+F5`）。

## 4. 以后更新

改完正文、图片或 PDF 后：

```bat
cd /d E:\Study\AIAgent技术
git status
git add -A
git commit -m "更新书稿"
git push
```

如果只想重新生成书：

```bat
python scripts\figures\figs_a.py
python scripts\figures\figs_b.py
python scripts\figures\figs_c.py
python build.py
python scripts\tools\verify_pdf_text.py
python scripts\tools\verify_repo.py
```

`build.py` 会自动执行 `scripts/tools/pdf_size_guard.py`。PDF 超过 20 MiB 时会先尝试压缩内嵌图片；仍然超限则构建失败，不会把超限 PDF 当成成功结果。

## 5. 哪些文件不会上传

`.gitignore` 已排除：

```text
assets/.local/build/       编译中间文件和测试 PDF
assets/.local/papers/      论文原始 PDF，约 274 MB
assets/.local/source-logo/ 封面用原始大图，约 17 MB
assets/.local/package/     重复的 KaTeX npm 包
assets/.local/katex.tgz    KaTeX 压缩包
__pycache__/               Python 缓存
```

这些文件仍保留在本地，不影响构建。不要用 `git add -f` 强行加入；GitHub 单文件限制为 100 MB，而本书要求最终 PDF 不超过 20 MiB。

## 6. 如果 PDF 被占用

构建时若 PDF 正在阅读器中打开，`build.py` 会退让生成 `从语言模型到智能体(新).pdf`。关掉阅读器后重新运行即可覆盖正式文件。不要把 `(新).pdf` 上传到仓库，`.gitignore` 已排除它。
