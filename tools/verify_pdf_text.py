# -*- coding: utf-8 -*-
"""编译后自检：PDF 里的每一个标题都必须能被正确提取出来。

为什么需要它：Chrome 打印 PDF 时，变量字体（Noto *SC-VF 这类）无法被嵌入，
会被拆成一堆 Type3 字形；在长文档里偶尔会有几个字形拿到错的编码 ——
在页面上表现为标题变成乱码或缺字（例如「什么时u」）。这类故障不会报错，
只会出现在少数几个标题上，肉眼翻页很难全部发现，所以用脚本对比：
把 book/*.md 里的每个标题逐字拿到 PDF 文本层里查一遍。

用法：python tools/verify_pdf_text.py [pdf路径]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
DEFAULT_PDF = ROOT / "从语言模型到智能体.pdf"


def normalise(text: str) -> str:
    """比较用的归一化：去掉空白和常见标点，只留文字本身。"""
    text = re.sub(r"\s+", "", text)
    return re.sub(r"[，。、：；！？“”‘’（）()《》〈〉·—\-\.\,\:\;\"'|]", "", text)


def headings() -> list[tuple[int, str]]:
    found = []
    for path in sorted(BOOK.glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^(#{1,4})\s+(.*\S)\s*$", line)
            if match:
                text = re.sub(r"\s*\{:[^}]*\}\s*$", "", match.group(2)).strip()
                found.append((len(match.group(1)), text))
    return found


def quote_issues() -> list[str]:
    """中文引号必须成对：左引号“与右引号”在同一行里数量应当相等。

    写错方向（把右引号写成左引号）在浏览器里看起来只是个小斜杠，
    但印出来会变成两个开头引号，读者会以为句子没写完。
    """
    issues = []
    for path in sorted(BOOK.glob("*.md")):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                continue
            opens, closes = line.count("\u201c"), line.count("\u201d")
            if opens != closes:
                issues.append(f"{path.name}:{number}  左引号 {opens} 个 / 右引号 {closes} 个")
    return issues


def unfinished_paragraphs() -> list[str]:
    """长段落却没有句末标点：多半是写到一半断了。"""
    endings = ("。", "！", "？", "…", "”", "）", "|", ":", "：", "；", "-", "—",
               "\"", "'", "`", "*")  # 行内强调/代码/表格/公式的行尾不算异常
    suspects = []
    for path in sorted(BOOK.glob("*.md")):
        in_code = False
        paragraph: list[str] = []
        start = 0

        def flush() -> None:
            text = "".join(paragraph).strip()
            looks_math = any(mark in text for mark in ("$$", "\\lvert", "\\lVert", "\\ldots"))
            if (text and not looks_math and len(text) > 60
                    and not text.endswith(endings)
                    and not text.startswith(("#", "|", ">", "-", "*", "![", "<"))):
                suspects.append(f"{path.name}:{start}  {text[-30:]}")

        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
                flush(); paragraph = []
                continue
            if in_code:
                continue
            if not line.strip():
                flush(); paragraph = []
                continue
            if not paragraph:
                start = number
            paragraph.append(line.strip())
        flush()
    return suspects


def main() -> int:
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PDF
    if not pdf.is_file():
        raise SystemExit(f"找不到 PDF：{pdf}")
    document = pymupdf.open(pdf)
    joined = normalise("".join(page.get_text() for page in document))

    # Type3 是 Chrome 的"描边兜底"：出现就说明有字体没能被真正嵌入。
    type3_pages = [index + 1 for index, page in enumerate(document)
                   if any(entry[2] == "Type3" for entry in page.get_fonts())]
    # 控制字符 = 该字形没有 ToUnicode 映射，复制/搜索会得到乱码。
    broken_spans = [
        (index + 1, span["text"])
        for index, page in enumerate(document)
        for block in page.get_text("dict")["blocks"]
        for line in block.get("lines", [])
        for span in line["spans"]
        if any(ord(ch) < 32 for ch in span["text"])
    ]

    missing = [(level, text) for level, text in headings()
               if normalise(text) not in joined]

    print(f"PDF        : {pdf.name}（{len(document)} 页）")
    print(f"标题总数   : {len(headings())}")
    print(f"缺字/乱码  : {len(missing)}")
    for level, text in missing:
        print(f"   H{level}  {text}")
    print(f"Type3 页数 : {len(type3_pages)}"
          + (f"（前几页 {type3_pages[:8]}）" if type3_pages else "（全部字体内嵌正常）"))
    print(f"无映射字形 : {len(broken_spans)}")
    for page, text in broken_spans[:10]:
        print(f"   p{page}  {text!r}")

    quotes = quote_issues()
    print(f"引号不成对 : {len(quotes)}")
    for item in quotes:
        print(f"   {item}")

    unfinished = unfinished_paragraphs()
    if unfinished:
        print(f"疑似没写完 : {len(unfinished)}（仅提示，不影响判定）")
        for item in unfinished[:10]:
            print(f"   {item}")

    ok = not missing and not broken_spans and not type3_pages and not quotes
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
