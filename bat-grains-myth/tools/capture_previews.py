import os
import time
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\bat-grains-myth"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
PREVIEWS_DIR = os.path.join(PROJECT_DIR, "preview_frames")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

with open(STANDALONE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

timestamps = [
    ("01_hook_waste_money.jpg", 3.0),
    ("02_grade1_card.jpg", 7.0),
    ("03_myth_or_fact.jpg", 12.2),
    ("04_tree_rings.jpg", 14.5),
    ("05_brittle_crack.jpg", 22.5),
    ("06_flexible_cannon.jpg", 31.0),
    ("07_balance_verdict.jpg", 36.0),
    ("08_cta_question.jpg", 39.5),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.set_content(html, wait_until="domcontentloaded")
    print("Page ready, capturing preview frames...")

    for fname, t in timestamps:
        t0 = time.time()
        page.evaluate(f"window.__timelines['main'].seek({t:.3f}); void 0;")
        out_path = os.path.join(PREVIEWS_DIR, fname)
        page.screenshot(path=out_path, type="jpeg", quality=85)
        dt = time.time() - t0
        print(f"Captured {fname} at t={t}s ({os.path.getsize(out_path)} bytes) in {dt:.2f}s")

    browser.close()

print("All preview frames captured successfully!")
