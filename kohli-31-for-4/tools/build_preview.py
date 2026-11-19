import base64
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

# Asset paths
ART_PATH = Path(r"C:\Users\Lenovo\.gemini\antigravity\brain\318419c7-d087-4891-8413-262c7f2aa1c6\kohli_mcg_cover_art_1795108932193.jpg")
FONT_PATH = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-31-for-4\assets\fonts\Anton-Regular.ttf")
OUT_JPG = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-31-for-4\preview.jpg")
SCRATCH_DIR = Path(r"C:\Users\Lenovo\.gemini\antigravity\brain\318419c7-d087-4891-8413-262c7f2aa1c6\scratch")
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

HTML_PATH = SCRATCH_DIR / "kohli_mcg_preview.html"
OUT_PNG_TMP = SCRATCH_DIR / "kohli_mcg_preview_raw.png"
CROP_3_4 = SCRATCH_DIR / "kohli_mcg_crop_3x4.jpg"
CROP_1_1 = SCRATCH_DIR / "kohli_mcg_crop_1x1.jpg"

art_b64 = base64.b64encode(ART_PATH.read_bytes()).decode("ascii")
font_b64 = base64.b64encode(FONT_PATH.read_bytes()).decode("ascii")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @font-face {{
    font-family: 'Anton';
    src: url(data:font/ttf;base64,{font_b64}) format('truetype');
    font-weight: 400;
    font-style: normal;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1080px; height: 1920px; overflow: hidden;
    background: #060e1e; font-family: 'Anton', Impact, sans-serif;
    -webkit-font-smoothing: antialiased;
  }}
  .canvas {{
    position: relative; width: 1080px; height: 1920px; overflow: hidden;
    background: #060e1e;
  }}

  /* Base 3D paper-cut artwork */
  .bg-art {{
    position: absolute; inset: 0;
    width: 1080px; height: 1920px;
    object-fit: cover; object-position: 50% 48%;
    transform: scale(1.03) translateY(10px);
    filter: contrast(1.08) saturate(1.10);
  }}

  /* Cinematic vignette for crisp typography readability */
  .vignette {{
    position: absolute; inset: 0;
    background:
      linear-gradient(180deg,
        rgba(5, 11, 24, 0.94) 0%,
        rgba(5, 11, 24, 0.65) 16%,
        rgba(5, 11, 24, 0.10) 30%,
        rgba(5, 11, 24, 0.00) 48%,
        rgba(5, 11, 24, 0.12) 65%,
        rgba(5, 11, 24, 0.72) 80%,
        rgba(4, 9, 20, 0.96) 100%
      ),
      radial-gradient(ellipse at 50% 50%,
        rgba(0,0,0,0) 44%,
        rgba(4, 9, 20, 0.52) 100%
      );
    pointer-events: none;
  }}

  /* Paper grain overlay */
  .grain {{
    position: absolute; inset: 0;
    opacity: 0.05; pointer-events: none; mix-blend-mode: overlay;
  }}

  /* ═══ TOP HOOK (Inside Instagram Explore 1:1 Safe Zone) ═══ */
  .top-header {{
    position: absolute; top: 410px; left: 0; width: 1080px;
    display: flex; flex-direction: column; align-items: center;
    z-index: 10;
  }}

  /* Crimson urgency eyebrow tape */
  .eyebrow-tape {{
    display: inline-flex; align-items: center; gap: 12px;
    background: #D32F2F;
    color: #FFFDF7; font-size: 32px; letter-spacing: 3.5px;
    padding: 8px 30px 9px 30px;
    transform: rotate(-1.4deg);
    clip-path: polygon(1% 5%, 99% 0%, 100% 95%, 0% 100%, 0.8% 50%);
    box-shadow: 0 12px 28px rgba(0,0,0,0.75), 0 0 24px rgba(211,47,47,0.45);
    margin-bottom: 10px;
    text-transform: uppercase;
  }}

  .warn-icon {{
    font-size: 28px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
  }}

  /* Giant hero score */
  .hero-wrap {{ position: relative; line-height: 0.88; text-align: center; }}

  .hero-shadow {{
    position: absolute; top: 10px; left: 0; width: 100%;
    font-size: 185px; letter-spacing: 4px;
    color: #030814; -webkit-text-stroke: 14px #030814;
    filter: drop-shadow(0 18px 26px rgba(0,0,0,0.92));
    z-index: 1; user-select: none;
  }}

  .hero-text {{
    position: relative; font-size: 185px; letter-spacing: 4px;
    background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 40%, #90CAF9 75%, #1E88E5 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 5px 0 rgba(3,8,20,0.95));
    z-index: 2;
  }}

  /* Subtitle tape */
  .hero-sub-tape {{
    display: inline-block;
    background: #FFD54F;
    color: #081020;
    font-size: 50px;
    letter-spacing: 3px;
    padding: 6px 36px 8px 36px;
    transform: rotate(1.2deg);
    clip-path: polygon(2% 0%, 98% 3%, 100% 97%, 0% 100%);
    box-shadow: 0 10px 22px rgba(0,0,0,0.8);
    margin-top: 4px;
  }}

  /* ═══ BOTTOM TORN PAPER VERDICT ═══ */
  .bottom-block {{
    position: absolute; top: 1290px; left: 0; width: 1080px;
    display: flex; flex-direction: column; align-items: center;
    z-index: 12;
  }}

  .torn-banner-wrap {{
    position: relative; transform: rotate(-1.5deg);
    filter: drop-shadow(0 22px 34px rgba(0,0,0,0.90));
  }}

  .torn-banner {{
    background: linear-gradient(180deg, #FFFDF7 0%, #EFE8D8 100%);
    padding: 14px 42px 18px 42px;
    clip-path: polygon(
      0% 6%, 4% 0%, 12% 4%, 25% 0%, 40% 3%, 56% 0%, 72% 3%, 86% 0%, 96% 2%, 100% 0%,
      99.3% 32%, 100% 65%, 99% 96%,
      94% 100%, 82% 96%, 68% 100%, 50% 97%, 34% 100%, 18% 96%, 5% 100%, 0.6% 95%,
      0% 64%, 1% 32%
    );
    border-bottom: 8px solid #D32F2F;
    display: flex; align-items: center; justify-content: center; gap: 14px;
    white-space: nowrap;
  }}

  .punch-dark {{ font-size: 78px; line-height: 0.95; color: #07101E; letter-spacing: 2px; white-space: nowrap; }}
  .punch-red {{ font-size: 78px; line-height: 0.95; color: #D32F2F; letter-spacing: 2px; white-space: nowrap; }}

  /* Stat strip underneath */
  .stat-strip {{
    margin-top: 18px;
    display: inline-flex; align-items: center; gap: 18px;
    background: rgba(5,13,28,0.94);
    border: 2px solid rgba(255,213,79,0.55);
    padding: 10px 32px 12px 32px;
    transform: rotate(0.8deg);
    box-shadow: 0 14px 28px rgba(0,0,0,0.85);
  }}

  .stat-gold {{ font-size: 36px; letter-spacing: 2px; color: #FFD54F; }}
  .stat-white {{ font-size: 36px; letter-spacing: 2px; color: #F4F6FA; }}
  .stat-blue {{ font-size: 36px; letter-spacing: 2px; color: #64B5F6; }}
  .stat-sep {{ width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.40); }}

  /* Corner frames */
  .corner-frame {{
    position: absolute; width: 60px; height: 60px;
    border-color: rgba(255,213,79,0.45); border-style: solid;
    z-index: 15; pointer-events: none;
  }}
  .cf-tl {{ top: 84px; left: 64px; border-width: 5px 0 0 5px; }}
  .cf-tr {{ top: 84px; right: 64px; border-width: 5px 5px 0 0; }}
  .cf-bl {{ bottom: 94px; left: 64px; border-width: 0 0 5px 5px; }}
  .cf-br {{ bottom: 94px; right: 64px; border-width: 0 5px 5px 0; }}

  .footer-tag {{
    position: absolute; bottom: 100px; left: 0; width: 1080px;
    text-align: center; font-size: 28px; letter-spacing: 7px;
    color: rgba(220,235,255,0.45); z-index: 15;
  }}
</style>
</head>
<body>
  <div class="canvas">
    <img class="bg-art" src="data:image/jpeg;base64,{art_b64}" alt="">
    <div class="vignette"></div>

    <svg class="grain" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
      <filter id="noiseFilter">
        <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" stitchTiles="stitch"/>
      </filter>
      <rect width="1080" height="1920" filter="url(#noiseFilter)"/>
    </svg>

    <div class="corner-frame cf-tl"></div>
    <div class="corner-frame cf-tr"></div>
    <div class="corner-frame cf-bl"></div>
    <div class="corner-frame cf-br"></div>

    <!-- TOP HOOK -->
    <div class="top-header">
      <div class="eyebrow-tape">
        <span class="warn-icon">⚡</span>
        <span>90,000 SILENCED • MCG 2022</span>
      </div>
      <div class="hero-wrap">
        <div class="hero-shadow">31 FOR 4.</div>
        <div class="hero-text">31 FOR 4.</div>
      </div>
      <div class="hero-sub-tape">
        <span>EVERYONE HAD GIVEN UP</span>
      </div>
    </div>

    <!-- BOTTOM TORN PAPER -->
    <div class="bottom-block">
      <div class="torn-banner-wrap">
        <div class="torn-banner">
          <span class="punch-dark">THEN HE DID</span>
          <span class="punch-red">THE IMPOSSIBLE!</span>
        </div>
      </div>
      <div class="stat-strip">
        <span class="stat-gold">82* (53)</span>
        <span class="stat-sep"></span>
        <span class="stat-blue">28 OFF 8 BALLS</span>
        <span class="stat-sep"></span>
        <span class="stat-white">THE GREATEST SHOT</span>
      </div>
    </div>

    <div class="footer-tag">THE SHOT THAT BROKE A STADIUM • KOHLI VS RAUF</div>
  </div>
</body>
</html>
"""

HTML_PATH.write_text(html, encoding="utf-8")
print(f"Wrote HTML to {HTML_PATH}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    page.goto(HTML_PATH.as_uri(), wait_until="networkidle")
    page.evaluate("document.fonts.ready")
    page.screenshot(path=str(OUT_PNG_TMP), full_page=False)
    browser.close()

img = Image.open(OUT_PNG_TMP).convert("RGB")
img.save(OUT_JPG, "JPEG", quality=96, subsampling=0)

# Instagram crop checks
img.crop((0, 240, 1080, 1680)).save(CROP_3_4, "JPEG", quality=90)  # 3:4 profile grid
img.crop((0, 420, 1080, 1500)).save(CROP_1_1, "JPEG", quality=90)  # 1:1 explore grid

print(f"Saved: {OUT_JPG} ({OUT_JPG.stat().st_size / 1024:.1f} KB)")
