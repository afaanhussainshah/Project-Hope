import os
import sys
import time
import math
import base64
import asyncio
import argparse
import subprocess
from playwright.async_api import async_playwright
import imageio_ffmpeg

sys.stdout.reconfigure(line_buffering=True)


async def render_video(
    html_path: str,
    audio_path: str,
    output_path: str,
    duration: float,
    fps: int = 60,
    workers: int = 4,
    width: int = 1080,
    height: int = 1920,
    scale: float = 1.0,
    crf: int = 18,
    preset: str = "fast",
    img_format: str = "jpeg",
    jpeg_quality: int = 92,
    use_gpu: bool = True,
    max_frames: int = 0,
):
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    total_frames = max_frames if max_frames > 0 else math.ceil(duration * fps)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    vcodec_in = "png" if img_format == "png" else "mjpeg"

    cmd = [
        ffmpeg, "-y",
        "-f", "image2pipe",
        "-vcodec", vcodec_in,
        "-framerate", str(fps),
        "-i", "-",
    ]
    if audio_path and os.path.exists(audio_path):
        cmd += ["-i", audio_path]

    cmd += [
        "-c:v", "libx264",
        "-preset", preset,
        "-crf", str(crf),
        "-pix_fmt", "yuv420p",
        "-r", str(fps),
    ]
    if audio_path and os.path.exists(audio_path):
        cmd += ["-c:a", "aac", "-b:a", "192k", "-shortest"]

    cmd.append(output_path)

    out_width = int(width * scale)
    out_height = int(height * scale)
    print("=== Project Hope Fast Parallel GPU-Chromium Renderer ===")
    print(f"HTML:       {html_path}")
    print(f"Audio:      {audio_path}")
    print(f"Output:     {output_path}")
    print(f"Frames:     {total_frames} ({duration:.2f}s @ {fps} fps, {out_width}x{out_height}) [scale={scale}]")
    print(f"Workers:    {workers} parallel Chromium tabs | GPU Raster: {use_gpu}")
    print(f"Quality:    {img_format.upper()}{f' q={jpeg_quality}' if img_format == 'jpeg' else ''} -> libx264 CRF {crf} ({preset})")

    ffmpeg_proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )

    launch_args = [
        "--disable-background-timer-throttling",
        "--disable-backgrounding-occluded-windows",
        "--disable-renderer-backgrounding",
        "--font-render-hinting=none",
        "--disable-dev-shm-usage",
        "--js-flags=--max-old-space-size=4096",
    ]
    if use_gpu:
        launch_args += [
            "--use-gl=angle",
            "--use-angle=d3d11",
            "--enable-gpu-rasterization",
            "--ignore-gpu-blocklist",
        ]

    file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    start_time = time.time()
    next_assign = 0
    next_write = 0
    ready_frames = {}
    max_buffer = workers * 4
    write_cond = asyncio.Condition()
    assign_lock = asyncio.Lock()

    async def flush_ready():
        nonlocal next_write
        while next_write in ready_frames:
            frame_bytes = ready_frames.pop(next_write)
            ffmpeg_proc.stdin.write(frame_bytes)
            if next_write % 60 == 0 or next_write == total_frames - 1:
                elapsed = time.time() - start_time
                done = next_write + 1
                rate = done / elapsed if elapsed > 0 else 0.0
                eta = (total_frames - done) / rate if rate > 0 else 0.0
                print(
                    f"Rendered {done}/{total_frames} frames ({(done / total_frames) * 100:.1f}%) "
                    f"- Speed: {rate:.2f} fps - Elapsed: {elapsed:.1f}s - ETA: {eta:.1f}s"
                )
            next_write += 1
        write_cond.notify_all()

    async def worker_loop(worker_id: int, page, cdp):
        nonlocal next_assign
        cdp_params = (
            {"format": "png"}
            if img_format == "png"
            else {"format": "jpeg", "quality": jpeg_quality}
        )
        if scale != 1.0:
            cdp_params["clip"] = {"x": 0, "y": 0, "width": width, "height": height, "scale": scale}
        
        while True:
            async with assign_lock:
                if next_assign >= total_frames:
                    return
                frame_idx = next_assign
                next_assign += 1

            # Backpressure so RAM stays tiny if one worker gets far ahead
            async with write_cond:
                while frame_idx - next_write >= max_buffer:
                    await write_cond.wait()

            t = frame_idx / fps
            img_bytes = None
            
            # Resilient retry with auto-tab recovery
            for attempt in range(4):
                try:
                    await page.evaluate(f"if (window.seekFrame) window.seekFrame({t:.4f}); else if (window.__timelines && window.__timelines['main']) window.__timelines['main'].seek({t:.4f}); void 0;")
                    res = await cdp.send("Page.captureScreenshot", cdp_params)
                    img_bytes = base64.b64decode(res["data"])
                    break
                except Exception as err:
                    print(f"\n[Worker {worker_id}] Transient error at frame {frame_idx} (attempt {attempt+1}/4): {err}")
                    if attempt == 3:
                        raise err
                    try:
                        await page.close()
                    except Exception:
                        pass
                    await asyncio.sleep(1.0)
                    page = await context.new_page()
                    await page.goto(file_url, wait_until="load")
                    await page.evaluate("document.fonts.ready")
                    cdp = await context.new_cdp_session(page)

            async with write_cond:
                ready_frames[frame_idx] = img_bytes
                await flush_ready()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=launch_args)
        context = await browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=scale,
        )

        pages = []
        cdps = []
        file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
        for w_idx in range(workers):
            page = await context.new_page()
            await page.goto(file_url, wait_until="load")
            await page.evaluate("document.fonts.ready")
            has_seek = await page.evaluate("typeof window.seekFrame === 'function'")
            if not has_seek:
                raise RuntimeError("CRITICAL ERROR: window.seekFrame is undefined on page! Animation cannot play.")
            cdp = await context.new_cdp_session(page)
            pages.append(page)
            cdps.append(cdp)

        # Quick motion verification test
        test_p = pages[0]
        await test_p.evaluate("window.seekFrame(0.0)")
        res0 = await cdps[0].send("Page.captureScreenshot", {"format": "jpeg", "quality": 50})
        await test_p.evaluate("window.seekFrame(5.0)")
        res5 = await cdps[0].send("Page.captureScreenshot", {"format": "jpeg", "quality": 50})
        if res0["data"] == res5["data"]:
            raise RuntimeError("CRITICAL ERROR: Frame at t=0.0 and t=5.0 are identical! The animation is stuck!")
        print("Verified animation seeking is fully dynamic (t=0.0 vs t=5.0 confirmed different).")

        print(f"Loaded {workers} GPU-Chromium CDP tabs in {time.time() - start_time:.2f}s. Starting parallel capture...")
        start_time = time.time()

        await asyncio.gather(*(worker_loop(i, pages[i], cdps[i]) for i in range(workers)))
        await browser.close()

    ffmpeg_proc.stdin.close()
    stderr_output = ffmpeg_proc.stderr.read().decode("utf-8", errors="replace")
    ffmpeg_proc.wait()

    total_elapsed = time.time() - start_time
    if ffmpeg_proc.returncode != 0:
        print(f"FFmpeg Error (code {ffmpeg_proc.returncode}):\n{stderr_output}")
        sys.exit(1)

    video_size = os.path.getsize(output_path)
    avg_fps = total_frames / total_elapsed if total_elapsed > 0 else 0.0
    print("\n=== Render Complete! ===")
    print(f"Total time:   {total_elapsed:.2f}s ({total_elapsed / 60:.2f} minutes)")
    print(f"Avg speed:    {avg_fps:.2f} fps")
    print(f"Output video: {output_path}")
    print(f"File size:    {video_size / (1024 * 1024):.2f} MB")


def main():
    parser = argparse.ArgumentParser(description="Fast parallel GPU-Chromium + libx264 reel renderer")
    parser.add_argument("--html", required=True, help="Path to standalone.html")
    parser.add_argument("--audio", default="", help="Path to master audio wav/mp3")
    parser.add_argument("--output", required=True, help="Output MP4 path")
    parser.add_argument("--duration", type=float, required=True, help="Video duration in seconds")
    parser.add_argument("--fps", type=int, default=60, help="Frames per second (default: 60)")
    parser.add_argument("--width", type=int, default=1080, help="Video width in pixels (default: 1080)")
    parser.add_argument("--height", type=int, default=1920, help="Video height in pixels (default: 1920)")
    parser.add_argument("--scale", type=float, default=1.0, help="Device scale factor (e.g. 2.0 for 4K)")
    parser.add_argument("--workers", type=int, default=4, help="Parallel Chromium tabs (default: 4)")
    parser.add_argument("--crf", type=int, default=18, help="libx264 CRF quality (default: 18)")
    parser.add_argument("--preset", default="fast", help="libx264 preset (default: fast)")
    parser.add_argument("--format", choices=["jpeg", "png"], default="jpeg", help="Screenshot pipe format")
    parser.add_argument("--quality", type=int, default=92, help="JPEG quality 1-100 (default: 92)")
    parser.add_argument("--no-gpu", action="store_true", help="Disable Chromium GPU raster flags")
    parser.add_argument("--max-frames", type=int, default=0, help="Limit frames for benchmarking")
    args = parser.parse_args()

    asyncio.run(
        render_video(
            html_path=args.html,
            audio_path=args.audio,
            output_path=args.output,
            duration=args.duration,
            fps=args.fps,
            workers=args.workers,
            width=args.width,
            height=args.height,
            scale=args.scale,
            crf=args.crf,
            preset=args.preset,
            img_format=args.format,
            jpeg_quality=args.quality,
            use_gpu=not args.no_gpu,
            max_frames=args.max_frames,
        )
    )


if __name__ == "__main__":
    main()
