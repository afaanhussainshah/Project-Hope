import os
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\index.html")
out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\preview_frames"
os.makedirs(out_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.text}"))
    page.on("pageerror", lambda exc: print(f"BROWSER ERROR: {exc}"))
    
    file_url = "file:///" + html_path.replace("\\", "/")
    print(f"Navigating to {file_url}...")
    page.goto(file_url, wait_until="domcontentloaded")
    print("Page loaded!")
    
    # Check if window.__timelines exists
    has_tl = page.evaluate("typeof window.__timelines !== 'undefined' && typeof window.__timelines['main'] !== 'undefined'")
    print(f"Has timeline: {has_tl}")
    
    # Seek to t=1.0 and capture
    page.evaluate("window.__timelines['main'].seek(1.0)")
    out_path = os.path.join(out_dir, "test_1s.jpg")
    page.screenshot(path=out_path, type="jpeg", quality=85)
    print(f"Saved {out_path}, size={os.path.getsize(out_path)} bytes")
    
    browser.close()
