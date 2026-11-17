import os
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\index.html")
out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\preview_frames"
os.makedirs(out_dir, exist_ok=True)

test_times = [
    (1.0, "s1_battles.jpg"),
    (8.2, "s1_untouchable.jpg"),
    (13.0, "s2_wankhede.jpg"),
    (16.5, "s2_sachin_bow.jpg"),
    (21.0, "s2_765runs.jpg"),
    (34.5, "s3_bowling.jpg"),
    (37.5, "s3_chop_on.jpg"),
    (40.5, "s3_silence.jpg"),
    (52.0, "s4_heartbreak.jpg"),
    (63.0, "s5_crown.jpg"),
    (69.0, "s5_immortal.jpg"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_timeout(1000)

    for t, fname in test_times:
        page.evaluate(f"window.__timelines['main'].seek({t})")
        out_path = os.path.join(out_dir, fname)
        page.screenshot(path=out_path, type="jpeg", quality=85)
        print(f"Captured {fname} at t={t}s -> {out_path}")

    browser.close()
print("Preview captures done!")
