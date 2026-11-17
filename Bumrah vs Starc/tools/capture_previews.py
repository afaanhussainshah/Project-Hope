import os
import time
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\Bumrah vs Starc"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
PREVIEWS_DIR = os.path.join(PROJECT_DIR, "preview_frames")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

with open(STANDALONE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

timestamps = [
    ("01_hook_toe_to_toe.jpg", 3.5),
    ("02_who_is_deadlier_stamp.jpg", 10.0),
    ("03_round1_opening_average.jpg", 14.5),
    ("04_round1_bumrah_point.jpg", 19.3),
    ("05_round2_starc_ball1_stumps.jpg", 25.5),
    ("06_round3_pink_ball_floodlights.jpg", 34.0),
    ("07_round4_h2h_deadlock.jpg", 44.5),
    ("08_tiebreaker_dead_heat.jpg", 54.0),
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
