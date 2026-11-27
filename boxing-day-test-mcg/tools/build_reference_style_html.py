import os
import json
import base64

def build():
    base_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\boxing-day-test-mcg"
    out_standalone = os.path.join(base_dir, "standalone.html")
    out_index = os.path.join(base_dir, "index.html")

    # Read and inline GSAP & Font for 100% self-contained standalone execution
    gsap_path = os.path.join(base_dir, "assets", "gsap.min.js")
    with open(gsap_path, "r", encoding="utf-8") as f:
        gsap_source = f.read()

    font_path = os.path.join(base_dir, "assets", "fonts", "Anton-Regular.ttf")
    with open(font_path, "rb") as f:
        font_b64 = base64.b64encode(f.read()).decode("utf-8")

    # Speech segment aligned captions
    # Speech timeline:
    # 0.03 - 1.38: "A nineteen-year-old."
    # 1.67 - 2.82: "His Test debut."
    # 3.42 - 6.40: "Jasprit Bumrah running in... and he ramp-shots him!"
    # 6.69 - 10.65: "Nearly ninety thousand people at the MCG went wild."
    # 11.11 - 12.06: "On Boxing Day."
    # 12.43 - 14.65: "So what IS Boxing Day cricket?"
    # 15.17 - 20.61: "Every year on the twenty-sixth of December, Australia starts a Test match at the Melbourne Cricket Ground."
    # 20.91 - 24.28: "Families skip the Christmas leftovers... and fill the stadium."
    # 24.53 - 26.84: "It's one of the biggest days in world cricket."
    # 27.23 - 28.95: "And it creates legends."
    # 29.39 - 31.93: "Shane Warne took a hat-trick here against England."
    # 32.38 - 37.21: "In twenty twenty, Ajinkya Rahane scored a hundred, and India came back to win."
    # 37.63 - 39.42: "So why 'Boxing Day'?"
    # 39.86 - 41.60: "It's a public holiday in Australia."
    # 41.87 - 42.89: "Everyone's off work."
    # 43.17 - 45.03: "So everyone goes to the cricket."
    # 45.40 - 46.95: "Christmas is for family."
    # 47.35 - 49.33: "Boxing Day is for TEST CRICKET."
    # 49.82 - 51.40: "Best Boxing Day moment you've seen?"
    # 51.73 - 52.61: "Comment below."

    caps = [
        {"start": 0.00, "dur": 1.50, "html": "<span>A <i>nineteen-year-old.</i></span>"},
        {"start": 1.50, "dur": 1.70, "html": "<span>His <b>Test debut.</b></span>"},
        {"start": 3.20, "dur": 3.49, "html": "<span>Bumrah running in... and he <b>ramp-shots him!</b></span>"},
        {"start": 6.69, "dur": 4.10, "html": "<span>Nearly <b>90,000 people</b> at the MCG went wild.</span>"},
        {"start": 10.80, "dur": 1.60, "html": "<span>On <i>Boxing Day.</i></span>"},
        {"start": 12.40, "dur": 2.60, "html": "<span>So what <i>IS</i> Boxing Day cricket?</span>"},
        {"start": 15.00, "dur": 5.80, "html": "<span>Every <b>26th of December</b>, Australia starts at the <i>MCG.</i></span>"},
        {"start": 20.80, "dur": 3.60, "html": "<span>Families skip <b>Christmas leftovers</b>... and fill the stadium.</span>"},
        {"start": 24.40, "dur": 2.50, "html": "<span>One of the <b>biggest days</b> in world cricket.</span>"},
        {"start": 26.90, "dur": 2.30, "html": "<span>And it creates <i>legends.</i></span>"},
        {"start": 29.20, "dur": 3.00, "html": "<span><b>Shane Warne</b> took a hat-trick here against England.</span>"},
        {"start": 32.20, "dur": 5.20, "html": "<span>In 2020, <b>Ajinkya Rahane</b> hit 100 and India won.</span>"},
        {"start": 37.40, "dur": 2.20, "html": "<span>So why <i>'Boxing Day'?</i></span>"},
        {"start": 39.60, "dur": 2.10, "html": "<span>It's a <b>public holiday</b> in Australia.</span>"},
        {"start": 41.70, "dur": 1.40, "html": "<span>Everyone's <i>off work.</i></span>"},
        {"start": 43.10, "dur": 2.10, "html": "<span>So everyone goes to <b>the cricket.</b></span>"},
        {"start": 45.20, "dur": 1.90, "html": "<span>Christmas is for <i>family.</i></span>"},
        {"start": 47.10, "dur": 2.40, "html": "<span>Boxing Day is for <b>TEST CRICKET.</b></span>"},
        {"start": 49.50, "dur": 1.90, "html": "<span>Best Boxing Day moment <b>you've seen?</b></span>"},
        {"start": 51.40, "dur": 1.21, "html": "<span><b>Comment below.</b></span>"}
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
      .cap {{ position: absolute; left: 50px; width: 980px; top: 1280px; height: 230px; z-index: 10; text-align: center; pointer-events: none; }}
      .cap span {{
        display: inline-block; max-width: 960px; padding: 14px 34px 20px; background: #f6f1e4; color: #1b1b1b;
        font-size: 80px; line-height: 1.06; letter-spacing: 1px; text-transform: uppercase;
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.35));
        opacity: 0;
      }}
      .cap b {{ font-weight: 400; color: #c1121f; }}
      .cap i {{ font-style: normal; background: #e3b23c; padding: 0 12px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="52.61" data-width="1080" data-height="1920">
      <!-- SCENES -->
      <!-- s1: 0.00s - 6.69s (19yo + Ramp shot showdown) -->
      <div id="s1" class="clip scene" data-start="0" data-duration="6.69"><div class="cam"></div></div>
      <!-- s2: 6.69s - 12.40s (90,000 MCG crowd wild) -->
      <div id="s2" class="clip scene" data-start="6.69" data-duration="5.71"><div class="cam"></div></div>
      <!-- s3: 12.40s - 20.80s (What is Boxing Day? 26 Dec Test match) -->
      <div id="s3" class="clip scene" data-start="12.40" data-duration="8.40"><div class="cam"></div></div>
      <!-- s4: 20.80s - 26.90s (Families skip leftovers / world cricket) -->
      <div id="s4" class="clip scene" data-start="20.80" data-duration="6.10"><div class="cam"></div></div>
      <!-- s5a: 26.90s - 32.20s (Creates legends: Shane Warne hat-trick 1994) -->
      <div id="s5a" class="clip scene" data-start="26.90" data-duration="5.30"><div class="cam"></div></div>
      <!-- s5b: 32.20s - 37.50s (Ajinkya Rahane 2020 century comeback) -->
      <div id="s5b" class="clip scene" data-start="32.20" data-duration="5.30"><div class="cam"></div></div>
      <!-- s6: 37.50s - 45.20s (Public holiday / Off work / Goes to cricket) -->
      <div id="s6" class="clip scene" data-start="37.50" data-duration="7.70"><div class="cam"></div></div>
      <!-- s7: 45.20s - 49.50s (Christmas is for family / Boxing Day is for TEST CRICKET) -->
      <div id="s7" class="clip scene" data-start="45.20" data-duration="4.30"><div class="cam"></div></div>
      <!-- s8: 49.50s - 52.61s (Pinned Debate Comment Card & CTA) -->
      <div id="s8" class="clip scene" data-start="49.50" data-duration="3.11"><div class="cam"></div></div>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- CAPTION OVERLAYS -->
{cap_divs}
    </div>

    <script>
      // ---------- DETERMINISTIC SEED & HELPERS (Direct from Reference) ----------
      let seed = 7;
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
        sky: "#BFD9E6",
        turf: "#6F9A4B",
        turfDark: "#5E8744",
        pitch: "#D9BC82"
      }};
      const svg = (inner, bg) =>
        `<svg viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg"><rect width="1080" height="1920" fill="${{bg}}"/>${{inner}}</svg>`;
      const put = (id, html) => (document.querySelector("#" + id + " .cam").innerHTML = html);
      const tx = (x, y, s, str, fill, anc = "middle", ex = "") =>
        `<text x="${{x}}" y="${{y}}" font-family="Anton" font-size="${{s}}" fill="${{fill}}" text-anchor="${{anc}}" ${{ex}}>${{str}}</text>`;

      // Torn Paper Generator (Jagged hand-crafted paper cut)
      function torn(x, y, w, h, j = 10, step = 40) {{
        const p = [];
        for (let i = 0; i <= w; i += step) p.push([x + Math.min(i, w), y + (rnd() - 0.5) * j]);
        for (let i = step; i <= h; i += step) p.push([x + w + (rnd() - 0.5) * j, y + Math.min(i, h)]);
        for (let i = w - step; i >= 0; i -= step) p.push([x + Math.max(i, 0), y + h + (rnd() - 0.5) * j]);
        for (let i = h - step; i > 0; i -= step) p.push([x + (rnd() - 0.5) * j, y + i]);
        return p.map((q) => q[0].toFixed(1) + "," + q[1].toFixed(1)).join(" ");
      }}
      const sheet = (x, y, w, h, fill, j = 10) => `<polygon points="${{torn(x, y, w, h, j)}}" fill="${{fill}}"/>`;

      // Spinning Rays
      const rays = (id, cx, cy, n, c) => {{
        let s = `<g id="${{id}}">`;
        for (let i = 0; i < n; i += 2) {{
          const a = (i * 2 * Math.PI) / n, b = ((i + 1) * 2 * Math.PI) / n;
          s += `<polygon points="${{cx}},${{cy}} ${{(cx + 1900 * Math.cos(a)).toFixed(0)}},${{(cy + 1900 * Math.sin(a)).toFixed(0)}} ${{(cx + 1900 * Math.cos(b)).toFixed(0)}},${{(cy + 1900 * Math.sin(b)).toFixed(0)}}" fill="${{c}}"/>`;
        }}
        return s + "</g>";
      }};

      // Red Cricket Ball with paper stitches
      const ball = (id, cx, cy, r, ex = "") =>
        `<g id="${{id}}" class="cut"><circle cx="${{cx}}" cy="${{cy}}" r="${{r}}" fill="${{C.red}}"/><path d="M${{cx - r * 0.62}} ${{cy - r * 0.5}} A${{r * 0.75}} ${{r * 0.75}} 0 0 1 ${{cx - r * 0.1}} ${{cy - r * 0.82}}" stroke="#D9574A" stroke-width="${{r * 0.09}}" fill="none" stroke-linecap="round"/>${{[-0.09, 0.09]
          .map((k) => `<path d="M${{cx + r * k}} ${{cy - r * 0.98}} Q${{cx + r * (k + 0.34)}} ${{cy}} ${{cx + r * k}} ${{cy + r * 0.98}}" stroke="${{C.paper}}" stroke-width="${{r * 0.035}}" fill="none" stroke-dasharray="${{r * 0.07}} ${{r * 0.06}}"/>`)
          .join("")}}${{ex}}</g>`;

      // Particle scraps for explosions/hits
      const scraps = (cls, cx, cy, n, colorA = C.gold, colorB = C.green) => {{
        let s = "";
        for (let i = 0; i < n; i++) {{
          const w = 30 + rnd() * 50;
          s += `<polygon class="${{cls}}" points="${{cx}},${{cy}} ${{(cx + w).toFixed(0)}},${{(cy + rnd() * 20).toFixed(0)}} ${{(cx + w * 0.6).toFixed(0)}},${{(cy + w * 0.8).toFixed(0)}}" fill="${{i % 2 ? colorA : colorB}}" opacity="0"/>`;
        }}
        return s;
      }};

      // Character Rig (Identical in geometry and API to Reference guy())
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

      // Classic Reference Stadium Ground Atmosphere
      const stadium = () => {{
        let s = `<rect width="1080" height="700" fill="${{C.sky}}"/><rect y="640" width="1080" height="420" fill="#39424E"/>`;
        const cols = [C.paper, C.gold, C.red, C.green, "#5FA8C9", "#F2CE6B"];
        for (let r = 0; r < 7; r++)
          for (let c = 0; c < 19; c++)
            s += `<circle cx="${{(c * 60 + (r % 2 ? 30 : 0) + rnd() * 10).toFixed(0)}}" cy="${{680 + r * 56}}" r="21" fill="${{cols[Math.floor(rnd() * 6)]}}"/>`;
        return s + `<rect y="1060" width="1080" height="24" fill="${{C.paper}}"/><rect y="1084" width="1080" height="836" fill="${{C.turf}}"/><rect y="1084" width="1080" height="30" fill="${{C.turfDark}}"/>`;
      }};

      // Full pitch perspective strip (for classic ground match showdown)
      const pitchStrip = () =>
        `<polygon points="420,1100 660,1100 780,1920 300,1920" fill="${{C.pitch}}"/>
         <line x1="390" y1="1200" x2="690" y2="1200" stroke="#FFFFFF" stroke-width="8"/>
         <g transform="translate(515, 1170)">
           <rect x="0" y="0" width="8" height="30" fill="${{C.paper}}"/><rect x="16" y="0" width="8" height="30" fill="${{C.paper}}"/><rect x="32" y="0" width="8" height="30" fill="${{C.paper}}"/>
           <rect x="-3" y="-4" width="46" height="5" fill="${{C.paper}}"/>
         </g>`;

      // Stamp helper (Generous width to prevent text clipping)
      const stamp = (id, cx, cy, l1, l2, color = C.stamp) =>
        `<g id="${{id}}"><g transform="rotate(-10 ${{cx}} ${{cy}})"><rect x="${{cx - 260}}" y="${{cy - 90}}" width="520" height="180" rx="16" fill="rgba(246,241,228,.92)" stroke="${{color}}" stroke-width="12"/>${{tx(cx, cy - 6, 66, l1, color)}}${{tx(cx, cy + 58, 46, l2, color)}}</g></g>`;

      // ==========================================================
      // SCENE 1 ART: "19 YEARS OLD" ON FRAME 1 & RAMP SHOT (0 - 6.69s)
      // USER REQUIREMENT: 19 YEARS OLD visible on frame 1, high energy!
      // ==========================================================
      reseed(101);
      const s1_bg = stadium() + pitchStrip();
      const s1_bat = `<g id="konstas_bat" class="cut" transform="translate(680 720) rotate(-55)">
        <rect x="0" y="0" width="36" height="240" rx="6" fill="${{C.gold}}"/>
        <rect x="10" y="-80" width="16" height="85" rx="4" fill="${{C.green}}"/>
        <rect x="4" y="40" width="28" height="40" fill="${{C.green}}"/>
        ${{tx(18, 68, 16, "KOOKA", C.gold)}}
      </g>`;
      put("s1", svg(
        s1_bg +
        // Bumrah bowling in Indian whites + blue headband
        guy("bumrah", 280, 840, 0.72, {{ skin: "#C68B59", sk2: "#A87042", hair: "#1B1B1B", cap: C.indiaBlue, trim: "#0D1B2A", badge: C.gold, beard: 1, collar: "#003566", m: "teeth" }}) +
        `<g id="bumrah_tag" class="cut">${{sheet(130, 1140, 310, 84, C.indiaBlue, 8)}}${{tx(285, 1202, 46, "JASPRIT BUMRAH", C.paper)}}</g>` +
        // Sam Konstas in Australian whites + Baggy Green
        guy("konstas", 780, 840, 0.72, {{ skin: "#E9B990", sk2: "#D69E73", hair: "#5A3A22", cap: C.green, trim: "#0F3B2C", badge: C.gold, collar: C.green, m: "o" }}) +
        s1_bat +
        `<g id="konstas_tag" class="cut">${{sheet(630, 1140, 310, 84, C.green, 8)}}${{tx(785, 1202, 46, "SAM KONSTAS (19)", C.gold)}}</g>` +
        // Delivery red cricket ball
        ball("s1_ball", 380, 780, 42) +
        // Dotted ramp flight path
        `<path id="ramp_path" d="M680 680 Q760 380 960 260" stroke="${{C.gold}}" stroke-width="12" stroke-dasharray="24 16" fill="none" opacity="0"/>` +
        // Bat crack starburst scraps
        scraps("s1_crack", 680, 680, 16, C.gold, C.red) +
        // USER REQUIREMENT: "19 YEARS OLD" ON FIRST FRAME!
        `<g id="hdr_19yo" class="cut"><g transform="rotate(-3 540 230)">${{sheet(120, 170, 840, 130, C.stamp, 10)}}${{tx(540, 262, 84, "⚡ 19 YEARS OLD · TEST DEBUT", C.paper)}}</g></g>` +
        `<g id="s1_ramp_stamp" class="cut" opacity="0"><g transform="rotate(5 540 540)">${{sheet(180, 480, 720, 120, C.gold, 10)}}${{tx(540, 568, 70, "AUDACIOUS RAMP SHOT!", C.ink)}}</g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 2 ART: CUT TO THE CROWD AT "90,000" (6.69 - 12.4s)
      // USER REQUIREMENT: Cut directly to the crowd at ninety thousand!
      // ==========================================================
      reseed(202);
      let crowdSvg = `<rect width="1080" height="1920" fill="#243329"/>`;
      // Curving grandstand tiers
      crowdSvg += `<path d="M0 200 Q540 260 1080 200 L1080 600 Q540 660 0 600 Z" fill="#1C2B22"/>`;
      crowdSvg += `<path d="M0 600 Q540 670 1080 600 L1080 1150 Q540 1220 0 1150 Z" fill="#17241C"/>`;
      // 90,000 crowd dots density
      const cColors = [C.paper, C.gold, C.red, C.green, C.indiaBlue, "#E05A47", "#5FA8C9"];
      for (let r = 0; r < 14; r++) {{
        const yBase = 240 + r * 62;
        for (let c = 0; c < 22; c++) {{
          crowdSvg += `<circle class="crowd-dot" cx="${{(c * 50 + (r % 2 ? 25 : 0) + rnd() * 8).toFixed(0)}}" cy="${{yBase + rnd() * 8}}" r="18" fill="${{cColors[Math.floor(rnd() * cColors.length)]}}"/>`;
        }}
      }}
      // Foreground cheering fans holding banners
      const bay13Banner = `<g id="bay13" class="cut"><g transform="rotate(-4 540 820)">${{sheet(180, 740, 720, 160, C.gold, 10)}}${{tx(540, 855, 104, "BAY 13 GOES WILD!", C.ink)}}</g></g>`;
      const banner90k = `<g id="banner90k" class="cut"><g transform="rotate(3 540 420)">${{sheet(100, 330, 880, 180, C.stamp, 12)}}${{tx(540, 460, 115, "90,000 AT THE MCG!", C.paper)}}</g></g>`;
      // Flashbulb bursts
      let flashG = "";
      [[200, 320], [820, 300], [350, 680], [720, 700], [520, 950]].forEach(([fx, fy]) => {{
        flashG += `<g class="mcg_flash" opacity="0"><circle cx="${{fx}}" cy="${{fy}}" r="80" fill="#fff" opacity=".7"/><polygon points="${{fx}},${{fy - 120}} ${{fx + 20}},${{fy - 20}} ${{fx + 120}},${{fy}} ${{fx + 20}},${{fy + 20}} ${{fx}},${{fy + 120}} ${{fx - 20}},${{fy + 20}} ${{fx - 120}},${{fy}} ${{fx - 20}},${{fy - 20}}" fill="#fff"/></g>`;
      }});
      put("s2", svg(crowdSvg + banner90k + bay13Banner + flashG + scraps("confetti", 540, 600, 24, C.paper, C.gold), "#1C2B22"));

      // ==========================================================
      // SCENE 3 ART: WHAT IS BOXING DAY CRICKET? & 26 DECEMBER (12.4 - 20.8s)
      // USER REQUIREMENT: Slow slightly for the explainer
      // ==========================================================
      reseed(303);
      const calLeaf = `<g id="cal" class="cut">
        <g transform="rotate(-3 540 580)">
          <!-- Top binder -->
          ${{sheet(220, 340, 640, 90, C.stamp, 8)}}
          ${{tx(540, 405, 52, "DECEMBER 2026", C.paper)}}
          <!-- Date sheet -->
          ${{sheet(220, 420, 640, 380, C.paper, 10)}}
          ${{tx(540, 670, 230, "26", C.stamp)}}
          ${{tx(540, 765, 62, "BOXING DAY", C.ink)}}
        </g>
      </g>`;
      put("s3", svg(
        stadium() +
        `<g id="s3_title" class="cut">${{sheet(140, 180, 800, 110, C.ink, 8)}}${{tx(540, 260, 64, "SO WHAT IS BOXING DAY CRICKET?", C.gold)}}</g>` +
        calLeaf +
        `<g id="s3_ground_tag" class="cut">${{sheet(100, 900, 880, 140, C.green, 10)}}${{tx(540, 995, 68, "MELBOURNE CRICKET GROUND", C.paper)}}</g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 4 ART: FAMILIES SKIP LEFTOVERS & BIGGEST DAYS (20.8 - 26.9s)
      // ==========================================================
      reseed(404);
      // Roast Leftovers Table card on left vs MCG Ticket on right
      const roastCard = `<g id="roast_card" class="cut"><g transform="rotate(-6 320 620)">
        ${{sheet(120, 440, 400, 380, C.paper, 8)}}
        ${{tx(320, 520, 48, "CHRISTMAS ROAST", C.ink)}}
        <ellipse cx="320" cy="620" rx="90" ry="55" fill="#A86539"/>
        <rect x="295" y="650" width="50" height="24" rx="8" fill="#F1C095"/>
        <rect x="150" y="720" width="340" height="60" rx="8" fill="${{C.stamp}}"/>
        ${{tx(320, 765, 40, "STAYS IN FRIDGE!", C.paper)}}
      </g></g>`;
      const ticketCard = `<g id="tkt_card" class="cut"><g transform="rotate(5 760 620)">
        ${{sheet(560, 440, 400, 380, C.gold, 8)}}
        ${{tx(760, 520, 48, "MCG TEST TICKET", C.ink)}}
        <rect x="590" y="560" width="340" height="150" rx="10" fill="${{C.paper}}" stroke="${{C.ink}}" stroke-width="4" stroke-dasharray="10 8"/>
        ${{tx(760, 630, 58, "ADMIT ONE", C.stamp)}}
        ${{tx(760, 685, 40, "BOXING DAY", C.ink)}}
        ${{tx(760, 775, 46, "OFF TO THE 'G!", C.green)}}
      </g></g>`;
      put("s4", svg(
        stadium() +
        `<g id="s4_hdr" class="cut">${{sheet(90, 180, 900, 120, C.stamp, 8)}}${{tx(540, 265, 68, "FAMILIES SKIP THE LEFTOVERS...", C.paper)}}</g>` +
        roastCard + ticketCard +
        `<g id="s4_biggest" class="cut">${{sheet(120, 920, 840, 140, C.green, 10)}}${{tx(540, 1015, 68, "THE BIGGEST DAY IN CRICKET", C.gold)}}</g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 5A ART: SHANE WARNE'S 1994 ASHES HAT-TRICK (26.9 - 32.2s)
      // ==========================================================
      reseed(505);
      const warneGuy = guy("warne", 540, 800, 0.85, {{
        skin: "#E9B990", sk2: "#D69E73", hair: "#E3B23C", cap: C.green, trim: "#0F3B2C", badge: C.gold, zinc: 1, m: "teeth"
      }});
      // Outstretched celebration arms
      const warneArms = `<g id="warne_arms" class="cut">
        <rect x="220" y="680" width="180" height="42" rx="18" fill="#E9B990" transform="rotate(-30 310 700)"/>
        <rect x="680" y="680" width="180" height="42" rx="18" fill="#E9B990" transform="rotate(30 770 700)"/>
      </g>`;
      // Flying English shattered stumps & bails
      const flyingStumps = `<g id="stumps94" class="cut">
        <rect x="180" y="780" width="16" height="110" rx="4" fill="${{C.paper}}" transform="rotate(-65 188 835)"/>
        <rect x="260" y="860" width="16" height="110" rx="4" fill="${{C.paper}}" transform="rotate(25 268 915)"/>
        <rect x="820" y="760" width="16" height="110" rx="4" fill="${{C.paper}}" transform="rotate(75 828 815)"/>
        <rect x="210" y="720" width="36" height="10" rx="3" fill="${{C.paper}}" transform="rotate(-120 228 725)"/>
        <rect x="800" y="710" width="36" height="10" rx="3" fill="${{C.paper}}" transform="rotate(130 818 715)"/>
      </g>`;
      put("s5a", svg(
        stadium() +
        `<g id="s5a_hdr" class="cut">${{sheet(140, 180, 800, 100, C.ink, 8)}}${{tx(540, 255, 62, "AND IT CREATES LEGENDS...", C.gold)}}</g>` +
        flyingStumps + warneArms + warneGuy +
        `<g id="warne_tag" class="cut">${{sheet(330, 1140, 420, 84, C.green, 8)}}${{tx(540, 1202, 50, "SHANE WARNE · 1994", C.gold)}}</g>` +
        stamp("warne_stamp", 540, 480, "ASHES HAT-TRICK", "3 WICKETS IN 3 BALLS!"),
        C.dgreen
      ));

      // ==========================================================
      // SCENE 5B ART: AJINKYA RAHANE'S 2020 CENTURY (32.2 - 37.5s)
      // ==========================================================
      reseed(606);
      const rahaneGuy = guy("rahane", 540, 800, 0.85, {{
        skin: "#C68B59", sk2: "#A87042", hair: "#1B1B1B", cap: C.indiaBlue, trim: "#0D1B2A", badge: C.gold, beard: 1, collar: "#003566", m: "smirk"
      }});
      // Raised helmet in left hand & raised bat in right hand
      const rahaneHands = `<g id="rahane_arms" class="cut">
        <!-- Left arm with helmet -->
        <rect x="250" y="660" width="150" height="40" rx="16" fill="#C68B59" transform="rotate(-40 325 680)"/>
        <circle cx="210" cy="560" r="44" fill="${{C.indiaBlue}}"/>
        <rect x="180" y="560" width="60" height="10" fill="${{C.gold}}"/>
        <!-- Right arm with bat -->
        <rect x="680" y="660" width="150" height="40" rx="16" fill="#C68B59" transform="rotate(40 755 680)"/>
        <rect x="820" y="420" width="40" height="220" rx="6" fill="${{C.gold}}" transform="rotate(15 840 530)"/>
        <rect x="830" y="630" width="18" height="80" rx="4" fill="${{C.paper}}" transform="rotate(15 839 670)"/>
        ${{tx(855, 530, 32, "100", C.indiaBlue, "middle", 'transform="rotate(15 855 530)"')}}
      </g>`;
      put("s5b", svg(
        stadium() +
        `<g id="s5b_hdr" class="cut">${{sheet(140, 180, 800, 100, C.indiaBlue, 8)}}${{tx(540, 255, 62, "2020: INDIA'S COMEBACK", C.paper)}}</g>` +
        rahaneHands + rahaneGuy +
        `<g id="rahane_tag" class="cut">${{sheet(310, 1140, 460, 84, C.indiaBlue, 8)}}${{tx(540, 1202, 50, "AJINKYA RAHANE · 112", C.gold)}}</g>` +
        stamp("rahane_stamp", 540, 480, "HISTORIC MCG 100", "INDIA WON BY 8 WICKETS", C.indiaBlue),
        C.dgreen
      ));

      // ==========================================================
      // SCENE 6 ART: PUBLIC HOLIDAY & EVERYONE GOES (37.5 - 45.2s)
      // ==========================================================
      reseed(707);
      put("s6", svg(
        stadium() +
        `<g id="s6_hdr" class="cut">${{sheet(160, 180, 760, 110, C.ink, 8)}}${{tx(540, 260, 66, "SO WHY 'BOXING DAY'?", C.gold)}}</g>` +
        stamp("holiday_stamp", 540, 480, "PUBLIC HOLIDAY", "EVERYONE'S OFF WORK!") +
        `<g id="s6_crowd_march" class="cut">${{sheet(100, 720, 880, 180, C.green, 10)}}${{tx(540, 805, 80, "EVERYONE GOES TO", C.paper)}}${{tx(540, 875, 74, "THE CRICKET!", C.gold)}}</g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 7 ART: CHRISTMAS VS BOXING DAY (45.2 - 49.5s)
      // ==========================================================
      reseed(808);
      put("s7", svg(
        rays("r7", 540, 960, 22, "#1A4A3A") +
        `<g id="s7_xmas" class="cut"><g transform="rotate(-4 540 420)">${{sheet(140, 320, 800, 180, C.paper, 10)}}${{tx(540, 405, 62, "CHRISTMAS IS FOR", C.ink)}}${{tx(540, 475, 78, "FAMILY.", C.green)}}</g></g>` +
        ball("s7_ball", 540, 780, 130) +
        `<g id="s7_boxing" class="cut"><g transform="rotate(3 540 1080)">${{sheet(100, 970, 880, 210, C.stamp, 12)}}${{tx(540, 1065, 74, "BOXING DAY IS FOR", C.paper)}}${{tx(540, 1155, 96, "TEST CRICKET!", C.gold)}}</g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 8 ART: PINNED DEBATE COMMENT CARD & CTA (49.5 - 52.61s)
      // USER REQUIREMENT: Pin a comment "Konstas vs Bumrah: best debut moment ever?"
      // ==========================================================
      reseed(909);
      const pinnedCard = `<g id="pinned_debate_card" class="cut">
        <g transform="rotate(-2 540 680)">
          <!-- Comment Card Paper Sheet -->
          ${{sheet(90, 420, 900, 460, C.paper, 10)}}
          <!-- Red Pin Tag -->
          <rect x="130" y="460" width="260" height="52" rx="8" fill="${{C.stamp}}"/>
          ${{tx(260, 498, 32, "📌 PINNED COMMENT", C.paper)}}
          <!-- Avatar & Handle -->
          <circle cx="165" cy="565" r="32" fill="${{C.green}}"/>
          ${{tx(165, 578, 32, "🏏", C.gold)}}
          ${{tx(220, 565, 40, "CricketDebate", C.ink, "start")}}
          <circle cx="460" cy="552" r="14" fill="${{C.indiaBlue}}"/>
          ${{tx(460, 561, 20, "✓", C.paper)}}
          <!-- The Debated Question (Exact User Prompt Wording) -->
          <rect x="130" y="625" width="820" height="150" rx="8" fill="#EDE4D0" stroke="${{C.ink}}" stroke-width="3"/>
          ${{tx(540, 690, 46, "“KONSTAS VS BUMRAH:", C.stamp)}}
          ${{tx(540, 745, 50, "BEST DEBUT MOMENT EVER?”", C.ink)}}
          <!-- Engagement stats -->
          ${{tx(160, 840, 32, "❤️ 58.4K", "#777", "start")}}
          ${{tx(400, 840, 32, "💬 4,120", "#777", "start")}}
          ${{tx(880, 840, 32, "SHARE ↗", C.stamp, "end")}}
        </g>
      </g>`;
      put("s8", svg(
        stadium() +
        `<g id="s8_hdr" class="cut">${{sheet(100, 180, 880, 110, C.gold, 8)}}${{tx(540, 260, 62, "BEST BOXING DAY MOMENT?", C.ink)}}</g>` +
        pinnedCard +
        `<g id="s8_cta" class="cut"><g transform="rotate(3 540 1020)">${{sheet(120, 950, 840, 130, C.stamp, 8)}}${{tx(540, 1045, 72, "👇 COMMENT BELOW!", C.paper)}}</g></g>`,
        C.dgreen
      ));

      // Paper wipe polygon setup (direct from Reference)
      reseed(999);
      document.getElementById("wipe").innerHTML = `<svg viewBox="0 0 1500 2300" width="1500" height="2300" xmlns="http://www.w3.org/2000/svg"><polygon id="wp" points="${{torn(20, 20, 1460, 2260, 60, 90)}}" fill="${{C.paper}}"/></svg>`;

      // ==========================================================
      // GSAP TIMELINE ENGINE (Direct Reference Architecture)
      // ==========================================================
      const tl = gsap.timeline({{ paused: true }});
      const CC = "50% 50%";

      // Origin setups
      gsap.set("#r7", {{ svgOrigin: "540 960" }});
      gsap.set("#hdr_19yo,#s1_ramp_stamp,#bay13,#banner90k,#s3_title,#cal,#s4_hdr,#roast_card,#tkt_card,#s4_biggest,#s5a_hdr,#warne_tag,#warne_stamp,#s5b_hdr,#rahane_tag,#rahane_stamp,#s6_hdr,#holiday_stamp,#s6_crowd_march,#s7_xmas,#s7_boxing,#s8_hdr,#pinned_debate_card,#s8_cta,.browL,.browR,.eye,.pupil", {{ transformOrigin: CC }});
      gsap.set("#s1_ball", {{ transformOrigin: CC }});
      gsap.set("#konstas_bat", {{ transformOrigin: "0% 0%" }});

      const pop = (sel, t, d = 0.22) => tl.fromTo(sel, {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: d, ease: "back.out(2.2)" }}, t);
      const slam = (sel, t, r = 0) => tl.fromTo(sel, {{ scale: 3.2, opacity: 0, rotation: r }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.14, ease: "power4.in" }}, t);
      const shake = (sel, t, a = 22) =>
        tl.to(sel, {{ x: a, y: -a * 0.6, duration: 0.04 }}, t)
          .to(sel, {{ x: -a * 0.8, y: a * 0.5, duration: 0.04 }}, t + 0.04)
          .to(sel, {{ x: a * 0.4, y: a * 0.3, duration: 0.04 }}, t + 0.08)
          .to(sel, {{ x: 0, y: 0, duration: 0.05 }}, t + 0.12);
      const zoom = (id, t, d, from, to, origin = CC, ease = "none") => tl.fromTo(`#${{id}} svg`, {{ scale: from }}, {{ scale: to, duration: d, ease, transformOrigin: origin }}, t);
      function face(id, t, o, d = 0.1) {{
        const q = (s) => `#${{id}} ${{s}}`;
        if (o.m) {{ tl.set(q(".m"), {{ opacity: 0 }}, t); tl.set(q(".m-" + o.m), {{ opacity: 1 }}, t + 0.001); }}
        if (o.b) {{
          tl.to(q(".browL"), {{ rotation: o.b[0], y: o.b[2] || 0, duration: d }}, t);
          tl.to(q(".browR"), {{ rotation: o.b[1], y: o.b[2] || 0, duration: d }}, t);
        }}
        if (o.e != null) tl.to(q(".eye"), {{ scale: o.e, duration: d }}, t);
        if (o.p) tl.to(q(".pupil"), {{ x: o.p[0], y: o.p[1], duration: d }}, t);
        if (o.ps != null) tl.to(q(".pupil"), {{ scale: o.ps, duration: d }}, t);
      }}
      const burst = (cls, t, sx, sy0, sy1) =>
        gsap.utils.toArray("." + cls).forEach((el) => {{
          tl.fromTo(el, {{ x: 0, y: 0, rotation: 0, opacity: 1 }}, {{ x: (rnd() - 0.5) * sx, y: sy0 + rnd() * (sy1 - sy0), rotation: (rnd() - 0.5) * 720, opacity: 0, duration: 0.75, ease: "power2.out", immediateRender: false }}, t);
        }});

      // Captions animation (Exact Reference timing & rotation)
      gsap.utils.toArray(".cap span").forEach((el, i) => {{
        const t = +el.parentNode.dataset.start;
        const dur = +el.parentNode.dataset.duration;
        // Pop in
        tl.fromTo(el, {{ scale: 0.5, rotation: i % 2 ? 5 : -5, opacity: 0 }}, {{ scale: 1, rotation: i % 2 ? -1.5 : 1.5, opacity: 1, duration: 0.14, ease: "back.out(2.6)" }}, t);
        // Pop out before next caption
        tl.to(el, {{ opacity: 0, scale: 0.85, duration: 0.1, ease: "power1.in" }}, t + dur - 0.1);
      }});

      // Stop-motion torn paper wipes between scenes
      tl.set("#wipe", {{ autoAlpha: 0, x: -2500 }}, 0);
      [
        [6.69, C.paper, 1],
        [12.40, C.gold, -1],
        [20.80, C.stamp, 1],
        [26.90, C.paper, -1],
        [32.20, C.green, 1],
        [37.50, C.paper, -1],
        [45.20, C.gold, 1],
        [49.50, C.stamp, -1]
      ].forEach(([t, c, dir]) => {{
        tl.set("#wp", {{ fill: c }}, t - 0.19);
        tl.set("#wipe", {{ autoAlpha: 1 }}, t - 0.19);
        tl.fromTo("#wipe", {{ x: dir > 0 ? -2200 : 1400 }}, {{ x: dir > 0 ? 1400 : -2200, duration: 0.36, ease: "none", immediateRender: false }}, t - 0.18);
        tl.set("#wipe", {{ autoAlpha: 0 }}, t + 0.19);
      }});

      // Set initial scene states
      tl.set("#s1", {{ autoAlpha: 1 }}, 0);
      tl.set(["#s2", "#s3", "#s4", "#s5a", "#s5b", "#s6", "#s7", "#s8"], {{ autoAlpha: 0 }}, 0);

      // Transitions between scenes
      tl.set("#s2", {{ autoAlpha: 1 }}, 6.69);
      tl.set("#s1", {{ autoAlpha: 0 }}, 6.69);

      tl.set("#s3", {{ autoAlpha: 1 }}, 12.40);
      tl.set("#s2", {{ autoAlpha: 0 }}, 12.40);

      tl.set("#s4", {{ autoAlpha: 1 }}, 20.80);
      tl.set("#s3", {{ autoAlpha: 0 }}, 20.80);

      tl.set("#s5a", {{ autoAlpha: 1 }}, 26.90);
      tl.set("#s4", {{ autoAlpha: 0 }}, 26.90);

      tl.set("#s5b", {{ autoAlpha: 1 }}, 32.20);
      tl.set("#s5a", {{ autoAlpha: 0 }}, 32.20);

      tl.set("#s6", {{ autoAlpha: 1 }}, 37.50);
      tl.set("#s5b", {{ autoAlpha: 0 }}, 37.50);

      tl.set("#s7", {{ autoAlpha: 1 }}, 45.20);
      tl.set("#s6", {{ autoAlpha: 0 }}, 45.20);

      tl.set("#s8", {{ autoAlpha: 1 }}, 49.50);
      tl.set("#s7", {{ autoAlpha: 0 }}, 49.50);

      // ----------------------------------------------------------
      // DETAILED STOP-MOTION ANIMATIONS
      // ----------------------------------------------------------
      // SCENE 1 (0.00s - 6.69s)
      // "19 YEARS OLD" text is already rendered on screen at t=0.00s!
      zoom("s1", 0, 6.69, 1, 1.08);
      // Gentle pulse on the 19yo header
      tl.to("#hdr_19yo", {{ scale: 1.06, duration: 0.35, repeat: 3, yoyo: true, ease: "sine.inOut" }}, 0.3);
      // Bumrah charging in
      tl.fromTo("#bumrah", {{ x: -120 }}, {{ x: 40, duration: 2.8, ease: "power1.inOut" }}, 0.2);
      face("bumrah", 0.1, {{ b: [12, -12, 6], p: [14, 0] }});
      face("konstas", 0.1, {{ b: [-10, 10, -8], p: [-15, 0] }});
      // Ball hurtles forward at 3.3s
      tl.fromTo("#s1_ball", {{ x: -180, y: -60, scale: 0.6 }}, {{ x: 280, y: -80, scale: 1.1, duration: 0.9, ease: "power2.in" }}, 3.3);
      // Konstas executes ramp shot at 4.15s
      tl.to("#konstas_bat", {{ rotation: 30, duration: 0.25, ease: "back.out(2)" }}, 3.95);
      face("konstas", 4.1, {{ m: "teeth", b: [15, -15, 8] }});
      // Bat crack & ball ramps
      burst("s1_crack", 4.2, 500, -250, 150);
      shake("#s1 .cam", 4.2, 28);
      tl.to("#ramp_path", {{ opacity: 1, duration: 0.2 }}, 4.2);
      tl.to("#s1_ball", {{ x: 540, y: -480, scale: 0.5, duration: 0.8, ease: "power1.out" }}, 4.2);
      face("bumrah", 4.3, {{ m: "o", e: 1.3, b: [-16, 16, -14], p: [18, -10] }});
      slam("#s1_ramp_stamp", 4.4, 6);

      // SCENE 2 (6.69s - 12.40s): CUT TO 90,000 CROWD WENT WILD!
      zoom("s2", 6.69, 5.71, 1, 1.12);
      slam("#banner90k", 6.75, 5);
      shake("#s2 .cam", 6.9, 30);
      pop("#bay13", 7.2);
      burst("confetti", 7.2, 900, -400, 300);
      // Flashes popping
      [7.0, 7.4, 7.8, 8.3, 8.9, 9.5, 10.2, 10.8, 11.5].forEach((t, i) => {{
        const el = gsap.utils.toArray(".mcg_flash")[i % 5];
        tl.fromTo(el, {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.05, immediateRender: false }}, t).to(el, {{ opacity: 0, duration: 0.08 }}, t + 0.06);
      }});

      // SCENE 3 (12.40s - 20.80s): WHAT IS BOXING DAY?
      zoom("s3", 12.40, 8.40, 1, 1.06);
      pop("#s3_title", 12.5);
      slam("#cal", 13.0, -8);
      shake("#s3 .cam", 13.15, 20);
      pop("#s3_ground_tag", 15.2);

      // SCENE 4 (20.80s - 26.90s): FAMILIES SKIP LEFTOVERS
      zoom("s4", 20.80, 6.10, 1, 1.08);
      pop("#s4_hdr", 20.9);
      slam("#roast_card", 21.2, -12);
      slam("#tkt_card", 22.0, 10);
      pop("#s4_biggest", 24.5);

      // SCENE 5A (26.90s - 32.20s): SHANE WARNE HAT-TRICK 1994
      zoom("s5a", 26.90, 5.30, 1, 1.1);
      pop("#s5a_hdr", 27.0);
      slam("#warne_stamp", 27.5, -12);
      shake("#s5a .cam", 27.65, 30);
      // Warne celebration jump
      tl.to("#warne,#warne_arms", {{ y: -40, duration: 0.25, repeat: 5, yoyo: true, ease: "sine.inOut" }}, 28.0);
      pop("#warne_tag", 29.4);

      // SCENE 5B (32.20s - 37.50s): AJINKYA RAHANE 2020 CENTURY
      zoom("s5b", 32.20, 5.30, 1, 1.08);
      pop("#s5b_hdr", 32.3);
      slam("#rahane_stamp", 32.8, 8);
      shake("#s5b .cam", 32.95, 25);
      pop("#rahane_tag", 34.0);

      // SCENE 6 (37.50s - 45.20s): PUBLIC HOLIDAY
      zoom("s6", 37.50, 7.70, 1, 1.06);
      pop("#s6_hdr", 37.6);
      slam("#holiday_stamp", 39.8, -10);
      shake("#s6 .cam", 39.95, 22);
      pop("#s6_crowd_march", 43.1);

      // SCENE 7 (45.20s - 49.50s): CHRISTMAS VS BOXING DAY
      tl.fromTo("#r7", {{ rotation: 0 }}, {{ rotation: 30, duration: 4.3, ease: "none" }}, 45.2);
      slam("#s7_xmas", 45.3, -8);
      pop("#s7_ball", 46.2);
      slam("#s7_boxing", 47.1, 10);
      shake("#s7 .cam", 47.25, 30);

      // SCENE 8 (49.50s - 52.61s): PINNED DEBATE COMMENT CARD & CTA
      zoom("s8", 49.50, 3.11, 1, 1.05);
      pop("#s8_hdr", 49.6);
      slam("#pinned_debate_card", 49.9, -6);
      shake("#s8 .cam", 50.05, 26);
      pop("#s8_cta", 51.4);

      // Standalone Clip & Scene Activation (Guarantees exact visibility for Playwright renderer)
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
