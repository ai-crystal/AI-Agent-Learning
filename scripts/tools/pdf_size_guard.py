# -*- coding: utf-8 -*-
"""保证最终 PDF 不超过体积上限；超限时重采样内嵌图片。

用法：
    python scripts/tools/pdf_size_guard.py               # 默认检查并尝试压缩主 PDF
    python scripts/tools/pdf_size_guard.py --check       # 只检查，不修改，超限返回 1
    python scripts/tools/pdf_size_guard.py path.pdf --limit 20
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PDF = ROOT / "从语言模型到智能体.pdf"
MIB = 1024 * 1024


def size_mib(path: Path) -> float:
    return path.stat().st_size / MIB


def optimize_once(src: Path, dst: Path, dpi_threshold: int, dpi_target: int,
                  quality: int) -> None:
    import pymupdf
    doc = pymupdf.open(src)
    try:
        doc.rewrite_images(
            dpi_threshold=dpi_threshold,
            dpi_target=dpi_target,
            quality=quality,
            lossy=True,
            lossless=True,
            bitonal=True,
            color=True,
            gray=True,
        )
        doc.save(dst, garbage=4, deflate=True)
    finally:
        doc.close()


def optimize(src: Path, limit_mib: float) -> bool:
    """先轻度重采样，再逐步加强；保留原文件，成功后才原子替换。"""
    print(f"PDF 超过 {limit_mib:g} MiB，尝试压缩内嵌图片 ...")
    attempts = [
        (200, 150, 84),
        (160, 120, 78),
        (130, 96, 72),
    ]
    best: tuple[float, Path] | None = None
    for threshold, target, quality in attempts:
        tmp = src.with_name(src.stem + f".opt-{target}.pdf")
        try:
            optimize_once(src, tmp, threshold, target, quality)
        except Exception as exc:
            print(f"  压缩尝试失败（目标 {target} dpi）：{exc}")
            if tmp.exists():
                tmp.unlink()
            continue
        mb = size_mib(tmp)
        print(f"  {target} dpi / quality {quality}: {mb:.2f} MiB")
        if best is None or mb < best[0]:
            if best and best[1].exists():
                best[1].unlink()
            best = (mb, tmp)
        else:
            tmp.unlink()

    if best is None or best[0] > limit_mib:
        if best and best[1].exists():
            best[1].unlink()
        print(f"[失败] 压缩后仍超过 {limit_mib:g} MiB，请减少插图或降低图片生成 dpi。")
        return False

    backup_dir = ROOT / "build"
    backup_dir.mkdir(exist_ok=True)
    backup = backup_dir / (src.stem + ".before_optimize.pdf")
    shutil.copy2(src, backup)
    os.replace(best[1], src)
    print(f"[完成] 已压缩到 {size_mib(src):.2f} MiB；压缩前副本：{backup}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="检查并保护 PDF 的 20 MiB 体积上限")
    parser.add_argument("pdf", nargs="?", default=str(DEFAULT_PDF))
    parser.add_argument("--limit", type=float, default=20.0, help="上限，单位 MiB")
    parser.add_argument("--check", action="store_true", help="只检查，不修改 PDF")
    args = parser.parse_args()

    pdf = Path(args.pdf)
    if not pdf.is_file():
        print(f"找不到 PDF：{pdf}")
        return 2

    mb = size_mib(pdf)
    print(f"PDF 体积：{mb:.2f} MiB / 上限 {args.limit:g} MiB")
    if mb <= args.limit:
        return 0
    if args.check:
        print("[失败] PDF 超过体积上限。")
        return 1
    return 0 if optimize(pdf, args.limit) else 1


if __name__ == "__main__":
    sys.exit(main())
