# -*- coding: utf-8 -*-
"""运行 books/*/code/chNN/figures.py，生成各书 images/NN/ 下的插图。"""
import argparse
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--book", help="只生成指定 slug 的插图")
args = parser.parse_args()
base = ROOT / "books"
if args.book:
    scripts = sorted((base / args.book).glob("code/ch*/figures.py"))
else:
    scripts = sorted(base.glob("*/code/ch*/figures.py"))
if not scripts:
    if args.book:
        print(f"{args.book} 没有插图脚本，跳过。")
        raise SystemExit(0)
    raise SystemExit("没有找到 books/*/code/ch*/figures.py")

for script in scripts:
    print(f"· {script.relative_to(ROOT)}")
    subprocess.run([sys.executable, str(script)], check=True)
print(f"完成：{len(scripts)} 个章节插图已更新到各自 book/images/")
