import os
import time
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\amir-2017-ct"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
PREVIEWS_DIR = os.path.join(PROJECT_DIR, "preview_frames")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

with open(STANDALONE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

timestamps = [
    ("01_exile_bars.jpg", 1.2),
    ("02_return_2016.jpg", 5.0),
    ("03_the_oval_trio.jpg", 9.0),
    ("04_rohit_lbw_duck.jpg", 14.0),
    ("05_kohli_dropped.jpg", 16.8),
    ("06_kohli_out_shock.jpg", 20.5),
    ("07_stumps_demolished.jpg", 26.5),
    ("08_amir_eagle_redemption.jpg", 32.5),
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
