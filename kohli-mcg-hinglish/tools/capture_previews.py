import os
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-mcg-hinglish"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
PREVIEWS_DIR = os.path.join(PROJECT_DIR, "preview_frames")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

checkpoints = [
    (0.8, "01_hook_28_runs.jpg"),
    (2.5, "02_sirf_8_balls.jpg"),
    (5.8, "03_lagbhag_namumkin.jpg"),
    (9.5, "04_mcg_target_160.jpg"),
    (14.2, "05_31_for_4_collapse.jpg"),
    (17.8, "06_khel_khatam.jpg"),
    (22.4, "07_kohli_refused_to_lose.jpg"),
    (27.8, "08_113_run_partnership.jpg"),
    (32.5, "09_time_khatam_crisis.jpg"),
    (38.2, "10_six_over_rauf_head.jpg"),
    (39.5, "11_another_six_flick.jpg"),
    (41.5, "12_match_wapas_aa_gaya.jpg"),
    (45.5, "13_82_off_53_stat.jpg"),
    (48.5, "14_diwali_fireworks_crown.jpg"),
    (51.2, "15_sabse_badi_innings_cta.jpg"),
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
