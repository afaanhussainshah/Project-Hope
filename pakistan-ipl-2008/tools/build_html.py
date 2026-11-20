import base64
from pathlib import Path

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\pakistan-ipl-2008")
font_path = base / "assets" / "fonts" / "Anton-Regular.ttf"
font_b64 = base64.b64encode(font_path.read_bytes()).decode("ascii")

gsap_path = base / "assets" / "gsap.min.js"
gsap_code = gsap_path.read_text(encoding="utf-8")

def get_html(inline_gsap=True):
    gsap_script = f"<script>{gsap_code}</script>" if inline_gsap else '<script src="assets/gsap.min.js"></script>'
    return f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    {gsap_script}
    <style>
      @font-face {{
        font-family: "Anton";
        src: url(data:font/ttf;base64,{font_b64}) format("truetype");
        font-weight: 400;
        font-style: normal;
      }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #0A1C3E; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: "Anton", sans-serif; }}
      .scene {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: hidden; z-index: 1; }}
      .cam, .cam svg {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; display: block; }}
      .cut {{ filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.3)); }}
      #wipe {{ position: absolute; left: 0; top: -190px; width: 1500px; height: 2300px; z-index: 5; pointer-events: none; }}
      #grain {{
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 8; opacity: 0.05; mix-blend-mode: multiply; pointer-events: none;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' seed='4'/><feColorMatrix values='0 0 0 0 .35  0 0 0 0 .3  0 0 0 0 .25  0 0 0 .9 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");
      }}
      #vig {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 9; pointer-events: none; background: radial-gradient(ellipse at 50% 45%, rgba(0, 0, 0, 0) 55%, rgba(0, 0, 0, 0.32) 100%); }}
      
      /* Standardized Safe Caption Box modeled after sandpaper-gate */
      .cap {{ position: absolute; left: 50px; width: 980px; top: 1320px; height: 230px; z-index: 10; text-align: center; pointer-events: none; }}
      .cap span {{
        display: inline-block; max-width: 960px; padding: 14px 34px 18px; background: #f6f1e4; color: #1b1b1b;
        font-size: 72px; line-height: 1.08; letter-spacing: 1px; text-transform: uppercase;
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.35));
      }}
      .cap b {{ font-weight: 400; color: #c1121f; }}
      .cap i {{ font-style: normal; background: #e3b23c; color: #1b1b1b; padding: 0 12px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="54.91" data-width="1080" data-height="1920">
      <!-- SCENES -->
      <div id="s1" class="clip scene" data-start="0" data-duration="8.8"><div class="cam"></div></div>
      <div id="s2a" class="clip scene" data-start="8.8" data-duration="3.2"><div class="cam"></div></div>
      <div id="s2b" class="clip scene" data-start="12.0" data-duration="4.2"><div class="cam"></div></div>
      <div id="s2c" class="clip scene" data-start="16.2" data-duration="7.6"><div class="cam"></div></div>
      <div id="s3" class="clip scene" data-start="23.8" data-duration="12.0"><div class="cam"></div></div>
      <div id="s4" class="clip scene" data-start="35.8" data-duration="12.0"><div class="cam"></div></div>
      <div id="s5" class="clip scene" data-start="47.8" data-duration="7.2"><div class="cam"></div></div>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- CAPTIONS (Aligned with Voiceover) -->
      <div class="clip cap" data-start="0.05" data-duration="1.45"><span>IN THE <b>FIRST IPL...</b></span></div>
      <div class="clip cap" data-start="1.50" data-duration="3.95"><span><b>SHAHID AFRIDI</b> & 10 PAKISTANI ICONS</span></div>
      <div class="clip cap" data-start="5.50" data-duration="2.15"><span>THEN... <b>THEY ALL VANISHED.</b></span></div>
      <div class="clip cap" data-start="7.70" data-duration="1.05"><span><i>HERE'S WHY.</i></span></div>
      <div class="clip cap" data-start="8.80" data-duration="3.15"><span><b>2008.</b> THE FIRST IPL.</span></div>
      <div class="clip cap" data-start="12.00" data-duration="4.15"><span><b>SHAHID AFRIDI:</b> <i>DECCAN CHARGERS</i></span></div>
      <div class="clip cap" data-start="16.20" data-duration="3.95"><span><b>TANVIR, YOUNIS & AKMAL</b> WERE THERE</span></div>
      <div class="clip cap" data-start="20.20" data-duration="3.55"><span>WON THE TROPHY WITH <b>RAJASTHAN ROYALS!</b> 🏆</span></div>
      <div class="clip cap" data-start="23.80" data-duration="3.55"><span>THEN CAME <b>NOVEMBER 2008.</b></span></div>
      <div class="clip cap" data-start="27.40" data-duration="2.95"><span>RELATIONS <b>COLLAPSED.</b></span></div>
      <div class="clip cap" data-start="30.40" data-duration="2.85"><span>IN THE <b>2009 IPL...</b></span></div>
      <div class="clip cap" data-start="33.30" data-duration="2.45"><span><b>NO PAKISTANI PLAYERS</b> WERE PICKED.</span></div>
      <div class="clip cap" data-start="35.80" data-duration="1.55"><span><i>HERE'S THE STRANGE PART.</i></span></div>
      <div class="clip cap" data-start="37.40" data-duration="3.05"><span>OFFICIALS SAID <b>TEAMS DECIDE.</b></span></div>
      <div class="clip cap" data-start="40.50" data-duration="2.85"><span>NO PAKISTANI PLAYER HAS FEATURED SINCE...</span></div>
      <div class="clip cap" data-start="43.40" data-duration="2.35"><span>THE ONLY EXCEPTION: <b>AZHAR MAHMOOD</b></span></div>
      <div class="clip cap" data-start="45.80" data-duration="1.95"><span>WHO PLAYED ON A <i>BRITISH PASSPORT!</i></span></div>
      <div class="clip cap" data-start="47.80" data-duration="3.65"><span>TWO DECADES ON... <b>QUESTION REMAINS.</b></span></div>
      <div class="clip cap" data-start="51.50" data-duration="3.41"><span>SHOULD PAKISTANI PLAYERS <b>RETURN TO THE IPL?</b> 👇</span></div>
    </div>

    <script>
      // =========================================================
      // DETERMINISTIC HELPERS (From Sandpaper Reference)
      // =========================================================
      let seed = 17;
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
        blue: "#0A2240",
        navy: "#0A1C3E",
        dcBlue: "#1C355E",
        green: "#174D3A",
        dgreen: "#0F3B2C",
        gold: "#E3B23C",
        pink: "#EA1A7F",
        red: "#B3261E",
        stamp: "#C1121F",
        dark: "#14171D"
      }};

      const svg = (inner, bg) =>
        `<svg viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg"><rect width="1080" height="1920" fill="${{bg}}"/>${{inner}}</svg>`;

      const put = (id, html) => (document.querySelector("#" + id + " .cam").innerHTML = html);

      const tx = (x, y, s, str, fill, anc = "middle", ex = "") =>
        `<text x="${{x}}" y="${{y}}" font-family="Anton" font-size="${{s}}" fill="${{fill}}" text-anchor="${{anc}}" ${{ex}}>${{str}}</text>`;

      function torn(x, y, w, h, j = 10, step = 40) {{
        const p = [];
        for (let i = 0; i <= w; i += step) p.push([x + Math.min(i, w), y + (rnd() - 0.5) * j]);
        for (let i = step; i <= h; i += step) p.push([x + w + (rnd() - 0.5) * j, y + Math.min(i, h)]);
        for (let i = w - step; i >= 0; i -= step) p.push([x + Math.max(i, 0), y + h + (rnd() - 0.5) * j]);
        for (let i = h - step; i > 0; i -= step) p.push([x + (rnd() - 0.5) * j, y + i]);
        return p.map((q) => q[0].toFixed(1) + "," + q[1].toFixed(1)).join(" ");
      }}

      const sheet = (x, y, w, h, fill, j = 10) => `<polygon points="${{torn(x, y, w, h, j)}}" fill="${{fill}}"/>`;

      const rays = (id, cx, cy, n, c) => {{
        let s = `<g id="${{id}}">`;
        for (let i = 0; i < n; i += 2) {{
          const a = (i * 2 * Math.PI) / n, b = ((i + 1) * 2 * Math.PI) / n;
          s += `<polygon points="${{cx}},${{cy}} ${{(cx + 1900 * Math.cos(a)).toFixed(0)}},${{(cy + 1900 * Math.sin(a)).toFixed(0)}} ${{(cx + 1900 * Math.cos(b)).toFixed(0)}},${{(cy + 1900 * Math.sin(b)).toFixed(0)}}" fill="${{c}}"/>`;
        }}
        return s + "</g>";
      }};

      function banner(id, x, y, title = "IPL 2008") {{
        const w = 860, h = 180, m = x + w / 2;
        const zig = `${{m - 30}},${{y - 20}} ${{m + 25}},${{y + 45}} ${{m - 20}},${{y + 95}} ${{m + 30}},${{y + 140}} ${{m - 15}},${{y + h + 20}}`;
        const inner = `<rect x="${{x}}" y="${{y}}" width="${{w}}" height="${{h}}" fill="${{C.blue}}"/><rect x="${{x}}" y="${{y + 14}}" width="${{w}}" height="10" fill="${{C.gold}}"/><rect x="${{x}}" y="${{y + h - 24}}" width="${{w}}" height="10" fill="${{C.gold}}"/>${{tx(m, y + 130, 110, title, C.gold, "middle", 'letter-spacing="6"')}}`;
        return `<defs><clipPath id="${{id}}cl"><polygon points="${{x - 20}},${{y - 20}} ${{zig}} ${{x - 20}},${{y + h + 20}}"/></clipPath><clipPath id="${{id}}cr"><polygon points="${{x + w + 20}},${{y - 20}} ${{zig}} ${{x + w + 20}},${{y + h + 20}}"/></clipPath></defs><g id="${{id}}" class="cut"><g id="${{id}}L"><g clip-path="url(#${{id}}cl)">${{inner}}</g></g><g id="${{id}}R"><g clip-path="url(#${{id}}cr)">${{inner}}</g></g></g>`;
      }}

      function scissors(id, x, y, s = 1) {{
        return `<g id="${{id}}" class="cut" transform="translate(${{x}} ${{y}}) scale(${{s}})">
          <circle cx="-35" cy="-25" r="22" fill="none" stroke="${{C.ink}}" stroke-width="8"/>
          <circle cx="-35" cy="25" r="22" fill="none" stroke="${{C.ink}}" stroke-width="8"/>
          <path d="M-15 -18 L80 15 L-15 18 Z" fill="#D6D6D6" stroke="${{C.ink}}" stroke-width="4"/>
          <path d="M-15 18 L80 -15 L-15 -18 Z" fill="#E8E8E8" stroke="${{C.ink}}" stroke-width="4"/>
          <circle cx="20" cy="0" r="7" fill="${{C.gold}}"/>
        </g>`;
      }}

      const scraps = (cls, cx, cy, n, col1 = C.gold, col2 = C.pink) => {{
        let s = "";
        for (let i = 0; i < n; i++) {{
          const w = 30 + rnd() * 50;
          s += `<polygon class="${{cls}}" points="${{cx}},${{cy}} ${{(cx + w).toFixed(0)}},${{(cy + rnd() * 20).toFixed(0)}} ${{(cx + w * 0.6).toFixed(0)}},${{(cy + w * 0.8).toFixed(0)}}" fill="${{i % 2 ? col1 : col2}}" opacity="0"/>`;
        }}
        return s;
      }};

      // =========================================================
      // AUTHENTIC CHARACTER GENERATOR (Directly from Sandpaper Reference)
      // =========================================================
      function guy(id, x, y, s, o = {{}}) {{
        const skin = o.skin || "#E9B990", sk2 = o.sk2 || "#D69E73", hair = o.hair || "#1B1B1B", m = o.m || "flat";
        const jersey = o.jersey || C.navy, trim = o.trim || C.gold;
        const mo = (n, h) => `<g class="m m-${{n}}" opacity="${{n === m ? 1 : 0}}">${{h}}</g>`;
        return `<g id="${{id}}"><g transform="translate(${{x}} ${{y}}) scale(${{s}})"><g class="cut">
<path d="M-250 430 Q-255 255 -105 218 L105 218 Q255 255 250 430Z" fill="${{jersey}}"/>
<path d="M-62 218 L0 305 L62 218 L38 200 L-38 200Z" fill="${{trim}}"/>
<rect x="-46" y="150" width="92" height="95" rx="20" fill="${{sk2}}"/></g>
<g class="head cut">
<ellipse cx="-148" cy="15" rx="26" ry="40" fill="${{sk2}}"/><ellipse cx="148" cy="15" rx="26" ry="40" fill="${{sk2}}"/>
<rect x="-145" y="-160" width="290" height="345" rx="135" fill="${{skin}}"/>
${{o.beard ? `<path d="M-145 30 Q-150 190 0 187 Q150 190 145 30 Q118 150 0 152 Q-118 150 -145 30Z" fill="${{hair}}"/>` : ""}}
<path d="M-150 -60 L-150 -95 L-118 -95 L-128 -20Z M150 -60 L150 -95 L118 -95 L128 -20Z" fill="${{hair}}"/>
${{o.cap ? `<path d="M-158 -92 Q-160 -262 0 -262 Q160 -262 158 -92Z" fill="${{o.capColor || C.green}}"/>
<path d="M-176 -96 Q0 -132 176 -96 Q196 -62 0 -72 Q-196 -62 -176 -96Z" fill="${{o.visorColor || "#0F3B2C"}}"/>
<circle cx="0" cy="-185" r="30" fill="${{C.gold}}"/>` : `<path d="M-158 -92 Q-160 -262 0 -262 Q160 -262 158 -92Z" fill="${{hair}}"/>`}}
<g class="eye"><circle cx="-62" cy="5" r="36" fill="#fff"/><circle class="pupil" cx="-62" cy="5" r="16" fill="${{C.ink}}"/></g>
<g class="eye"><circle cx="62" cy="5" r="36" fill="#fff"/><circle class="pupil" cx="62" cy="5" r="16" fill="${{C.ink}}"/></g>
<rect class="browL" x="-102" y="-58" width="80" height="17" rx="6" fill="${{hair}}"/><rect class="browR" x="22" y="-58" width="80" height="17" rx="6" fill="${{hair}}"/>
<path d="M-10 30 Q-4 72 22 62" stroke="${{sk2}}" stroke-width="9" fill="none" stroke-linecap="round"/>
${{mo("flat", '<rect x="-44" y="112" width="88" height="13" rx="6" fill="#7A2E22"/>')}}
${{mo("o", '<ellipse cx="0" cy="118" rx="28" ry="32" fill="#4A1410"/>')}}
${{mo("smirk", '<path d="M-48 116 Q14 150 62 98" stroke="#7A2E22" stroke-width="13" fill="none" stroke-linecap="round"/>')}}
${{mo("frown", '<path d="M-48 138 Q0 98 48 138" stroke="#7A2E22" stroke-width="13" fill="none" stroke-linecap="round"/>')}}
${{mo("teeth", '<rect x="-58" y="96" width="116" height="46" rx="14" fill="#fff" stroke="#7A2E22" stroke-width="9"/><path d="M-20 98V140M20 98V140M-56 119H56" stroke="#C9B9A8" stroke-width="4"/>')}}
${{mo("talk", '<ellipse cx="0" cy="120" rx="34" ry="20" fill="#4A1410"/>')}}
</g></g></g>`;
      }}

      // =========================================================
      // AUTHENTIC STADIUM (From Sandpaper Reference + Pitch & Floodlights)
      // =========================================================
      const stadium = () => {{
        let s = `<rect width="1080" height="640" fill="#BFD9E6"/><rect y="620" width="1080" height="440" fill="#39424E"/>`;
        const cols = [C.paper, C.gold, C.red, C.green, C.pink, C.blue, "#5FA8C9"];
        for (let r = 0; r < 7; r++)
          for (let c = 0; c < 19; c++)
            s += `<circle cx="${{(c * 60 + (r % 2 ? 30 : 0) + rnd() * 10).toFixed(0)}}" cy="${{660 + r * 56}}" r="21" fill="${{cols[Math.floor(rnd() * cols.length)]}}"/>`;
        
        // Floodlight Towers
        s += `
          <g class="cut" transform="translate(60, 480)">
            <line x1="-30" y1="200" x2="0" y2="0" stroke="#88929A" stroke-width="12"/>
            <line x1="30" y1="200" x2="0" y2="0" stroke="#88929A" stroke-width="12"/>
            <line x1="-25" y1="120" x2="25" y2="120" stroke="#88929A" stroke-width="8"/>
            <line x1="-15" y1="60" x2="15" y2="60" stroke="#88929A" stroke-width="8"/>
            <rect x="-60" y="-30" width="120" height="40" rx="8" fill="#5A6672"/>
            <circle cx="-35" cy="-10" r="12" fill="#FFFBE6"/>
            <circle cx="0" cy="-10" r="12" fill="#FFFBE6"/>
            <circle cx="35" cy="-10" r="12" fill="#FFFBE6"/>
          </g>
          <g class="cut" transform="translate(1020, 480)">
            <line x1="-30" y1="200" x2="0" y2="0" stroke="#88929A" stroke-width="12"/>
            <line x1="30" y1="200" x2="0" y2="0" stroke="#88929A" stroke-width="12"/>
            <line x1="-25" y1="120" x2="25" y2="120" stroke="#88929A" stroke-width="8"/>
            <line x1="-15" y1="60" x2="15" y2="60" stroke="#88929A" stroke-width="8"/>
            <rect x="-60" y="-30" width="120" height="40" rx="8" fill="#5A6672"/>
            <circle cx="-35" cy="-10" r="12" fill="#FFFBE6"/>
            <circle cx="0" cy="-10" r="12" fill="#FFFBE6"/>
            <circle cx="35" cy="-10" r="12" fill="#FFFBE6"/>
          </g>
        `;
        // Lawn, Boundary Rope, and Turf
        s += `<rect y="1040" width="1080" height="24" fill="${{C.paper}}"/><rect y="1064" width="1080" height="856" fill="#6F9A4B"/><rect y="1064" width="1080" height="30" fill="#5E8744"/>`;
        return s;
      }};

      const stamp = (id, cx, cy, l1, l2) =>
        `<g id="${{id}}"><g transform="rotate(-10 ${{cx}} ${{cy}})"><rect x="${{cx - 240}}" y="${{cy - 85}}" width="480" height="170" rx="16" fill="rgba(246,241,228,.92)" stroke="${{C.stamp}}" stroke-width="12"/>${{tx(cx, cy - 2, 68, l1, C.stamp)}}${{tx(cx, cy + 62, 44, l2, C.stamp)}}</g></g>`;

      const card = (id, x, y, rot, gid, o, name, role) =>
        `<g transform="rotate(${{rot}} ${{x + 185}} ${{y + 220}})"><g id="${{id}}"><g class="cut">${{sheet(x, y, 370, 430, C.paper, 8)}}</g><rect x="${{x + 20}}" y="${{y + 20}}" width="330" height="300" fill="${{o.bg || "#9DB7C4"}}"/>${{guy(gid, x + 185, y + 170, 0.42, o)}}<rect x="${{x + 20}}" y="${{y + 325}}" width="330" height="52" fill="${{C.ink}}"/>${{tx(x + 185, y + 364, 34, name, C.paper)}}<rect x="${{x + 20}}" y="${{y + 377}}" width="330" height="38" fill="${{C.gold}}"/>${{tx(x + 185, y + 404, 21, role, C.ink)}}</g></g>`;

      // =========================================================
      // SCENE ART ASSEMBLY (Direct Reference Style)
      // =========================================================
      reseed(11);
      // S1: Afridi + 10 Pakistani Players
      const afridi_o = {{ hair: "#1B1B1B", beard: 1, jersey: C.dcBlue, trim: "#E0E6ED", m: "smirk" }};
      
      // 10 small Pakistani figures flanking Afridi (5 on left, 5 on right, fully visible)
      let s1_ten = '<g id="s1_squad">';
      // Left 5
      for (let i = 0; i < 5; i++) {{
        const px = 40 + i * 55;
        const py = 500 + (i % 2) * 40;
        s1_ten += `<g id="sq_${{i}}" class="cut">${{guy(`sq_g_${{i}}`, px, py, 0.28, {{ jersey: C.green, trim: C.gold, hair: "#1B1B1B", m: "flat" }})}}</g>`;
      }}
      // Right 5
      for (let i = 5; i < 10; i++) {{
        const px = 820 + (i - 5) * 55;
        const py = 500 + (i % 2) * 40;
        s1_ten += `<g id="sq_${{i}}" class="cut">${{guy(`sq_g_${{i}}`, px, py, 0.28, {{ jersey: C.green, trim: C.gold, hair: "#1B1B1B", m: "flat" }})}}</g>`;
      }}
      s1_ten += '</g>';

      put("s1", svg(
        rays("r1", 540, 700, 20, "#0E2442") +
        s1_ten +
        guy("afridi_hero", 540, 720, 1.02, afridi_o) +
        banner("bn1", 110, 1060, "IPL 2008") + scraps("scA", 540, 1060, 16) +
        scissors("sci1", 200, 600, 1.2) +
        `<g id="ts1" class="cut"><g transform="rotate(-6 270 230)">${{sheet(70, 180, 440, 96, C.stamp, 8)}}${{tx(290, 252, 56, "TRUE CRICKET STORY", C.paper)}}</g></g>` +
        stamp("st_zero", 540, 700, "2009: ZERO", "ALL VANISHED"), C.navy));

      // S2a: Inaugural Season Stadium Reveal + Cricket Pitch
      reseed(21);
      const pitchCut = `
        <g id="stadium_pitch" class="cut">
          ${{sheet(360, 1060, 360, 240, "#E5D8B5", 6)}}
          <!-- Pitch creases -->
          <line x1="390" y1="1100" x2="690" y2="1100" stroke="#FFF" stroke-width="6"/>
          <line x1="390" y1="1260" x2="690" y2="1260" stroke="#FFF" stroke-width="6"/>
          <!-- Stumps & red cricket ball -->
          <g transform="translate(540, 1100)">
            <rect x="-18" y="-45" width="8" height="45" rx="3" fill="#D9A855"/>
            <rect x="-4" y="-45" width="8" height="45" rx="3" fill="#D9A855"/>
            <rect x="10" y="-45" width="8" height="45" rx="3" fill="#D9A855"/>
            <rect x="-22" y="-49" width="44" height="6" rx="2" fill="#C48E3A"/>
            <circle cx="45" cy="-15" r="16" fill="${{C.stamp}}"/>
          </g>
        </g>
      `;

      put("s2a", svg(
        stadium() +
        pitchCut +
        `<circle id="sun" cx="820" cy="420" r="105" fill="${{C.gold}}"/>` +
        `<g id="tgA" class="cut">${{sheet(70, 200, 640, 104, C.ink, 8)}}${{tx(100, 280, 68, "INAUGURAL SEASON", C.paper, "start")}}</g>` +
        `<g id="tgB" class="cut">${{sheet(70, 320, 540, 88, C.gold, 8)}}${{tx(100, 384, 52, "11 PAKISTANI ICONS", C.ink, "start")}}</g>` +
        `<g id="yr" class="cut"><g transform="rotate(-4 350 490)">${{sheet(70, 430, 540, 120, C.stamp, 8)}}${{tx(340, 522, 86, "SEASON 2008", C.paper)}}</g></g>`, "#BFD9E6"));

      // S2b: Broadcast Cam & Afridi Deccan Chargers Star
      reseed(31);
      put("s2b", svg(
        stadium() +
        guy("afridi_s2", 540, 720, 0.95, {{ ...afridi_o, m: "talk" }}) +
        `<g id="tg_dc" class="cut">${{sheet(200, 1100, 680, 96, C.blue, 8)}}${{tx(540, 1168, 50, "DECCAN CHARGERS · STAR", C.gold)}}</g>`, "#6F9A4B"));

      // S2c: Rajasthan Royals Champions Trio & Gold Trophy
      reseed(41);
      const rr_tanvir = {{ jersey: C.pink, trim: C.blue, cap: 1, capColor: "#6A1B9A", visorColor: "#4A148C", m: "smirk" }};
      const rr_younis = {{ jersey: C.pink, trim: C.blue, hair: "#1B1B1B", m: "smirk" }};
      const rr_akmal = {{ jersey: C.pink, trim: C.blue, hair: "#1B1B1B", m: "teeth" }};
      put("s2c", svg(
        stadium() +
        `<g id="rr_banner" class="cut">${{sheet(120, 110, 840, 92, C.pink, 8)}}${{tx(540, 175, 50, "RAJASTHAN ROYALS: 2008 CHAMPIONS", C.paper)}}</g>` +
        `<g id="rr_trophy" class="cut">
          <g transform="translate(540 330)">
            <path d="M-90,-120 L90,-120 L70,0 Q50,70 0,90 Q-50,70 -70,0 Z" fill="${{C.gold}}" stroke="${{C.ink}}" stroke-width="6"/>
            <path d="M-90,-100 Q-150,-50 -70,10" fill="none" stroke="${{C.gold}}" stroke-width="14" stroke-linecap="round"/>
            <path d="M90,-100 Q150,-50 70,10" fill="none" stroke="${{C.gold}}" stroke-width="14" stroke-linecap="round"/>
            <rect x="-60" y="90" width="120" height="30" rx="4" fill="#C59B27"/>
            <rect x="-80" y="120" width="160" height="42" rx="6" fill="${{C.ink}}"/>
            ${{tx(0, 152, 24, "IPL 2008 TROPHY", C.gold)}}
          </g>
        </g>` +
        card("c2_tanvir", 30, 360, -5, "g_rr1", rr_tanvir, "SOHAIL TANVIR", "PURPLE CAP · 22 WKTS") +
        card("c2_younis", 680, 360, 5, "g_rr2", rr_younis, "YOUNIS KHAN", "MIDDLE ORDER PILLAR") +
        card("c2_akmal", 355, 760, 0, "g_rr3", rr_akmal, "KAMRAN AKMAL", "CHAMPION WICKETKEEPER") +
        scraps("sc_rr", 540, 360, 24, C.gold, C.pink), "#6F9A4B"));

      // S3: November 2008 & Collapse
      reseed(51);
      put("s3", svg(
        `<circle id="moon" cx="840" cy="360" r="80" fill="${{C.paper}}"/><circle cx="875" cy="345" r="70" fill="${{C.dark}}"/>` +
        `<g id="skyline_cut" class="cut">
          <path d="M 0,1160 L 0,820 L 70,820 L 70,760 L 140,760 L 140,860 L 220,860 L 220,680 L 260,680 L 260,630 L 300,630 L 300,680 L 350,680 L 350,880 L 440,880 L 440,600 Q 510,500 580,600 L 580,880 L 630,880 L 630,640 Q 675,560 720,640 L 720,880 L 810,880 L 810,720 L 870,720 L 870,680 L 930,680 L 930,720 L 990,720 L 990,850 L 1080,850 L 1080,1160 Z" fill="#0A0D12"/>
          <!-- Skyline warm window squares -->
          <rect x="235" y="710" width="8" height="12" fill="#E3B23C" opacity="0.8"/>
          <rect x="245" y="730" width="8" height="12" fill="#E3B23C" opacity="0.6"/>
          <rect x="475" y="660" width="10" height="14" fill="#E3B23C" opacity="0.7"/>
          <rect x="520" y="690" width="10" height="14" fill="#E3B23C" opacity="0.6"/>
          <rect x="830" y="740" width="8" height="12" fill="#E3B23C" opacity="0.7"/>
          <rect x="950" y="740" width="8" height="12" fill="#E3B23C" opacity="0.7"/>
        </g>` +
        `<rect y="1160" width="1080" height="760" fill="#06080B"/>` +
        `<g id="tg_nov" class="cut">${{sheet(140, 210, 800, 104, C.ink, 8)}}${{tx(540, 290, 68, "NOVEMBER 2008", C.paper)}}</g>` +
        `<g id="nov_rupture" class="cut">${{sheet(100, 450, 880, 135, C.stamp, 8)}}${{tx(540, 520, 46, "RELATIONS COLLAPSED", C.paper)}}${{tx(540, 565, 34, "DIPLOMATIC TIES SEVERED", C.paper)}}</g>` +
        `<g id="s3_auction_board" class="cut">${{sheet(120, 630, 840, 460, C.paper, 8)}}
          <rect x="120" y="630" width="840" height="50" fill="#E8DEC8"/>
          ${{tx(540, 668, 30, "OFFICIAL PLAYER AUCTION LIST", C.ink)}}
          ${{tx(540, 745, 52, "IPL 2009 AUCTION", C.blue)}}
          ${{tx(540, 805, 36, "PAKISTAN PLAYER ROSTER", C.ink)}}
          <rect x="220" y="845" width="640" height="8" fill="${{C.gold}}"/>
          <g transform="translate(540 970)">
            <rect x="-310" y="-55" width="620" height="110" rx="10" fill="#FFF5F5" stroke="${{C.stamp}}" stroke-width="8"/>
            ${{tx(0, 18, 48, "NO PAKISTANI PLAYERS PICKED", C.stamp)}}
          </g>
        </g>`, C.dark));

      // S4: The Unwritten Ban & Azhar Mahmood British Passport Exception
      reseed(61);
      put("s4", svg(
        `<g id="tg_ban" class="cut">${{sheet(140, 190, 800, 96, C.blue, 8)}}${{tx(540, 260, 56, "THE UNWRITTEN RULE", C.paper)}}</g>` +
        `<g id="doc_board" class="cut">${{sheet(120, 320, 840, 380, C.paper, 8)}}
          <rect x="120" y="320" width="840" height="46" fill="#E8DEC8"/>
          ${{tx(540, 354, 26, "IPL GOVERNING COUNCIL GUIDELINES", C.ink)}}
          ${{tx(540, 430, 42, "“TEAMS MAKE THEIR OWN DECISIONS”", C.ink)}}
          ${{tx(540, 480, 30, "- OFFICIAL BCCI STANCE", "#555")}}
        </g>` +
        stamp("st_unwritten", 540, 560, "NEVER OFFICIALLY", "BANNED") +
        card("c4_azhar", 340, 720, -2, "g_azhar", {{ jersey: "#3A225D", trim: C.gold, hair: "#1B1B1B", m: "smirk" }}, "AZHAR MAHMOOD", "PLAYED AS BRITISH CITIZEN") +
        `<g id="passport_cut" class="cut">
          <g transform="translate(770 870) rotate(12)">
            <rect x="-95" y="-125" width="190" height="250" rx="10" fill="#58111A" stroke="${{C.ink}}" stroke-width="4"/>
            <rect x="-85" y="-115" width="170" height="230" rx="6" fill="none" stroke="${{C.gold}}" stroke-width="2"/>
            ${{tx(0, -80, 14, "BRITISH", C.gold)}}
            ${{tx(0, -64, 14, "PASSPORT", C.gold)}}
            <circle cx="0" cy="-10" r="28" fill="none" stroke="${{C.gold}}" stroke-width="2"/>
            ${{tx(0, 56, 20, "UNITED KINGDOM", C.gold)}}
          </g>
        </g>`, C.dgreen));

      // S5: Close & Audience CTA
      reseed(71);
      put("s5", svg(
        rays("r5", 540, 800, 20, "#1A4A3A") +
        `<g id="tg_final" class="cut">${{sheet(140, 180, 800, 96, C.blue, 8)}}${{tx(540, 250, 54, "ALMOST TWO DECADES ON...", C.paper)}}</g>` +
        `<g id="s5_hanger" class="cut">
          <g transform="translate(540 300)">
            <circle cx="0" cy="0" r="14" fill="${{C.ink}}"/>
            <line x1="0" y1="0" x2="0" y2="40" stroke="#444" stroke-width="6"/>
            <!-- Swinging wire hanger & empty green jersey -->
            <g id="s5_pendulum">
              <path d="M0,40 L-180,120 L180,120 Z" fill="none" stroke="#555" stroke-width="8" stroke-linejoin="round"/>
              <g transform="translate(0 120)">
                <path d="M-160,0 L-260,70 L-230,140 L-170,110 L-170,440 L170,440 L170,110 L230,140 L260,70 L160,0 Q0,40 -160,0 Z" fill="${{C.green}}" stroke="${{C.ink}}" stroke-width="6"/>
                <path d="M-50,20 Q0,60 50,20 Q0,80 -50,20 Z" fill="${{C.gold}}"/>
                ${{tx(0, 260, 160, "?", C.gold, "middle", 'font-weight="bold"')}}
                ${{tx(0, 380, 36, "EMPTY ROSTER", C.paper)}}
              </g>
            </g>
          </g>
        </g>` +
        `<g id="s5_years" class="cut">${{sheet(180, 940, 720, 96, C.ink, 8)}}${{tx(540, 1008, 52, "2008 ➔ 2026: 18 YEARS LATER", C.paper)}}</g>` +
        `<g id="s5_cta" class="cut">${{sheet(120, 1080, 840, 140, C.stamp, 8)}}${{tx(540, 1145, 46, "WHAT DO YOU THINK?", C.paper)}}${{tx(540, 1195, 40, "CAST YOUR VOTE BELOW 👇", C.gold)}}</g>`, C.dgreen));

      // Paper wipe transition polygon
      reseed(91);
      document.getElementById("wipe").innerHTML = `<svg viewBox="0 0 1500 2300" width="1500" height="2300" xmlns="http://www.w3.org/2000/svg"><polygon id="wp" points="${{torn(20, 20, 1460, 2260, 60, 90)}}" fill="${{C.paper}}"/></svg>`;

      // =========================================================
      // TIMELINE CHOREOGRAPHY (Direct Reference Style)
      // =========================================================
      const tl = gsap.timeline({{ paused: true }});
      const CC = "50% 50%";

      gsap.set("#r1", {{ svgOrigin: "540 700" }});
      gsap.set("#r5", {{ svgOrigin: "540 800" }});
      gsap.set("#ts1,#yr,#tgA,#tgB,#tg_dc,#rr_banner,#rr_trophy,#tg_nov,#nov_rupture,#s3_auction_board,#tg_ban,#doc_board,#st_unwritten,#passport_cut,#tg_final,#s5_years,#s5_cta,#sci1,#stadium_pitch", {{ transformOrigin: CC }});
      gsap.set(".browL,.browR,.eye,.pupil", {{ transformOrigin: CC }});

      const pop = (sel, t, d = 0.22) => tl.fromTo(sel, {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: d, ease: "back.out(2.2)" }}, t);
      const slam = (sel, t, r = 0) => tl.fromTo(sel, {{ scale: 3.2, opacity: 0, rotation: r }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.16, ease: "power4.in" }}, t);
      const shake = (sel, t, a = 22) =>
        tl.to(sel, {{ x: a, y: -a * 0.6, duration: 0.04 }}, t).to(sel, {{ x: -a * 0.8, y: a * 0.5, duration: 0.04 }}, t + 0.04).to(sel, {{ x: a * 0.4, y: a * 0.3, duration: 0.04 }}, t + 0.08).to(sel, {{ x: 0, y: 0, duration: 0.05 }}, t + 0.12);
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

      // VISIBILITY MANAGEMENT FOR ALL CLIPS (Scenes and Captions)
      gsap.utils.toArray(".clip").forEach((el) => {{
        const start = +el.dataset.start || 0;
        const dur = +el.dataset.duration || 0;
        if (dur > 0) {{
          tl.set(el, {{ display: "none" }}, 0);
          tl.set(el, {{ display: "block" }}, start);
          tl.set(el, {{ display: "none" }}, start + dur);
        }}
      }});

      // Captions Pop animation (Direct Reference from sandpaper-gate)
      gsap.utils.toArray(".cap span").forEach((el, i) => {{
        const t = +el.parentNode.dataset.start;
        tl.fromTo(el, {{ scale: 0.5, rotation: i % 2 ? 4 : -4, opacity: 0 }}, {{ scale: 1, rotation: i % 2 ? -1.5 : 1.5, opacity: 1, duration: 0.14, ease: "back.out(2.6)" }}, t);
      }});

      // Paper Wipes between scenes
      gsap.set("#wipe", {{ x: -1700 }});
      [
        [8.80, C.paper, 1],
        [16.20, C.pink, -1],
        [23.80, C.dark, 1],
        [35.80, C.gold, -1],
        [47.80, C.paper, 1]
      ].forEach(([t, c, dir]) => {{
        tl.set("#wp", {{ fill: c }}, t - 0.19);
        tl.fromTo("#wipe", {{ x: dir > 0 ? -1700 : 1300 }}, {{ x: dir > 0 ? 1300 : -1700, duration: 0.36, ease: "none" }}, t - 0.18);
      }});

      // S1: 0.00s - 8.80s (Hook)
      tl.fromTo("#r1", {{ rotation: 0 }}, {{ rotation: 40, duration: 8.8, ease: "none" }}, 0);
      zoom("s1", 0, 8.8, 1, 1.1);
      tl.fromTo("#afridi_hero", {{ scale: 0, y: 500 }}, {{ scale: 1.02, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 0.1);
      pop("#ts1", 0.5);
      tl.fromTo("#bn1", {{ y: 800 }}, {{ y: 0, duration: 0.4, ease: "back.out(1.4)" }}, 1.0);

      // Ten squad members slide in (left 5, then right 5)
      for (let i = 0; i < 10; i++) {{
        tl.fromTo(`#sq_${{i}}`, {{ y: 300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25, ease: "back.out(1.2)" }}, 1.4 + i * 0.15);
      }}

      // Scissors snip across: left 5, then right 5
      tl.set("#sci1", {{ opacity: 0 }}, 0);
      tl.fromTo("#sci1", {{ opacity: 0, scale: 0.4, x: -50, y: 500 }}, {{ opacity: 1, scale: 1.2, x: 40, y: 500, duration: 0.3, ease: "back.out(1.5)" }}, 4.8);
      for (let i = 0; i < 5; i++) {{
        const cutTime = 5.1 + i * 0.14;
        tl.to("#sci1", {{ x: 40 + i * 55, y: 500 + (i % 2 ? -20 : 20), rotation: (i % 2 ? 15 : -15), duration: 0.12 }}, cutTime);
        tl.to(`#sq_${{i}}`, {{ y: 500, rotation: (i % 2 ? 25 : -25), opacity: 0, duration: 0.25, ease: "power2.in" }}, cutTime + 0.05);
      }}
      // Jump scissors to right 5
      tl.to("#sci1", {{ x: 820, y: 500, duration: 0.15 }}, 5.85);
      for (let i = 5; i < 10; i++) {{
        const cutTime = 6.0 + (i - 5) * 0.14;
        tl.to("#sci1", {{ x: 820 + (i - 5) * 55, y: 500 + (i % 2 ? -20 : 20), rotation: (i % 2 ? 15 : -15), duration: 0.12 }}, cutTime);
        tl.to(`#sq_${{i}}`, {{ y: 500, rotation: (i % 2 ? 25 : -25), opacity: 0, duration: 0.25, ease: "power2.in" }}, cutTime + 0.05);
      }}
      tl.to("#sci1", {{ opacity: 0, duration: 0.2 }}, 6.8);
      tl.to("#afridi_hero", {{ scale: 0.8, opacity: 0.3, duration: 0.5 }}, 5.8);
      slam("#st_zero", 5.8, -10);
      shake("#s1 .cam", 5.95, 28);

      // S2a: 8.80s - 12.00s (Inaugural Season Reveal + Pitch)
      zoom("s2a", 8.8, 3.2, 1, 1.12);
      tl.fromTo("#sun", {{ y: 400 }}, {{ y: 0, duration: 0.6, ease: "back.out(1.4)" }}, 8.8);
      tl.fromTo("#stadium_pitch", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.5, ease: "back.out(1.4)" }}, 8.85);
      tl.fromTo("#tgA", {{ x: -900 }}, {{ x: 0, duration: 0.28, ease: "back.out(1.3)" }}, 9.0);
      tl.fromTo("#tgB", {{ x: -1100 }}, {{ x: 0, duration: 0.28, ease: "back.out(1.3)" }}, 9.3);
      slam("#yr", 10.4, -6);
      shake("#s2a .cam", 10.55, 22);

      // S2b: 12.00s - 16.20s (Shahid Afridi Deccan Chargers)
      zoom("s2b", 12.0, 4.2, 1, 1.08);
      tl.fromTo("#afridi_s2", {{ scale: 0.5, opacity: 0 }}, {{ scale: 0.95, opacity: 1, duration: 0.4, ease: "back.out(1.5)" }}, 12.0);
      pop("#tg_dc", 12.3);
      face("afridi_s2", 12.0, {{ b: [8, -8, 6], p: [10, 0] }}, 0.01);
      [12.3, 12.8, 13.3, 13.8, 14.3, 14.8].forEach((t) => {{
        face("afridi_s2", t, {{ m: "talk" }});
        face("afridi_s2", t + 0.2, {{ m: "smirk" }});
      }});

      // S2c: 16.20s - 23.80s (Rajasthan Royals Champions & Trophy)
      zoom("s2c", 16.2, 7.6, 1, 1.1);
      pop("#rr_banner", 16.2);
      // Trophy rises proudly first!
      tl.fromTo("#rr_trophy", {{ scale: 0.2, y: 300, opacity: 0 }}, {{ scale: 1, y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.8)" }}, 16.3);
      gsap.utils.toArray(".sc_rr").forEach((el, i) =>
        tl.fromTo(el, {{ x: 0, y: 0, opacity: 1 }}, {{ x: (rnd() - 0.5) * 500, y: (rnd() - 0.5) * 400, opacity: 0, duration: 0.8, ease: "power2.out" }}, 16.4 + i * 0.02)
      );
      tl.fromTo("#c2_tanvir", {{ x: -600 }}, {{ x: 0, duration: 0.35, ease: "back.out(1.3)" }}, 16.7);
      tl.fromTo("#c2_younis", {{ x: 600 }}, {{ x: 0, duration: 0.35, ease: "back.out(1.3)" }}, 17.6);
      tl.fromTo("#c2_akmal", {{ y: 600 }}, {{ y: 0, duration: 0.35, ease: "back.out(1.3)" }}, 18.8);
      shake("#s2c .cam", 16.5, 22);

      // S3: 23.80s - 35.80s (November 2008 & Collapse)
      zoom("s3", 23.8, 12.0, 1, 1.12);
      tl.fromTo("#tg_nov", {{ y: -400 }}, {{ y: 0, duration: 0.35, ease: "back.out(1.4)" }}, 23.9);
      slam("#nov_rupture", 27.4, -4);
      shake("#s3 .cam", 27.55, 30);
      tl.to("#nov_rupture", {{ opacity: 0.4, scale: 0.95, duration: 0.3 }}, 30.2);
      tl.fromTo("#s3_auction_board", {{ y: 600, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.3)" }}, 30.4);

      // S4: 35.80s - 47.80s (The Unwritten Rule & Azhar Mahmood)
      zoom("s4", 35.8, 12.0, 1, 1.1);
      pop("#tg_ban", 35.9);
      tl.fromTo("#doc_board", {{ y: -400 }}, {{ y: 0, duration: 0.35, ease: "back.out(1.3)" }}, 36.5);
      slam("#st_unwritten", 38.6, -10);
      shake("#s4 .cam", 38.75, 32);

      tl.fromTo("#c4_azhar", {{ x: -600 }}, {{ x: 0, duration: 0.35, ease: "back.out(1.3)" }}, 43.4);
      pop("#passport_cut", 45.8, 0.3);

      // S5: 47.80s - 54.91s (Close & CTA)
      tl.fromTo("#r5", {{ rotation: 0 }}, {{ rotation: 35, duration: 7.2, ease: "none" }}, 47.8);
      zoom("s5", 47.8, 7.2, 1, 1.1);
      pop("#tg_final", 47.9);
      tl.fromTo("#s5_hanger", {{ y: -300 }}, {{ y: 0, duration: 0.4, ease: "back.out(1.4)" }}, 48.1);

      // Pendulum swing for hanging empty jersey
      tl.fromTo("#s5_pendulum",
        {{ rotation: -7, transformOrigin: "0% 0%" }},
        {{ rotation: 7, duration: 1.4, repeat: 5, yoyo: true, ease: "sine.inOut" }},
        48.2
      );

      pop("#s5_years", 49.5);
      slam("#s5_cta", 51.5, -4);
      shake("#s5 .cam", 51.65, 24);

      // =========================================================
      // DETERMINISTIC PLAYWRIGHT SEEKER
      // =========================================================
      window.seekFrame = function(timeSeconds) {{
        tl.seek(timeSeconds);
      }};

      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""

(base / "index.html").write_text(get_html(inline_gsap=False), encoding="utf-8")
print(f"Generated {base / 'index.html'}")

(base / "standalone.html").write_text(get_html(inline_gsap=True), encoding="utf-8")
print(f"Generated {base / 'standalone.html'}")
