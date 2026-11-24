import json
import base64
from pathlib import Path

base_dir = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\follow-on-gamble")
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
        opacity: 0; /* hidden by default, animated by GSAP */
      }
      .cap span {
        display: inline-block; max-width: 960px; padding: 16px 36px 22px;
        background: #F6F1E4; color: #1B1B1B;
        font-size: 82px; line-height: 1.08; letter-spacing: 1px; text-transform: uppercase;
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.4));
      }
      .cap b { font-weight: 400; color: #C1121F; }
      .cap i { font-style: normal; background: #E3B23C; padding: 0 12px; }
      .cap mark { font-weight: 400; background: #003366; color: #F6F1E4; padding: 0 10px; }
    </style>
  </head>
  <body>
    <div id="root" data-start="0" data-duration="49.48" data-width="1080" data-height="1920">
      <!-- 5 SCENES -->
      <div id="s1" class="clip scene" data-start="0" data-duration="7.60"><div class="cam"></div></div>
      <div id="s2" class="clip scene" data-start="7.60" data-duration="8.90"><div class="cam"></div></div>
      <div id="s3" class="clip scene" data-start="16.50" data-duration="10.10"><div class="cam"></div></div>
      <div id="s4" class="clip scene" data-start="26.60" data-duration="15.40"><div class="cam"></div></div>
      <div id="s5" class="clip scene" data-start="42.00" data-duration="7.48"><div class="cam"></div></div>

      <audio id="vo" src="renders/full_audio_mix.wav" data-start="0" data-duration="49.476"></audio>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- EXACT 20 SYNCED CAPTIONS (START & DURATION - NO OVERLAP!) -->
      <div class="clip cap" data-start="0.03" data-duration="3.85"><span><b>99% OF CRICKET FANS</b><br>DON'T KNOW THIS</span></div>
      <div class="clip cap" data-start="4.14" data-duration="3.30"><span>AND IT COST AUSTRALIA<br>THE <i>GREATEST STREAK</i></span></div>
      <div class="clip cap" data-start="7.65" data-duration="0.95"><span>HERE'S <b>THE RULE.</b></span></div>
      <div class="clip cap" data-start="8.69" data-duration="3.25"><span>IF 1ST BATTING TEAM<br>LEADS BY <b>200+ RUNS</b></span></div>
      <div class="clip cap" data-start="12.05" data-duration="2.10"><span>THEY CAN MAKE YOU<br><b>BAT AGAIN</b> STRAIGHT AWAY</span></div>
      <div class="clip cap" data-start="14.25" data-duration="2.25"><span>BUT IT'S <i>THEIR CHOICE.</i><br>THEY DON'T HAVE TO.</span></div>
      <div class="clip cap" data-start="16.65" data-duration="1.40"><span>AND THAT'S <b>THE GAMBLE.</b></span></div>
      <div class="clip cap" data-start="18.15" data-duration="1.50"><span>THEIR BOWLERS<br><b>GET TIRED.</b></span></div>
      <div class="clip cap" data-start="19.75" data-duration="2.75"><span>CHASE ON A<br><b>WORN-OUT PITCH.</b></span></div>
      <div class="clip cap" data-start="22.65" data-duration="2.65"><span>FOUR TIMES IN HISTORY<br>A TEAM <i>FOLLOWED ON</i></span></div>
      <div class="clip cap" data-start="25.40" data-duration="1.20"><span>...AND <b>STILL WON!</b></span></div>
      <div class="clip cap" data-start="26.70" data-duration="1.85"><span><b>KOLKATA, 2001.</b></span></div>
      <div class="clip cap" data-start="28.70" data-duration="2.85"><span>AUSTRALIA HAD WON<br><b>16 TESTS IN A ROW.</b></span></div>
      <div class="clip cap" data-start="31.70" data-duration="3.20"><span>INDIA WERE <b>274 RUNS</b><br>BEHIND!</span></div>
      <div class="clip cap" data-start="35.05" data-duration="2.10"><span>AUSTRALIA <b>ENFORCED</b><br>THE FOLLOW-ON.</span></div>
      <div class="clip cap" data-start="37.30" data-duration="3.30"><span>THEN <b>LAXMAN & DRAVID</b><br>BATTED AN ENTIRE DAY...</span></div>
      <div class="clip cap" data-start="40.75" data-duration="1.25"><span>...AND <b>INDIA WON!</b></span></div>
      <div class="clip cap" data-start="42.20" data-duration="1.85"><span>THE FOLLOW-ON IS<br>A <i>WEAPON.</i></span></div>
      <div class="clip cap" data-start="44.15" data-duration="2.10"><span>BUT SOMETIMES...<br>IT'S A <b>TRAP!</b></span></div>
      <div class="clip cap" data-start="46.40" data-duration="3.00"><span>FOLLOW FOR MORE<br><i>CRICKET SECRETS!</i></span></div>
    </div>

    <script>
__GSAP_CODE__
    </script>

    <script>
      // ==========================================================
      // DETERMINISTIC HELPERS & PALETTE
      // ==========================================================
      let seed = 42;
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
        green: "#174D3A",
        dgreen: "#143D30",
        gold: "#E3B23C",
        red: "#B3261E",
        stamp: "#C1121F",
        sky: "#9DB7C4",
        ausGreen: "#00553B",
        indiaBlue: "#003366",
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
          const col = colors ? colors[i % colors.length] : (i % 2 ? C.gold : C.stamp);
          s += `<polygon class="${cls}" points="${cx},${cy} ${(cx + w).toFixed(0)},${(cy + rnd() * 26).toFixed(0)} ${(cx + w * 0.5).toFixed(0)},${(cy + w * 0.9).toFixed(0)}" fill="${col}" opacity="0"/>`;
        }
        return s;
      };

      const drop = (cls, x, y, s = 1) =>
        `<path class="${cls}" d="M${x} ${y - 34 * s} Q${x + 24 * s} ${y + 4 * s} ${x} ${y + 22 * s} Q${x - 24 * s} ${y + 4 * s} ${x} ${y - 34 * s}Z" fill="#9AD0EC" opacity="0"/>`;

      // ==========================================================
      // CHARACTER RIG FUNCTION (Matching Sandpaper Reference!)
      // ==========================================================
      function guy(id, x, y, s, o = {}) {
        const skin = o.skin || "#E9B990";
        const sk2 = o.sk2 || "#D69E73";
        const hair = o.hair || "#4A3222";
        const m = o.m || "flat";
        const cap = o.cap || C.ausGreen;
        const visor = o.visor || "#0D3024";
        const jersey = o.jersey || C.white;
        const badge = o.badge || C.gold;

        const mo = (n, h) => `<g class="m m-${n}" opacity="${n === m ? 1 : 0}">${h}</g>`;

        return `<g id="${id}"><g transform="translate(${x} ${y}) scale(${s})">
          <!-- Torso / Jersey -->
          <g class="cut">
            <path d="M-240 430 Q-245 250 -100 215 L100 215 Q245 250 240 430Z" fill="${jersey}"/>
            <path d="M-60 215 L0 300 L60 215 L38 198 L-38 198Z" fill="#DDD5C0"/>
            <rect x="-44" y="148" width="88" height="92" rx="18" fill="${sk2}"/>
            ${o.crest ? `<circle cx="0" cy="330" r="32" fill="${o.crest}"/><circle cx="0" cy="330" r="14" fill="${C.gold}"/>` : ""}
          </g>
          <!-- Head -->
          <g class="head cut">
            <!-- Ears -->
            <ellipse cx="-145" cy="15" rx="25" ry="38" fill="${sk2}"/><ellipse cx="145" cy="15" rx="25" ry="38" fill="${sk2}"/>
            <!-- Face -->
            <rect x="-142" y="-155" width="284" height="340" rx="130" fill="${skin}"/>
            ${o.beard ? `<path d="M-142 30 Q-148 185 0 185 Q148 185 142 30 Q115 145 0 148 Q-115 145 -142 30Z" fill="${hair}"/>` : ""}
            ${o.mustache ? `<path d="M-55 85 Q0 55 55 85 Q20 115 0 100 Q-20 115 -55 85Z" fill="${hair}"/>` : ""}
            <!-- Hair Sideburns -->
            <path d="M-148 -55 L-148 -90 L-118 -90 L-128 -15Z M148 -55 L148 -90 L118 -90 L128 -15Z" fill="${hair}"/>
            <!-- Cap -->
            <path d="M-156 -88 Q-158 -255 0 -255 Q158 -255 156 -88Z" fill="${cap}"/>
            <path d="M-174 -92 Q0 -128 174 -92 Q194 -58 0 -68 Q-194 -58 -174 -92Z" fill="${visor}"/>
            <circle cx="0" cy="-180" r="28" fill="${badge}"/>
            <!-- Eyes -->
            <g class="eye eyeL"><circle cx="-60" cy="5" r="35" fill="#fff"/><circle class="pupil pupilL" cx="-60" cy="5" r="16" fill="${C.ink}"/></g>
            <g class="eye eyeR"><circle cx="60" cy="5" r="35" fill="#fff"/><circle class="pupil pupilR" cx="60" cy="5" r="16" fill="${C.ink}"/></g>
            <!-- Eyebrows -->
            <rect class="browL" x="-100" y="-56" width="78" height="17" rx="6" fill="${hair}"/>
            <rect class="browR" x="22" y="-56" width="78" height="17" rx="6" fill="${hair}"/>
            <!-- Nose -->
            <path d="M-10 28 Q-4 70 20 60" stroke="${sk2}" stroke-width="9" fill="none" stroke-linecap="round"/>
            <!-- Mouth Variants -->
            ${mo("flat", '<rect x="-44" y="112" width="88" height="13" rx="6" fill="#7A2E22"/>')}
            ${mo("o", '<ellipse cx="0" cy="118" rx="28" ry="32" fill="#4A1410"/>')}
            ${mo("smirk", '<path d="M-48 116 Q14 150 62 98" stroke="#7A2E22" stroke-width="13" fill="none" stroke-linecap="round"/>')}
            ${mo("frown", '<path d="M-48 138 Q0 98 48 138" stroke="#7A2E22" stroke-width="13" fill="none" stroke-linecap="round"/>')}
            ${mo("teeth", '<rect x="-58" y="96" width="116" height="46" rx="14" fill="#fff" stroke="#7A2E22" stroke-width="9"/><path d="M-20 98V140M20 98V140M-56 119H56" stroke="#C9B9A8" stroke-width="4"/>')}
            ${mo("talk", '<ellipse cx="0" cy="120" rx="34" ry="20" fill="#4A1410"/>')}
          </g>
        </g></g>`;
      }

      // Hand with pointing finger or clutching
      function pointingHand(id, x, y, s = 1) {
        return `<g id="${id}" class="cut"><g transform="translate(${x} ${y}) scale(${s})">
          <rect x="-120" y="-40" width="160" height="80" rx="25" fill="#E9B990"/>
          <rect x="20" y="-35" width="140" height="45" rx="20" fill="#E9B990"/>
          <path d="M-60 -40V-10M-20 -40V-10M20 -40V-10" stroke="#D69E73" stroke-width="6"/>
        </g></g>`;
      }

      // Cricket Bat Raised
      function cricketBat(id, x, y, rot, s = 1) {
        return `<g id="${id}" class="cut" transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
          <!-- Handle -->
          <rect x="-14" y="-320" width="28" height="140" rx="8" fill="#F6F1E4" stroke="#D9BC82" stroke-width="4"/>
          <rect x="-10" y="-300" width="20" height="20" fill="#C1121F"/>
          <rect x="-10" y="-260" width="20" height="20" fill="#C1121F"/>
          <!-- Blade -->
          <path d="M-36 -180 L36 -180 L42 160 Q42 200 0 200 Q-42 200 -42 160 Z" fill="#E5C38E" stroke="#B89358" stroke-width="5"/>
          <rect x="-24" y="-140" width="48" height="120" fill="#C1121F" rx="4"/>
          ${tx(0, -70, 32, "MRF", "#FFF")}
        </g>`;
      }

      // ==========================================================
      // SCENE 1: HOOK & STEVE WAUGH'S SMUG DECISION
      // ==========================================================
      reseed(101);
      const s1_waugh = guy("gWaugh1", 540, 780, 0.95, {
        cap: C.ausGreen, visor: "#0D3024", badge: C.gold, mustache: 1, m: "smirk"
      });

      function ripBanner(id, x, y) {
        const w = 880, h = 180, m = x + w / 2;
        const zig = `${m - 30},${y - 20} ${m + 25},${y + 45} ${m - 20},${y + 90} ${m + 30},${y + 135} ${m - 15},${y + h + 20}`;
        const inner = `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${C.ausGreen}"/>
          <rect x="${x}" y="${y + 12}" width="${w}" height="8" fill="${C.gold}"/>
          <rect x="${x}" y="${y + h - 20}" width="${w}" height="8" fill="${C.gold}"/>
          ${tx(m, y + 80, 42, "GREATEST STREAK IN TEST HISTORY", C.paper)}
          ${tx(m, y + 140, 60, "AUSTRALIA: 16 WINS IN A ROW", C.gold)}`;
        return `<defs>
          <clipPath id="${id}cl"><polygon points="${x - 20},${y - 20} ${zig} ${x - 20},${y + h + 20}"/></clipPath>
          <clipPath id="${id}cr"><polygon points="${x + w + 20},${y - 20} ${zig} ${x + w + 20},${y + h + 20}"/></clipPath>
        </defs>
        <g id="${id}" class="cut">
          <g id="${id}L"><g clip-path="url(#${id}cl)">${inner}</g></g>
          <g id="${id}R"><g clip-path="url(#${id}cr)">${inner}</g></g>
        </g>`;
      }

      put("s1", svg(
        rays("r1", 540, 800, 20, "#1A4A3A") +
        s1_waugh +
        pointingHand("waughHand", 380, 920, 1.2) +
        `<g id="s1_quote" class="cut"><g transform="rotate(-6 310 440)">
          ${sheet(120, 390, 420, 100, C.paper, 8)}
          ${tx(330, 460, 56, '"BAT AGAIN!"', C.stamp)}
        </g></g>` +
        ripBanner("bn1", 100, 980) +
        scraps("scA", 540, 1060, 16) +
        `<g id="ts1" class="cut"><g transform="rotate(-5 540 260)">
          ${sheet(160, 210, 760, 110, C.stamp, 8)}
          ${tx(540, 288, 70, "THE FOLLOW-ON SECRET", C.paper)}
        </g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 2: THE RULE & THE FORK (OPTIONAL CHOICE)
      // ==========================================================
      reseed(202);
      const s2_stadium = `<rect width="1080" height="660" fill="${C.sky}"/>
        <rect y="580" width="1080" height="360" fill="#39424E"/>
        ${(() => {
          let crowd = "";
          const cols = [C.paper, C.gold, C.red, C.green, "#5FA8C9", "#FFF"];
          for (let r = 0; r < 5; r++)
            for (let c = 0; c < 20; c++)
              crowd += `<circle cx="${(c * 56 + (r % 2 ? 28 : 0) + rnd() * 8).toFixed(0)}" cy="${610 + r * 50}" r="18" fill="${cols[Math.floor(rnd() * cols.length)]}"/>`;
          return crowd;
        })()}
        <rect y="920" width="1080" height="1000" fill="${C.green}"/>
        <rect y="920" width="1080" height="26" fill="#0D3024"/>`;

      put("s2", svg(
        s2_stadium +
        `<g id="s2_ruleCard" class="cut">
          ${sheet(100, 200, 880, 280, C.paper, 10)}
          <rect x="130" y="225" width="820" height="230" fill="#202A36"/>
          ${tx(540, 290, 42, "MCC LAWS OF CRICKET", C.gold)}
          ${tx(540, 365, 76, "LAW 14: THE FOLLOW-ON", C.paper)}
          ${tx(540, 425, 42, "MANDATORY MINIMUM 200-RUN LEAD", "#9DB7C4")}
        </g>` +
        // Score Comparison Cards
        `<g id="s2_bars" class="cut">
          <g id="leadBarA">
            ${sheet(110, 520, 400, 340, C.paper, 8)}
            <rect x="130" y="540" width="360" height="110" fill="${C.ausGreen}"/>
            ${tx(310, 605, 44, "TEAM 1 (BAT 1ST)", C.gold)}
            ${tx(310, 640, 28, "AUSTRALIA", C.paper)}
            ${tx(310, 755, 108, "445", C.ink)}
            ${tx(310, 820, 38, "RUNS SCORED", C.green)}
          </g>
          <g id="leadBarB">
            ${sheet(570, 520, 400, 340, C.paper, 8)}
            <rect x="590" y="540" width="360" height="110" fill="${C.indiaBlue}"/>
            ${tx(770, 605, 44, "TEAM 2 (BAT 2ND)", C.gold)}
            ${tx(770, 640, 28, "INDIA", C.paper)}
            ${tx(770, 755, 108, "171", C.ink)}
            ${tx(770, 820, 38, "RUNS SCORED", C.red)}
          </g>
        </g>` +
        // Difference Stamp: 274 RUNS!
        `<g id="s2_diff" class="cut"><g transform="rotate(-10 540 880)">
          ${sheet(300, 820, 480, 120, C.stamp, 8)}
          ${tx(540, 898, 68, "LEAD: 274 RUNS!", C.paper)}
        </g></g>` +
        // Choice Fork Card
        `<g id="s2_choiceCard" class="cut">
          ${sheet(120, 960, 840, 240, C.gold, 10)}
          <rect x="140" y="980" width="800" height="200" fill="${C.ink}"/>
          ${tx(540, 1045, 52, "CAPTAIN'S CHOICE", C.gold)}
          ${tx(540, 1125, 68, "THEY DON'T HAVE TO ENFORCE!", C.paper)}
        </g>` +
        // Stamp: "OPTIONAL!"
        `<g id="s2_stampOpt" class="cut"><g transform="rotate(12 540 1140)">
          ${sheet(340, 1080, 400, 110, C.stamp, 8)}
          ${tx(540, 1155, 66, "IT'S A GAMBLE!", C.paper)}
        </g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 3: THE GAMBLE & THE EXHAUSTED BOWLER
      // ==========================================================
      reseed(303);
      // Sweating tired bowler figure
      const s3_bowler = guy("gBowler", 540, 750, 0.95, {
        hair: "#D4A359", skin: "#F2C29B", sk2: "#DC9B6B",
        cap: C.ausGreen, visor: "#0D3024", badge: C.gold,
        m: "o"
      });

      // Sweat drops
      let s3_sweat = "";
      [ [380, 680], [700, 660], [720, 740], [360, 760], [540, 880] ].forEach(([x, y]) => {
        s3_sweat += drop("sw3", x, y, 1.2);
      });

      // Cracked Pitch Graphic
      const s3_pitch = `<g id="s3_cracks" class="cut">
        <polygon points="120,950 960,950 1020,1280 60,1280" fill="${C.pitch}"/>
        <!-- Cracks -->
        <path d="M300 950 L340 1050 L280 1150 L360 1280" stroke="#5A3A1A" stroke-width="12" fill="none" stroke-linejoin="round"/>
        <path d="M540 950 L500 1040 L580 1160 L520 1280" stroke="#5A3A1A" stroke-width="16" fill="none" stroke-linejoin="round"/>
        <path d="M780 950 L740 1080 L820 1200 L790 1280" stroke="#5A3A1A" stroke-width="10" fill="none" stroke-linejoin="round"/>
        ${tx(540, 1240, 52, "DAY 5: CRACKED, WORN-OUT PITCH", C.ink)}
      </g>`;

      put("s3", svg(
        `<rect width="1080" height="950" fill="#E88D67"/>` +
        `<circle cx="540" cy="400" r="280" fill="#FFC857" opacity="0.4"/>` +
        s3_bowler +
        s3_sweat +
        s3_pitch +
        // Only 4 wins card
        `<g id="s3_recordCard" class="cut"><g transform="rotate(-6 540 400)">
          ${sheet(160, 320, 760, 160, C.stamp, 10)}
          ${tx(540, 395, 66, "ONLY 4 WINS IN 147 YEARS!", C.paper)}
          ${tx(540, 450, 42, "AFTER FOLLOWING ON IN TEST HISTORY", C.gold)}
        </g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 4: EDEN GARDENS 2001 - LAXMAN & DRAVID MIRACLE
      // ==========================================================
      reseed(404);
      // Indian batting heroes
      const s4_laxman = guy("gLaxman", 340, 820, 0.85, {
        cap: C.indiaBlue, visor: "#051D3B", crest: C.gold, badge: C.gold,
        hair: "#222", skin: "#C48E66", sk2: "#A8724D", m: "smirk"
      });
      const s4_dravid = guy("gDravid", 740, 820, 0.85, {
        cap: C.indiaBlue, visor: "#051D3B", crest: C.gold, badge: C.gold,
        hair: "#1B1B1B", skin: "#D69E73", sk2: "#B37B50", m: "smirk"
      });

      // Shocked Steve Waugh in corner
      const s4_shockWaugh = guy("gWaughShock", 920, 500, 0.55, {
        cap: C.ausGreen, visor: "#0D3024", badge: C.gold, mustache: 1, m: "teeth"
      });

      put("s4", svg(
        `<circle id="s4_sun" cx="200" cy="420" r="130" fill="${C.gold}"/>` +
        s2_stadium +
        // Kolkata 2001 Title Banner
        `<g id="s4_banner" class="cut">
          ${sheet(100, 180, 880, 160, C.paper, 8)}
          <rect x="120" y="200" width="840" height="120" fill="${C.ink}"/>
          ${tx(540, 255, 42, "EDEN GARDENS · KOLKATA", C.gold)}
          ${tx(540, 305, 54, "THE GREATEST TEST MATCH EVER", C.paper)}
        </g>` +
        // Australia 16-win streak vs India 274 behind
        `<g id="s4_stats" class="cut">
          <g id="s4_streakTag" transform="rotate(-5 320 420)">
            ${sheet(100, 360, 440, 110, C.ausGreen, 6)}
            ${tx(320, 415, 38, "AUSTRALIA", C.gold)}
            ${tx(320, 455, 46, "16 WINS IN A ROW", C.paper)}
          </g>
          <g id="s4_behindTag" transform="rotate(5 760 420)">
            ${sheet(540, 360, 440, 110, C.stamp, 6)}
            ${tx(760, 415, 38, "INDIA WERE", C.paper)}
            ${tx(760, 455, 46, "274 RUNS BEHIND!", C.paper)}
          </g>
        </g>` +
        // Characters: Laxman & Dravid + Bats
        `<g id="s4_heroes">
          ${s4_laxman}
          ${cricketBat("batLaxman", 190, 820, -35, 0.8)}
          ${s4_dravid}
          ${cricketBat("batDravid", 890, 820, 35, 0.8)}
          <!-- Name tags -->
          <g class="cut" transform="translate(340, 1100)">
            ${sheet(-180, -45, 360, 95, C.paper, 6)}
            ${tx(0, -6, 44, "V.V.S. LAXMAN", C.ink)}
            ${tx(0, 36, 44, "281 RUNS", C.stamp)}
          </g>
          <g class="cut" transform="translate(740, 1100)">
            ${sheet(-180, -45, 360, 95, C.paper, 6)}
            ${tx(0, -6, 44, "RAHUL DRAVID", C.ink)}
            ${tx(0, 36, 44, "180 RUNS", C.stamp)}
          </g>
        </g>` +
        // Shocked Waugh in corner
        `<g id="s4_waughBox" class="cut">
          ${s4_shockWaugh}
          <g transform="rotate(10 920 640)">
            ${sheet(790, 610, 260, 70, C.stamp, 4)}
            ${tx(920, 655, 38, "STREAK ENDED!", C.paper)}
          </g>
        </g>` +
        // Confetti scraps
        scraps("scConfetti", 540, 800, 36, [C.gold, C.indiaBlue, C.stamp, C.paper, "#FFF"]) +
        // Victory Slam Card
        `<g id="s4_win" class="cut"><g transform="rotate(-8 540 600)">
          ${sheet(160, 520, 760, 180, C.gold, 12)}
          <rect x="180" y="540" width="720" height="140" fill="${C.indiaBlue}"/>
          ${tx(540, 615, 86, "INDIA WON BY 171 RUNS!", C.paper)}
          ${tx(540, 665, 40, "AFTER FOLLOWING ON!", C.gold)}
        </g></g>`,
        C.dgreen
      ));

      // ==========================================================
      // SCENE 5: WEAPON VS TRAP (CLIMAX & CTA)
      // ==========================================================
      reseed(505);
      function bearTrap(id, cx, cy) {
        return `<g id="${id}" class="cut">
          <!-- Base -->
          <rect x="${cx - 240}" y="${cy + 60}" width="480" height="40" rx="12" fill="#2B2B2B"/>
          <circle cx="${cx}" cy="${cy + 75}" r="35" fill="#C1121F"/>
          <!-- Left Jaw -->
          <g id="trapJawL" style="transform-origin: ${cx - 220}px ${cy + 70}px;">
            <path d="M${cx - 220} ${cy + 70} Q${cx - 240} ${cy - 160} ${cx} ${cy - 160} L${cx} ${cy - 120} Q${cx - 180} ${cy - 120} ${cx - 180} ${cy + 70} Z" fill="#4A4A4A"/>
            <!-- Teeth -->
            ${[-140, -100, -60, -20].map((dx) => `<polygon points="${cx + dx},${cy - 120} ${cx + dx + 18},${cy - 80} ${cx + dx + 36},${cy - 120}" fill="#F6F1E4"/>`).join("")}
          </g>
          <!-- Right Jaw -->
          <g id="trapJawR" style="transform-origin: ${cx + 220}px ${cy + 70}px;">
            <path d="M${cx + 220} ${cy + 70} Q${cx + 240} ${cy - 160} ${cx} ${cy - 160} L${cx} ${cy - 120} Q${cx + 180} ${cy - 120} ${cx + 180} ${cy + 70} Z" fill="#3B3B3B"/>
            <!-- Teeth -->
            ${[20, 60, 100, 140].map((dx) => `<polygon points="${cx + dx},${cy - 120} ${cx + dx - 18},${cy - 80} ${cx + dx - 36},${cy - 120}" fill="#F6F1E4"/>`).join("")}
          </g>
        </g>`;
      }

      put("s5", svg(
        rays("r5", 540, 800, 22, "#1A4A3A") +
        // Weapon Card
        `<g id="s5_weapon" class="cut"><g transform="rotate(-6 540 320)">
          ${sheet(160, 240, 760, 140, C.paper, 8)}
          ${tx(540, 310, 44, "THE FOLLOW-ON IS A...", C.ink)}
          ${tx(540, 365, 76, "DEADLY WEAPON", C.ausGreen)}
        </g></g>` +
        // Trap Graphic
        bearTrap("trap5", 540, 700) +
        // Trap Stamp
        `<g id="s5_trap" class="cut"><g transform="rotate(8 540 680)">
          ${sheet(220, 610, 640, 140, C.stamp, 8)}
          ${tx(540, 690, 84, "BUT IT'S A TRAP!", C.paper)}
        </g></g>` +
        // Final CTA
        `<g id="s5_cta" class="cut">
          ${sheet(120, 920, 840, 240, C.gold, 10)}
          <rect x="140" y="940" width="800" height="200" fill="${C.ink}"/>
          ${tx(540, 1005, 48, "ONLY TRUE CRICKET FANS KNOW", C.gold)}
          ${tx(540, 1075, 72, "FOLLOW FOR MORE SECRETS!", C.paper)}
          ${tx(540, 1120, 36, "SHARE THIS WITH A CRICKET FAN", C.gold)}
        </g>`,
        C.dgreen
      ));

      // ==========================================================
      // TIMELINE ORCHESTRATION (GSAP 3)
      // ==========================================================
      const tl = gsap.timeline({ paused: true });
      const CC = "50% 50%";

      // Register transform origins
      gsap.set("#r1,#r5", { svgOrigin: "540 800" });
      gsap.set("#waughHand", { svgOrigin: "380 920" });
      gsap.set("#s1_quote,#ts1,#s1_cost,#s2_diff,#s2_stampOpt,#s3_recordCard,#s4_win,#s4_waughBox,#s5_weapon,#s5_trap", { transformOrigin: CC });
      gsap.set("#batLaxman", { svgOrigin: "190 820" });
      gsap.set("#batDravid", { svgOrigin: "890 820" });
      gsap.set(".browL,.browR,.eye,.pupil", { transformOrigin: CC });

      // Core Animation Primitives
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

      const burst = (cls, t, sx, sy0, sy1) =>
        gsap.utils.toArray("." + cls).forEach((el) => {
          tl.fromTo(el, { x: 0, y: 0, rotation: 0, opacity: 1 }, {
            x: (rnd() - 0.5) * sx, y: sy0 + rnd() * (sy1 - sy0),
            rotation: (rnd() - 0.5) * 720, opacity: 0, duration: 0.75,
            ease: "power2.out", immediateRender: false
          }, t);
        });

      const sweat = (cls, t) =>
        gsap.utils.toArray("." + cls).forEach((el, i) =>
          tl.fromTo(el, { opacity: 0, y: -20 }, { opacity: 1, y: 0, duration: 0.1, immediateRender: false }, t + i * 0.06)
            .to(el, { y: 90, opacity: 0, duration: 0.5, ease: "power1.in" }, t + i * 0.06 + 0.2)
        );

      // ==========================================================
      // SCENE VISIBILITY CONTROLLER: STRICT TIME WINDOWS!
      // ==========================================================
      const sceneList = [
        { id: "#s1", start: 0.00, end: 7.60 },
        { id: "#s2", start: 7.60, end: 16.50 },
        { id: "#s3", start: 16.50, end: 26.60 },
        { id: "#s4", start: 26.60, end: 42.00 },
        { id: "#s5", start: 42.00, end: 49.48 }
      ];

      // Initially ensure only s1 is active at t=0
      tl.set("#s2,#s3,#s4,#s5", { display: "none", zIndex: 1 }, 0);
      tl.set("#s1", { display: "block", zIndex: 2 }, 0);

      sceneList.forEach((sc) => {
        tl.set(sc.id, { display: "block", zIndex: 3 }, sc.start);
        if (sc.end < 49.4) {
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

        // Pop in at exact start time
        tl.fromTo(
          capEl,
          { opacity: 0, scale: 0.6, rotation: i % 2 ? 4 : -4 },
          { opacity: 1, scale: 1, rotation: i % 2 ? -1.5 : 1.5, duration: 0.14, ease: "back.out(2.5)" },
          start
        );

        // Disappear cleanly right before next caption or at end!
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

      [[7.60, C.paper, 1], [16.50, C.stamp, -1], [26.60, C.gold, 1], [42.00, C.ink, -1]].forEach(([t, c, dir]) => {
        tl.set("#wp", { fill: c }, t - 0.19);
        tl.fromTo("#wipe", { x: dir > 0 ? -1700 : 1300 }, { x: dir > 0 ? 1300 : -1700, duration: 0.36, ease: "none" }, t - 0.18);
      });

      // ==========================================================
      // SCENE 1 TIMELINE (0.00s - 7.60s): HOOK & STREAK
      // ==========================================================
      tl.fromTo("#r1", { rotation: 0 }, { rotation: 36, duration: 7.6, ease: "none" }, 0);
      zoom("s1", 0, 7.6, 1, 1.08);

      // Waugh appears with smirk
      tl.fromTo("#gWaugh1", { y: 1000 }, { y: 0, duration: 0.45, ease: "back.out(1.4)" }, 0);
      face("gWaugh1", 0, { m: "smirk", b: [12, -12, 8] }, 0.01);
      face("gWaugh1", 1.2, { p: [14, 4] });
      face("gWaugh1", 2.2, { p: [-14, 4] });

      // Pointing hand animates forward
      tl.fromTo("#waughHand", { scale: 0, rotation: -20 }, { scale: 1.2, rotation: 0, duration: 0.3, ease: "back.out(1.8)" }, 0.2);
      pop("#s1_quote", 0.4, 0.25);
      shake("#s1 .cam", 0.45, 14);

      // Streak Banner Rips in Half at 4.14s!
      tl.fromTo("#bn1", { y: 800 }, { y: 0, duration: 0.35, ease: "back.out(1.4)" }, 3.9);
      tl.to("#bn1L", { x: -140, y: 50, rotation: -12, duration: 0.45, ease: "power3.out" }, 4.3);
      tl.to("#bn1R", { x: 140, y: 70, rotation: 10, duration: 0.45, ease: "power3.out" }, 4.3);
      burst("scA", 4.3, 900, -450, 350);
      shake("#s1 .cam", 4.32, 28);

      // Cost badge slams down
      slam("#ts1", 0.1, -6);
      face("gWaugh1", 4.4, { m: "o", b: [-14, 14, -18], e: 1.25, p: [0, 8] });

      // ==========================================================
      // SCENE 2 TIMELINE (7.60s - 16.50s): THE RULE & THE CHOICE
      // ==========================================================
      zoom("s2", 7.6, 8.9, 1, 1.07);

      // Rule Card drops
      tl.fromTo("#s2_ruleCard", { y: -500 }, { y: 0, duration: 0.3, ease: "back.out(1.3)" }, 7.65);
      shake("#s2 .cam", 7.95, 16);

      // Lead bars pop up
      tl.fromTo("#leadBarA", { y: 800 }, { y: 0, duration: 0.32, ease: "back.out(1.4)" }, 8.70);
      tl.fromTo("#leadBarB", { y: 800 }, { y: 0, duration: 0.32, ease: "back.out(1.4)" }, 9.00);

      // 274-run diff stamp slams
      slam("#s2_diff", 10.5, -12);
      shake("#s2 .cam", 10.66, 24);

      // Choice Card pops at "THEIR CHOICE"
      pop("#s2_choiceCard", 14.25, 0.28);
      shake("#s2 .cam", 14.50, 18);

      slam("#s2_stampOpt", 15.10, 14);
      shake("#s2 .cam", 15.26, 26);

      // ==========================================================
      // SCENE 3 TIMELINE (16.50s - 26.60s): TIRED BOWLER & GAMBLE
      // ==========================================================
      zoom("s3", 16.5, 10.1, 1, 1.06);

      // Bowler slides in, visibly exhausted
      tl.fromTo("#gBowler", { y: 900 }, { y: 0, duration: 0.4, ease: "back.out(1.3)" }, 16.6);
      face("gBowler", 16.6, { m: "o", b: [-16, 16, -20], e: 1.25 }, 0.01);

      // Bowler panting up and down (chest heaving)
      tl.to("#gBowler", { y: 25, duration: 0.35, ease: "sine.inOut", repeat: 16, yoyo: true }, 17.0);

      // Sweat drops flying
      sweat("sw3", 18.2);
      sweat("sw3", 19.8);
      sweat("sw3", 21.4);

      // Cracked pitch slides in
      tl.fromTo("#s3_cracks", { y: 400, opacity: 0 }, { y: 0, opacity: 1, duration: 0.3, ease: "power3.out" }, 19.75);
      shake("#s3 .cam", 20.05, 18);

      // Only 4 wins record card slams down
      slam("#s3_recordCard", 22.65, -8);
      shake("#s3 .cam", 22.81, 28);
      face("gBowler", 22.9, { m: "teeth", b: [-18, 18, -24], p: [0, 10] });

      // ==========================================================
      // SCENE 4 TIMELINE (26.60s - 42.00s): KOLKATA 2001 MIRACLE
      // ==========================================================
      zoom("s4", 26.6, 15.4, 1, 1.07);

      // Title banner
      slam("#s4_banner", 26.70, -4);
      shake("#s4 .cam", 26.86, 20);

      // 16 Streak vs 274 Behind
      pop("#s4_streakTag", 28.70, 0.25);
      pop("#s4_behindTag", 31.70, 0.25);
      shake("#s4 .cam", 31.95, 22);

      // Sun time-lapse moving across Eden Gardens sky
      tl.fromTo("#s4_sun", { cx: 200, cy: 420 }, { cx: 880, cy: 420, duration: 5.5, ease: "sine.inOut" }, 34.8);

      // Laxman & Dravid pop up heroically
      tl.fromTo("#gLaxman", { y: 900 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, 37.25);
      tl.fromTo("#gDravid", { y: 900 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, 37.55);
      tl.fromTo("#batLaxman", { scale: 0, rotation: -90 }, { scale: 0.8, rotation: -35, duration: 0.35, ease: "back.out(1.6)" }, 37.4);
      tl.fromTo("#batDravid", { scale: 0, rotation: 90 }, { scale: 0.8, rotation: 35, duration: 0.35, ease: "back.out(1.6)" }, 37.7);

      face("gLaxman", 37.3, { m: "smirk", b: [10, -10, 6] }, 0.01);
      face("gDravid", 37.6, { m: "smirk", b: [10, -10, 6] }, 0.01);
      shake("#s4 .cam", 37.95, 20);

      // Shocked Waugh
      tl.fromTo("#s4_waughBox", { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2)" }, 38.8);
      face("gWaughShock", 38.8, { m: "teeth", b: [-18, 18, -26], p: [-12, 12] }, 0.01);

      // Victory Card + Confetti Slam!
      slam("#s4_win", 40.75, -8);
      shake("#s4 .cam", 40.91, 34);
      burst("scConfetti", 40.91, 1100, -600, 450);

      // ==========================================================
      // SCENE 5 TIMELINE (42.00s - 49.48s): WEAPON VS TRAP & CTA
      // ==========================================================
      tl.fromTo("#r5", { rotation: 0 }, { rotation: 28, duration: 7.48, ease: "none" }, 42.0);
      zoom("s5", 42.0, 7.48, 1, 1.06);

      // Weapon card slides in
      tl.fromTo("#s5_weapon", { x: -700, opacity: 0 }, { x: 0, opacity: 1, duration: 0.32, ease: "back.out(1.4)" }, 42.20);
      shake("#s5 .cam", 42.45, 18);

      // Bear trap snaps shut aggressively!
      tl.fromTo("#trap5", { scale: 0.5, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.25, ease: "back.out(1.4)" }, 43.80);
      tl.fromTo("#trapJawL", { rotation: 0 }, { rotation: 38, duration: 0.07, ease: "power4.in" }, 44.18);
      tl.fromTo("#trapJawR", { rotation: 0 }, { rotation: -38, duration: 0.07, ease: "power4.in" }, 44.18);
      shake("#s5 .cam", 44.25, 30);

      // Trap stamp slams
      slam("#s5_trap", 44.30, 8);
      shake("#s5 .cam", 44.46, 28);

      // Final CTA pop
      pop("#s5_cta", 46.40, 0.26);
      shake("#s5 .cam", 46.68, 18);

      // Register for headless render
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
