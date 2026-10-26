# -*- coding: utf-8 -*-
"""把书稿涉及的论文下载到 papers/，并用首页文本校验标题是否对得上。"""
import os, sys, subprocess, json, time
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from papers_list import PAPERS
import fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "papers")
os.makedirs(OUT, exist_ok=True)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

def fetch(pid, path):
    url = f"https://arxiv.org/pdf/{pid}"
    if os.path.exists(path) and os.path.getsize(path) > 40000:
        return True, "cached"
    for attempt in range(3):
        r = subprocess.run(["curl", "-sSL", "-m", "120", "-A", UA, "-o", path, url],
                           capture_output=True, text=True)
        if os.path.exists(path) and os.path.getsize(path) > 40000:
            return True, "ok"
        time.sleep(3)
    return False, "fail"

def first_page_text(path, n=700):
    try:
        d = fitz.open(path)
        t = d[0].get_text().replace("\n", " ")
        d.close()
        return " ".join(t.split())[:n]
    except Exception as e:
        return f"<unreadable: {e}>"

rows = []
for pid, slug, title, ch in PAPERS:
    fn = f"{slug}__{pid}.pdf"
    path = os.path.join(OUT, fn)
    ok, status = fetch(pid, path)
    head = first_page_text(path) if ok else ""
    rows.append({"id": pid, "file": fn, "title": title, "ch": ch, "ok": ok,
                 "size": os.path.getsize(path) if ok else 0, "head": head})
    print(f"[{ 'OK ' if ok else 'FAIL' }] {pid:14s} {slug:34s} {rows[-1]['size']//1024:6d}KB  {head[:70]}")

with open(os.path.join(OUT, "_check.json"), "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)

bad = [r for r in rows if not r["ok"]]
print(f"\n总计 {len(rows)} 篇，成功 {len(rows)-len(bad)}，失败 {len(bad)}")
for b in bad:
    print("  失败:", b["id"], b["title"])
