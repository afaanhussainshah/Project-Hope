import os
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-31-for-4"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
PREVIEWS_DIR = os.path.join(PROJECT_DIR, "preview_frames")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

checkpoints = [
    (1.2, "01_hook_31_for_4.jpg"),
    (4.6, "02_except_one_man.jpg"),
    (8.2, "03_mcg_target_160.jpg"),
    (11.5, "04_top_order_collapse.jpg"),
    (14.8, "05_unbearable_pressure.jpg"),
    (22.0, "06_113_run_stand.jpg"),
    (25.2, "07_19th_over_crisis.jpg"),
    (29.0, "08_six_over_rauf_head.jpg"),
    (32.8, "09_two_sixes_banner.jpg"),
    (38.2, "10_82_off_53_stat.jpg"),
    (42.8, "11_king_kohli_crown.jpg"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.goto(f"file:///{STANDALONE_HTML.replace(os.sep, '/')}", wait_until="domcontentloaded")
    page.evaluate("document.fonts.ready")

    for t, filename in checkpoints:
        page.evaluate(f"window.__timelines['main'].seek({t}); void 0;")
        out_path = os.path.join(PREVIEWS_DIR, filename)
        page.screenshot(path=out_path, type="jpeg", quality=90)
        print(f"Captured {filename} at t={t}s")

    browser.close()

print("All preview frames captured successfully!")
