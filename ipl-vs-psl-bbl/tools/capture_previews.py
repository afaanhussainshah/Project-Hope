import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\ipl-vs-psl-bbl")
html_path = base / "index.html"
out_dir = base / "preview_frames"
out_dir.mkdir(parents=True, exist_ok=True)

checkpoints = [
    (1.5, "01_hook_three_cards.jpg"),
    (4.5, "02_hook_9x_stamp.jpg"),
    (7.1, "03_hook_guess_which.jpg"),
    (8.5, "04_psl_intro.jpg"),
    (11.5, "05_psl_team_budget.jpg"),
    (15.0, "06_psl_star_player.jpg"),
    (18.0, "07_bbl_stadium.jpg"),
    (21.0, "08_bbl_salary.jpg"),
    (25.5, "09_bbl_stamps_contrast.jpg"),
    (27.5, "10_ipl_intro.jpg"),
    (30.5, "11_ipl_120_crore.jpg"),
    (36.5, "12_ipl_pant_27_crore.jpg"),
    (40.5, "13_ipl_vs_psl_shock.jpg"),
    (45.0, "14_economy_climax.jpg"),
    (48.2, "15_ballot_cta.jpg"),
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
            await page.screenshot(path=str(out_file), type="jpeg", quality=90)
            print(f"Captured {name} at {t:.2f}s")

        await browser.close()

asyncio.run(run())
