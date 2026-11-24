import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(line_buffering=True)

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\rcb-2016-vs-2026")
html_path = base / "standalone.html"
out_dir = base / "preview_frames"
out_dir.mkdir(parents=True, exist_ok=True)

checkpoints = [
    (1.5, "01_hook_faceoff.jpg"),
    (4.2, "02_hook_lightning_bolt.jpg"),
    (5.3, "03_hook_who_wins_stamp.jpg"),
    (6.5, "04_round1_batting_title.jpg"),
    (8.8, "05_gayle_ab_kohli_trio.jpg"),
    (11.5, "06_chinnaswamy_220.jpg"),
    (14.8, "07_advantage_2016_stamp.jpg"),
    (16.8, "08_round2_bowling_title.jpg"),
    (19.0, "09_bhuvi_hazlewood_attack.jpg"),
    (25.2, "10_wickets_shattered.jpg"),
    (27.0, "11_advantage_2026_stamp.jpg"),
    (29.2, "12_round3_chase_title.jpg"),
    (33.5, "13_tim_david_sr188.jpg"),
    (36.8, "14_chases_anything_stamp.jpg"),
    (39.5, "15_verdict_by_whisker.jpg"),
    (42.5, "16_depends_who_bats_first.jpg"),
    (45.8, "17_cta_comment_pick.jpg"),
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
