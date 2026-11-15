# -*- coding: utf-8 -*-
"""按 book.json 顺序构建 books/ 下的所有书。"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
build_script = ROOT / "build" / "build.py"
books = sorted(p for p in (ROOT / "books").iterdir() if (p / "book.json").is_file())
for book in books:
    slug = json.loads((book / "book.json").read_text(encoding="utf-8"))["slug"]
    print(f"\n=== {slug} ===")
    subprocess.run([sys.executable, str(build_script), "--book", slug], check=True)
