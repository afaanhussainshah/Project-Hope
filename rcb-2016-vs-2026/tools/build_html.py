import json
import base64
from pathlib import Path

base_dir = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\rcb-2016-vs-2026")
font_path = base_dir / "assets" / "fonts" / "Anton-Regular.ttf"
gsap_path = base_dir / "assets" / "gsap.min.js"

font_b64 = base64.b64encode(font_path.read_bytes()).decode("utf-8")
gsap_code = gsap_path.read_text(encoding="utf-8")

html_content = r'''<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <style>
      @font-face {
        font-family: "Anton";
        src: url("data:font/truetype;charset=utf-8;base64,__FONT_B64__") format("truetype");
        font-weight: 400;
        font-style: normal;
      }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body {
        margin: 0; width: 1080px; height: 1920px; overflow: hidden;
        background: #143D30; font-family: "Anton", sans-serif;
      }
      #root {
        position: relative; width: 1080px; height: 1920px; overflow: hidden;
      }
      .scene {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px;
        overflow: hidden; z-index: 1; display: none;
      }
      #s1 { display: block; z-index: 2; }
      .cam, .cam svg {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; display: block;
      }
      .cut {
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.35));
      }
      #wipe {
        position: absolute; left: 0; top: -190px; width: 1500px; height: 2300px; z-index: 5;
      }
      #grain {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 8;
        opacity: 0.08; mix-blend-mode: multiply; pointer-events: none;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' seed='4'/><feColorMatrix values='0 0 0 0 .35 0 0 0 0 .3 0 0 0 0 .25 0 0 0 .9 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");
      }
      #vig {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 9;
        pointer-events: none;
        background: radial-gradient(ellipse at 50% 45%, rgba(0, 0, 0, 0) 55%, rgba(0, 0, 0, 0.32) 100%);
      }
      /* CAPTION CONTAINER: Strictly single caption at a time, zero overlapping! */
      .cap {
        position: absolute; left: 50px; width: 980px; top: 1260px; height: 250px;
        z-index: 10; text-align: center; pointer-events: none;
        opacity: 0;
      }
      .cap span {
        display: inline-block; max-width: 960px; padding: 16px 36px 22px;
        background: #F6F1E4; color: #1B1B1B;
        font-size: 82px; line-height: 1.08; letter-spacing: 1px; text-transform: uppercase;
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.4));
      }
      .cap b { font-weight: 400; color: #C1121F; }
      .cap i { font-style: normal; background: #E3B23C; padding: 0 12px; }
      .cap mark { font-weight: 400; background: #1B1B1B; color: #F6F1E4; padding: 0 10px; }
    </style>
  </head>
  <body>
    <div id="root" data-start="0" data-duration="47.07" data-width="1080" data-height="1920">
      <!-- 5 SCENES -->
      <div id="s1" class="clip scene" data-start="0" data-duration="6.00"><div class="cam"></div></div>
      <div id="s2" class="clip scene" data-start="6.00" data-duration="10.20"><div class="cam"></div></div>
      <div id="s3" class="clip scene" data-start="16.20" data-duration="12.40"><div class="cam"></div></div>
      <div id="s4" class="clip scene" data-start="28.60" data-duration="10.20"><div class="cam"></div></div>
      <div id="s5" class="clip scene" data-start="38.80" data-duration="8.27"><div class="cam"></div></div>

      <audio id="vo" src="renders/full_audio_mix.wav" data-start="0" data-duration="47.073"></audio>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- EXACT 19 SYNCED CAPTIONS (NO OVERLAP!) -->
      <div class="clip cap" data-start="0.06" data-duration="3.64"><span><b>2016 RCB</b><br>VERSUS <i>2026 RCB</i></span></div>
      <div class="clip cap" data-start="3.90" data-duration="0.95"><span>ONE <b>MATCH.</b></span></div>
      <div class="clip cap" data-start="5.05" data-duration="0.90"><span><i>WHO WINS?</i></span></div>
      <div class="clip cap" data-start="6.15" data-duration="1.55"><span>ROUND ONE:<br><b>BATTING.</b></span></div>
      <div class="clip cap" data-start="7.85" data-duration="3.00"><span>GAYLE, DE VILLIERS<br>& <b>KOHLI AT THEIR PEAK.</b></span></div>
      <div class="clip cap" data-start="11.00" data-duration="3.15"><span>ON FLAT CHINNASWAMY,<br><b>220 IS EASY!</b></span></div>
      <div class="clip cap" data-start="14.30" data-duration="1.80"><span>ADVANTAGE<br><b>2016!</b></span></div>
      <div class="clip cap" data-start="16.35" data-duration="1.75"><span>ROUND TWO:<br><b>BOWLING.</b></span></div>
      <div class="clip cap" data-start="18.25" data-duration="3.70"><span>BHUVI · HAZLEWOOD<br><b>RASIKH · KRUNAL</b></span></div>
      <div class="clip cap" data-start="22.15" data-duration="2.70"><span>THEY'D LEAK RUNS...</span></div>
      <div class="clip cap" data-start="25.00" data-duration="1.50"><span>BUT THEY TAKE<br><b>WICKETS!</b></span></div>
      <div class="clip cap" data-start="26.65" data-duration="1.90"><span>ADVANTAGE<br><i>2026!</i></span></div>
      <div class="clip cap" data-start="28.75" data-duration="1.90"><span>ROUND THREE:<br><b>THE CHASE.</b></span></div>
      <div class="clip cap" data-start="30.80" data-duration="1.85"><span>KOHLI &<br><b>VENKATESH IYER.</b></span></div>
      <div class="clip cap" data-start="32.75" data-duration="3.40"><span>TIM DAVID FINISHING<br>AT <b>SR OF 188!</b></span></div>
      <div class="clip cap" data-start="36.30" data-duration="2.40"><span><b>2026</b><br>CHASES ANYTHING!</span></div>
      <div class="clip cap" data-start="38.90" data-duration="2.25"><span>MY PICK? <b>2026.</b><br>BY A <i>WHISKER.</i></span></div>
      <div class="clip cap" data-start="41.30" data-duration="3.75"><span>BUT IT ALL DEPENDS ON<br><b>WHO BATS FIRST!</b></span></div>
      <div class="clip cap" data-start="45.25" data-duration="1.82"><span>WHO WINS?<br><b>COMMENT YOUR PICK!</b></span></div>
    </div>

    <script>
__GSAP_CODE__
    </script>

    <script>
      // ==========================================================
      // PALETTE & HELPERS
      // ==========================================================
      let seed = 77;
      const reseed = (n) => (seed = n);
      const rnd = () => {
        seed = (seed + 0x6d2b79f5) | 0;
        let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
        t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
      };

      const C = {
        paper: "#F6F1E4",
        ink: "#1B1B1B",
        rcbRed: "#D71920",
        rcbGold: "#E3B23C",
        rcbBlack: "#141414",
        rcbNavy: "#001D3D",
        green: "#174D3A",
        dgreen: "#143D30",
        sky: "#9DB7C4",
        stamp: "#C1121F",
        white: "#FAF8F5",
        pitch: "#C2A675"
      };

      const svg = (inner, bg) =>
        `<svg viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg"><rect width="1080" height="1920" fill="${bg}"/>${inner}</svg>`;
      const put = (id, html) => (document.querySelector("#" + id + " .cam").innerHTML = html);
      const tx = (x, y, s, str, fill, anc = "middle", ex = "") =>
        `<text x="${x}" y="${y}" font-family="Anton" font-size="${s}" fill="${fill}" text-anchor="${anc}" ${ex}>${str}</text>`;

      function torn(x, y, w, h, j = 10, step = 38) {
        const p = [];
        for (let i = 0; i <= w; i += step) p.push([x + Math.min(i, w), y + (rnd() - 0.5) * j]);
        for (let i = step; i <= h; i += step) p.push([x + w + (rnd() - 0.5) * j, y + Math.min(i, h)]);
        for (let i = w - step; i >= 0; i -= step) p.push([x + Math.max(i, 0), y + h + (rnd() - 0.5) * j]);
        for (let i = h - step; i > 0; i -= step) p.push([x + (rnd() - 0.5) * j, y + i]);
        return p.map((q) => q[0].toFixed(1) + "," + q[1].toFixed(1)).join(" ");
      }
      const sheet = (x, y, w, h, fill, j = 10) => `<polygon points="${torn(x, y, w, h, j)}" fill="${fill}"/>`;

      const rays = (id, cx, cy, n, c) => {
        let s = `<g id="${id}">`;
        for (let i = 0; i < n; i += 2) {
          const a = (i * 2 * Math.PI) / n, b = ((i + 1) * 2 * Math.PI) / n;
          s += `<polygon points="${cx},${cy} ${(cx + 2000 * Math.cos(a)).toFixed(0)},${(cy + 2000 * Math.sin(a)).toFixed(0)} ${(cx + 2000 * Math.cos(b)).toFixed(0)},${(cy + 2000 * Math.sin(b)).toFixed(0)}" fill="${c}"/>`;
        }
        return s + "</g>";
      };

      const scraps = (cls, cx, cy, n, colors) => {
        let s = "";
        for (let i = 0; i < n; i++) {
          const w = 35 + rnd() * 65;
          const col = colors ? colors[i % colors.length] : (i % 2 ? C.rcbGold : C.rcbRed);
          s += `<polygon class="${cls}" points="${cx},${cy} ${(cx + w).toFixed(0)},${(cy + rnd() * 26).toFixed(0)} ${(cx + w * 0.5).toFixed(0)},${(cy + w * 0.9).toFixed(0)}" fill="${col}" opacity="0"/>`;
        }
        return s;
      };

      // ==========================================================
      // CHARACTER RIG FUNCTION (Gayle, Kohli, AB, Bhuvi, Hazlewood, David)
      // ==========================================================
      function guy(id, x, y, s, o = {}) {
        const skin = o.skin || "#E9B990";
        const sk2 = o.sk2 || "#D69E73";
        const hair = o.hair || "#332211";
        const m = o.m || "flat";
        const cap = o.cap || C.rcbRed;
        const visor = o.visor || C.rcbGold;
        const jersey = o.jersey || C.rcbRed;
        const badge = o.badge || C.rcbGold;

        const mo = (n, h) => `<g class="m m-${n}" opacity="${n === m ? 1 : 0}">${h}</g>`;

        return `<g id="${id}"><g transform="translate(${x} ${y}) scale(${s})">
          <!-- Torso -->
          <g class="cut">
            <path d="M-240 430 Q-245 250 -100 215 L100 215 Q245 250 240 430Z" fill="${jersey}"/>
            <!-- Collar / Trim -->
            <path d="M-60 215 L0 300 L60 215 L38 198 L-38 198Z" fill="${C.rcbGold}"/>
            <rect x="-44" y="148" width="88" height="92" rx="18" fill="${sk2}"/>
            <!-- Team Crest -->
            <circle cx="0" cy="330" r="32" fill="${badge}"/><circle cx="0" cy="330" r="14" fill="${C.ink}"/>
          </g>
          <!-- Head -->
          <g class="head cut">
            <!-- Ears -->
            <ellipse cx="-145" cy="15" rx="25" ry="38" fill="${sk2}"/><ellipse cx="145" cy="15" rx="25" ry="38" fill="${sk2}"/>
            <!-- Face -->
            <rect x="-142" y="-155" width="284" height="340" rx="130" fill="${skin}"/>
            ${o.beard ? `<path d="M-142 30 Q-148 185 0 185 Q148 185 142 30 Q115 145 0 148 Q-115 145 -142 30Z" fill="${hair}"/>` : ""}
            ${o.dreads ? `<!-- Gayle Dreads -->
              <path d="M-160 -40 Q-200 80 -180 220 M-140 -20 Q-180 120 -150 260 M-170 -10 Q-220 140 -170 280" stroke="${hair}" stroke-width="26" fill="none" stroke-linecap="round"/>
              <path d="M160 -40 Q200 80 180 220 M140 -20 Q180 120 150 260 M170 -10 Q220 140 170 280" stroke="${hair}" stroke-width="26" fill="none" stroke-linecap="round"/>` : ""}
            <!-- Hair Sideburns -->
            <path d="M-148 -55 L-148 -90 L-118 -90 L-128 -15Z M148 -55 L148 -90 L118 -90 L128 -15Z" fill="${hair}"/>
            <!-- Cap -->
            <path d="M-156 -88 Q-158 -255 0 -255 Q158 -255 156 -88Z" fill="${cap}"/>
            <path d="M-174 -92 Q0 -128 174 -92 Q194 -58 0 -68 Q-194 -58 -174 -92Z" fill="${visor}"/>
            <circle cx="0" cy="-180" r="28" fill="${badge}"/>
            ${o.shades ? `<g class="cut"><rect x="-110" y="-15" width="220" height="42" rx="12" fill="#1B1B1B"/><line x1="-12" y1="4" x2="12" y2="4" stroke="${C.rcbGold}" stroke-width="6"/></g>` : `
            <!-- Eyes -->
            <g class="eye eyeL"><circle cx="-60" cy="5" r="35" fill="#fff"/><circle class="pupil pupilL" cx="-60" cy="5" r="16" fill="${C.ink}"/></g>
            <g class="eye eyeR"><circle cx="60" cy="5" r="35" fill="#fff"/><circle class="pupil pupilR" cx="60" cy="5" r="16" fill="${C.ink}"/></g>`}
            <!-- Eyebrows -->
            <rect class="browL" x="-100" y="-56" width="78" height="17" rx="6" fill="${hair}"/>
            <rect class="browR" x="22" y="-56" width="78" height="17" rx="6" fill="${hair}"/>
            <!-- Nose -->
            <path d="M-10 28 Q-4 70 20 60" stroke="${sk2}" stroke-width="9" fill="none" stroke-linecap="round"/>
            <!-- Mouths -->
            ${mo("flat", '<rect x="-44" y="112" width="88" height="13" rx="6" fill="#7A2E22"/>')}
            ${mo("o", '<ellipse cx="0" cy="118" rx="28" ry="32" fill="#4A1410"/>')}
            ${mo("smirk", '<path d="M-48 116 Q14 150 62 98" stroke="#7A2E22" stroke-width="13" fill="none" stroke-linecap="round"/>')}
            ${mo("teeth", '<rect x="-58" y="96" width="116" height="46" rx="14" fill="#fff" stroke="#7A2E22" stroke-width="9"/><path d="M-20 98V140M20 98V140M-56 119H56" stroke="#C9B9A8" stroke-width="4"/>')}
            ${mo("roar", '<path d="M-55 100 Q0 160 55 100 Q30 75 0 80 Q-30 75 -55 100Z" fill="#4A1410"/>')}
          </g>
        </g></g>`;
      }

      function cricketBat(id, x, y, rot, s = 1) {
        return `<g id="${id}" class="cut" transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
          <rect x="-14" y="-320" width="28" height="140" rx="8" fill="#F6F1E4" stroke="#D9BC82" stroke-width="4"/>
          <path d="M-36 -180 L36 -180 L42 160 Q42 200 0 200 Q-42 200 -42 160 Z" fill="#E5C38E" stroke="#B89358" stroke-width="5"/>
          <rect x="-24" y="-140" width="48" height="120" fill="${C.rcbRed}" rx="4"/>
          ${tx(0, -70, 32, "MRF", "#FFF")}
        </g>`;
      }

      function wickets(id, x, y, s = 1) {
        return `<g id="${id}" class="cut" transform="translate(${x} ${y}) scale(${s})">
          <rect id="stump1" x="-45" y="-180" width="16" height="180" rx="4" fill="#E5C38E"/>
          <rect id="stump2" x="-8" y="-180" width="16" height="180" rx="4" fill="#E5C38E"/>
          <rect id="stump3" x="29" y="-180" width="16" height="180" rx="4" fill="#E5C38E"/>
          <rect id="bail1" x="-50" y="-195" width="45" height="12" rx="3" fill="#D71920"/>
          <rect id="bail2" x="-2" y="-195" width="45" height="12" rx="3" fill="#D71920"/>
        </g>`;
      }

      // ==========================================================
      // SCENE 1: THE ULTIMATE RCB CLASH (0.00s - 6.00s)
      // ==========================================================
      reseed(11);
      const s1_k16 = guy("gK16", 300, 780, 0.78, {
        hair: "#1B1B1B", beard: 1, cap: C.rcbRed, visor: C.rcbGold, jersey: C.rcbRed, m: "roar"
      });
      const s1_k26 = guy("gK26", 780, 780, 0.78, {
        hair: "#1B1B1B", beard: 1, cap: C.rcbNavy, visor: C.rcbRed, jersey: C.rcbNavy, m: "smirk"
      });

      put("s1", svg(
        rays("r1", 540, 780, 22, "#241014") +
        // Split Banners
        `<g id="s1_split">
          <!-- 2016 Side -->
          <g id="s1_b16" class="cut">
            ${sheet(70, 200, 440, 220, C.rcbRed, 8)}
            <rect x="90" y="220" width="400" height="180" fill="${C.rcbBlack}"/>
            ${tx(290, 285, 42, "RCB VINTAGE", C.rcbGold)}
            ${tx(290, 365, 84, "2016", C.rcbRed)}
          </g>
          <!-- 2026 Side -->
          <g id="s1_b26" class="cut">
            ${sheet(570, 200, 440, 220, C.rcbNavy, 8)}
            <rect x="590" y="220" width="400" height="180" fill="${C.rcbBlack}"/>
            ${tx(790, 285, 42, "RCB MODERN", C.rcbGold)}
            ${tx(790, 365, 84, "2026", C.rcbGold)}
          </g>
        </g>` +
        // Characters Faceoff
        `<g id="s1_faceoff">${s1_k16}${s1_k26}</g>` +
        // Center Lightning Bolt Tear
        `<polygon id="s1_bolt" points="540,120 570,450 510,650 580,950 500,1250 560,1550 540,1850" fill="${C.rcbGold}" class="cut"/>` +
        // Slam Badge: ONE MATCH. WHO WINS?
        `<g id="s1_badge" class="cut"><g transform="rotate(-6 540 680)">
          ${sheet(160, 600, 760, 160, C.stamp, 10)}
          ${tx(540, 675, 78, "ONE MATCH. WHO WINS?", C.paper)}
          ${tx(540, 730, 40, "THE ULTIMATE FRANCHISE CLASH", C.rcbGold)}
        </g></g>`,
        C.rcbBlack
      ));

      // ==========================================================
      // SCENE 2: ROUND 1 - BATTING (THE HOLY TRINITY) (6.00 - 16.20s)
      // ==========================================================
      reseed(22);
      const s2_gayle = guy("gGayle", 260, 780, 0.72, {
        skin: "#7A4E2B", sk2: "#5E3A1D", hair: "#1B1B1B", beard: 1, dreads: 1, shades: 1, cap: C.rcbGold, visor: C.rcbRed, jersey: C.rcbRed, m: "teeth"
      });
      const s2_ab = guy("gAB", 540, 750, 0.78, {
        skin: "#F5CBA7", sk2: "#E59866", hair: "#D4AC0D", cap: C.rcbRed, visor: C.rcbGold, jersey: C.rcbRed, m: "smirk"
      });
      const s2_kohli = guy("gKohli16", 820, 780, 0.72, {
        hair: "#1B1B1B", beard: 1, cap: C.rcbRed, visor: C.rcbGold, jersey: C.rcbRed, m: "roar"
      });

      put("s2", svg(
        `<rect width="1080" height="700" fill="#2E1114"/>` +
        `<rect y="700" width="1080" height="1220" fill="${C.dgreen}"/>` +
        // Stadium light rays
        rays("r2", 540, 600, 20, "#4A181C") +
        // Title: Round 1 Batting
        `<g id="s2_title" class="cut">
          ${sheet(120, 180, 840, 150, C.paper, 8)}
          <rect x="140" y="200" width="800" height="110" fill="${C.rcbRed}"/>
          ${tx(540, 255, 38, "ROUND ONE", C.rcbGold)}
          ${tx(540, 295, 52, "PEAK BATTING FIREPOWER", C.paper)}
        </g>` +
        // Trio figures
        `<g id="s2_trio">
          ${s2_gayle}
          ${cricketBat("batGayle", 160, 760, -30, 0.7)}
          ${s2_ab}
          ${cricketBat("batAB", 540, 700, 15, 0.75)}
          ${s2_kohli}
          ${cricketBat("batKohli", 920, 760, 35, 0.7)}
        </g>` +
        // 220 Score Tag
        `<g id="s2_score" class="cut"><g transform="rotate(-5 540 1020)">
          ${sheet(160, 950, 760, 140, C.rcbGold, 8)}
          <rect x="180" y="970" width="720" height="100" fill="${C.ink}"/>
          ${tx(540, 1025, 42, "CHINNASWAMY HIGHWAY", C.rcbGold)}
          ${tx(540, 1055, 54, "220 IS CHILD'S PLAY!", C.paper)}
        </g></g>` +
        // Advantage 2016 Stamp
        `<g id="s2_adv16" class="cut"><g transform="rotate(8 540 650)">
          ${sheet(200, 580, 680, 150, C.stamp, 10)}
          ${tx(540, 655, 78, "ADVANTAGE 2016!", C.paper)}
          ${tx(540, 705, 38, "UNSTOPPABLE RUN MACHINE", C.rcbGold)}
        </g></g>`,
        C.rcbBlack
      ));

      // ==========================================================
      // SCENE 3: ROUND 2 - BOWLING (THE 2026 ATTACK) (16.20 - 28.60s)
      // ==========================================================
      reseed(33);
      const s3_bhuvi = guy("gBhuvi", 320, 780, 0.78, {
        hair: "#1B1B1B", beard: 1, cap: C.rcbNavy, visor: C.rcbRed, jersey: C.rcbNavy, m: "smirk"
      });
      const s3_hazle = guy("gHazle", 760, 750, 0.82, {
        skin: "#F5CBA7", sk2: "#E59866", hair: "#D4AC0D", cap: C.rcbNavy, visor: C.rcbGold, jersey: C.rcbNavy, m: "teeth"
      });

      put("s3", svg(
        `<rect width="1080" height="700" fill="#0C1B2A"/>` +
        `<rect y="700" width="1080" height="1220" fill="${C.dgreen}"/>` +
        rays("r3", 540, 600, 20, "#162E48") +
        // Title: Round 2 Bowling
        `<g id="s3_title" class="cut">
          ${sheet(120, 180, 840, 150, C.paper, 8)}
          <rect x="140" y="200" width="800" height="110" fill="${C.rcbNavy}"/>
          ${tx(540, 255, 38, "ROUND TWO", C.rcbGold)}
          ${tx(540, 295, 52, "THE 2026 BOWLING MACHINE", C.paper)}
        </g>` +
        // Bowlers
        `<g id="s3_bowlers">${s3_bhuvi}${s3_hazle}</g>` +
        // Stumps tumbling
        wickets("s3_stumps", 540, 950, 1.2) +
        // Wicket Ball
        `<circle id="s3_ball" cx="540" cy="850" r="32" fill="${C.rcbRed}" class="cut"/>` +
        // Tag: Bhuvi / Hazlewood / Rasikh / Krunal
        `<g id="s3_names" class="cut">
          ${sheet(140, 1020, 800, 110, C.paper, 6)}
          ${tx(540, 1085, 46, "BHUVI · HAZLEWOOD · RASIKH · KRUNAL", C.ink)}
        </g>` +
        // Advantage 2026 Stamp
        `<g id="s3_adv26" class="cut"><g transform="rotate(-8 540 620)">
          ${sheet(200, 550, 680, 150, C.stamp, 10)}
          ${tx(540, 625, 78, "ADVANTAGE 2026!", C.paper)}
          ${tx(540, 675, 38, "THEY TAKE CRUCIAL WICKETS", C.rcbGold)}
        </g></g>`,
        C.rcbBlack
      ));

      // ==========================================================
      // SCENE 4: ROUND 3 - THE CHASE (28.60 - 38.80s)
      // ==========================================================
      reseed(44);
      const s4_david = guy("gDavid", 540, 750, 0.88, {
        skin: "#F5CBA7", sk2: "#E59866", hair: "#5A3A22", beard: 1, cap: C.rcbNavy, visor: C.rcbRed, jersey: C.rcbNavy, m: "roar"
      });

      put("s4", svg(
        rays("r4", 540, 750, 22, "#241014") +
        // Title: Round 3 The Chase
        `<g id="s4_title" class="cut">
          ${sheet(120, 180, 840, 150, C.paper, 8)}
          <rect x="140" y="200" width="800" height="110" fill="${C.rcbRed}"/>
          ${tx(540, 255, 38, "ROUND THREE", C.rcbGold)}
          ${tx(540, 295, 52, "THE IMPOSSIBLE CHASE", C.paper)}
        </g>` +
        // Tim David Monster Finisher
        `<g id="s4_hero">${s4_david}${cricketBat("batDavid", 360, 720, -45, 0.9)}</g>` +
        // Strike Rate 188 Badge
        `<g id="s4_srBadge" class="cut"><g transform="rotate(-6 540 460)">
          ${sheet(220, 390, 640, 130, C.rcbGold, 8)}
          ${tx(540, 455, 62, "TIM DAVID: SR 188.0!", C.ink)}
          ${tx(540, 495, 32, "DEATH OVER DEMOLITION", C.stamp)}
        </g></g>` +
        // Chases Anything Stamp
        `<g id="s4_stampChase" class="cut"><g transform="rotate(7 540 1020)">
          ${sheet(160, 950, 760, 150, C.stamp, 10)}
          ${tx(540, 1025, 76, "CHASES ANYTHING!", C.paper)}
          ${tx(540, 1075, 38, "2026 DEPTH IS RUTHLESS", C.rcbGold)}
        </g></g>`,
        C.rcbBlack
      ));

      // ==========================================================
      // SCENE 5: VERDICT & CTA (38.80 - 47.07s)
      // ==========================================================
      reseed(55);
      put("s5", svg(
        rays("r5", 540, 800, 24, "#241014") +
        // Verdict Card: 2026 BY A WHISKER
        `<g id="s5_verdict" class="cut"><g transform="rotate(-5 540 340)">
          ${sheet(140, 260, 800, 170, C.paper, 8)}
          <rect x="160" y="280" width="760" height="130" fill="${C.rcbNavy}"/>
          ${tx(540, 335, 42, "THE EXPERT VERDICT", C.rcbGold)}
          ${tx(540, 385, 66, "2026 BY A WHISKER!", C.paper)}
        </g></g>` +
        // Stamped Condition: WHO BATS FIRST!
        `<g id="s5_cond" class="cut"><g transform="rotate(6 540 560)">
          ${sheet(180, 490, 720, 130, C.rcbGold, 8)}
          ${tx(540, 555, 52, "ALL DEPENDS ON...", C.ink)}
          ${tx(540, 598, 44, "WHO BATS FIRST!", C.stamp)}
        </g></g>` +
        // Final CTA Card
        `<g id="s5_cta" class="cut">
          ${sheet(100, 880, 880, 250, C.rcbRed, 10)}
          <rect x="120" y="900" width="840" height="210" fill="${C.ink}"/>
          ${tx(540, 965, 48, "WHO WINS IN YOUR BOOK?", C.rcbGold)}
          ${tx(540, 1035, 78, "COMMENT YOUR PICK!", C.paper)}
          ${tx(540, 1085, 36, "DROP 2016 OR 2026 BELOW", C.rcbGold)}
        </g>`,
        C.rcbBlack
      ));

      // ==========================================================
      // TIMELINE ORCHESTRATION (GSAP 3)
      // ==========================================================
      const tl = gsap.timeline({ paused: true });
      const CC = "50% 50%";

      // Origins
      gsap.set("#r1,#r2,#r3,#r4,#r5", { svgOrigin: "540 800" });
      gsap.set("#s1_badge,#s2_adv16,#s2_score,#s3_adv26,#s3_names,#s4_srBadge,#s4_stampChase,#s5_verdict,#s5_cond,#s5_cta", { transformOrigin: CC });
      gsap.set("#batGayle,#batAB,#batKohli,#batDavid", { transformOrigin: "bottom center" });
      gsap.set("#stump1,#stump2,#stump3,#bail1,#bail2", { transformOrigin: "bottom center" });
      gsap.set(".browL,.browR,.eye,.pupil", { transformOrigin: CC });

      // Primitives
      const pop = (sel, t, d = 0.22) =>
        tl.fromTo(sel, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: d, ease: "back.out(2.2)" }, t);
      const slam = (sel, t, r = 0) =>
        tl.fromTo(sel, { scale: 3.0, opacity: 0, rotation: r }, { scale: 1, opacity: 1, rotation: 0, duration: 0.16, ease: "power4.in" }, t);
      const shake = (sel, t, a = 24) =>
        tl.to(sel, { x: a, y: -a * 0.6, duration: 0.04 }, t)
          .to(sel, { x: -a * 0.8, y: a * 0.5, duration: 0.04 }, t + 0.04)
          .to(sel, { x: a * 0.4, y: a * 0.3, duration: 0.04 }, t + 0.08)
          .to(sel, { x: 0, y: 0, duration: 0.05 }, t + 0.12);
      const zoom = (id, t, d, from, to, origin = CC, ease = "none") =>
        tl.fromTo(`#${id} svg`, { scale: from }, { scale: to, duration: d, ease, transformOrigin: origin }, t);

      function face(id, t, o, d = 0.1) {
        const q = (s) => `#${id} ${s}`;
        if (o.m) {
          tl.set(q(".m"), { opacity: 0 }, t);
          tl.set(q(".m-" + o.m), { opacity: 1 }, t + 0.001);
        }
        if (o.b) {
          tl.to(q(".browL"), { rotation: o.b[0], y: o.b[2] || 0, duration: d }, t);
          tl.to(q(".browR"), { rotation: o.b[1], y: o.b[2] || 0, duration: d }, t);
        }
        if (o.e != null) tl.to(q(".eye"), { scale: o.e, duration: d }, t);
        if (o.p) {
          tl.to(q(".pupilL"), { x: o.p[0], y: o.p[1], duration: d }, t);
          tl.to(q(".pupilR"), { x: o.p[0], y: o.p[1], duration: d }, t);
        }
      }

      // ==========================================================
      // SCENE VISIBILITY CONTROLLER: STRICT TIME WINDOWS!
      // ==========================================================
      const sceneList = [
        { id: "#s1", start: 0.00, end: 6.00 },
        { id: "#s2", start: 6.00, end: 16.20 },
        { id: "#s3", start: 16.20, end: 28.60 },
        { id: "#s4", start: 28.60, end: 38.80 },
        { id: "#s5", start: 38.80, end: 47.07 }
      ];

      tl.set("#s2,#s3,#s4,#s5", { display: "none", zIndex: 1 }, 0);
      tl.set("#s1", { display: "block", zIndex: 2 }, 0);

      sceneList.forEach((sc) => {
        tl.set(sc.id, { display: "block", zIndex: 3 }, sc.start);
        if (sc.end < 47.0) {
          tl.set(sc.id, { display: "none", zIndex: 1 }, sc.end);
        }
      });

      // ==========================================================
      // CAPTIONS: SINGLE ACTIVE CAPTION AT A TIME (ZERO OVERLAP!)
      // ==========================================================
      gsap.utils.toArray(".cap").forEach((capEl, i) => {
        const start = +capEl.dataset.start;
        const dur = +capEl.dataset.duration || 2.0;
        const end = start + dur;

        tl.fromTo(
          capEl,
          { opacity: 0, scale: 0.6, rotation: i % 2 ? 4 : -4 },
          { opacity: 1, scale: 1, rotation: i % 2 ? -1.5 : 1.5, duration: 0.14, ease: "back.out(2.5)" },
          start
        );

        tl.to(
          capEl,
          { opacity: 0, scale: 0.85, duration: 0.10, ease: "power2.in" },
          end - 0.08
        );
      });

      // ==========================================================
      // PAPER WIPE TRANSITIONS
      // ==========================================================
      const wipe = document.getElementById("wipe");
      wipe.innerHTML = `<svg viewBox="0 0 1500 2300" width="1500" height="2300" xmlns="http://www.w3.org/2000/svg">
        <polygon id="wp" points="${torn(0, 0, 1500, 2300, 18, 48)}" fill="${C.paper}" class="cut"/>
      </svg>`;
      gsap.set("#wipe", { x: -1700 });

      [[6.00, C.paper, 1], [16.20, C.rcbRed, -1], [28.60, C.rcbGold, 1], [38.80, C.ink, -1]].forEach(([t, c, dir]) => {
        tl.set("#wp", { fill: c }, t - 0.19);
        tl.fromTo("#wipe", { x: dir > 0 ? -1700 : 1300 }, { x: dir > 0 ? 1300 : -1700, duration: 0.36, ease: "none" }, t - 0.18);
      });

      // ==========================================================
      // SCENE 1 TIMELINE (0.00s - 6.00s): THE HOOK
      // ==========================================================
      tl.fromTo("#r1", { rotation: 0 }, { rotation: 25, duration: 6.0, ease: "none" }, 0);
      zoom("s1", 0, 6.0, 1, 1.08);

      // Banners slide in
      tl.fromTo("#s1_b16", { x: -600 }, { x: 0, duration: 0.35, ease: "back.out(1.4)" }, 0.1);
      tl.fromTo("#s1_b26", { x: 600 }, { x: 0, duration: 0.35, ease: "back.out(1.4)" }, 0.2);

      // Characters rise
      tl.fromTo("#gK16", { y: 1000 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, 0.25);
      tl.fromTo("#gK26", { y: 1000 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, 0.35);

      // Lightning bolt rips down center at 3.90s
      tl.fromTo("#s1_bolt", { scaleY: 0 }, { scaleY: 1, duration: 0.18, ease: "power4.in" }, 3.85);
      shake("#s1 .cam", 3.92, 22);

      // Slam Badge: ONE MATCH. WHO WINS?
      slam("#s1_badge", 5.05, -6);
      shake("#s1 .cam", 5.21, 28);

      // ==========================================================
      // SCENE 2 TIMELINE (6.00s - 16.20s): ROUND 1 BATTING
      // ==========================================================
      zoom("s2", 6.0, 10.2, 1, 1.07);

      // Title Card
      tl.fromTo("#s2_title", { y: -400 }, { y: 0, duration: 0.3, ease: "back.out(1.3)" }, 6.10);
      shake("#s2 .cam", 6.35, 16);

      // Trio rises up
      tl.fromTo("#gGayle", { y: 800 }, { y: 0, duration: 0.35, ease: "back.out(1.4)" }, 7.80);
      tl.fromTo("#gAB", { y: 800 }, { y: 0, duration: 0.35, ease: "back.out(1.4)" }, 8.05);
      tl.fromTo("#gKohli16", { y: 800 }, { y: 0, duration: 0.35, ease: "back.out(1.4)" }, 8.30);

      // Bat swings
      tl.fromTo("#batGayle", { rotation: -70 }, { rotation: -30, duration: 0.3, ease: "back.out(2)" }, 8.0);
      tl.fromTo("#batAB", { rotation: -30 }, { rotation: 15, duration: 0.3, ease: "back.out(2)" }, 8.3);
      tl.fromTo("#batKohli", { rotation: 60 }, { rotation: 35, duration: 0.3, ease: "back.out(2)" }, 8.5);

      // 220 Score Card pops
      pop("#s2_score", 11.00, 0.28);
      shake("#s2 .cam", 11.25, 20);

      // Advantage 2016 Slam
      slam("#s2_adv16", 14.30, 8);
      shake("#s2 .cam", 14.46, 30);

      // ==========================================================
      // SCENE 3 TIMELINE (16.20s - 28.60s): ROUND 2 BOWLING
      // ==========================================================
      zoom("s3", 16.2, 12.4, 1, 1.06);

      // Title
      tl.fromTo("#s3_title", { y: -400 }, { y: 0, duration: 0.3, ease: "back.out(1.3)" }, 16.30);
      shake("#s3 .cam", 16.55, 16);

      // Bowlers slide in
      tl.fromTo("#gBhuvi", { x: -600 }, { x: 0, duration: 0.35, ease: "back.out(1.4)" }, 18.20);
      tl.fromTo("#gHazle", { x: 600 }, { x: 0, duration: 0.35, ease: "back.out(1.4)" }, 18.45);

      // Names bar pops
      pop("#s3_names", 18.70, 0.25);

      // Ball bowls down the pitch
      tl.fromTo("#s3_ball", { x: -400, y: -200, scale: 0.4 }, { x: 0, y: 0, scale: 1, duration: 0.45, ease: "power2.in" }, 24.50);

      // Stumps shattered!
      tl.to("#stump1", { rotation: -35, x: -40, duration: 0.2, ease: "power3.out" }, 24.95);
      tl.to("#stump2", { rotation: 15, y: -20, duration: 0.2, ease: "power3.out" }, 24.95);
      tl.to("#stump3", { rotation: 40, x: 50, duration: 0.2, ease: "power3.out" }, 24.95);
      tl.to("#bail1", { y: -120, rotation: -180, duration: 0.3, ease: "power1.out" }, 24.95);
      tl.to("#bail2", { y: -140, rotation: 180, duration: 0.3, ease: "power1.out" }, 24.95);
      shake("#s3 .cam", 25.00, 26);

      // Advantage 2026 Slam
      slam("#s3_adv26", 26.65, -8);
      shake("#s3 .cam", 26.81, 30);

      // ==========================================================
      // SCENE 4 TIMELINE (28.60s - 38.80s): ROUND 3 THE CHASE
      // ==========================================================
      zoom("s4", 28.6, 10.2, 1, 1.07);

      // Title
      tl.fromTo("#s4_title", { y: -400 }, { y: 0, duration: 0.3, ease: "back.out(1.3)" }, 28.70);
      shake("#s4 .cam", 28.95, 16);

      // Tim David slides up
      tl.fromTo("#gDavid", { y: 800 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, 32.70);
      tl.fromTo("#batDavid", { scale: 0, rotation: 30 }, { scale: 0.9, rotation: -45, duration: 0.35, ease: "back.out(2)" }, 32.90);

      // SR 188 badge slams
      slam("#s4_srBadge", 33.20, -6);
      shake("#s4 .cam", 33.36, 22);

      // Chases Anything Stamp
      slam("#s4_stampChase", 36.30, 7);
      shake("#s4 .cam", 36.46, 32);

      // ==========================================================
      // SCENE 5 TIMELINE (38.80s - 47.07s): VERDICT & CTA
      // ==========================================================
      tl.fromTo("#r5", { rotation: 0 }, { rotation: 30, duration: 8.27, ease: "none" }, 38.80);
      zoom("s5", 38.8, 8.27, 1, 1.06);

      // Verdict Card drops
      tl.fromTo("#s5_verdict", { y: -500 }, { y: 0, duration: 0.32, ease: "back.out(1.4)" }, 38.90);
      shake("#s5 .cam", 39.15, 20);

      // Condition Stamp slams
      slam("#s5_cond", 41.30, 6);
      shake("#s5 .cam", 41.46, 24);

      // Final CTA pop
      pop("#s5_cta", 45.25, 0.28);
      shake("#s5 .cam", 45.50, 22);

      // Exposure for render
      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = tl;
      window.seekFrame = (t) => { tl.seek(t); };
      tl.seek(0);
    </script>
  </body>
</html>
'''

html_content = html_content.replace("__FONT_B64__", font_b64)
html_content = html_content.replace("__GSAP_CODE__", gsap_code)

(base_dir / "standalone.html").write_text(html_content, encoding="utf-8")
(base_dir / "index.html").write_text(html_content, encoding="utf-8")
print(f"Built standalone.html and index.html successfully! Size: {len(html_content)/1024:.1f} KB")
