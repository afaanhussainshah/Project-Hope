import os
import time
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\imran-khan-two-legends"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
PREVIEWS_DIR = os.path.join(PROJECT_DIR, "preview_frames")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

with open(STANDALONE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

timestamps = [
    ("01_hook_bumrah_or_smith.jpg", 2.5),
    ("02_hook_trick_question.jpg", 6.2),
    ("03_bumrah_yorker_survive.jpg", 18.0),
    ("04_smith_unstoppable.jpg", 29.1),
    ("05_impossible_fusion.jpg", 34.8),
    ("06_imran_khan_stats.jpg", 41.2),
    ("07_imran_1992_world_cup.jpg", 45.2),
    ("08_finale_carried_both.jpg", 51.4),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.set_content(html, wait_until="domcontentloaded")
    page.evaluate("document.fonts.ready")
    print("Page ready, capturing preview frames...")

    for fname, t in timestamps:
        t0 = time.time()
        page.evaluate(f"window.__timelines['main'].seek({t:.3f}); void 0;")
        out_path = os.path.join(PREVIEWS_DIR, fname)
        page.screenshot(path=out_path, type="jpeg", quality=88)
        dt = time.time() - t0
        print(f"Captured {fname} at t={t}s ({os.path.getsize(out_path)} bytes) in {dt:.2f}s")

    browser.close()

print("All preview frames captured successfully!")
