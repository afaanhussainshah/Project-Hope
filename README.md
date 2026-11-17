# 🏏 Project Hope: Paper-Cut Cricket Animation Engine

An automated, high-retention vertical short-form video generation pipeline designed for Instagram Reels, YouTube Shorts, and TikTok. 

Inspired by iconic cutout and stop-motion aesthetics (e.g., *HyperFrames / Sandpaper Gate / Rain Rule 1992*), this engine generates 100% custom SVG-based paper animation, millisecond-accurate subtitle typography, synthesized sound-effects beds, and frame-accurate voiceover synchronization.

---

## 📽️ Featured Video Productions

### 1. Mohammad Amir — 2017 Champions Trophy Final (Redemption Arc)
- **File:** [`mohammad-amir-2017-reel.mp4`](./mohammad-amir-2017-reel.mp4)
- **Duration:** 34.43 seconds
- **Framerate:** **60 FPS (Ultra-Smooth)**
- **Resolution:** 1080 × 1920 (Vertical 9:16)
- **Storyline:** 
  - *Act 1: The Dark Exile* — 5 years banned in the shadows with metallic prison bars.
  - *Act 2: The Return* — 2016 return in Pakistan green.
  - *Act 3: The Oval Stage* — Facing India's terrifying trio (Rohit Sharma, Virat Kohli, Shikhar Dhawan).
  - *Act 4: The Demolition* — Late inswinger traps Rohit for a duck; Kohli dropped at slip then caught at point next ball; Dhawan caught behind. 3 wickets for 16 runs.
  - *Act 5: Immortal Redemption* — Amir's iconic soaring eagle celebration with the Champions Trophy.

### 2. Virat Kohli — 765 Runs (2023 World Cup Chronicle)
- **File:** [`kohli-765-runs-reel.mp4`](./kohli-765-runs-reel.mp4)
- **Duration:** 44.04 seconds
- **Framerate:** **60 FPS (Ultra-Smooth)**
- **Resolution:** 1080 × 1920 (Vertical 9:16)
- **Storyline:**
  - *Mystery Hook:* First 6 seconds reveal an anonymous batter's superhuman stats (95.62 Average, 90.31 Strike Rate, 765 Runs) without naming him.
  - *The Reveal:* Virat Kohli bowing to Sachin Tendulkar after surpassing 50 ODI centuries at Wankhede.
  - *Ahmedabad Heartbreak:* Inside edge chop-on silencing 130,000 fans (dead silence drop).
  - *Trophy Dust vs Immortal Legacy:* Walk tall, King.

### 3. Cricket Bat Grains — Myth vs Fact (The Science of Willow)
- **File:** [`bat-grains-myth-reel.mp4`](./bat-grains-myth-reel.mp4)
- **Duration:** 40.36 seconds
- **Framerate:** **60 FPS (Ultra-Smooth)**
- **Resolution:** 1080 × 1920 (Vertical 9:16)
- **Storyline:**
  - *Act 1: The Money Waste Hook* — Magnifying glass examining tightly packed grains on an $800 price tag with a torn paper rip effect and `WASTING MONEY` stamp slam.
  - *Act 2: The Myth or Fact Dilemma* — Grade 1 English Willow card questioning if 12-14 grains actually hit further (`MYTH OR FACT?` double stamp).
  - *Act 3: The Growth Ring Science* — Cross-section tree trunk revealing that 1 grain simply represents 1 year of natural tree growth.
  - *Act 4: The 14 Grains Paradox* — Tight grains mean older, drier wood $\rightarrow$ cricket ball impact creates brittle toe cracks (`BRITTLE WOOD CRACKS FAST` stamp).
  - *Act 5: The 6 Grains Cannon* — Wider grains contain natural moisture and flex $\rightarrow$ wooden mallet knocking generates a glowing trampoline sweet spot (`THE CANNON · 2X LIFESPAN` stamp).
  - *Act 6: The Final Verdict* — Mechanical balance scale tilting decisively towards pickup, balance, and ping over grain count (`STOP COUNTING LINES` stamp & CTA).

### 4. MS Dhoni — The Final Whistle (IPL Retirement)
- **File:** [`dhoni-ipl-retirement-reel.mp4`](./dhoni-ipl-retirement-reel.mp4)
- **Duration:** 47.73 seconds
- **Framerate:** **60 FPS (Ultra-Smooth)**
- **Resolution:** 1080 × 1920 (Vertical 9:16)
- **Storyline:**
  - *Act 1: The Iconic Smile (0.0s – 12.8s)* — Danny Morrison asking *"Is this your last season in yellow?"* with Dhoni smirking and slamming the legendary `"DEFINITELY NOT!"` stamp.
  - *Act 2: The Sudden Silence (12.8s – 14.8s)* — Red marker strikes through `"DEFINITELY NOT"` with sudden sub-bass drop and `UNTIL TODAY. THE FINAL WHISTLE 🛑` stamp slam.
  - *Act 3: The 5 Trophies Dynasty (14.8s – 23.0s)* — Grand wooden presentation table with royal blue apron; 5 golden IPL trophies (2010, 2011, 2018, 2021, 2023) sequentially slamming down with metallic dings and `5 IPL TROPHIES · 10 FINALS ⭐` stamp slam.
  - *Act 4: Busted Knees & Warrior Heart (23.0s – 35.8s)* — Night floodlights with 40,000 yellow crowd dots; Dhoni with heavy white crepe knee strapping limping heroically between the wickets; `WARRIOR IN YELLOW` stamp slam.
  - *Act 5: Never Another Thala (35.8s – 41.2s)* — Giant suspended CSK Canary Yellow Jersey #7 with a golden royal ruby crown and sunburst rays; `NEVER ANOTHER THALA! 👑` stamp slam.
  - *Act 6: The Farewell Walk-Off (41.2s – 47.73s)* — Dhoni in iconic #7 jersey raising his right arm in salute walking into the Chepauk players' tunnel with golden confetti; `END OF AN ERA` & `THANK YOU #7` stamp slams.

---

## 🛠️ Architecture & Tech Stack

```
Project Hope/
├── amir-2017-ct/                 # Mohammad Amir 2017 CT Reel Pipeline
│   ├── assets/                   # Fonts (Anton), GSAP library, voiceover & SFX WAV
│   ├── preview_frames/           # Render verification snapshots
│   ├── renders/                  # Final 60 FPS MP4 & mixed audio master
│   ├── tools/                    # Speech alignment, SFX synthesizer & Playwright renderer
│   ├── index.html                # Master GSAP animation composition
│   └── standalone.html           # Zero-dependency Base64 bundled HTML
│
├── kohli-765-runs/               # Virat Kohli 765 Runs Reel Pipeline
│   ├── assets/                   # Audio stems, fonts & GSAP
│   ├── preview_frames/           # Verification snapshots
│   ├── renders/                  # Final MP4 & mixed audio master
│   ├── tools/                    # Audio analysis & Playwright rendering scripts
│   ├── index.html                # Master GSAP animation composition
│   └── standalone.html           # Bundled standalone HTML
│
├── bat-grains-myth/              # Bat Grains Myth vs Fact Reel Pipeline
│   ├── assets/                   # Voiceover, fonts & GSAP
│   ├── preview_frames/           # Render verification snapshots
│   ├── renders/                  # Final 60 FPS MP4 & mixed audio master
│   ├── tools/                    # Speech alignment, SFX synth & Playwright renderer
│   ├── index.html                # Master GSAP animation composition
│   └── standalone.html           # Bundled standalone HTML
│
├── dhoni-ipl-retirement/         # MS Dhoni IPL Retirement Reel Pipeline
│   ├── assets/                   # Voiceover, fonts & GSAP
│   ├── preview_frames/           # Render verification snapshots (01 to 08)
│   ├── renders/                  # Final 60 FPS MP4 & mixed audio master
│   ├── tools/                    # Speech alignment, SFX synth & Playwright renderer
│   ├── index.html                # Master GSAP animation composition
│   └── standalone.html           # Bundled standalone HTML
│
├── mohammad-amir-2017-reel.mp4   # Master 60 FPS Export (Amir 2017 CT)
├── kohli-765-runs-reel.mp4       # Master Export (Kohli 765 Runs)
├── bat-grains-myth-reel.mp4      # Master 60 FPS Export (Bat Grains Myth vs Fact)
└── dhoni-ipl-retirement-reel.mp4 # Master 60 FPS Export (MS Dhoni IPL Retirement)
```

---

## 🚀 How to Run the Pipeline

### Prerequisites
- Python 3.10+
- `playwright` (`pip install playwright` && `playwright install chromium`)
- `imageio-ffmpeg` / FFmpeg
- `numpy`, `scipy`

### 1. Generate SFX & Master Audio Mix
```bash
python dhoni-ipl-retirement/tools/make_sfx.py
```

### 2. Compile Standalone Composition
Bundles SVGs, Base64 fonts, and GSAP timelines into an isolated zero-dependency file:
```bash
python dhoni-ipl-retirement/tools/build_standalone.py
```

### 3. Render High-FPS MP4
Drives headless Chromium via Playwright, steps through the GSAP timeline with millisecond precision, and pipes frames directly into FFmpeg stdin:
```bash
python dhoni-ipl-retirement/tools/render_reel.py
```

---

## 🎨 Visual System & Paper-Cut Aesthetics
- **Polygonal Cutouts:** Vector-drawn SVG shapes with procedural jagged edge displacements.
- **Drop Shadows & Depth:** Multi-tiered layered shadows (`rgba(0,0,0,0.42)`) simulating physical layered paper.
- **Micro-Texture Overlays:** Inlined procedural fractal turbulence noise with `mix-blend-mode: multiply`.
- **Physical Impact Stamps:** Rubber-stamp placards with dashed border cutouts and back-out spring physics.
