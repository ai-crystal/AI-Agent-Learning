# -*- coding: utf-8 -*-
"""检查 GitHub 网页阅读所需的本地链接、插图和 PDF 是否存在。"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
PDF = ROOT / "output" / "book.pdf"
BOOK = ROOT / "book"
MD_FILES = [
    ROOT / "README.md",
    ROOT / "_sidebar.md",
    ROOT / "_coverpage.md",
    *sorted((BOOK / "front").glob("*.md")),
    *sorted((BOOK / "chapters").glob("*.md")),
    *sorted((BOOK / "appendix").glob("*.md")),
]

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


def main() -> int:
    errors: list[str] = []
    images = links = 0

    for md in MD_FILES:
        if not md.is_file():
            errors.append(f"缺少 Markdown 文件：{md.relative_to(ROOT)}")
            continue
        text = strip_code(md.read_text(encoding="utf-8"))
        for raw in IMAGE_RE.findall(text):
            target = local_target(raw)
            if target is None:
                continue
            images += 1
            path = (md.parent / target).resolve()
            if not path.is_file():
                errors.append(f"{md.relative_to(ROOT)} 图片不存在：{raw}")
            elif not path.is_relative_to(ROOT):
                errors.append(f"{md.relative_to(ROOT)} 图片跳到仓库外：{raw}")
        for raw in LINK_RE.findall(text):
            target = local_target(raw)
            if target is None:
                continue
            links += 1
            path = (md.parent / target).resolve()
            if not path.exists():
                errors.append(f"{md.relative_to(ROOT)} 链接目标不存在：{raw}")

    for required in (BOOK / "front", BOOK / "chapters", BOOK / "appendix",
                     BOOK / "images", BOOK / "code", BOOK / "build",
                     ROOT / "index.html", ROOT / "_sidebar.md",
                     ROOT / "_coverpage.md", ROOT / ".nojekyll", PDF):
        if not required.exists():
            errors.append(f"缺少必需路径：{required.relative_to(ROOT)}")

    if PDF.is_file():
        mb = PDF.stat().st_size / (1024 * 1024)
        print(f"PDF：{mb:.2f} MiB")
        if mb > 20:
            errors.append(f"PDF 超过 20 MiB：{mb:.2f} MiB")
    else:
        errors.append("缺少完整 PDF：output/book.pdf")

    print(f"检查 {len(MD_FILES)} 个 Markdown 文件，{images} 个本地图片，{links} 个本地链接。")
    if errors:
        print("\n发现问题：")
        for item in errors:
            print(" -", item)
        return 1
    print("PASS：章节、图片、链接和 PDF 均可用。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
