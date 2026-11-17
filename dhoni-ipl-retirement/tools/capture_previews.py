import os
import time
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\dhoni-ipl-retirement"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
PREVIEWS_DIR = os.path.join(PROJECT_DIR, "preview_frames")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

with open(STANDALONE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

timestamps = [
    ("01_reporter_question.jpg", 3.5),
    ("02_last_season_yellow.jpg", 7.0),
    ("03_definitely_not_stamp.jpg", 11.5),
    ("04_until_today_strike.jpg", 13.6),
    ("05_five_trophies_dynasty.jpg", 18.5),
    ("06_busted_knees_warrior.jpg", 28.5),
    ("07_never_another_thala.jpg", 41.2),
    ("08_final_farewell_walkoff.jpg", 46.5),
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
