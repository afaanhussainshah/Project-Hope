import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(line_buffering=True)

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\follow-on-gamble")
html_path = base / "standalone.html"
out_dir = base / "preview_frames"
out_dir.mkdir(parents=True, exist_ok=True)

checkpoints = [
    (1.5, "01_hook_99_percent.jpg"),
    (4.5, "02_hook_streak_rip.jpg"),
    (6.0, "03_hook_cost_badge.jpg"),
    (8.2, "04_law14_follow_on.jpg"),
    (10.5, "05_lead_graphic.jpg"),
    (13.0, "06_bat_straight_away.jpg"),
    (15.0, "07_choice_stamp.jpg"),
    (17.2, "08_gamble_card.jpg"),
    (19.0, "09_tired_bowler_sweat.jpg"),
    (21.0, "10_cracked_pitch_day5.jpg"),
    (24.5, "11_history_4_wins.jpg"),
    (27.5, "12_kolkata_2001.jpg"),
    (30.0, "13_aus_16_streak.jpg"),
    (33.0, "14_india_274_behind.jpg"),
    (39.0, "15_laxman_dravid_duo.jpg"),
    (41.2, "16_india_wins_confetti.jpg"),
    (43.0, "17_weapon_vs_trap.jpg"),
    (45.0, "18_trap_snapped_shut.jpg"),
    (47.5, "19_cta_cricket_secrets.jpg"),
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
        # IMPORTANT: append 'void 0;' so Playwright doesn't attempt to serialize the cyclic GSAP timeline object!
        page.evaluate(f"window.__timelines.main.seek({t}); void 0;")
        out_file = out_dir / name
        page.screenshot(path=str(out_file), type="jpeg", quality=85)
        print(f"[{time.time()-t0:.1f}s] Captured {name} at {t:.2f}s in {time.time()-t_frame:.2f}s")
        
    browser.close()
    p.stop()
    print(f"All {len(checkpoints)} frames captured successfully in {time.time()-t0:.2f}s!")

if __name__ == "__main__":
    main()
