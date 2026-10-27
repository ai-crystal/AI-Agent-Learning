# -*- coding: utf-8 -*-
"""运行 book/code/chNN/figures.py，生成 book/images/NN/ 下的插图。"""
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
CODE = ROOT / "book" / "code"
scripts = sorted(CODE.glob("ch*/figures.py"))
if not scripts:
    raise SystemExit("没有找到 book/code/ch*/figures.py")

for script in scripts:
    print(f"· {script.relative_to(ROOT)}")
    subprocess.run([sys.executable, str(script)], check=True)
print(f"完成：{len(scripts)} 个章节的插图已更新到 book/images/")
