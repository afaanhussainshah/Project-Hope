import os
import sys
import time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(line_buffering=True)

standalone_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\standalone.html"
with open(standalone_path, "r", encoding="utf-8") as f:
    html = f.read()

out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\preview_frames"
os.makedirs(out_dir, exist_ok=True)

test_scenes = [
    (1.2, "new_01_hook_avg.jpg"),
    (5.0, "new_02_hook_sr_runs.jpg"),
    (14.5, "new_03_kohli_reveal.jpg"),
    (18.0, "new_04_wankhede_bow.jpg"),
    (26.8, "new_05_stump_shatter.jpg"),
    (30.0, "new_06_ahmedabad_silence.jpg"),
    (34.5, "new_07_heartbreak.jpg"),
    (41.5, "new_08_immortal_king.jpg")
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.set_content(html, wait_until="domcontentloaded")
    print("Page ready, capturing scene frames...")
    
    for t_val, fname in test_scenes:
        t0 = time.time()
        page.evaluate(f"window.__timelines['main'].seek({t_val}); void 0;")
        data = page.screenshot(type="jpeg", quality=85)
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "wb") as f:
            f.write(data)
        print(f"Captured {fname} at t={t_val}s ({len(data)} bytes) in {time.time() - t0:.2f}s")
        
    browser.close()
print("All 8 preview frames captured successfully!")
