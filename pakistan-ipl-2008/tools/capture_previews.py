import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\pakistan-ipl-2008")
html_path = base / "index.html"
out_dir = base / "preview_frames"
out_dir.mkdir(parents=True, exist_ok=True)

checkpoints = [
    (2.5, "01_hook_afridi_lineup.jpg"),
    (6.2, "02_hook_scissors_cutting.jpg"),
    (7.5, "03_hook_zero_players_stamp.jpg"),
    (9.8, "04_stadium_popup.jpg"),
    (13.5, "05_afridi_deccan_chargers.jpg"),
    (17.5, "06_rr_tanvir_purple_cap.jpg"),
    (21.0, "07_rr_trophy_celebration.jpg"),
    (25.5, "08_november_mumbai_night.jpg"),
    (28.5, "09_relations_collapsed.jpg"),
    (32.0, "10_empty_2009_roster.jpg"),
    (37.0, "11_the_unwritten_rule.jpg"),
    (39.5, "12_never_officially_banned.jpg"),
    (44.5, "13_azhar_mahmood_exception.jpg"),
    (46.8, "14_british_passport_zoom.jpg"),
    (49.5, "15_swinging_jersey_empty.jpg"),
    (53.0, "16_final_question_cta.jpg"),
]

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            args=[
                "--disable-background-timer-throttling",
                "--disable-renderer-backgrounding",
                "--font-render-hinting=none"
            ]
        )
        page = await browser.new_page(viewport={"width": 1080, "height": 1920})
        await page.goto(f"file:///{html_path.resolve().as_posix()}", wait_until="networkidle")
        await asyncio.sleep(0.5)

        for t, name in checkpoints:
            await page.evaluate(f"window.seekFrame({t});")
            await asyncio.sleep(0.08)
            out_file = out_dir / name
            await page.screenshot(path=str(out_file), type="jpeg", quality=92)
            print(f"Captured {name} at {t:.2f}s")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())

