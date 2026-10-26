# -*- coding: utf-8 -*-
"""
把 book/*.md 编译成 PDF。

流程：Markdown -> HTML（本地 KaTeX 渲染公式）-> Chrome 打印 PDF
      -> 扫描标题所在页码回填目录 -> 二次打印 -> 合并封面 -> 加书签
用法：python build.py            正常编译
      python build.py --keep     保留中间文件
"""
import os, re, sys, shutil, glob, json, subprocess, html as htmlmod
import markdown
from pygments.formatters import HtmlFormatter

ROOT = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(ROOT, "build")
BOOK = os.path.join(ROOT, "book")
ASSETS = os.path.join(ROOT, "assets")
OUT_PDF = os.path.join(ROOT, "从语言模型到智能体.pdf")
TITLE = "从语言模型到智能体"
SUBTITLE = "AI Agent 的技术演进与工程实现"

os.makedirs(BUILD, exist_ok=True)

# ---------- 1. 准备 KaTeX 静态资源 ----------
def ensure_katex():
    dst = os.path.join(ASSETS, "katex")
    if os.path.isdir(dst) and os.path.exists(os.path.join(dst, "katex.min.js")):
        return
    src = os.path.join(ASSETS, "package", "dist")
    if not os.path.isdir(src):
        raise SystemExit("缺少 assets/katex，请检查 assets 目录")
    shutil.copytree(src, dst, dirs_exist_ok=True)

# ---------- 2. 读入章节 ----------
def load_chapters():
    files = sorted(glob.glob(os.path.join(BOOK, "*.md")))
    if not files:
        raise SystemExit("book/ 目录下没有 .md 文件")
    parts = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            parts.append(fh.read().strip())
    return parts

MD_EXT = ["extra", "def_list", "sane_lists", "toc", "md_in_html", "admonition",
          "codehilite", "pymdownx.arithmatex", "pymdownx.tilde",
          "pymdownx.smartsymbols", "legacy_attrs"]
MD_CFG = {
    "pymdownx.arithmatex": {"generic": True},
    "codehilite": {"guess_lang": False, "css_class": "codehilite", "use_pygments": True},
    "toc": {"permalink": False},
}

def md2html(text):
    return markdown.markdown(text, extensions=MD_EXT, extension_configs=MD_CFG)

# ---------- 3. 图片 -> figure，抽目录 ----------
HEAD_RE = re.compile(r"<h([12])\s+id=\"([^\"]*)\">(.*?)</h\1>", re.S)
IMG_P_RE = re.compile(r"<p>\s*(<img[^>]*>)\s*</p>", re.S)
ALT_RE = re.compile(r'alt="([^"]*)"')

def process_body(body):
    # 图片包裹成 figure + figcaption
    def repl(m):
        tag = m.group(1)
        alt = ALT_RE.search(tag)
        cap = alt.group(1) if alt else ""
        tag = re.sub(r'\s*alt="[^"]*"', "", tag)
        return ('<figure>' + tag + (f'<figcaption>{cap}</figcaption>' if cap else "") + '</figure>')
    body = IMG_P_RE.sub(repl, body)
    return body

def build_toc(body):
    heads = []
    for m in HEAD_RE.finditer(body):
        lvl = int(m.group(1))
        hid = m.group(2)
        txt = re.sub(r"<[^>]+>", "", m.group(3))
        heads.append((lvl, hid, txt))
    rows = []
    for i, (lvl, hid, txt) in enumerate(heads):
        rows.append(
            f'<div class="toc-item lv{lvl}"><span class="t">{htmlmod.escape(txt)}</span>'
            f'<span class="dots"></span><span class="pg" data-hid="{hid}"></span></div>'
        )
    return heads, "\n".join(rows)

# ---------- 4. 组装 HTML ----------
def page(title, body_html):
    katex = os.path.join(ASSETS, "katex")
    root = ROOT.replace(os.sep, "/")
    book_root = os.path.join(ROOT, "book").replace(os.sep, "/")
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<base href="file:///{book_root}/">
<title>{title}</title>
<link rel="stylesheet" href="file:///{katex.replace(os.sep,'/')}/katex.min.css">
<link rel="stylesheet" href="file:///{os.path.join(ROOT,'style.css').replace(os.sep,'/')}">
<style>{HtmlFormatter(style='xcode').get_style_defs('.codehilite')}
.codehilite {{ background: #f7f7f5; }}
</style>
<script src="file:///{katex.replace(os.sep,'/')}/katex.min.js"></script>
<script src="file:///{katex.replace(os.sep,'/')}/contrib/auto-render.min.js"></script>
</head><body>{body_html}
<script>
document.addEventListener("DOMContentLoaded", function () {{
  renderMathInElement(document.body, {{
    delimiters: [
      {{left: "$$", right: "$$", display: true}},
      {{left: "\\\\[", right: "\\\\]", display: true}},
      {{left: "\\\\(", right: "\\\\)", display: false}},
      {{left: "$", right: "$", display: false}}
    ],
    throwOnError: false,
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"]
  }});
  window.__mathDone = true;
}});
</script></body></html>"""

def render(html_path, pdf_path, footer=False, margin=None):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = None
        for ch in ("chrome", "msedge", None):
            try:
                browser = p.chromium.launch(channel=ch, args=["--font-render-hinting=none"])                     if ch else p.chromium.launch(args=["--font-render-hinting=none"])
                break
            except Exception:
                continue
        if browser is None:
            raise SystemExit("找不到可用的浏览器：请安装 Chrome 或 Edge，或运行 playwright install chromium")
        b = browser
        pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file:///" + html_path.replace(os.sep, "/"), wait_until="load")
        pg.wait_for_function("window.__mathDone === true", timeout=120000)
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(1200)
        opts = dict(path=pdf_path, width="170mm", height="240mm",
                    print_background=True,
                    margin=margin or {"top": "19mm", "bottom": "17mm", "left": "19mm", "right": "17mm"},
                    prefer_css_page_size=False)
        if footer:
            opts["display_header_footer"] = True
            opts["header_template"] = "<div></div>"
            opts["footer_template"] = (
                '<div style="width:100%;font-size:7.6pt;color:#666;font-family:serif;'
                'text-align:center;margin-top:4mm;"><span class="pageNumber"></span></div>')
        pg.pdf(**opts)
        b.close()

# ---------- 5. 回填目录页码 ----------
def norm(s):
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[，。、：；！？“”‘’（）()《》〈〉·—\-\.\,\:\;\"']", "", s)
    return s

def find_pages(pdf_path, heads):
    import fitz
    doc = fitz.open(pdf_path)
    texts = [norm(doc[i].get_text()) for i in range(len(doc))]
    # 正文起始页：包含「〖BODY〗」的页之后
    start = 0
    for i, t in enumerate(texts):
        if "〖BODY〗" in t:
            start = i
            break
    pages, ptr, missing = {}, start + 1, []
    for lvl, hid, txt in heads:
        key = norm(txt)
        found = None
        for L in (14, 10, 7, 5):
            k = key[:L]
            for i in range(ptr, len(texts)):
                if k and k in texts[i]:
                    found = i + 1
                    break
            if found:
                break
        if found:
            pages[hid] = found
            ptr = found - 1
        else:
            pages[hid] = pages.get(heads[max(0, len(pages)-1)][1], 1)
            missing.append(txt)
    doc.close()
    return pages, missing, start

# ---------- 6. 封面与封底 ----------
AUTHOR = "Dr. Dezeming"

COVER = """
<div style="position:relative;width:170mm;height:240mm;overflow:hidden;background:#04070e;">
  <img src="file:///{root}/assets/logo/cover.jpg"
       style="position:absolute;left:0;top:0;width:170mm;height:240mm;object-fit:cover;object-position:0% 45%;">
  <div style="position:absolute;left:0;top:0;width:170mm;height:240mm;
       background:linear-gradient(180deg,rgba(4,7,14,0.04) 0%,rgba(4,7,14,0.18) 30%,
       rgba(4,7,14,0.62) 48%,rgba(4,7,14,0.90) 60%,rgba(4,7,14,0.97) 72%,#04070e 88%);"></div>
  <div style="position:absolute;left:0;top:42%;width:170mm;height:34%;
       background:linear-gradient(180deg,rgba(4,7,14,0) 0%,rgba(4,7,14,0.55) 45%,
       rgba(4,7,14,0.80) 100%);"></div>
  <div style="position:absolute;left:13mm;top:13mm;width:144mm;height:214mm;
       border:0.5pt solid rgba(255,255,255,0.20);"></div>
  <div style="position:absolute;left:22mm;top:24mm;font-family:'Microsoft YaHei',sans-serif;
       font-size:8pt;letter-spacing:0.55em;color:#e5bd82;">AI AGENT</div>
  <div style="position:absolute;left:22mm;top:32mm;width:20mm;height:0.9pt;
       background:rgba(229,189,130,0.9);"></div>
  <div style="position:absolute;left:22mm;bottom:100mm;width:128mm;
       font-family:'SimSun',serif;font-size:33pt;font-weight:700;line-height:1.42;
       letter-spacing:0.06em;color:#ffffff;">{title}</div>
  <div style="position:absolute;left:22mm;bottom:78mm;width:124mm;
       font-family:'Microsoft YaHei',sans-serif;font-size:10.2pt;letter-spacing:0.16em;
       color:#c3d2e6;">{subtitle}</div>
  <div style="position:absolute;left:22mm;bottom:66mm;width:26mm;height:1.2pt;
       background:#e5bd82;"></div>
  <div style="position:absolute;left:22mm;bottom:42mm;width:122mm;
       font-family:'SimSun',serif;font-size:9pt;line-height:2.2;color:#9fb0c6;">
       从下一个词预测，到能在真实世界里连续工作数小时的智能体<br>
       十六章，一条从背景动机走到工程实现的路
  </div>
  <div style="position:absolute;left:22mm;bottom:22mm;font-family:'Microsoft YaHei',sans-serif;
       font-size:11pt;letter-spacing:0.1em;color:#e8eef7;">{author}</div>
  <div style="position:absolute;right:22mm;bottom:22mm;font-family:'Microsoft YaHei',sans-serif;
       font-size:8.4pt;letter-spacing:0.22em;color:#7d8ea6;">2026</div>
</div>
"""

BACK = """
<div style="position:relative;width:170mm;height:240mm;overflow:hidden;background:#04070e;">
  <img src="file:///{root}/assets/logo/back.jpg"
       style="position:absolute;left:0;top:0;width:170mm;height:240mm;object-fit:cover;object-position:62% 52%;">
  <div style="position:absolute;left:0;top:0;width:170mm;height:240mm;
       background:linear-gradient(180deg,rgba(4,7,14,0.99) 0%,rgba(4,7,14,0.99) 32%,
       rgba(4,7,14,0.96) 46%,rgba(4,7,14,0.82) 58%,rgba(4,7,14,0.42) 74%,
       rgba(4,7,14,0.16) 100%);"></div>
  <div style="position:absolute;left:13mm;top:13mm;width:144mm;height:214mm;
       border:0.5pt solid rgba(255,255,255,0.14);"></div>
  <div style="position:absolute;left:22mm;top:26mm;font-family:'Microsoft YaHei',sans-serif;
       font-size:8pt;letter-spacing:0.42em;color:#e5bd82;">关于本书</div>
  <div style="position:absolute;left:22mm;top:40mm;width:126mm;
       font-family:'SimSun',serif;font-size:12.2pt;line-height:1.95;color:#f2f6fb;">
       一个只会预测下一个词的模型，为什么不能直接拿来做事？<br>
       它缺的不是知识，而是反馈、状态和后果。
  </div>
  <div style="position:absolute;left:22mm;top:70mm;width:126mm;
       font-family:'SimSun',serif;font-size:9pt;line-height:2.05;color:#bccbdd;">
       这本书从 2020 年那个只会接着往下写的模型讲起，一路讲到今天可以连续工作几个小时的智能体。
       每补上一块缺口，就长出一代新技术：思维链让推理露在明处，ReAct 把思考和行动缝在一起，
       工具协议把接口固定下来，记忆与上下文决定它能走多远，代码和界面把动作真正落到世界上，
       harness 兜住失败，多 agent 与强化学习把它推向更长、更自主的任务。
  </div>
  <div style="position:absolute;left:22mm;top:118mm;width:126mm;
       font-family:'Microsoft YaHei',sans-serif;font-size:8.2pt;line-height:2.4;color:#8fa2b8;">
       推理与行动　·　记忆与上下文　·　工具与界面<br>
       Harness 与协作　·　训练、评测与安全
  </div>
  <div style="position:absolute;left:22mm;top:140mm;width:28mm;height:0.8pt;
       background:rgba(229,189,130,0.6);"></div>
  <div style="position:absolute;left:22mm;top:147mm;font-family:'Microsoft YaHei',sans-serif;
       font-size:10.4pt;letter-spacing:0.1em;color:#eef4fb;">{author}</div>
</div>
"""


def main():
    ensure_katex()
    chapters = load_chapters()
    raw = "\n\n".join(chapters)
    body = process_body(md2html(raw))
    heads, toc_rows = build_toc(body)

    toc_html = (
        '<div class="toc"><h1 style="break-before:auto">目录</h1>'
        f'<div class="toc-list">{toc_rows}</div></div>'
        '<div class="body-sentinel">〖BODY〗</div>'
    )
    full = toc_html + body

    p1 = os.path.join(BUILD, "body_pass1.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(page(TITLE, full))
    pdf1 = os.path.join(BUILD, "body_pass1.pdf")
    print("· 第一次排版 ...")
    render(p1, pdf1, footer=True)

    print("· 计算目录页码 ...")
    pages, missing, start = find_pages(pdf1, heads)
    if missing:
        print("  未能定位的标题：", missing[:6])

    def fill(m):
        hid = m.group(1)
        return f'<span class="pg" data-hid="{hid}">{pages.get(hid, "")}</span>'
    full2 = re.sub(r'<span class="pg" data-hid="([^"]*)"></span>', fill, full)
    # 哨兵只用于第一次排版定位正文起始页，不能进入最终 PDF。
    full2 = full2.replace('<div class="body-sentinel">〖BODY〗</div>', '')
    p2 = os.path.join(BUILD, "body.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(page(TITLE, full2))
    pdf2 = os.path.join(BUILD, "body.pdf")
    print("· 第二次排版 ...")
    render(p2, pdf2, footer=True)

    print("· 生成封面与封底 ...")
    root = ROOT.replace(os.sep, "/")
    zero = {"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
    pc = os.path.join(BUILD, "cover.html")
    with open(pc, "w", encoding="utf-8") as f:
        f.write(page(TITLE, COVER.format(root=root, title=TITLE, subtitle=SUBTITLE, author=AUTHOR)))
    pdfc = os.path.join(BUILD, "cover.pdf")
    render(pc, pdfc, footer=False, margin=zero)

    pb = os.path.join(BUILD, "back.html")
    with open(pb, "w", encoding="utf-8") as f:
        f.write(page(TITLE, BACK.format(root=root, author=AUTHOR)))
    pdfb = os.path.join(BUILD, "back.pdf")
    render(pb, pdfb, footer=False, margin=zero)

    print("· 合并并写入书签 ...")
    import fitz
    out = fitz.open()
    out.insert_pdf(fitz.open(pdfc))
    body_doc = fitz.open(pdf2)
    out.insert_pdf(body_doc)
    out.insert_pdf(fitz.open(pdfb))
    toc = [[1, TITLE, 1]]
    for lvl, hid, txt in heads:
        pg = pages.get(hid, 1) + 1  # 封面占一页
        toc.append([lvl, re.sub(r"<[^>]+>", "", txt), pg])
    out.set_toc(toc)
    out.set_metadata({"title": TITLE, "author": "许春晓",
                      "subject": SUBTITLE, "keywords": "AI Agent, LLM, ReAct, Harness"})
    target = OUT_PDF
    if "--out" in sys.argv:
        target = os.path.join(ROOT, sys.argv[sys.argv.index("--out") + 1])
    tmp = target + ".tmp"
    try:
        out.save(tmp, garbage=3, deflate=True)
        try:
            os.replace(tmp, target)
        except PermissionError:
            alt = target[:-4] + "(新).pdf"
            os.replace(tmp, alt)
            print("提示：%s 正被占用（可能开着阅读器），这次先存为 %s" % (target, alt))
            target = alt
    except Exception as e:
        out.close()
        raise SystemExit(
            "保存 PDF 失败：%s\n"
            "多半是这个文件正被阅读器占用。关掉已打开的 PDF 再编译一次即可。" % e)
    if os.path.exists(tmp):
        try:
            os.remove(tmp)
        except OSError:
            pass
    page_count = len(out)
    out.close()

    guard = os.path.join(ROOT, "tools", "pdf_size_guard.py")
    if os.path.exists(guard):
        result = subprocess.run([sys.executable, guard, target])
        if result.returncode != 0:
            raise SystemExit("PDF 体积检查未通过；请根据上面的提示压缩图片或减少插图。")

    print(f"完成：{target}  共 {page_count} 页")

    if "--keep" not in sys.argv:
        for f in (p1, pdf1):
            pass  # 保留中间产物，便于排查

if __name__ == "__main__":
    main()
