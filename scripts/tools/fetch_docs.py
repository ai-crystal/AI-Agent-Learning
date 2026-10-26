# -*- coding: utf-8 -*-
"""把关键的网页资料（博客、规范）打印成 PDF，放进 assets/.local/papers/。"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                   "assets", ".local", "papers")
DOCS = [
    ("doc-anthropic-building-effective-agents.pdf", "https://www.anthropic.com/engineering/building-effective-agents"),
    ("doc-anthropic-context-engineering.pdf", "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"),
    ("doc-mcp-specification.pdf", "https://modelcontextprotocol.io/specification/2025-06-18"),
    ("doc-openai-practical-guide-building-agents.pdf", "https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf"),
    ("doc-agents-md.pdf", "https://agents.md/"),
    ("doc-a2a-protocol.pdf", "https://a2a-protocol.org/latest/specification/"),
]

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    for fn, url in DOCS:
        path = os.path.join(OUT, fn)
        try:
            pg = b.new_page(viewport={"width": 1280, "height": 1600})
            pg.goto(url, wait_until="networkidle", timeout=60000)
            pg.wait_for_timeout(1500)
            if url.endswith(".pdf"):
                r = pg.request.get(url)
                open(path, "wb").write(r.body())
            else:
                pg.pdf(path=path, format="A4", print_background=True,
                       margin={"top": "16mm", "bottom": "16mm", "left": "14mm", "right": "14mm"},
                       display_header_footer=True, header_template="<div></div>",
                       footer_template='<div style="width:100%;font-size:8px;color:#888;text-align:center;'
                                       'font-family:sans-serif;"><span class="pageNumber"></span>/<span class="totalPages"></span></div>')
            print("OK  ", fn, os.path.getsize(path) // 1024, "KB")
            pg.close()
        except Exception as e:
            print("FAIL", fn, repr(e)[:120])
    b.close()
