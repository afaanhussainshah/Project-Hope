import os
import asyncio
from playwright.async_api import async_playwright

async def capture():
    html_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\boxing-day-test-mcg\standalone.html"
    out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\boxing-day-test-mcg\preview_frames"
    os.makedirs(out_dir, exist_ok=True)

    checkpoints = [
        (0.00, "00_frame_0s_19_years_old.jpg"),
        (2.50, "01_frame_2_5s_debut.jpg"),
        (4.20, "02_frame_4_2s_bumrah.jpg"),
        (5.50, "03_frame_5_5s_rampshot.jpg"),
        (7.50, "04_frame_7_5s_90k_crowd.jpg"),
        (10.50, "05_frame_10_5s_boxing_day.jpg"),
        (13.20, "06_frame_13_2s_what_is_boxing_day.jpg"),
        (17.50, "07_frame_17_5s_26_december_mcg.jpg"),
        (23.50, "08_frame_23_5s_families_leftovers.jpg"),
        (29.00, "09_frame_29_0s_creates_legends.jpg"),
        (30.50, "10_frame_30_5s_warne_hattrick.jpg"),
        (34.50, "11_frame_34_5s_rahane_hundred.jpg"),
        (43.00, "12_frame_43_0s_public_holiday.jpg"),
        (47.50, "13_frame_47_5s_boxing_day_test_cricket.jpg"),
        (50.50, "14_frame_50_5s_pinned_comment_debate.jpg"),
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1080, "height": 1920}, device_scale_factor=1.0)
        page = await context.new_page()
        await page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="load")
        await page.wait_for_timeout(500)

        for t, fname in checkpoints:
            await page.evaluate(f"window.seekFrame({t:.4f});")
            out_file = os.path.join(out_dir, fname)
            await page.screenshot(path=out_file, quality=90, type="jpeg")
            print(f"Captured {fname} at t={t:.2f}s")

        # Copy first frame (t=0.0) as preview.jpg
        cover_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\boxing-day-test-mcg\preview.jpg"
        await page.evaluate("window.seekFrame(0.0);")
        await page.screenshot(path=cover_path, quality=92, type="jpeg")
        print(f"Captured preview.jpg at t=0.0s")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
