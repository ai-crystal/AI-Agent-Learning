# -*- coding: utf-8 -*-
"""逐本检查 PDF 的标题、字体、引号和段落完整性。"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
BOOKS = ROOT / "books"


def content_files(book: Path) -> list[Path]:
    files: list[Path] = []
    for folder in ("front", "chapters", "appendix"):
        files.extend(sorted((book / folder).glob("*.md")))
    return files


def normalise(text: str) -> str:
    text = re.sub(r"\s+", "", text)
    return re.sub(r"[，。、：；！？“”‘’（）()《》〈〉·—\-\.\,\:\;\"'|]", "", text)


def headings(book: Path) -> list[tuple[int, str]]:
    found = []
    for path in content_files(book):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^(#{1,4})\s+(.*\S)\s*$", line)
            if match:
                text = re.sub(r"\s*\{:[^}]*\}\s*$", "", match.group(2)).strip()
                found.append((len(match.group(1)), text))
    return found


def quote_issues(book: Path) -> list[str]:
    issues = []
    for path in content_files(book):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                continue
            opens, closes = line.count("\u201c"), line.count("\u201d")
            if opens != closes:
                issues.append(f"{path.relative_to(ROOT)}:{number}  左引号 {opens} / 右引号 {closes}")
    return issues


def unfinished_paragraphs(book: Path) -> list[str]:
    endings = ("。", "！", "？", "…", "”", "）", "|", ":", "：", "；", "-", "—",
               "\"", "'", "`", "*")
    suspects = []
    for path in content_files(book):
        in_code = False
        paragraph: list[str] = []
        start = 0

        def flush() -> None:
            text = "".join(paragraph).strip()
            looks_math = any(mark in text for mark in ("$$", "\\lvert", "\\lVert", "\\ldots"))
            if (text and not looks_math and len(text) > 60
                    and not text.endswith(endings)
                    and not text.startswith(("#", "|", ">", "-", "*", "![", "<"))):
                suspects.append(f"{path.relative_to(ROOT)}:{start}  {text[-30:]}")

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


def check_book(book: Path) -> tuple[bool, dict]:
    import json
    config = json.loads((book / "book.json").read_text(encoding="utf-8"))
    pdf = book / "output" / config.get("pdf", book.name + ".pdf")
    if not pdf.is_file():
        print(f"[{book.name}] 缺少 PDF：{pdf.relative_to(ROOT)}")
        return False, {}
    document = pymupdf.open(pdf)
    joined = normalise("".join(page.get_text() for page in document))
    type3_pages = [index + 1 for index, page in enumerate(document)
                   if any(entry[2] == "Type3" for entry in page.get_fonts())]
    broken = [
        (index + 1, span["text"])
        for index, page in enumerate(document)
        for block in page.get_text("dict")["blocks"]
        for line in block.get("lines", [])
        for span in line.get("spans", [])
        if any(ord(ch) < 32 for ch in span["text"])
    ]
    hs = headings(book)
    missing = [(level, text) for level, text in hs if normalise(text) not in joined]
    quotes = quote_issues(book)
    unfinished = unfinished_paragraphs(book)
    ok = not missing and not broken and not type3_pages and not quotes
    print(f"\n[{book.name}] {pdf.name}（{len(document)} 页，{len(hs)} 标题）")
    print(f"  缺字/乱码 {len(missing)}；Type3 {len(type3_pages)}；无映射字形 {len(broken)}；引号问题 {len(quotes)}")
    for item in missing[:5]:
        print("   缺标题：", item)
    for item in quotes[:5]:
        print("   引号：", item)
    if unfinished:
        print(f"  未完成段落提示：{len(unfinished)}（仅提示）")
    return ok, {"pages": len(document), "headings": len(hs), "missing": missing,
                "type3": type3_pages, "broken": broken, "quotes": quotes}


def main() -> int:
    if "--book" in sys.argv:
        selected = [BOOKS / sys.argv[sys.argv.index("--book") + 1]]
    else:
        selected = sorted(p for p in BOOKS.iterdir() if (p / "book.json").is_file())
    all_ok = True
    for book in selected:
        ok, _ = check_book(book)
        all_ok = all_ok and ok
    print("\nPASS" if all_ok else "\nFAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
