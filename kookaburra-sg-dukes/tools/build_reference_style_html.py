import os
import json
import base64

def build():
    base_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kookaburra-sg-dukes"
    out_standalone = os.path.join(base_dir, "standalone.html")
    out_index = os.path.join(base_dir, "index.html")

    # Read and inline GSAP & Font for 100% self-contained standalone execution
    gsap_path = os.path.join(base_dir, "assets", "gsap.min.js")
    with open(gsap_path, "r", encoding="utf-8") as f:
        gsap_source = f.read()

    font_path = os.path.join(base_dir, "assets", "fonts", "Anton-Regular.ttf")
    with open(font_path, "rb") as f:
        font_b64 = base64.b64encode(f.read()).decode("utf-8")

    # Captions aligned with speech segments
    caps = [
        {"start": 0.00, "dur": 4.80, "html": "<span>Australia, India & England<br><b>DON'T</b> play with the same ball.</span>"},
        {"start": 4.80, "dur": 2.70, "html": "<span>And that <i>changes everything.</i></span>"},
        {"start": 7.60, "dur": 2.20, "html": "<span>Australia uses the <b>Kookaburra.</b></span>"},
        {"start": 9.80, "dur": 2.10, "html": "<span>India uses the <i>SG.</i></span>"},
        {"start": 11.90, "dur": 2.20, "html": "<span>England uses the <b>Dukes.</b></span>"},
        {"start": 14.10, "dur": 3.40, "html": "<span>In Test cricket, the<br><b>home board picks the ball.</b></span>"},
        {"start": 17.50, "dur": 2.30, "html": "<span>That's why <i>visiting teams struggle.</i></span>"},
        {"start": 19.80, "dur": 2.80, "html": "<span>Kookaburra <b>swings early</b>,<br>then goes soft.</span>"},
        {"start": 22.60, "dur": 3.90, "html": "<span>SG <i>grips for spinners</i>,<br>and reverses as it ages.</span>"},
        {"start": 26.50, "dur": 2.90, "html": "<span>Dukes swings and<br><b>seams for longer.</b></span>"},
        {"start": 29.40, "dur": 2.70, "html": "<span>So what if everyone used <b>ONE ball?</b></span>"},
        {"start": 32.10, "dur": 3.00, "html": "<span>Visiting batters <i>wouldn't get exposed</i> as badly.</span>"},
        {"start": 35.10, "dur": 2.00, "html": "<span>Home advantage <b>would shrink.</b></span>"},
        {"start": 37.10, "dur": 3.10, "html": "<span>But <i>pitches and weather</i><br>would still decide matches.</span>"},
        {"start": 40.20, "dur": 4.00, "html": "<span>The ball is part of<br><b>cricket's character.</b></span>"},
        {"start": 44.20, "dur": 2.90, "html": "<span>Should cricket use<br><b>ONE ball everywhere?</b></span>"},
        {"start": 47.10, "dur": 2.85, "html": "<span>Or <b>keep the chaos?</b><br><i>Comment below.</i></span>"}
    ]

    cap_divs = "\n".join([
        f'      <div class="clip cap" data-start="{c["start"]}" data-duration="{c["dur"]}" data-track-index="1">{c["html"]}</div>'
        for c in caps
    ])

    html = f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script>{gsap_source}</script>
    <style>
      @font-face {{
        font-family: "Anton";
        src: url("data:font/truetype;charset=utf-8;base64,{font_b64}") format("truetype"), url("assets/fonts/Anton-Regular.ttf") format("truetype");
        font-weight: 400;
        font-style: normal;
      }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #143d30; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: "Anton", sans-serif; }}
      .scene {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: hidden; z-index: 1; }}
      .cam, .cam svg {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; display: block; }}
      .cut {{ filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.3)); }}
      #wipe {{ position: absolute; left: 0; top: -190px; width: 1500px; height: 2300px; z-index: 5; pointer-events: none; transform: translateX(-2200px); }}
      #grain {{
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 8; opacity: 0.2; mix-blend-mode: multiply; pointer-events: none;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' seed='4'/><feColorMatrix values='0 0 0 0 .35  0 0 0 0 .3  0 0 0 0 .25  0 0 0 .9 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");
      }}
      #vig {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 9; pointer-events: none; background: radial-gradient(ellipse at 50% 45%, rgba(0, 0, 0, 0) 55%, rgba(0, 0, 0, 0.32) 100%); }}
      .cap {{ position: absolute; left: 50px; width: 980px; top: 1280px; height: 240px; z-index: 10; text-align: center; pointer-events: none; }}
      .cap span {{
        display: inline-block; max-width: 960px; padding: 14px 34px 20px; background: #f6f1e4; color: #1b1b1b;
        font-size: 74px; line-height: 1.08; letter-spacing: 1px; text-transform: uppercase;
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.35));
        opacity: 0;
      }}
      .cap b {{ font-weight: 400; color: #c1121f; }}
      .cap i {{ font-style: normal; background: #e3b23c; padding: 0 12px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="49.95" data-width="1080" data-height="1920">
      <!-- SCENES -->
      <!-- s1: 0.00s - 7.50s (Australia, India & England don't play with the same ball + Stamp Slam) -->
      <div id="s1" class="clip scene" data-start="0" data-duration="7.50"><div class="cam"></div></div>
      <!-- s2: 7.50s - 14.10s (The 3 Balls Spotlight: Kookaburra, SG, Dukes with Players) -->
      <div id="s2" class="clip scene" data-start="7.50" data-duration="6.60"><div class="cam"></div></div>
      <!-- s3: 14.10s - 19.80s (Home board picks the ball -> Visiting teams struggle) -->
      <div id="s3" class="clip scene" data-start="14.10" data-duration="5.70"><div class="cam"></div></div>
      <!-- s4: 19.80s - 29.40s (Ball Mechanics: Kookaburra soft, SG reverses, Dukes seams forever) -->
      <div id="s4" class="clip scene" data-start="19.80" data-duration="9.60"><div class="cam"></div></div>
      <!-- s5: 29.40s - 37.10s (What if ONE ball? Batters protected vs Home edge shrinks) -->
      <div id="s5" class="clip scene" data-start="29.40" data-duration="7.70"><div class="cam"></div></div>
      <!-- s6: 37.10s - 44.20s (Pitches & weather decide + Ball is cricket's character) -->
      <div id="s6" class="clip scene" data-start="37.10" data-duration="7.10"><div class="cam"></div></div>
      <!-- s7: 44.20s - 49.95s (Pinned Debate Card: One Ball vs Keep the Chaos) -->
      <div id="s7" class="clip scene" data-start="44.20" data-duration="5.75"><div class="cam"></div></div>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- CAPTION OVERLAYS -->
{cap_divs}
    </div>

    <script>
      // ---------- DETERMINISTIC SEED & HELPERS (Reference Paper-Cut Architecture) ----------
      let seed = 42;
      const reseed = (n) => (seed = n);
      const rnd = () => {{
        seed = (seed + 0x6d2b79f5) | 0;
        let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
        t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
      }};
      const C = {{
        paper: "#F6F1E4",
        ink: "#1B1B1B",
        green: "#174D3A",
        dgreen: "#143D30",
        gold: "#E3B23C",
        red: "#B3261E",
        stamp: "#C1121F",
        indiaBlue: "#003566",
        englandNavy: "#0B2238",
        sky: "#BFD9E6",
        turf: "#6F9A4B",
        turfDark: "#5E8744",
        pitch: "#D9BC82",
        dukesRed: "#781822",
        sgRed: "#8E202B",
        kookaRed: "#C82333"
      }};
      const svg = (inner, bg) =>
        `<svg viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg"><rect width="1080" height="1920" fill="${{bg}}"/>${{inner}}</svg>`;
      const put = (id, html) => (document.querySelector("#" + id + " .cam").innerHTML = html);
      const tx = (x, y, s, str, fill, anc = "middle", ex = "") =>
        `<text x="${{x}}" y="${{y}}" font-family="Anton" font-size="${{s}}" fill="${{fill}}" text-anchor="${{anc}}" ${{ex}}>${{str}}</text>`;

      // Procedural Torn Paper Generator (Jagged hand-crafted paper cut)
      function torn(x, y, w, h, j = 10, step = 40) {{
        const p = [];
        for (let i = 0; i <= w; i += step) p.push([x + Math.min(i, w), y + (rnd() - 0.5) * j]);
        for (let i = step; i <= h; i += step) p.push([x + w + (rnd() - 0.5) * j, y + Math.min(i, h)]);
        for (let i = w - step; i >= 0; i -= step) p.push([x + Math.max(i, 0), y + h + (rnd() - 0.5) * j]);
        for (let i = h - step; i > 0; i -= step) p.push([x + (rnd() - 0.5) * j, y + i]);
        return p.map((q) => q[0].toFixed(1) + "," + q[1].toFixed(1)).join(" ");
      }}
      const sheet = (x, y, w, h, fill, j = 10) => `<polygon points="${{torn(x, y, w, h, j)}}" fill="${{fill}}"/>`;

      // Spinning Paper Rays
      const rays = (id, cx, cy, n, c) => {{
        let s = `<g id="${{id}}">`;
        for (let i = 0; i < n; i += 2) {{
          const a = (i * 2 * Math.PI) / n, b = ((i + 1) * 2 * Math.PI) / n;
          s += `<polygon points="${{cx}},${{cy}} ${{(cx + 1900 * Math.cos(a)).toFixed(0)}},${{(cy + 1900 * Math.sin(a)).toFixed(0)}} ${{(cx + 1900 * Math.cos(b)).toFixed(0)}},${{(cy + 1900 * Math.sin(b)).toFixed(0)}}" fill="${{c}}"/>`;
        }}
        return s + "</g>";
      }};

      // Particle scraps for explosions/stamps
      const scraps = (cls, cx, cy, n, colorA = C.gold, colorB = C.green) => {{
        let s = "";
        for (let i = 0; i < n; i++) {{
          const w = 30 + rnd() * 50;
          s += `<polygon class="${{cls}}" points="${{cx}},${{cy}} ${{(cx + w).toFixed(0)}},${{(cy + rnd() * 20).toFixed(0)}} ${{(cx + w * 0.6).toFixed(0)}},${{(cy + w * 0.8).toFixed(0)}}" fill="${{i % 2 ? colorA : colorB}}" opacity="0"/>`;
        }}
        return s;
      }};

      // Specific Cricket Balls with Distinct Seam & Papercut Textures
      // 1. Kookaburra: Low embedded machine seam, bright turf red, Australian gold logo
      // 2. SG: High prominent hand-stitched seam, abrasive maroon, Indian script stamp
      // 3. Dukes: Raised 6-row spine, deep rich grease lacquer, dark crimson
      const cricketBall = (id, type, cx, cy, r, ex = "") => {{
        let color = C.kookaRed, seamW = r * 0.04, label = "KOOKABURRA", sub = "TURF", stitchColor = C.paper;
        if (type === "sg") {{
          color = C.sgRed; seamW = r * 0.08; label = "SG TEST"; sub = "HAND STITCHED";
        }} else if (type === "dukes") {{
          color = C.dukesRed; seamW = r * 0.11; label = "DUKES"; sub = "6-ROW SEAM";
        }}
        return `<g id="${{id}}" class="cut">
          <circle cx="${{cx}}" cy="${{cy}}" r="${{r}}" fill="${{color}}"/>
          <!-- Leather shine arc -->
          <path d="M${{cx - r * 0.62}} ${{cy - r * 0.5}} A${{r * 0.75}} ${{r * 0.75}} 0 0 1 ${{cx - r * 0.1}} ${{cy - r * 0.82}}" stroke="#FFAA9A" stroke-width="${{r * 0.08}}" fill="none" stroke-linecap="round" opacity="0.6"/>
          <!-- Main Seam spine -->
          <path d="M${{cx}} ${{cy - r * 0.98}} Q${{cx + r * 0.2}} ${{cy}} ${{cx}} ${{cy + r * 0.98}}" stroke="${{stitchColor}}" stroke-width="${{seamW}}" fill="none"/>
          <path d="M${{cx}} ${{cy - r * 0.98}} Q${{cx + r * 0.2}} ${{cy}} ${{cx}} ${{cy + r * 0.98}}" stroke="#330000" stroke-width="${{seamW * 0.35}}" fill="none" stroke-dasharray="10 8"/>
          <!-- Seam row borders -->
          ${{[-0.12, 0.12].map(k => `<path d="M${{cx + r * k}} ${{cy - r * 0.95}} Q${{cx + r * (k + 0.2)}} ${{cy}} ${{cx + r * k}} ${{cy + r * 0.95}}" stroke="${{stitchColor}}" stroke-width="${{r * 0.025}}" fill="none" stroke-dasharray="8 6" opacity="0.85"/>`).join("")}}
          <!-- Brand Badge in center -->
          <g transform="translate(${{cx - r * 0.45}}, ${{cy - r * 0.2}})">
            <rect x="0" y="0" width="${{r * 0.9}}" height="${{r * 0.4}}" rx="${{r * 0.08}}" fill="rgba(0,0,0,0.35)"/>
            <text x="${{r * 0.45}}" y="${{r * 0.22}}" font-family="Anton" font-size="${{r * 0.16}}" fill="${{C.gold}}" text-anchor="middle">${{label}}</text>
            <text x="${{r * 0.45}}" y="${{r * 0.33}}" font-family="Anton" font-size="${{r * 0.10}}" fill="${{C.paper}}" text-anchor="middle">${{sub}}</text>
          </g>
          ${{ex}}
        </g>`;
      }};

      // Procedural Character Rig from Reference guy()
      function guy(id, x, y, s, o = {{}}) {{
        const skin = o.skin || "#E9B990", sk2 = o.sk2 || "#D69E73", hair = o.hair || "#5A3A22", m = o.m || "flat";
        const capCol = o.cap || C.green, capTrim = o.trim || "#0F3B2C", badgeCol = o.badge || C.gold;
        const mo = (n, h) => `<g class="m m-${{n}}" opacity="${{n === m ? 1 : 0}}">${{h}}</g>`;
        return `<g id="${{id}}"><g transform="translate(${{x}} ${{y}}) scale(${{s}})"><g class="cut">
<path d="M-250 430 Q-255 255 -105 218 L105 218 Q255 255 250 430Z" fill="${{o.jersey || C.paper}}"/>
<path d="M-62 218 L0 305 L62 218 L38 200 L-38 200Z" fill="${{o.collar || '#DDD5C0'}}"/>
<rect x="-46" y="150" width="92" height="95" rx="20" fill="${{sk2}}"/></g>
<g class="head cut">
<ellipse cx="-148" cy="15" rx="26" ry="40" fill="${{sk2}}"/><ellipse cx="148" cy="15" rx="26" ry="40" fill="${{sk2}}"/>
<rect x="-145" y="-160" width="290" height="345" rx="135" fill="${{skin}}"/>
${{o.beard ? `<path d="M-145 30 Q-150 190 0 187 Q150 190 145 30 Q118 150 0 152 Q-118 150 -145 30Z" fill="${{hair}}"/>` : ""}}
<path d="M-150 -60 L-150 -95 L-118 -95 L-128 -20Z M150 -60 L150 -95 L118 -95 L128 -20Z" fill="${{hair}}"/>
<!-- Cap / Headgear -->
<path d="M-158 -92 Q-160 -262 0 -262 Q160 -262 158 -92Z" fill="${{capCol}}"/>
<path d="M-176 -96 Q0 -132 176 -96 Q196 -62 0 -72 Q-196 -62 -176 -96Z" fill="${{capTrim}}"/>
<circle cx="0" cy="-185" r="30" fill="${{badgeCol}}"/>
<!-- Eyes & Eyebrows -->
<g class="eye"><circle cx="-62" cy="5" r="36" fill="#fff"/><circle class="pupil" cx="-62" cy="5" r="16" fill="${{C.ink}}"/></g>
<g class="eye"><circle cx="62" cy="5" r="36" fill="#fff"/><circle class="pupil" cx="62" cy="5" r="16" fill="${{C.ink}}"/></g>
<rect class="browL" x="-102" y="-58" width="80" height="17" rx="6" fill="${{hair}}"/><rect class="browR" x="22" y="-58" width="80" height="17" rx="6" fill="${{hair}}"/>
<!-- Nose -->
<path d="M-10 30 Q-4 72 22 62" stroke="${{sk2}}" stroke-width="9" fill="none" stroke-linecap="round"/>
${{o.zinc ? `<rect x="-14" y="24" width="28" height="48" rx="6" fill="#FFFFFF" stroke="${{sk2}}" stroke-width="3"/>` : ""}}
<!-- Mouth shapes -->
${{mo("flat", '<rect x="-44" y="112" width="88" height="13" rx="6" fill="#7A2E22"/>')}}
${{mo("o", '<ellipse cx="0" cy="118" rx="28" ry="32" fill="#4A1410"/>')}}
${{mo("smirk", '<path d="M-48 116 Q14 150 62 98" stroke="#7A2E22" stroke-width="13" fill="none" stroke-linecap="round"/>')}}
${{mo("frown", '<path d="M-48 138 Q0 98 48 138" stroke="#7A2E22" stroke-width="13" fill="none" stroke-linecap="round"/>')}}
${{mo("teeth", '<rect x="-58" y="96" width="116" height="46" rx="14" fill="#fff" stroke="#7A2E22" stroke-width="9"/><path d="M-20 98V140M20 98V140M-56 119H56" stroke="#C9B9A8" stroke-width="4"/>')}}
${{mo("talk", '<ellipse cx="0" cy="120" rx="34" ry="20" fill="#4A1410"/>')}}
</g></g></g>`;
      }}

      // Reference Stadium Ground Atmosphere (Sky, grandstand crowd, mown turf, pitch)
      const stadiumGround = () => {{
        let s = `<rect width="1080" height="660" fill="${{C.sky}}"/><rect y="600" width="1080" height="460" fill="#39424E"/>`;
        const cols = [C.paper, C.gold, C.red, C.green, "#5FA8C9", "#F2CE6B"];
        for (let r = 0; r < 7; r++)
          for (let c = 0; c < 19; c++)
            s += `<circle cx="${{(c * 60 + (r % 2 ? 30 : 0) + rnd() * 10).toFixed(0)}}" cy="${{640 + r * 56}}" r="21" fill="${{cols[Math.floor(rnd() * 6)]}}"/>`;
        return s + `<rect y="1040" width="1080" height="24" fill="${{C.paper}}"/><rect y="1064" width="1080" height="856" fill="${{C.turf}}"/><rect y="1064" width="1080" height="30" fill="${{C.turfDark}}"/>`;
      }};

      // Perspective Cricket Pitch Strip
      const pitchStrip = () =>
        `<polygon points="420,1080 660,1080 800,1920 280,1920" fill="${{C.pitch}}"/>
         <line x1="390" y1="1180" x2="690" y2="1180" stroke="#FFFFFF" stroke-width="8"/>
         <g transform="translate(515, 1150)">
           <rect x="0" y="0" width="8" height="30" fill="${{C.paper}}"/><rect x="16" y="0" width="8" height="30" fill="${{C.paper}}"/><rect x="32" y="0" width="8" height="30" fill="${{C.paper}}"/>
           <rect x="-3" y="-4" width="46" height="5" fill="${{C.paper}}"/>
         </g>`;

      // Stamp helper
      const stamp = (id, cx, cy, l1, l2, color = C.stamp) =>
        `<g id="${{id}}"><g transform="rotate(-8 ${{cx}} ${{cy}})"><rect x="${{cx - 300}}" y="${{cy - 95}}" width="600" height="190" rx="16" fill="rgba(246,241,228,.95)" stroke="${{color}}" stroke-width="12"/>${{tx(cx, cy - 8, 62, l1, color)}}${{tx(cx, cy + 54, 46, l2, color)}}</g></g>`;

      // ==========================================================
      // SCENE 1 ART: THREE BALLS HOOK & STAMP (0.00s - 7.50s)
      // "Australia, India and England DON'T play with the same cricket ball. And that changes everything."
      // ==========================================================
      reseed(101);
      put("s1", svg(
        stadiumGround() + pitchStrip() +
        // Top Header Banner
        `<g id="s1_hdr" class="cut"><g transform="rotate(-1 540 180)">${{sheet(80, 110, 920, 130, C.stamp, 8)}}${{tx(540, 195, 68, "⚡ TEST CRICKET'S SECRET INEQUALITY", C.paper)}}</g></g>` +
        // Three Bowlers on Ground:
        // Left: Pat Cummins (Australia)
        guy("cummins_s1", 200, 780, 0.62, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#5A3A22", cap: C.green, trim: "#0F3B2C", badge: C.gold, collar: C.green, m: "smirk" }}) +
        cricketBall("ball_cummins_s1", "koo", 200, 930, 65) +
        `<g id="tag_aus" class="cut">${{sheet(70, 1020, 260, 65, C.green, 6)}}${{tx(200, 1068, 36, "AUSTRALIA", C.gold)}}</g>` +
        // Center: Jasprit Bumrah (India)
        guy("bumrah_s1", 540, 750, 0.66, {{ skin: "#C68B59", sk2: "#A87042", hair: "#1B1B1B", cap: C.indiaBlue, trim: "#0D1B2A", badge: C.gold, collar: C.indiaBlue, beard: 1, m: "teeth" }}) +
        cricketBall("ball_bumrah_s1", "sg", 540, 915, 75) +
        `<g id="tag_ind" class="cut">${{sheet(410, 1010, 260, 65, C.indiaBlue, 6)}}${{tx(540, 1058, 36, "INDIA", C.paper)}}</g>` +
        // Right: Jimmy Anderson (England)
        guy("anderson_s1", 880, 780, 0.62, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#3A332C", cap: C.englandNavy, trim: "#081624", badge: C.gold, collar: C.englandNavy, m: "smirk" }}) +
        cricketBall("ball_anderson_s1", "dukes", 880, 930, 65) +
        `<g id="tag_eng" class="cut">${{sheet(750, 1020, 260, 65, C.englandNavy, 6)}}${{tx(880, 1068, 36, "ENGLAND", C.paper)}}</g>` +
        // Slam Stamp: "AND THAT CHANGES EVERYTHING!"
        `<g id="stamp_changes" class="cut" opacity="0"><g transform="rotate(4 540 450)">${{sheet(100, 380, 880, 140, C.gold, 10)}}${{tx(540, 475, 72, "⚡ AND THAT CHANGES EVERYTHING!", C.ink)}}</g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 2 ART: THE 3 BALL MAJORS (7.50s - 14.10s)
      // "Australia uses the Kookaburra. India uses the SG. England uses the Dukes."
      // ==========================================================
      reseed(202);
      put("s2", svg(
        `<rect width="1080" height="1920" fill="#202A24"/>` +
        rays("r2", 540, 960, 24, "#293730") +
        `<g id="s2_hdr" class="cut"><g transform="rotate(1 540 160)">${{sheet(140, 90, 800, 120, C.paper, 8)}}${{tx(540, 172, 60, "THE 3 TEST CRICKET BALLS", C.ink)}}</g></g>` +
        // Card 1: Kookaburra (Australia)
        `<g id="card_koo" class="cut" transform="translate(60, 260)">
          ${{sheet(0, 0, 960, 260, C.paper, 8)}}
          ${{cricketBall("s2_b_koo", "koo", 160, 130, 95)}}
          ${{tx(320, 90, 56, "KOOKABURRA TURF", C.green, "start")}}
          ${{tx(320, 150, 36, "AUSTRALIA • NZ • SOUTH AFRICA", C.ink, "start")}}
          ${{tx(320, 210, 32, "MACHINE STITCHED · FLAT EMBEDDED SEAM", "#555", "start")}}
        </g>` +
        // Card 2: SG (India)
        `<g id="card_sg" class="cut" transform="translate(60, 570)">
          ${{sheet(0, 0, 960, 260, C.paper, 8)}}
          ${{cricketBall("s2_b_sg", "sg", 160, 130, 95)}}
          ${{tx(320, 90, 56, "SG TEST (SANSPAREILS)", C.indiaBlue, "start")}}
          ${{tx(320, 150, 36, "INDIA EXCLUSIVE · ABRASIVE SOIL", C.ink, "start")}}
          ${{tx(320, 210, 32, "PROMINENT HAND-STITCHED THICK SEAM", "#555", "start")}}
        </g>` +
        // Card 3: Dukes (England)
        `<g id="card_dukes" class="cut" transform="translate(60, 880)">
          ${{sheet(0, 0, 960, 260, C.paper, 8)}}
          ${{cricketBall("s2_b_dukes", "dukes", 160, 130, 95)}}
          ${{tx(320, 90, 56, "DUKES SPECIAL MATCH", C.red, "start")}}
          ${{tx(320, 150, 36, "ENGLAND & WEST INDIES", C.ink, "start")}}
          ${{tx(320, 210, 32, "RAISED 6-ROW SEAM · DEEP GREASE LACQUER", "#555", "start")}}
        </g>`,
        "#1B221E"
      ));

      // ==========================================================
      // SCENE 3 ART: HOME BOARD PICKS BALL -> TOURING STRUGGLE (14.10s - 19.80s)
      // "In Test cricket, the home board picks the ball. That's why visiting teams struggle."
      // ==========================================================
      reseed(303);
      put("s3", svg(
        stadiumGround() + pitchStrip() +
        // ICC Regulation Card
        `<g id="icc_rule_card" class="cut"><g transform="rotate(-2 540 260)">${{sheet(100, 160, 880, 200, C.paper, 10)}}
          ${{tx(540, 235, 42, "OFFICIAL ICC TEST PLAYING CONDITIONS", C.stamp)}}
          ${{tx(540, 310, 64, "“THE HOME BOARD PICKS THE BALL”", C.ink)}}
        </g></g>` +
        // Smirking Home Captain (Cummins) vs Troubled Visiting Batter
        guy("cummins_s3", 300, 800, 0.72, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#5A3A22", cap: C.green, trim: "#0F3B2C", badge: C.gold, collar: C.green, m: "smirk" }}) +
        `<g id="tag_home" class="cut">${{sheet(150, 1100, 300, 75, C.green, 6)}}${{tx(300, 1152, 42, "HOST BOARD ADVANTAGE", C.gold)}}</g>` +
        // Visiting Batsman looking nervous/sweating
        guy("visiting_batter", 780, 800, 0.72, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#3A332C", cap: C.englandNavy, trim: "#081624", badge: C.gold, collar: C.englandNavy, m: "o" }}) +
        // Sweat droplets
        `<ellipse id="sweat1" cx="890" cy="720" rx="10" ry="16" fill="#88CCEE" opacity="0"/>` +
        `<ellipse id="sweat2" cx="880" cy="760" rx="8" ry="14" fill="#88CCEE" opacity="0"/>` +
        `<g id="tag_visitor" class="cut">${{sheet(630, 1100, 300, 75, C.red, 6)}}${{tx(780, 1152, 42, "VISITING BATTER", C.paper)}}</g>` +
        // Stamp: "VISITING TEAMS STRUGGLE!"
        `<g id="stamp_struggle" class="cut" opacity="0"><g transform="rotate(4 540 520)">${{sheet(120, 450, 840, 140, C.stamp, 8)}}${{tx(540, 540, 70, "VISITING TEAMS STRUGGLE!", C.paper)}}</g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 4 ART: BALL MECHANICS COMPARISON (19.80s - 29.40s)
      // "Kookaburra swings early, then goes soft. SG grips for spinners, and reverses as it ages. Dukes swings and seams for longer."
      // ==========================================================
      reseed(404);
      put("s4", svg(
        `<rect width="1080" height="1920" fill="#1C2420"/>` +
        rays("r4", 540, 960, 24, "#24302A") +
        `<g id="s4_hdr" class="cut"><g transform="rotate(-1 540 140)">${{sheet(100, 80, 880, 110, C.paper, 8)}}${{tx(540, 156, 56, "HOW EACH BALL BEHAVES", C.ink)}}</g></g>` +
        // 1. Kookaburra Behavior Card
        `<g id="s4_card_koo" class="cut" transform="translate(60, 220)">
          ${{sheet(0, 0, 960, 290, C.paper, 8)}}
          ${{cricketBall("s4_b1", "koo", 150, 145, 90)}}
          ${{tx(290, 85, 44, "KOOKABURRA: EARLY SWING, THEN SOFT", C.green, "start")}}
          ${{tx(290, 145, 34, "Fierce swing for 15-20 overs.", C.ink, "start")}}
          <!-- Progress timeline -->
          <rect x="290" y="170" width="620" height="36" rx="8" fill="#DDD"/>
          <rect x="290" y="170" width="220" height="36" rx="8" fill="${{C.gold}}"/>
          ${{tx(400, 196, 24, "SWING 15-20 OVERS", C.ink)}}
          ${{tx(680, 196, 24, "OVERS 20-80: SEAM FLATTENS & GOES SOFT", "#666")}}
          ${{tx(290, 250, 30, "➜ Batters cash in once ball goes soft!", C.stamp, "start")}}
        </g>` +
        // 2. SG Behavior Card
        `<g id="s4_card_sg" class="cut" transform="translate(60, 540)">
          ${{sheet(0, 0, 960, 290, C.paper, 8)}}
          ${{cricketBall("s4_b2", "sg", 150, 145, 90)}}
          ${{tx(290, 85, 44, "SG: SPINNER GRIP & LATE REVERSE", C.indiaBlue, "start")}}
          ${{tx(290, 145, 34, "Prominent upright seam grips dry dirt wickets.", C.ink, "start")}}
          <rect x="290" y="170" width="620" height="36" rx="8" fill="#DDD"/>
          <rect x="460" y="170" width="450" height="36" rx="8" fill="${{C.indiaBlue}}"/>
          ${{tx(370, 196, 24, "SPINNER GRIP", "#555")}}
          ${{tx(685, 196, 24, "OVERS 30-80: REVERSE SWING WEAPON!", C.paper)}}
          ${{tx(290, 250, 30, "➜ Abrasive outfield scuffs one side for late reverse!", C.indiaBlue, "start")}}
        </g>` +
        // 3. Dukes Behavior Card
        `<g id="s4_card_dukes" class="cut" transform="translate(60, 860)">
          ${{sheet(0, 0, 960, 290, C.paper, 8)}}
          ${{cricketBall("s4_b3", "dukes", 150, 145, 90)}}
          ${{tx(290, 85, 44, "DUKES: RELENTLESS SWING & SEAM", C.red, "start")}}
          ${{tx(290, 145, 34, "Hand-stitched spine keeps seam erect for 70+ overs.", C.ink, "start")}}
          <rect x="290" y="170" width="620" height="36" rx="8" fill="${{C.red}}"/>
          ${{tx(600, 196, 24, "SWING & SEAM MOVEMENT LASTS 60-70+ OVERS NON-STOP", C.gold)}}
          ${{tx(290, 250, 30, "➜ Visiting openers fight moving ball all day!", C.stamp, "start")}}
        </g>`,
        "#171F1B"
      ));

      // ==========================================================
      // SCENE 5 ART: WHAT IF ONE BALL EVERYWHERE? (29.40s - 37.10s)
      // "So what if everyone used ONE ball? Visiting batters wouldn't get exposed as badly. Home advantage would shrink."
      // ==========================================================
      reseed(505);
      put("s5", svg(
        stadiumGround() + pitchStrip() +
        `<g id="s5_hdr" class="cut"><g transform="rotate(-1 540 180)">${{sheet(80, 110, 920, 130, C.gold, 10)}}${{tx(540, 198, 66, "SO WHAT IF EVERYONE USED ONE BALL?", C.ink)}}</g></g>` +
        // Side by Side Comparison Cards
        // Left Card: Batter Protected
        `<g id="card_fair" class="cut" transform="translate(60, 320)">
          ${{sheet(0, 0, 460, 720, C.paper, 8)}}
          ${{guy("fair_batter", 230, 340, 0.65, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#3A332C", cap: C.indiaBlue, badge: C.gold, collar: C.indiaBlue, m: "smirk" }})}}
          ${{sheet(20, 20, 420, 75, C.green, 6)}}
          ${{tx(230, 70, 36, "VISITING BATTERS", C.paper)}}
          ${{tx(230, 560, 44, "NO BALL AMBUSH!", C.ink)}}
          ${{tx(230, 620, 30, "Familiar seam & bounce", "#666")}}
          ${{tx(230, 660, 30, "Fair global test trial", "#666")}}
        </g>` +
        // Right Card: Home Advantage Shrinks
        `<g id="card_shrink" class="cut" transform="translate(560, 320)">
          ${{sheet(0, 0, 460, 720, C.paper, 8)}}
          ${{guy("shocked_bowler", 230, 340, 0.65, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#5A3A22", cap: C.green, badge: C.gold, collar: C.green, m: "o" }})}}
          ${{sheet(20, 20, 420, 75, C.stamp, 6)}}
          ${{tx(230, 70, 36, "HOME ADVANTAGE", C.paper)}}
          ${{tx(230, 560, 44, "WOULD SHRINK!", C.stamp)}}
          ${{tx(230, 620, 30, "No secret ball tricks", "#666")}}
          ${{tx(230, 660, 30, "Home fortress weakens", "#666")}}
        </g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 6 ART: PITCHES, WEATHER & SOUL OF CRICKET (37.10s - 44.20s)
      // "But pitches and weather would still decide matches. And some fans say... the ball is part of cricket's character."
      // ==========================================================
      reseed(606);
      put("s6", svg(
        stadiumGround() + pitchStrip() +
        // Pitch & Weather Banner
        `<g id="s6_hdr" class="cut"><g transform="rotate(1 540 180)">${{sheet(80, 110, 920, 130, C.paper, 8)}}${{tx(540, 198, 58, "PITCHES & WEATHER STILL REIGN SUPREME!", C.ink)}}</g></g>` +
        // Weather & Conditions Board
        `<g id="card_conditions" class="cut" transform="translate(70, 280)">
          ${{sheet(0, 0, 940, 340, C.paper, 8)}}
          ${{tx(470, 70, 46, "PERTH BOUNCE • LORD'S SLOPE • KANPUR DUST", C.stamp)}}
          <!-- Condition Icons / Torn Badges -->
          <g transform="translate(50, 110)">${{sheet(0, 0, 250, 180, "#E8F0F8", 6)}}${{tx(125, 60, 32, "☁️ ENGLAND", C.indiaBlue)}}${{tx(125, 110, 26, "Overcast Clouds", C.ink)}}${{tx(125, 145, 26, "& Relentless Swing", C.ink)}}</g>
          <g transform="translate(345, 110)">${{sheet(0, 0, 250, 180, "#FDF2E9", 6)}}${{tx(125, 60, 32, "☀️ AUSTRALIA", C.green)}}${{tx(125, 110, 26, "Hard Baked Turf", C.ink)}}${{tx(125, 145, 26, "& Steep Bounce", C.ink)}}</g>
          <g transform="translate(640, 110)">${{sheet(0, 0, 250, 180, "#FEF9E7", 6)}}${{tx(125, 60, 32, "🌪️ INDIA", C.stamp)}}${{tx(125, 110, 26, "Dry Turning Soil", C.ink)}}${{tx(125, 145, 26, "& Reverse Magic", C.ink)}}</g>
        </g>` +
        // Heritage Soul Card
        `<g id="card_soul" class="cut" transform="translate(70, 680)">
          ${{sheet(0, 0, 940, 420, "#1C1A17", 8)}}
          ${{sheet(15, 15, 910, 390, "none", 0)}}
          <polygon points="${{torn(20, 20, 900, 380, 6)}}" fill="none" stroke="${{C.gold}}" stroke-width="4"/>
          <!-- 3 Balls aligned horizontally -->
          ${{cricketBall("s6_b1", "koo", 220, 180, 80)}}
          ${{cricketBall("s6_b2", "sg", 470, 180, 80)}}
          ${{cricketBall("s6_b3", "dukes", 720, 180, 80)}}
          ${{tx(470, 80, 42, "CRICKET'S SOUL & CRAFT", C.gold)}}
          ${{tx(470, 320, 52, "“THE BALL IS PART OF CRICKET’S CHARACTER”", C.paper)}}
          ${{tx(470, 370, 32, "Different balls require different mastery.", C.gold)}}
        </g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 7 ART: THE BIG DEBATE & PINNED COMMENT CARD (44.20s - 49.95s)
      // "So should cricket use ONE ball everywhere? Or keep the chaos? Comment below."
      // ==========================================================
      reseed(707);
      put("s7", svg(
        stadiumGround() + pitchStrip() +
        `<g id="s7_hdr" class="cut"><g transform="rotate(-1 540 180)">${{sheet(80, 110, 920, 130, C.paper, 8)}}${{tx(540, 198, 64, "SHOULD TEST CRICKET USE ONE BALL?", C.stamp)}}</g></g>` +
        // Option A: ONE BALL EVERYWHERE
        `<g id="btn_one" class="cut" transform="translate(60, 280)">
          ${{sheet(0, 0, 960, 230, C.paper, 8)}}
          ${{guy("cummins_vote", 130, 90, 0.40, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#5A3A22", cap: C.green, badge: C.gold, collar: C.green, m: "smirk" }})}}
          <circle cx="250" cy="115" r="50" fill="${{C.indiaBlue}}"/>
          ${{tx(250, 134, 52, "A", C.paper)}}
          ${{tx(330, 95, 56, "ONE BALL EVERYWHERE", C.indiaBlue, "start")}}
          ${{tx(330, 155, 34, "Standardize test matches for global fairness.", C.ink, "start")}}
          ${{sheet(330, 175, 230, 40, C.indiaBlue, 4)}}
          ${{tx(445, 203, 24, "UNIFIED FAIR TEST", C.paper)}}
        </g>` +
        // Option B: KEEP THE CHAOS!
        `<g id="btn_chaos" class="cut" transform="translate(60, 540)">
          ${{sheet(0, 0, 960, 230, C.paper, 8)}}
          ${{guy("bumrah_vote", 130, 90, 0.40, {{ skin: "#C68B59", sk2: "#A87042", hair: "#1B1B1B", cap: C.indiaBlue, badge: C.gold, collar: C.indiaBlue, beard: 1, m: "teeth" }})}}
          <circle cx="250" cy="115" r="50" fill="${{C.stamp}}"/>
          ${{tx(250, 134, 52, "B", C.paper)}}
          ${{tx(330, 95, 56, "KEEP THE CHAOS!", C.stamp, "start")}}
          ${{tx(330, 155, 34, "Preserve pitch heritage, ball quirks & tradition.", C.ink, "start")}}
          ${{sheet(330, 175, 230, 40, C.stamp, 4)}}
          ${{tx(445, 203, 24, "PURE TRADITION", C.paper)}}
        </g>` +
        // Pinned Debate Card (Prominent Call to Action)
        `<g id="pinned_card" class="cut" transform="translate(70, 800)">
          ${{sheet(0, 0, 940, 290, C.paper, 8)}}
          <polygon points="${{torn(15, 15, 910, 260, 6)}}" fill="none" stroke="${{C.stamp}}" stroke-width="6"/>
          ${{tx(470, 75, 52, "📌 PINNED DEBATE", C.stamp)}}
          ${{tx(470, 155, 64, "COMMENT: A OR B?", C.ink)}}
          ${{tx(470, 220, 36, "ONE BALL EVERYWHERE OR KEEP THE CHAOS?", C.stamp)}}
        </g>`,
        C.dgreen
      ));

      // ==========================================================
      // TORN PAPER SCENE TRANSITION WIPE
      // ==========================================================
      reseed(888);
      document.querySelector("#wipe").innerHTML = `<svg viewBox="0 0 1500 2300" width="1500" height="2300" xmlns="http://www.w3.org/2000/svg">
        <g class="cut"><polygon points="${{torn(0, 0, 1500, 2300, 25)}}" fill="${{C.paper}}"/></g>
      </svg>`;

      // ==========================================================
      // GSAP MASTER TIMELINE & STOP-MOTION PAPER ANIMATION
      // ==========================================================
      const tl = gsap.timeline({{ paused: true }});

      // Helper animation functions matching reference
      const wipe = (t) =>
        tl.fromTo("#wipe", {{ x: -2200 }}, {{ x: 1200, duration: 0.55, ease: "power2.inOut" }}, t - 0.28);
      const pop = (el, t, s = 1.08) =>
        tl.fromTo(el, {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.42, ease: "back.out(2)" }}, t);
      const slam = (el, t, rot = -8) =>
        tl.fromTo(el, {{ scale: 2.2, opacity: 0, rotation: rot * 2.5 }}, {{ scale: 1, opacity: 1, rotation: rot, duration: 0.38, ease: "power4.in" }}, t);
      const shake = (el, t, mag = 18) => {{
        tl.to(el, {{ x: mag, y: -mag * 0.5, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }}, t)
          .to(el, {{ x: 0, y: 0, duration: 0.05 }}, t + 0.3);
      }};
      const zoom = (id, t0, dur, z0 = 1, z1 = 1.08) =>
        tl.fromTo("#" + id + " .cam", {{ scale: z0 }}, {{ scale: z1, duration: dur, ease: "none" }}, t0);

      // Procedural character face expressions & eye tracking
      const face = (id, t, o) => {{
        const g = "#" + id;
        if (o.m) {{
          tl.set(g + " .m", {{ opacity: 0 }}, t);
          tl.set(g + " .m-" + o.m, {{ opacity: 1 }}, t);
        }}
        if (o.p) tl.to(g + " .pupil", {{ x: o.p[0], y: o.p[1], duration: 0.25, ease: "power1.out" }}, t);
        if (o.b) {{
          tl.to(g + " .browL", {{ y: o.b[0], rotation: o.b[2] || 0, duration: 0.25 }}, t);
          tl.to(g + " .browR", {{ y: o.b[1], rotation: -(o.b[2] || 0), duration: 0.25 }}, t);
        }}
      }};

      // Scene transition wipes
      [7.50, 14.10, 19.80, 29.40, 37.10, 44.20].forEach((t) => wipe(t));

      // ----------------------------------------------------------
      // SCENE 1 (0.00s - 7.50s): AUSTRALIA, INDIA, ENGLAND DON'T PLAY WITH SAME BALL
      // ----------------------------------------------------------
      zoom("s1", 0.00, 7.50, 1, 1.06);
      pop("#s1_hdr", 0.1);
      // Bowlers look at each other
      face("cummins_s1", 1.2, {{ p: [12, -4], m: "smirk" }});
      face("bumrah_s1", 1.8, {{ p: [-14, 0], m: "teeth" }});
      face("anderson_s1", 2.4, {{ p: [-12, -4], m: "smirk" }});
      // Ball pulses in hands
      tl.to("#ball_cummins_s1", {{ scale: 1.15, duration: 0.3, yoyo: true, repeat: 1 }}, 1.2);
      tl.to("#ball_bumrah_s1", {{ scale: 1.15, duration: 0.3, yoyo: true, repeat: 1 }}, 2.0);
      tl.to("#ball_anderson_s1", {{ scale: 1.15, duration: 0.3, yoyo: true, repeat: 1 }}, 2.8);
      // Slam "AND THAT CHANGES EVERYTHING!"
      slam("#stamp_changes", 4.85, 4);
      shake("#s1 .cam", 4.90, 26);
      face("bumrah_s1", 4.90, {{ m: "o", b: [-14, 14, -10] }});

      // ----------------------------------------------------------
      // SCENE 2 (7.50s - 14.10s): THE 3 BALL MAJORS
      // ----------------------------------------------------------
      zoom("s2", 7.50, 6.60, 1, 1.08);
      tl.fromTo("#r2", {{ rotation: 0 }}, {{ rotation: 35, duration: 6.60, ease: "none" }}, 7.50);
      pop("#s2_hdr", 7.60);
      // Kookaburra Card pops
      pop("#card_koo", 7.75);
      tl.fromTo("#s2_b_koo", {{ rotation: -120 }}, {{ rotation: 0, duration: 0.5, ease: "back.out(2)" }}, 7.80);
      // SG Card pops
      pop("#card_sg", 9.85);
      tl.fromTo("#s2_b_sg", {{ rotation: 120 }}, {{ rotation: 0, duration: 0.5, ease: "back.out(2)" }}, 9.90);
      // Dukes Card pops
      pop("#card_dukes", 11.95);
      tl.fromTo("#s2_b_dukes", {{ rotation: -120 }}, {{ rotation: 0, duration: 0.5, ease: "back.out(2)" }}, 12.00);

      // ----------------------------------------------------------
      // SCENE 3 (14.10s - 19.80s): HOME BOARD PICKS BALL -> TOURING STRUGGLE
      // ----------------------------------------------------------
      zoom("s3", 14.10, 5.70, 1, 1.06);
      pop("#icc_rule_card", 14.20);
      face("cummins_s3", 15.00, {{ m: "smirk", p: [14, 0] }});
      // Batter sweats and looks panicked
      face("visiting_batter", 15.50, {{ m: "o", b: [-16, 16, -12], p: [-14, -4] }});
      tl.to("#sweat1", {{ opacity: 1, y: 30, duration: 0.5 }}, 16.00);
      tl.to("#sweat2", {{ opacity: 1, y: 30, duration: 0.5 }}, 16.60);
      // Slam "VISITING TEAMS STRUGGLE!"
      slam("#stamp_struggle", 17.55, -6);
      shake("#s3 .cam", 17.60, 24);

      // ----------------------------------------------------------
      // SCENE 4 (19.80s - 29.40s): BALL BEHAVIOR MECHANICS
      // ----------------------------------------------------------
      zoom("s4", 19.80, 9.60, 1, 1.06);
      tl.fromTo("#r4", {{ rotation: 0 }}, {{ rotation: 40, duration: 9.60, ease: "none" }}, 19.80);
      pop("#s4_hdr", 19.90);
      // Kookaburra goes soft
      pop("#s4_card_koo", 20.00);
      tl.fromTo("#s4_b1", {{ scale: 0.4, rotation: -90 }}, {{ scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }}, 20.05);
      // SG reverse weapon
      pop("#s4_card_sg", 22.70);
      tl.fromTo("#s4_b2", {{ scale: 0.4, rotation: 90 }}, {{ scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }}, 22.75);
      // Dukes relentless seam
      pop("#s4_card_dukes", 26.60);
      tl.fromTo("#s4_b3", {{ scale: 0.4, rotation: -90 }}, {{ scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }}, 26.65);

      // ----------------------------------------------------------
      // SCENE 5 (29.40s - 37.10s): WHAT IF ONE BALL?
      // ----------------------------------------------------------
      zoom("s5", 29.40, 7.70, 1, 1.06);
      pop("#s5_hdr", 29.50);
      pop("#card_fair", 32.20);
      face("fair_batter", 32.50, {{ m: "smirk", p: [8, 0] }});
      pop("#card_shrink", 35.15);
      face("shocked_bowler", 35.30, {{ m: "o", b: [-14, 14, -12], p: [-10, 0] }});
      shake("#card_shrink", 35.40, 16);

      // ----------------------------------------------------------
      // SCENE 6 (37.10s - 44.20s): PITCHES, WEATHER & SOUL OF CRICKET
      // ----------------------------------------------------------
      zoom("s6", 37.10, 7.10, 1, 1.06);
      pop("#s6_hdr", 37.20);
      pop("#card_conditions", 37.40);
      pop("#card_soul", 40.30);
      // Balls shimmer on certificate
      tl.to("#s6_b1", {{ scale: 1.1, duration: 0.3, yoyo: true, repeat: 1 }}, 41.20);
      tl.to("#s6_b2", {{ scale: 1.1, duration: 0.3, yoyo: true, repeat: 1 }}, 41.80);
      tl.to("#s6_b3", {{ scale: 1.1, duration: 0.3, yoyo: true, repeat: 1 }}, 42.40);

      // ----------------------------------------------------------
      // SCENE 7 (44.20s - 49.95s): SHOULD CRICKET USE ONE BALL? PINNED DEBATE
      // ----------------------------------------------------------
      zoom("s7", 44.20, 5.75, 1, 1.06);
      pop("#s7_hdr", 44.30);
      pop("#btn_one", 44.50);
      face("cummins_vote", 44.80, {{ m: "smirk" }});
      pop("#btn_chaos", 47.15);
      face("bumrah_vote", 47.30, {{ m: "teeth" }});
      // Pinned debate card slams
      slam("#pinned_card", 47.60, -4);
      shake("#s7 .cam", 47.65, 20);

      // Standalone Clip & Scene Activation (Guarantees exact frame-by-frame visibility for Playwright renderer)
      function updateClips(time) {{
        document.querySelectorAll(".clip").forEach(el => {{
          const start = parseFloat(el.getAttribute("data-start"));
          const dur = parseFloat(el.getAttribute("data-duration"));
          if (!isNaN(start) && !isNaN(dur)) {{
            const isVisible = (time >= start && time < start + dur);
            el.style.display = isVisible ? "block" : "none";
          }}
        }});
      }}

      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
      window.seekFrame = function(timeInSeconds) {{
        updateClips(timeInSeconds);
        tl.seek(timeInSeconds);
      }};
      window.seekFrame(0);
    </script>
  </body>
</html>
"""

    with open(out_standalone, "w", encoding="utf-8") as f:
        f.write(html)
    with open(out_index, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated reference-styled standalone.html ({len(html)/1024:.1f} KB)")
    print(f"Successfully generated reference-styled index.html ({len(html)/1024:.1f} KB)")

if __name__ == "__main__":
    build()
