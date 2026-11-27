import os
import sys
import time
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(line_buffering=True)

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kookaburra-sg-dukes")
html_path = base / "standalone.html"
out_dir = base / "preview_frames"
out_dir.mkdir(parents=True, exist_ok=True)

checkpoints = [
    (0.1, "00_first_frame.jpg"),
    (2.5, "01_hook_three_balls.jpg"),
    (5.8, "02_hook_changes_everything_stamp.jpg"),
    (8.8, "03_kookaburra_spotlight.jpg"),
    (10.8, "04_sg_spotlight.jpg"),
    (13.0, "05_dukes_spotlight.jpg"),
    (15.5, "06_home_board_rule.jpg"),
    (18.5, "07_visiting_teams_struggle.jpg"),
    (21.0, "08_kookaburra_goes_soft.jpg"),
    (24.5, "09_sg_reverses_and_grips.jpg"),
    (27.5, "10_dukes_seams_longer.jpg"),
    (30.5, "11_what_if_one_ball.jpg"),
    (33.5, "12_visiting_batters_protected.jpg"),
    (36.0, "13_home_advantage_shrinks.jpg"),
    (38.5, "14_pitches_weather_decide.jpg"),
    (42.5, "15_crickets_character.jpg"),
    (46.0, "16_cta_one_ball_vs_chaos.jpg"),
    (48.5, "17_pinned_debate_card.jpg"),
]

def main():
    t0 = time.time()
    file_url = "file:///" + str(html_path.resolve()).replace("\\", "/")
    
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    
    print(f"[{time.time()-t0:.1f}s] Loading {file_url}...")
    page.goto(file_url, wait_until="load")
    page.evaluate("document.fonts.ready")
    print(f"[{time.time()-t0:.1f}s] Page ready. Capturing {len(checkpoints)} preview frames...")
    
    for t, name in checkpoints:
        t_frame = time.time()
        page.evaluate(f"window.seekFrame({t}); void 0;")
        out_file = out_dir / name
        page.screenshot(path=str(out_file), type="jpeg", quality=90)
        print(f"[{time.time()-t0:.1f}s] Captured {name} at {t:.2f}s in {time.time()-t_frame:.2f}s")
        
    browser.close()
    p.stop()

    # Also copy 00_first_frame.jpg to preview.jpg
    shutil.copyfile(out_dir / "00_first_frame.jpg", base / "preview.jpg")
    print(f"All {len(checkpoints)} frames captured successfully in {time.time()-t0:.2f}s!")

if __name__ == "__main__":
    main()
