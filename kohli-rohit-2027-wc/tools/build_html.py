import json
import base64
from pathlib import Path

base_dir = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-rohit-2027-wc")
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
        background: #0B2238; font-family: "Anton", sans-serif;
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
        background: radial-gradient(ellipse at 50% 45%, rgba(0, 0, 0, 0) 55%, rgba(0, 0, 0, 0.35) 100%);
      }
      /* STRICT CAPTION SYSTEM: Exactly one caption at a time, zero overlapping! */
      .cap {
        position: absolute; left: 50px; width: 980px; top: 1260px; height: 250px;
        z-index: 10; text-align: center; pointer-events: none;
        opacity: 0;
      }
      .cap span {
        display: inline-block; max-width: 960px; padding: 16px 36px 22px;
        background: #F6F1E4; color: #1B1B1B;
        font-size: 80px; line-height: 1.08; letter-spacing: 1px; text-transform: uppercase;
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.4));
      }
      .cap b { font-weight: 400; color: #C1121F; }
      .cap i { font-style: normal; background: #E3B23C; padding: 0 12px; }
      .cap mark { font-weight: 400; background: #003366; color: #F6F1E4; padding: 0 10px; }
    </style>
  </head>
  <body>
    <div id="root" data-start="0" data-duration="48.59" data-width="1080" data-height="1920">
      <!-- 5 SCENES -->
      <div id="s1" class="clip scene" data-start="0" data-duration="8.60"><div class="cam"></div></div>
      <div id="s2" class="clip scene" data-start="8.60" data-duration="9.90"><div class="cam"></div></div>
      <div id="s3" class="clip scene" data-start="18.50" data-duration="7.70"><div class="cam"></div></div>
      <div id="s4" class="clip scene" data-start="26.20" data-duration="10.70"><div class="cam"></div></div>
      <div id="s5" class="clip scene" data-start="36.90" data-duration="11.69"><div class="cam"></div></div>

      <audio id="vo" src="renders/full_audio_mix.wav" data-start="0" data-duration="48.588"></audio>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- EXACT 19 SYNCED CAPTIONS (NO OVERLAP!) -->
      <div class="clip cap" data-start="0.04" data-duration="3.86"><span>WILL KOHLI & ROHIT PLAY<br>THE <b>2027 WORLD CUP?</b></span></div>
      <div class="clip cap" data-start="4.25" data-duration="2.20"><span>NOBODY'S ASKING<br>THE <i>REAL QUESTION.</i></span></div>
      <div class="clip cap" data-start="6.75" data-duration="1.80"><span>WHAT IF <b>INDIA</b><br>DOESN'T NEED THEM?</span></div>
      <div class="clip cap" data-start="8.85" data-duration="4.60"><span>KOHLI IS <b>38.</b><br>ROHIT WILL BE <i>40!</i></span></div>
      <div class="clip cap" data-start="13.75" data-duration="2.00"><span>BOTH ONLY<br><b>PLAY ODIS NOW.</b></span></div>
      <div class="clip cap" data-start="15.85" data-duration="2.60"><span>AND <i>NOBODY</i> PROMISED<br>EITHER A SPOT!</span></div>
      <div class="clip cap" data-start="18.65" data-duration="1.90"><span>ROHIT IS THE ONE<br><b>UNDER PRESSURE.</b></span></div>
      <div class="clip cap" data-start="20.75" data-duration="2.45"><span>SELECTORS WANTED TO<br><b>MOVE ON.</b></span></div>
      <div class="clip cap" data-start="23.50" data-duration="2.65"><span>THEN HE SMASHED<br>A <i>CENTURY</i> VS WI!</span></div>
      <div class="clip cap" data-start="26.40" data-duration="0.75"><span>AND <b>KOHLI?</b></span></div>
      <div class="clip cap" data-start="27.25" data-duration="4.00"><span><b>139 NOT OUT</b><br>IN A MASTER CHASE!</span></div>
      <div class="clip cap" data-start="31.35" data-duration="2.45"><span>PLUS <b>74 OFF 51</b><br>IN AUCKLAND!</span></div>
      <div class="clip cap" data-start="34.05" data-duration="1.45"><span>RUNS AREN'T<br>THE PROBLEM.</span></div>
      <div class="clip cap" data-start="35.70" data-duration="1.00"><span><b>TIME IS.</b></span></div>
      <div class="clip cap" data-start="37.05" data-duration="4.10"><span>BCCI: <b>PERFORMANCE,</b><br>NOT AGE, SHOULD DECIDE.</span></div>
      <div class="clip cap" data-start="41.45" data-duration="2.00"><span>SRI LANKA:<br><b>DECEMBER 13TH.</b></span></div>
      <div class="clip cap" data-start="43.75" data-duration="2.25"><span>THE NEXT 6 ODIS<br>ARE THE <i>AUDITION!</i></span></div>
      <div class="clip cap" data-start="46.15" data-duration="1.00"><span>SHOULD INDIA<br><b>PICK THEM?</b></span></div>
      <div class="clip cap" data-start="47.25" data-duration="1.33"><span>COMMENT<br><b>YES OR NO!</b></span></div>
    </div>

    <script>
__GSAP_CODE__
    </script>

    <script>
      // ==========================================================
      // PALETTE & HELPERS
      // ==========================================================
      let seed = 99;
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
        indiaBlue: "#003366",
        navy: "#0A1F36",
        saffron: "#FF9933",
        gold: "#E3B23C",
        stamp: "#C1121F",
        sky: "#9DB7C4",
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
          const col = colors ? colors[i % colors.length] : (i % 2 ? C.gold : C.saffron);
          s += `<polygon class="${cls}" points="${cx},${cy} ${(cx + w).toFixed(0)},${(cy + rnd() * 26).toFixed(0)} ${(cx + w * 0.5).toFixed(0)},${(cy + w * 0.9).toFixed(0)}" fill="${col}" opacity="0"/>`;
        }
        return s;
      };

      // ==========================================================
      // CRICKETER RIG FUNCTION (Kohli, Rohit, Selectors)
      // ==========================================================
      function guy(id, x, y, s, o = {}) {
        const skin = o.skin || "#E9B990";
        const sk2 = o.sk2 || "#D69E73";
        const hair = o.hair || "#222222";
        const m = o.m || "flat";
        const cap = o.cap || C.indiaBlue;
        const visor = o.visor || "#051A33";
        const jersey = o.jersey || C.indiaBlue;
        const badge = o.badge || C.gold;

        const mo = (n, h) => `<g class="m m-${n}" opacity="${n === m ? 1 : 0}">${h}</g>`;

        return `<g id="${id}"><g transform="translate(${x} ${y}) scale(${s})">
          <!-- Torso -->
          <g class="cut">
            <path d="M-240 430 Q-245 250 -100 215 L100 215 Q245 250 240 430Z" fill="${jersey}"/>
            <!-- Collar Tricolor -->
            <path d="M-60 215 L0 300 L60 215 L38 198 L-38 198Z" fill="${C.saffron}"/>
            <rect x="-44" y="148" width="88" height="92" rx="18" fill="${sk2}"/>
            <!-- BCCI Crest -->
            <circle cx="0" cy="330" r="32" fill="${C.indiaBlue}"/><circle cx="0" cy="330" r="14" fill="${C.gold}"/>
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
          <rect x="-24" y="-140" width="48" height="120" fill="${C.indiaBlue}" rx="4"/>
          ${tx(0, -70, 32, "CEAT", "#FFF")}
        </g>`;
      }

      function worldCupTrophy(id, cx, cy, s = 1) {
        return `<g id="${id}" class="cut" transform="translate(${cx} ${cy}) scale(${s})">
          <!-- Globe -->
          <circle cx="0" cy="-140" r="70" fill="${C.gold}"/>
          <circle cx="0" cy="-140" r="55" fill="#F3CA65"/>
          <!-- Columns -->
          <path d="M-45 -70 Q-60 40 -25 120 L25 120 Q60 40 45 -70 Z" fill="${C.gold}"/>
          <path d="M-15 -70 L-15 120 L15 120 L15 -70 Z" fill="#C89B3C"/>
          <!-- Base -->
          <rect x="-70" y="120" width="140" height="40" rx="10" fill="#2B2B2B"/>
          ${tx(0, 148, 22, "ICC 2027", C.paper)}
        </g>`;
      }

      // ==========================================================
      // SCENE 1: THE REAL QUESTION (0.00s - 8.60s)
      // ==========================================================
      reseed(101);
      const s1_kohli = guy("gS1_Kohli", 280, 780, 0.78, {
        skin: "#C48E66", sk2: "#A8724D", hair: "#1B1B1B", beard: 1, m: "smirk"
      });
      const s1_rohit = guy("gS1_Rohit", 800, 780, 0.78, {
        skin: "#E0AC82", sk2: "#C59368", hair: "#262626", beard: 1, mustache: 1, m: "flat"
      });

      put("s1", svg(
        rays("r1", 540, 750, 24, "#0E2A47") +
        worldCupTrophy("s1_trophy", 540, 720, 1.1) +
        `<g id="s1_heroes">${s1_kohli}${s1_rohit}</g>` +
        // Hook Question Banner
        `<g id="s1_banner" class="cut">
          ${sheet(80, 180, 920, 160, C.paper, 8)}
          <rect x="100" y="200" width="880" height="120" fill="${C.indiaBlue}"/>
          ${tx(540, 255, 42, "THE 2027 WORLD CUP DILEMMA", C.gold)}
          ${tx(540, 305, 54, "WILL KOHLI & ROHIT PLAY?", C.paper)}
        </g>` +
        // The Real Question Stamp
        `<g id="s1_realQuestion" class="cut"><g transform="rotate(-6 540 980)">
          ${sheet(140, 910, 800, 150, C.stamp, 10)}
          ${tx(540, 980, 72, "WHAT IF INDIA DOESN'T", C.paper)}
          ${tx(540, 1035, 60, "NEED THEM AT ALL?", C.gold)}
        </g></g>`,
        C.navy
      ));

      // ==========================================================
      // SCENE 2: THE AGE CLOCK (8.60s - 18.50s)
      // ==========================================================
      reseed(202);
      put("s2", svg(
        rays("r2", 540, 750, 20, "#102C4D") +
        // Title
        `<g id="s2_title" class="cut">
          ${sheet(120, 180, 840, 140, C.paper, 8)}
          <rect x="140" y="200" width="800" height="100" fill="${C.indiaBlue}"/>
          ${tx(540, 265, 52, "THE TICKING CLOCK", C.gold)}
        </g>` +
        // Two Player Age Cards
        `<g id="s2_cards" class="cut">
          <!-- Kohli Card -->
          <g id="s2_cardK">
            ${sheet(90, 360, 420, 480, C.paper, 8)}
            <rect x="110" y="380" width="380" height="110" fill="${C.indiaBlue}"/>
            ${tx(300, 440, 48, "VIRAT KOHLI", C.paper)}
            ${tx(300, 475, 30, "LEGENDARY BATTER", C.gold)}
            ${tx(300, 600, 120, "38", C.stamp)}
            ${tx(300, 670, 36, "YEARS OLD", C.ink)}
            ${tx(300, 750, 42, "WILL BE 39 IN 2027", C.indiaBlue)}
          </g>
          <!-- Rohit Card -->
          <g id="s2_cardR">
            ${sheet(570, 360, 420, 480, C.paper, 8)}
            <rect x="590" y="380" width="380" height="110" fill="${C.indiaBlue}"/>
            ${tx(780, 440, 48, "ROHIT SHARMA", C.paper)}
            ${tx(780, 475, 30, "INDIAN CAPTAIN", C.gold)}
            ${tx(780, 600, 120, "39", C.stamp)}
            ${tx(780, 670, 36, "YEARS OLD", C.ink)}
            ${tx(780, 750, 42, "WILL BE 40 AT WC!", C.stamp)}
          </g>
        </g>` +
        // Format restriction: ODIS ONLY
        `<g id="s2_format" class="cut"><g transform="rotate(-4 540 920)">
          ${sheet(200, 860, 680, 110, C.gold, 6)}
          ${tx(540, 935, 56, "ONLY PLAY ODIS NOW", C.ink)}
        </g></g>` +
        // Stamp: NO PROMISED SPOT!
        `<g id="s2_stampNoSpot" class="cut"><g transform="rotate(8 540 1080)">
          ${sheet(160, 1010, 760, 150, C.stamp, 10)}
          ${tx(540, 1085, 78, "NO PROMISED SPOT!", C.paper)}
          ${tx(540, 1135, 38, "SELECTORS HAVEN'T GUARANTEED IT", C.gold)}
        </g></g>`,
        C.navy
      ));

      // ==========================================================
      // SCENE 3: ROHIT UNDER PRESSURE & THE CENTURY (18.50 - 26.20s)
      // ==========================================================
      reseed(303);
      const s3_rohit = guy("gS3_Rohit", 540, 780, 0.88, {
        skin: "#E0AC82", sk2: "#C59368", hair: "#262626", beard: 1, mustache: 1, m: "roar"
      });

      put("s3", svg(
        rays("r3", 540, 750, 20, "#102C4D") +
        // Newspaper Headlines
        `<g id="s3_news" class="cut">
          <g transform="rotate(-6 320 340)">
            ${sheet(80, 270, 480, 130, C.paper, 6)}
            ${tx(320, 335, 38, "REPORT: SELECTORS", C.stamp)}
            ${tx(320, 375, 42, "WANTED TO MOVE ON!", C.ink)}
          </g>
          <g transform="rotate(7 740 340)">
            ${sheet(520, 270, 480, 130, C.paper, 6)}
            ${tx(760, 335, 38, "ROHIT UNDER PRESSURE", C.stamp)}
            ${tx(760, 375, 42, "CAPTAINCY IN QUESTION?", C.ink)}
          </g>
        </g>` +
        // Hero Rohit & Bat
        `<g id="s3_hero">${s3_rohit}${cricketBat("batRohit", 360, 760, -45, 0.9)}</g>` +
        // Century Slam Banner
        `<g id="s3_century" class="cut"><g transform="rotate(-5 540 1020)">
          ${sheet(140, 950, 800, 160, C.gold, 10)}
          <rect x="160" y="970" width="760" height="120" fill="${C.indiaBlue}"/>
          ${tx(540, 1035, 78, "100! CENTURY VS WI!", C.paper)}
          ${tx(540, 1075, 36, "SILENCED THE CRITICS IN STYLE", C.gold)}
        </g></g>`,
        C.navy
      ));

      // ==========================================================
      // SCENE 4: KOHLI THE CHASE MASTER (26.20 - 36.90s)
      // ==========================================================
      reseed(404);
      const s4_kohli = guy("gS4_Kohli", 540, 780, 0.88, {
        skin: "#C48E66", sk2: "#A8724D", hair: "#1B1B1B", beard: 1, m: "roar"
      });

      put("s4", svg(
        rays("r4", 540, 750, 22, "#102C4D") +
        // Title: Kohli Masterclass
        `<g id="s4_scores" class="cut">
          <!-- 139* Card -->
          <g transform="rotate(-6 320 320)">
            ${sheet(80, 250, 480, 150, C.gold, 8)}
            <rect x="100" y="270" width="440" height="110" fill="${C.indiaBlue}"/>
            ${tx(320, 325, 54, "139* NOT OUT!", C.paper)}
            ${tx(320, 365, 32, "CHASING VS WEST INDIES", C.gold)}
          </g>
          <!-- 74 Auckland Card -->
          <g transform="rotate(7 760 320)">
            ${sheet(520, 250, 480, 150, C.paper, 8)}
            <rect x="540" y="270" width="440" height="110" fill="${C.indiaBlue}"/>
            ${tx(760, 325, 54, "74 OFF 51!", C.paper)}
            ${tx(760, 365, 32, "DESTRUCTION IN AUCKLAND", C.gold)}
          </g>
        </g>` +
        // Hero Kohli
        `<g id="s4_hero">${s4_kohli}${cricketBat("batKohliS4", 720, 760, 45, 0.9)}</g>` +
        // Clock / Time is the Enemy Stamp
        `<g id="s4_timeStamp" class="cut"><g transform="rotate(-6 540 1020)">
          ${sheet(140, 950, 800, 160, C.stamp, 10)}
          ${tx(540, 1020, 68, "RUNS AREN'T THE PROBLEM...", C.paper)}
          ${tx(540, 1080, 86, "TIME IS!", C.gold)}
        </g></g>`,
        C.navy
      ));

      // ==========================================================
      // SCENE 5: BCCI AUDITION & CTA (36.90 - 48.59s)
      // ==========================================================
      reseed(505);
      put("s5", svg(
        rays("r5", 540, 780, 24, "#102C4D") +
        // BCCI Mandate Card
        `<g id="s5_bcci" class="cut"><g transform="rotate(-4 540 300)">
          ${sheet(120, 220, 840, 160, C.paper, 8)}
          <rect x="140" y="240" width="800" height="120" fill="${C.indiaBlue}"/>
          ${tx(540, 295, 42, "BCCI PRESIDENT DECREE", C.gold)}
          ${tx(540, 345, 56, "PERFORMANCE, NOT AGE, DECIDES!", C.paper)}
        </g></g>` +
        // Audition Banner
        `<g id="s5_audition" class="cut"><g transform="rotate(5 540 500)">
          ${sheet(160, 430, 760, 150, C.gold, 8)}
          <rect x="180" y="450" width="720" height="110" fill="${C.ink}"/>
          ${tx(540, 505, 44, "SRI LANKA · DEC 13", C.gold)}
          ${tx(540, 545, 48, "THE NEXT 6 ODIS ARE THE AUDITION!", C.paper)}
        </g></g>` +
        // Viral Interactive CTA Card
        `<g id="s5_cta" class="cut">
          ${sheet(100, 840, 880, 300, C.paper, 10)}
          <rect x="120" y="860" width="840" height="260" fill="${C.indiaBlue}"/>
          ${tx(540, 925, 52, "SHOULD INDIA PICK THEM?", C.gold)}
          <!-- Voting Buttons -->
          <rect x="220" y="970" width="280" height="110" rx="16" fill="#146C43" class="cut"/>
          ${tx(360, 1045, 66, "YES!", C.paper)}
          <rect x="580" y="970" width="280" height="110" rx="16" fill="${C.stamp}" class="cut"/>
          ${tx(720, 1045, 66, "NO!", C.paper)}
          ${tx(540, 1145, 34, "COMMENT YOUR VOTE BELOW", C.gold)}
        </g>`,
        C.navy
      ));

      // ==========================================================
      // TIMELINE ORCHESTRATION (GSAP 3)
      // ==========================================================
      const tl = gsap.timeline({ paused: true });
      const CC = "50% 50%";

      // Origins
      gsap.set("#r1,#r2,#r3,#r4,#r5", { svgOrigin: "540 800" });
      gsap.set("#s1_trophy,#s1_realQuestion,#s2_stampNoSpot,#s2_format,#s3_century,#s4_timeStamp,#s5_bcci,#s5_audition,#s5_cta", { transformOrigin: CC });
      gsap.set("#batRohit,#batKohS4", { transformOrigin: "bottom center" });
      gsap.set(".browL,.browR,.eye,.pupil", { transformOrigin: CC });

      // Animation Primitives
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

      // ==========================================================
      // SCENE VISIBILITY CONTROLLER: STRICT TIME WINDOWS!
      // ==========================================================
      const sceneList = [
        { id: "#s1", start: 0.00, end: 8.60 },
        { id: "#s2", start: 8.60, end: 18.50 },
        { id: "#s3", start: 18.50, end: 26.20 },
        { id: "#s4", start: 26.20, end: 36.90 },
        { id: "#s5", start: 36.90, end: 48.59 }
      ];

      tl.set("#s2,#s3,#s4,#s5", { display: "none", zIndex: 1 }, 0);
      tl.set("#s1", { display: "block", zIndex: 2 }, 0);

      sceneList.forEach((sc) => {
        tl.set(sc.id, { display: "block", zIndex: 3 }, sc.start);
        if (sc.end < 48.5) {
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

      [[8.60, C.paper, 1], [18.50, C.saffron, -1], [26.20, C.indiaBlue, 1], [36.90, C.gold, -1]].forEach(([t, c, dir]) => {
        tl.set("#wp", { fill: c }, t - 0.19);
        tl.fromTo("#wipe", { x: dir > 0 ? -1700 : 1300 }, { x: dir > 0 ? 1300 : -1700, duration: 0.36, ease: "none" }, t - 0.18);
      });

      // ==========================================================
      // SCENE 1 TIMELINE (0.00s - 8.60s): THE HOOK
      // ==========================================================
      tl.fromTo("#r1", { rotation: 0 }, { rotation: 25, duration: 8.6, ease: "none" }, 0);
      zoom("s1", 0, 8.6, 1, 1.08);

      // Trophy drops
      pop("#s1_trophy", 0.1, 0.4);

      // Heroes enter
      tl.fromTo("#gS1_Kohli", { x: -600 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, 0.2);
      tl.fromTo("#gS1_Rohit", { x: 600 }, { x: 0, duration: 0.4, ease: "back.out(1.4)" }, 0.3);

      // Title banner
      tl.fromTo("#s1_banner", { y: -400 }, { y: 0, duration: 0.35, ease: "back.out(1.3)" }, 0.15);
      shake("#s1 .cam", 0.45, 14);

      // Real question stamp slams
      slam("#s1_realQuestion", 6.75, -6);
      shake("#s1 .cam", 6.91, 30);

      // ==========================================================
      // SCENE 2 TIMELINE (8.60s - 18.50s): THE AGE CLOCK
      // ==========================================================
      zoom("s2", 8.6, 9.9, 1, 1.07);

      tl.fromTo("#s2_title", { y: -400 }, { y: 0, duration: 0.3, ease: "back.out(1.3)" }, 8.70);
      shake("#s2 .cam", 8.95, 16);

      // Cards drop in
      tl.fromTo("#s2_cardK", { y: 800 }, { y: 0, duration: 0.35, ease: "back.out(1.4)" }, 8.85);
      tl.fromTo("#s2_cardR", { y: 800 }, { y: 0, duration: 0.35, ease: "back.out(1.4)" }, 9.15);

      // ODIs only pop
      pop("#s2_format", 13.75, 0.25);
      shake("#s2 .cam", 14.00, 18);

      // No spot stamp slam
      slam("#s2_stampNoSpot", 15.85, 8);
      shake("#s2 .cam", 16.01, 30);

      // ==========================================================
      // SCENE 3 TIMELINE (18.50s - 26.20s): ROHIT CENTURY
      // ==========================================================
      zoom("s3", 18.5, 7.7, 1, 1.06);

      // News pops
      pop("#s3_news", 18.65, 0.3);
      shake("#s3 .cam", 18.90, 18);

      // Rohit slides up
      tl.fromTo("#gS3_Rohit", { y: 800 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, 20.70);
      tl.fromTo("#batRohit", { rotation: -90, scale: 0 }, { rotation: -45, scale: 0.9, duration: 0.35, ease: "back.out(2)" }, 21.0);

      // Century Slam
      slam("#s3_century", 23.50, -5);
      shake("#s3 .cam", 23.66, 32);

      // ==========================================================
      // SCENE 4 TIMELINE (26.20s - 36.90s): KOHLI CHASE MASTER
      // ==========================================================
      zoom("s4", 26.2, 10.7, 1, 1.07);

      // Scores pop
      pop("#s4_scores", 27.25, 0.3);
      shake("#s4 .cam", 27.50, 18);

      // Kohli slides up
      tl.fromTo("#gS4_Kohli", { y: 800 }, { y: 0, duration: 0.4, ease: "back.out(1.4)" }, 27.50);
      tl.fromTo("#batKohliS4", { rotation: 90, scale: 0 }, { rotation: 45, scale: 0.9, duration: 0.35, ease: "back.out(2)" }, 27.80);

      // Time stamp slam
      slam("#s4_timeStamp", 35.70, -6);
      shake("#s4 .cam", 35.86, 32);

      // ==========================================================
      // SCENE 5 TIMELINE (36.90s - 48.59s): AUDITION & CTA
      // ==========================================================
      tl.fromTo("#r5", { rotation: 0 }, { rotation: 30, duration: 11.69, ease: "none" }, 36.90);
      zoom("s5", 36.9, 11.69, 1, 1.06);

      // BCCI Card drops
      tl.fromTo("#s5_bcci", { y: -500 }, { y: 0, duration: 0.32, ease: "back.out(1.4)" }, 37.05);
      shake("#s5 .cam", 37.30, 18);

      // Audition banner slams
      slam("#s5_audition", 41.45, 5);
      shake("#s5 .cam", 41.61, 24);

      // Final CTA pop
      pop("#s5_cta", 46.15, 0.28);
      shake("#s5 .cam", 46.40, 24);

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
