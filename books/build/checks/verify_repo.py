# -*- coding: utf-8 -*-
"""检查系列书站点的本地链接、插图、书稿和 PDF。"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
BOOKS = sorted(p for p in (ROOT / "books").iterdir() if (p / "book.json").is_file())
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.S)


def strip_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def local_target(raw: str):
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0].strip()
    target = re.sub(r"\s+['\"]?:ignore['\"]?$", "", target).strip()
    if not target or target.startswith(("#", "http://", "https://", "mailto:", "data:")):
        return None
    return unquote(target)


def resolve_target(md: Path, target: str) -> Path:
    """单册侧栏使用 books/ 开头的仓库绝对路径，其余链接相对当前 md。"""
    if target.startswith(("books/", "output/")):
        return (ROOT / target).resolve()
    return (md.parent / target).resolve()


def main() -> int:
    errors: list[str] = []
    images = links = 0
    required_root = [
        ROOT / "README.md", ROOT / "index.html", ROOT / "_sidebar.md",
        ROOT / "_coverpage.md", ROOT / ".nojekyll",
    ]
    for path in required_root:
        if not path.exists():
            errors.append(f"缺少站点文件：{path.relative_to(ROOT)}")

    md_files = [ROOT / "README.md", ROOT / "_sidebar.md", ROOT / "_coverpage.md"]
    for book in BOOKS:
        for name in ("README.md", "_sidebar.md", "structure.json"):
            p = book / name
            if name.endswith(".md") and p.is_file():
                md_files.append(p)
            if name == "structure.json" and not p.is_file():
                errors.append(f"缺少章节顺序文件：{p.relative_to(ROOT)}")
        for folder in ("front", "chapters", "appendix"):
            md_files.extend(sorted((book / folder).glob("*.md")))
        for folder in ("front", "chapters", "appendix"):
            if not (book / folder).exists():
                errors.append(f"缺少书稿目录：{(book / folder).relative_to(ROOT)}")
        cfg = json.loads((book / "book.json").read_text(encoding="utf-8"))
        pdf = ROOT / "output" / cfg.get("pdf", book.name + ".pdf")
        if not pdf.is_file():
            errors.append(f"缺少 PDF：{pdf.relative_to(ROOT)}")
        else:
            mb = pdf.stat().st_size / (1024 * 1024)
            print(f"PDF {book.name}: {mb:.2f} MiB")
            if mb > 20:
                errors.append(f"PDF 超过 20 MiB：{pdf.relative_to(ROOT)}")

    for md in md_files:
        if not md.is_file():
            errors.append(f"缺少 Markdown：{md.relative_to(ROOT)}")
            continue
        text = strip_code(md.read_text(encoding="utf-8"))
        for raw in IMAGE_RE.findall(text):
            target = local_target(raw)
            if target is None:
                continue
            images += 1
            path = resolve_target(md, target)
            if not path.is_file():
                errors.append(f"{md.relative_to(ROOT)} 图片不存在：{raw}")
            elif not path.is_relative_to(ROOT):
                errors.append(f"{md.relative_to(ROOT)} 图片跳到仓库外：{raw}")
        for raw in LINK_RE.findall(text):
            target = local_target(raw)
            if target is None:
                continue
            links += 1
            path = resolve_target(md, target)
            if not path.exists():
                errors.append(f"{md.relative_to(ROOT)} 链接目标不存在：{raw}")

    if not BOOKS:
        errors.append("books/ 下没有找到书籍配置")
    print(f"检查 {len(BOOKS)} 本书、{len(md_files)} 个 Markdown、{images} 个图片、{links} 个本地链接。")
    if errors:
        print("\n发现问题：")
        for item in errors:
            print(" -", item)
        return 1
    print("PASS：系列书稿、站点、图片、链接和 PDF 均可用。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
