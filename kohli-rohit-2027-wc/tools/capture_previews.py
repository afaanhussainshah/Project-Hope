import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(line_buffering=True)

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-rohit-2027-wc")
html_path = base / "standalone.html"
out_dir = base / "preview_frames"
out_dir.mkdir(parents=True, exist_ok=True)

checkpoints = [
    (1.5, "01_hook_trophy_duo.jpg"),
    (4.5, "02_hook_real_question.jpg"),
    (7.0, "03_hook_doesnt_need_them_stamp.jpg"),
    (9.2, "04_age_cards_38_and_40.jpg"),
    (14.0, "05_odis_only_format.jpg"),
    (16.2, "06_no_promised_spot_stamp.jpg"),
    (19.0, "07_rohit_under_pressure_news.jpg"),
    (24.0, "08_rohit_century_vs_wi.jpg"),
    (27.5, "09_kohli_139_not_out.jpg"),
    (31.8, "10_kohli_74_auckland.jpg"),
    (36.0, "11_time_is_the_problem_stamp.jpg"),
    (38.5, "12_bcci_performance_decree.jpg"),
    (42.0, "13_sri_lanka_dec_13.jpg"),
    (44.5, "14_six_odis_audition.jpg"),
    (46.5, "15_should_india_pick_them.jpg"),
    (47.8, "16_cta_comment_yes_or_no.jpg"),
]

def main():
    t0 = time.time()
    html_content = html_path.read_text(encoding="utf-8")
    
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    
    print(f"[{time.time()-t0:.1f}s] Setting page content...")
    page.set_content(html_content, wait_until="domcontentloaded")
    print(f"[{time.time()-t0:.1f}s] Page ready. Capturing {len(checkpoints)} preview frames...")
    
    for t, name in checkpoints:
        t_frame = time.time()
        page.evaluate(f"window.__timelines.main.seek({t}); void 0;")
        out_file = out_dir / name
        page.screenshot(path=str(out_file), type="jpeg", quality=85)
        print(f"[{time.time()-t0:.1f}s] Captured {name} at {t:.2f}s in {time.time()-t_frame:.2f}s")
        
    browser.close()
    p.stop()
    print(f"All {len(checkpoints)} frames captured successfully in {time.time()-t0:.2f}s!")

if __name__ == "__main__":
    main()
