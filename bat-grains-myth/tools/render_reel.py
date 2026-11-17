import os
import sys
import time
import math
import subprocess
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

sys.stdout.reconfigure(line_buffering=True)

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\bat-grains-myth"
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
AUDIO_MIX = os.path.join(PROJECT_DIR, "renders", "full_audio_mix.wav")
OUTPUT_VIDEO = os.path.join(PROJECT_DIR, "renders", "bat-grains-myth-reel.mp4")

FPS = 60
DURATION = 40.36
TOTAL_FRAMES = math.ceil(DURATION * FPS)

print(f"=== Starting Bat Grains Myth Reel Render (60 FPS Ultra-Smooth) ===")
print(f"Duration: {DURATION}s @ {FPS} fps = {TOTAL_FRAMES} frames")
print(f"Input HTML: {STANDALONE_HTML}")
print(f"Audio mix: {AUDIO_MIX}")
print(f"Output MP4: {OUTPUT_VIDEO}")

with open(STANDALONE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

cmd = [
    FFMPEG, "-y",
    "-f", "image2pipe",
    "-vcodec", "mjpeg",
    "-framerate", str(FPS),
    "-i", "-",
    "-i", AUDIO_MIX,
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-r", str(FPS),
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    OUTPUT_VIDEO
]

ffmpeg_proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

start_time = time.time()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1920})
    page.set_content(html, wait_until="domcontentloaded")
    print("Chromium loaded standalone page successfully.")

    for frame_idx in range(TOTAL_FRAMES):
        t = frame_idx / FPS
        page.evaluate(f"window.__timelines['main'].seek({t:.4f}); void 0;")
        jpeg_bytes = page.screenshot(type="jpeg", quality=85)
        ffmpeg_proc.stdin.write(jpeg_bytes)

        if frame_idx % 50 == 0 or frame_idx == TOTAL_FRAMES - 1:
            elapsed = time.time() - start_time
            rate = (frame_idx + 1) / elapsed if elapsed > 0 else 0
            eta = (TOTAL_FRAMES - frame_idx - 1) / rate if rate > 0 else 0
            print(f"Rendered {frame_idx + 1}/{TOTAL_FRAMES} frames ({((frame_idx + 1) / TOTAL_FRAMES)*100:.1f}%) "
                  f"- Speed: {rate:.2f} fps - Elapsed: {elapsed:.1f}s - ETA: {eta:.1f}s")

    browser.close()

ffmpeg_proc.stdin.close()
stderr_output = ffmpeg_proc.stderr.read().decode("utf-8", errors="replace")
ffmpeg_proc.wait()

total_elapsed = time.time() - start_time
if ffmpeg_proc.returncode != 0:
    print(f"FFmpeg Error (code {ffmpeg_proc.returncode}):\n{stderr_output}")
    sys.exit(1)

video_size = os.path.getsize(OUTPUT_VIDEO)
print(f"\n=== Render Complete! ===")
print(f"Total time: {total_elapsed:.1f}s ({total_elapsed/60:.2f} minutes)")
print(f"Output video: {OUTPUT_VIDEO}")
print(f"File size: {video_size / (1024*1024):.2f} MB")
