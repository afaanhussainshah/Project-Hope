import json
import base64
from pathlib import Path

base_dir = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kookaburra-sg-dukes")
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
        background: #F7F3EB; font-family: "Anton", sans-serif;
      }
      #root {
        position: relative; width: 1080px; height: 1920px; overflow: hidden;
        background: #F7F3EB;
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
        filter: drop-shadow(8px 12px 0 rgba(35, 20, 10, 0.16)) drop-shadow(2px 4px 0 rgba(0, 0, 0, 0.08));
      }
      .heavy-cut {
        filter: drop-shadow(12px 18px 0 rgba(35, 20, 10, 0.22)) drop-shadow(3px 6px 0 rgba(0, 0, 0, 0.12));
      }
      #wipe {
        position: absolute; left: 0; top: -190px; width: 1500px; height: 2300px; z-index: 6; pointer-events: none;
      }
      #grain {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 8;
        opacity: 0.08; mix-blend-mode: multiply; pointer-events: none;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' seed='5'/><feColorMatrix values='0 0 0 0 .3 0 0 0 0 .25 0 0 0 0 .2 0 0 0 .9 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");
      }
      #vig {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 9;
        pointer-events: none;
        background: radial-gradient(ellipse at 50% 50%, rgba(247, 243, 235, 0) 65%, rgba(180, 160, 130, 0.35) 100%);
      }
      /* STRICT DEDICATED CAPTION PEDESTAL ZONE (1240px - 1480px) */
      .cap {
        position: absolute; left: 50px; width: 980px; top: 1250px; height: 220px;
        z-index: 10; text-align: center; pointer-events: none;
        opacity: 0;
      }
      .cap span {
        display: inline-block; max-width: 960px; padding: 16px 36px 20px;
        background: #1C1A17; color: #FAF7F0;
        font-size: 74px; line-height: 1.10; letter-spacing: 1px; text-transform: uppercase;
        border: 4px solid #F7F3EB;
        filter: drop-shadow(9px 13px 0 rgba(35, 20, 10, 0.35));
      }
      .cap b { font-weight: 400; color: #E63946; }
      .cap i { font-style: normal; color: #FFB703; }
      .cap mark { font-weight: 400; padding: 0 12px; }
    </style>
  </head>
  <body>
    <div id="root" data-start="0" data-duration="49.95" data-width="1080" data-height="1920">
      <!-- 5 SCENES -->
      <div id="s1" class="clip scene" data-start="0" data-duration="7.50"><div class="cam"></div></div>
      <div id="s2" class="clip scene" data-start="7.50" data-duration="6.60"><div class="cam"></div></div>
      <div id="s3" class="clip scene" data-start="14.10" data-duration="15.30"><div class="cam"></div></div>
      <div id="s4" class="clip scene" data-start="29.40" data-duration="14.80"><div class="cam"></div></div>
      <div id="s5" class="clip scene" data-start="44.20" data-duration="5.75"><div class="cam"></div></div>

      <audio id="vo" src="renders/full_audio_mix.wav" data-start="0" data-duration="49.946"></audio>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- EXACT 19 SYNCED CAPTIONS (NO OVERLAP!) -->
      <div class="clip cap" data-start="0.09" data-duration="4.30"><span>AUSTRALIA, INDIA & ENGLAND<br><b>DON'T PLAY</b> WITH THE SAME BALL.</span></div>
      <div class="clip cap" data-start="4.90" data-duration="2.40"><span>AND THAT<br><i>CHANGES EVERYTHING!</i></span></div>
      <div class="clip cap" data-start="7.80" data-duration="2.00"><span>AUSTRALIA USES THE<br><mark style="background:#004B23;color:#FFB703;">KOOKABURRA.</mark></span></div>
      <div class="clip cap" data-start="9.95" data-duration="1.95"><span>INDIA USES THE<br><mark style="background:#002855;color:#FAF7F0;">SG BALL.</mark></span></div>
      <div class="clip cap" data-start="12.05" data-duration="1.95"><span>ENGLAND USES THE<br><mark style="background:#580C1F;color:#FAF7F0;">DUKES.</mark></span></div>
      <div class="clip cap" data-start="14.20" data-duration="3.10"><span>IN TEST CRICKET,<br>THE <b>HOME BOARD PICKS THE BALL!</b></span></div>
      <div class="clip cap" data-start="17.65" data-duration="2.00"><span>THAT'S WHY<br><b>VISITING TEAMS STRUGGLE!</b></span></div>
      <div class="clip cap" data-start="19.85" data-duration="2.65"><span>KOOKABURRA:<br>SWINGS EARLY, THEN <i>GOES SOFT!</i></span></div>
      <div class="clip cap" data-start="22.75" data-duration="3.65"><span>SG: GRIPS FOR SPINNERS,<br>AND <b>REVERSES AS IT AGES!</b></span></div>
      <div class="clip cap" data-start="26.60" data-duration="2.60"><span>DUKES: SWINGS AND SEAMS<br>FOR <i>MUCH LONGER!</i></span></div>
      <div class="clip cap" data-start="29.50" data-duration="2.60"><span>SO WHAT IF EVERYONE<br>USED <b>ONE BALL?</b></span></div>
      <div class="clip cap" data-start="32.25" data-duration="2.80"><span>VISITING BATTERS WOULDN'T<br>GET EXPOSED AS BADLY.</span></div>
      <div class="clip cap" data-start="35.25" data-duration="1.80"><span>HOME ADVANTAGE<br><b>WOULD SHRINK!</b></span></div>
      <div class="clip cap" data-start="37.25" data-duration="2.85"><span>BUT PITCHES & WEATHER<br>WOULD <i>STILL DECIDE MATCHES.</i></span></div>
      <div class="clip cap" data-start="40.30" data-duration="1.35"><span>AND SOME FANS SAY...</span></div>
      <div class="clip cap" data-start="41.75" data-duration="2.35"><span>THE BALL IS PART OF<br><b>CRICKET'S CHARACTER!</b></span></div>
      <div class="clip cap" data-start="44.35" data-duration="2.70"><span>SHOULD CRICKET USE<br><b>ONE BALL EVERYWHERE?</b></span></div>
      <div class="clip cap" data-start="47.25" data-duration="1.50"><span>OR <i>KEEP THE CHAOS?</i></span></div>
      <div class="clip cap" data-start="48.95" data-duration="0.95"><span>COMMENT<br><b>YOUR PICK BELOW!</b></span></div>
    </div>

    <script>
__GSAP_CODE__
    </script>

    <script>
      // ==========================================================
      // PALETTE & STYLES (LIGHT CLASSIC VINTAGE THEME)
      // ==========================================================
      const C = {
        bg: "#F7F3EB",
        parchment: "#FCF9F2",
        creamCard: "#EFE8DC",
        kraftPaper: "#DBC8AC",
        ink: "#1C1B1A",
        inkSub: "#524A42",
        kooRed: "#C82333",
        sgMaroon: "#8B1E2B",
        dukesBurgundy: "#540C1A",
        seamWhite: "#FAF6EE",
        gold: "#E0A926",
        goldDark: "#9E7310",
        ausGreen: "#004B23",
        ausGold: "#FFB703",
        indNavy: "#002855",
        indOrange: "#FB8500",
        engNavy: "#0B2238",
        engRed: "#C1121F",
        stampRed: "#C82333",
        turfGreen: "#3B6E3F",
        pitchDirt: "#D4A373",
      };

      // PAPER BALL GENERATOR (Realistic papercut seam, highlights, logo stamp)
      function createPaperBall(id, type, size, cx, cy) {
        let baseColor = C.kooRed;
        let brandText = "KOOKABURRA";
        let subText = "TURF • AUS";
        let crestColor = C.ausGold;
        let seamStyle = "low";
        
        if (type === "sg") {
          baseColor = C.sgMaroon;
          brandText = "SG TEST";
          subText = "HANDMADE • IND";
          crestColor = C.indOrange;
          seamStyle = "high";
        } else if (type === "dukes") {
          baseColor = C.dukesBurgundy;
          brandText = "DUKES";
          subText = "MATCH • ENG";
          crestColor = C.gold;
          seamStyle = "prominent";
        }

        const r = size / 2;
        let stitches = "";
        const numStitches = 12;
        for (let i = 0; i <= numStitches; i++) {
          const sy = cy - r * 0.80 + (i / numStitches) * (r * 1.60);
          const offset = Math.sin((i / numStitches) * Math.PI) * 3.5;
          const stitchW = seamStyle === "high" ? 14 : seamStyle === "prominent" ? 18 : 10;
          stitches += `<line x1="${cx - stitchW/2 + offset}" y1="${sy}" x2="${cx + stitchW/2 + offset}" y2="${sy}" stroke="${C.seamWhite}" stroke-width="${seamStyle==='low'?2.5:4}" stroke-linecap="round"/>`;
        }

        return `
          <g id="${id}" class="cut">
            <ellipse cx="${cx + 6}" cy="${cy + r + 18}" rx="${r * 0.70}" ry="14" fill="rgba(35,20,10,0.18)"/>
            <circle cx="${cx}" cy="${cy}" r="${r}" fill="${baseColor}" stroke="#3D0B12" stroke-width="3.5"/>
            <!-- Quarter panels crease -->
            <path d="M${cx - r * 0.88} ${cy} C${cx - r * 0.4} ${cy - r * 0.55}, ${cx + r * 0.4} ${cy - r * 0.55}, ${cx + r * 0.88} ${cy}" fill="none" stroke="rgba(0,0,0,0.25)" stroke-width="2.5" stroke-dasharray="5,4"/>
            <path d="M${cx - r * 0.88} ${cy} C${cx - r * 0.4} ${cy + r * 0.55}, ${cx + r * 0.4} ${cy + r * 0.55}, ${cx + r * 0.88} ${cy}" fill="none" stroke="rgba(0,0,0,0.25)" stroke-width="2.5" stroke-dasharray="5,4"/>

            <!-- Main Central Seam -->
            <path d="M${cx} ${cy - r + 3} Q${cx + 6} ${cy} ${cx} ${cy + r - 3}" fill="none" stroke="${seamStyle==='prominent'?'#FBF7EE':'#EBE5D6'}" stroke-width="${seamStyle==='low'?6:seamStyle==='high'?9:12}" stroke-linecap="round"/>
            <path d="M${cx} ${cy - r + 3} Q${cx + 6} ${cy} ${cx} ${cy + r - 3}" fill="none" stroke="rgba(0,0,0,0.3)" stroke-width="1.8"/>
            ${stitches}

            <!-- Leather highlight -->
            <path d="M${cx - r * 0.55} ${cy - r * 0.60} A${r * 0.80} ${r * 0.80} 0 0 1 ${cx - r * 0.1} ${cy - r * 0.80}" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="6" stroke-linecap="round"/>

            <!-- Brand crest stamp -->
            <g transform="translate(${cx - 70}, ${cy - 30})">
              <rect x="0" y="0" width="140" height="60" rx="6" fill="rgba(20,10,12,0.38)" stroke="${crestColor}" stroke-width="1.8" stroke-dasharray="3,2"/>
              <text x="70" y="26" fill="${crestColor}" font-size="18" font-family="Anton" text-anchor="middle" letter-spacing="2">${brandText}</text>
              <text x="70" y="47" fill="#FAF7F0" font-size="13" font-family="Anton" text-anchor="middle" letter-spacing="2">${subText}</text>
            </g>
          </g>
        `;
      }

      // ==========================================================
      // CRICKETER RIG FUNCTION (Pat Cummins, Virat Kohli, Jimmy Anderson)
      // ==========================================================
      function cricketerRig(id, x, y, s, opts = {}) {
        const skin = opts.skin || "#E8BA91";
        const sk2 = opts.sk2 || "#D49D70";
        const hair = opts.hair || "#24201D";
        const capColor = opts.cap || C.ausGreen;
        const visorColor = opts.visor || "#002B14";
        const badgeColor = opts.badge || C.ausGold;
        const jerseyColor = opts.jersey || "#F4F1EA";
        const vestColor = opts.vest || C.ausGreen;
        const nameText = opts.name || "CUMMINS";
        const countryFlag = opts.flag || "🇦🇺";
        const beard = opts.beard || false;
        const stubble = opts.stubble || false;
        const mustache = opts.mustache || false;
        const mouthType = opts.mouth || "flat";

        const mo = (n, h) => `<g class="m m-${n}" opacity="${n === mouthType ? 1 : 0}">${h}</g>`;

        return `
          <g id="${id}" class="cricketer-rig" transform="translate(${x}, ${y}) scale(${s})">
            <!-- Ground Paper Shadow -->
            <ellipse cx="0" cy="480" rx="200" ry="24" fill="rgba(35,20,10,0.22)"/>

            <!-- Name Tag Badge on Base -->
            <g class="cut" transform="translate(-160, 420)">
              <rect x="0" y="0" width="320" height="65" rx="10" fill="#1C1A17" stroke="#FAF7F0" stroke-width="3"/>
              <text x="160" y="44" fill="${badgeColor}" font-size="34" font-family="Anton" text-anchor="middle" letter-spacing="2">${countryFlag} ${nameText}</text>
            </g>

            <!-- Torso & Cricket White Uniform -->
            <g class="cut">
              <!-- Cricket White Shirt / Sweater -->
              <path d="M-180 430 Q-185 240 -85 210 L85 210 Q185 240 180 430 Z" fill="${jerseyColor}" stroke="#3A332C" stroke-width="4"/>
              <!-- Cable knit sweater V-Neck / Vest Trim -->
              <path d="M-65 210 L0 310 L65 210 L40 195 L-40 195 Z" fill="${vestColor}"/>
              <path d="M-40 210 L0 280 L40 210 Z" fill="${jerseyColor}"/>
              <!-- Neck -->
              <rect x="-35" y="150" width="70" height="75" rx="14" fill="${sk2}"/>
              <!-- Country / Board Emblem Crest -->
              <circle cx="0" cy="335" r="26" fill="${vestColor}" stroke="${badgeColor}" stroke-width="2"/>
              <circle cx="0" cy="335" r="10" fill="${badgeColor}"/>
            </g>

            <!-- Head & Face Rigs -->
            <g class="head cut">
              <!-- Ears -->
              <ellipse cx="-115" cy="18" rx="20" ry="30" fill="${sk2}" stroke="#3A332C" stroke-width="2"/>
              <ellipse cx="115" cy="18" rx="20" ry="30" fill="${sk2}" stroke="#3A332C" stroke-width="2"/>
              <!-- Face Shape -->
              <rect x="-110" y="-120" width="220" height="270" rx="100" fill="${skin}" stroke="#3A332C" stroke-width="4"/>

              <!-- Facial Hair (Kohli's sharp beard / Cummins stubble) -->
              ${beard ? `<path d="M-110 30 Q-115 150 0 150 Q115 150 110 30 Q85 120 0 122 Q-85 120 -110 30 Z" fill="${hair}"/>` : ""}
              ${stubble ? `<path d="M-90 60 Q-95 138 0 138 Q95 138 90 60 Q70 115 0 116 Q-70 115 -90 60 Z" fill="rgba(36,32,29,0.35)"/>` : ""}
              ${mustache ? `<path d="M-45 68 Q0 45 45 68 Q18 90 0 80 Q-18 90 -45 68 Z" fill="${hair}"/>` : ""}

              <!-- Hair / Sideburns -->
              <path d="M-115 -40 L-115 -75 L-90 -75 L-98 -10 Z M115 -40 L115 -75 L90 -75 L98 -10 Z" fill="${hair}"/>

              <!-- Cap (Baggy Green, India Blue, England Cap) -->
              <path d="M-122 -65 Q-124 -205 0 -205 Q124 -205 122 -65 Z" fill="${capColor}" stroke="#3A332C" stroke-width="3"/>
              <!-- Visor Peak -->
              <path d="M-135 -70 Q0 -98 135 -70 Q150 -44 0 -52 Q-150 -44 -135 -70 Z" fill="${visorColor}" stroke="#3A332C" stroke-width="3"/>
              <!-- Cap Gold Crest -->
              <circle cx="0" cy="-140" r="22" fill="${badgeColor}" stroke="#3A332C" stroke-width="2"/>

              <!-- Animated Eyes & Pupils -->
              <g class="eye eyeL"><circle cx="-48" cy="5" r="28" fill="#FFF" stroke="#3A332C" stroke-width="2"/><circle class="pupil pupilL" cx="-48" cy="5" r="13" fill="${C.ink}"/></g>
              <g class="eye eyeR"><circle cx="48" cy="5" r="28" fill="#FFF" stroke="#3A332C" stroke-width="2"/><circle class="pupil pupilR" cx="48" cy="5" r="13" fill="${C.ink}"/></g>

              <!-- Eyebrows -->
              <rect class="browL" x="-80" y="-42" width="62" height="14" rx="5" fill="${hair}"/>
              <rect class="browR" x="18" y="-42" width="62" height="14" rx="5" fill="${hair}"/>

              <!-- Nose -->
              <path d="M-8 22 Q-3 55 16 48" stroke="${sk2}" stroke-width="7" fill="none" stroke-linecap="round"/>

              <!-- Expressive Mouths -->
              ${mo("flat", '<rect x="-35" y="90" width="70" height="11" rx="5" fill="#7A2E22"/>')}
              ${mo("o", '<ellipse cx="0" cy="95" rx="22" ry="26" fill="#4A1410"/>')}
              ${mo("smirk", '<path d="M-38 94 Q10 120 48 80" stroke="#7A2E22" stroke-width="10" fill="none" stroke-linecap="round"/>')}
              ${mo("teeth", '<rect x="-45" y="80" width="90" height="34" rx="10" fill="#fff" stroke="#7A2E22" stroke-width="7"/><path d="M-15 82V112M15 82V112M-43 97H43" stroke="#C9B9A8" stroke-width="3"/>')}
            </g>
          </g>
        `;
      }

      // BATTER IN ACTION RIG
      function batterRig(id, x, y, s) {
        return `
          <g id="${id}" class="cut" transform="translate(${x}, ${y}) scale(${s})">
            <ellipse cx="0" cy="460" rx="170" ry="22" fill="rgba(35,20,10,0.2)"/>
            <!-- Torso in stance -->
            <path d="M-130 420 Q-150 250 -60 210 L60 210 Q150 250 130 420 Z" fill="#F4F1EA" stroke="#3A332C" stroke-width="4"/>
            <!-- Batting Pads -->
            <rect x="-90" y="320" width="70" height="150" rx="12" fill="#FAF6EE" stroke="#3A332C" stroke-width="3"/>
            <rect x="20" y="320" width="70" height="150" rx="12" fill="#FAF6EE" stroke="#3A332C" stroke-width="3"/>
            <!-- Blue Helmet -->
            <circle cx="0" cy="60" r="105" fill="#002855" stroke="#3A332C" stroke-width="4"/>
            <path d="M-115 50 Q0 25 115 50 L105 85 Q0 65 -105 85 Z" fill="#001833"/>
            <!-- Steel Grill -->
            <path d="M-75 75 L-75 145 Q0 175 75 145 L75 75" fill="none" stroke="#D3D3D3" stroke-width="6"/>
            <line x1="-70" y1="105" x2="70" y2="105" stroke="#D3D3D3" stroke-width="5"/>
            <line x1="-60" y1="130" x2="60" y2="130" stroke="#D3D3D3" stroke-width="5"/>
            <!-- Wide Shocked Eyes behind grill -->
            <circle cx="-38" cy="78" r="22" fill="#FFF"/><circle cx="-38" cy="78" r="11" fill="#1C1B1A"/>
            <circle cx="38" cy="78" r="22" fill="#FFF"/><circle cx="38" cy="78" r="11" fill="#1C1B1A"/>
            <!-- Bat in hands -->
            <g id="batter_bat" transform="translate(110, 220) rotate(-45)">
              <rect x="-10" y="-220" width="20" height="100" rx="5" fill="#FAF7F0" stroke="#888" stroke-width="2"/>
              <path d="M-26 -120 L26 -120 L30 140 Q30 170 0 170 Q-30 170 -30 140 Z" fill="#DDBB88" stroke="#886633" stroke-width="4"/>
              <rect x="-18" y="-90" width="36" height="80" fill="#C82333"/>
            </g>
          </g>
        `;
      }

      // ==========================================================
      // SVG SCENE INJECTIONS
      // ==========================================================
      const s1 = document.querySelector("#s1 .cam");
      const s2 = document.querySelector("#s2 .cam");
      const s3 = document.querySelector("#s3 .cam");
      const s4 = document.querySelector("#s4 .cam");
      const s5 = document.querySelector("#s5 .cam");
      const wipe = document.querySelector("#wipe");

      // WIPE TRANSITION CURTAIN
      wipe.innerHTML = `
        <svg viewBox="0 0 1500 2300" width="1500" height="2300">
          <g id="wipeCut" class="heavy-cut">
            <path d="M-50 -50 L1550 -50 L1550 2000 L1400 2060 L1250 1980 L1100 2080 L950 2000 L800 2090 L650 2010 L500 2100 L350 2020 L200 2110 L50 2030 L-50 2120 Z" fill="${C.creamCard}" stroke="${C.ink}" stroke-width="6"/>
          </g>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 1: THE SHOCK HOOK (0.00 - 7.50s)
      // ----------------------------------------------------------
      s1.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <pattern id="grid1" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(180, 160, 135, 0.22)" stroke-width="1.5"/>
          </pattern>
          <rect width="1080" height="1920" fill="${C.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid1)"/>

          <!-- Top Category Header -->
          <g id="s1_header" class="cut" transform="translate(190, 80)">
            <rect x="0" y="0" width="700" height="75" rx="10" fill="#1C1A17" stroke="#FAF7F0" stroke-width="3"/>
            <text x="350" y="50" fill="#FAF7F0" font-size="36" font-family="Anton" text-anchor="middle" letter-spacing="3">TEST CRICKET'S SECRET INEQUALITY</text>
          </g>

          <!-- Main Title Card (Strictly above y=320) -->
          <g id="s1_title" class="heavy-cut" transform="translate(70, 175)">
            <rect x="0" y="0" width="940" height="150" rx="16" fill="${C.parchment}" stroke="${C.ink}" stroke-width="5"/>
            <rect x="10" y="10" width="920" height="130" rx="10" fill="none" stroke="${C.stampRed}" stroke-width="2.5" stroke-dasharray="10,6"/>
            <text x="470" y="65" fill="${C.ink}" font-size="46" font-family="Anton" text-anchor="middle">AUSTRALIA • INDIA • ENGLAND</text>
            <text x="470" y="122" fill="${C.stampRed}" font-size="58" font-family="Anton" text-anchor="middle">DON'T PLAY WITH THE SAME CRICKET BALL!</text>
          </g>

          <!-- HERO CHARACTERS STAGE (y=340 to y=1180) -->
          <!-- 1. Pat Cummins (Left) -->
          ${cricketerRig("s1_cummins", 220, 480, 0.85, {
            name: "CUMMINS", flag: "🇦🇺", cap: C.ausGreen, visor: "#002B14", badge: C.ausGold, vest: C.ausGreen, mouth: "smirk", stubble: true
          })}
          <!-- Cummins Ball -->
          <g id="s1_koo_ball">
            ${createPaperBall("s1_b1", "koo", 180, 220, 920)}
          </g>

          <!-- 2. Virat Kohli (Center Hero) -->
          ${cricketerRig("s1_kohli", 540, 440, 0.95, {
            name: "KOHLI", flag: "🇮🇳", cap: C.indNavy, visor: "#001833", badge: C.indOrange, vest: C.indNavy, beard: true, mouth: "o"
          })}
          <!-- Kohli SG Ball -->
          <g id="s1_sg_ball">
            ${createPaperBall("s1_b2", "sg", 190, 540, 900)}
          </g>

          <!-- 3. James Anderson (Right) -->
          ${cricketerRig("s1_anderson", 860, 480, 0.85, {
            name: "ANDERSON", flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿", cap: C.engNavy, visor: "#051524", badge: C.gold, vest: C.engNavy, mouth: "teeth", stubble: true
          })}
          <!-- Anderson Dukes Ball -->
          <g id="s1_dukes_ball">
            ${createPaperBall("s1_b3", "dukes", 180, 860, 920)}
          </g>

          <!-- Stamp Slam Across Stage (At y=1040, strictly above y=1240!) -->
          <g id="s1_stamp" class="heavy-cut" transform="translate(160, 1030) rotate(-6)">
            <rect x="0" y="0" width="760" height="130" rx="14" fill="${C.stampRed}" stroke="#3A050B" stroke-width="5"/>
            <rect x="10" y="10" width="740" height="110" rx="8" fill="none" stroke="#FAF7F0" stroke-width="3" stroke-dasharray="12,6"/>
            <text x="380" y="85" fill="#FAF7F0" font-size="74" font-family="Anton" text-anchor="middle" letter-spacing="4">CHANGES EVERYTHING!</text>
          </g>

          <!-- Turf Base Line at Bottom -->
          <rect x="0" y="1720" width="1080" height="200" fill="${C.turfGreen}"/>
          <line x1="0" y1="1720" x2="1080" y2="1720" stroke="#FAF7F0" stroke-width="8" stroke-dasharray="25,15"/>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 2: THE BIG THREE (7.50 - 14.10s)
      // ----------------------------------------------------------
      s2.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${C.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid1)"/>

          <!-- Top Stage Card -->
          <g id="s2_header" class="cut" transform="translate(140, 80)">
            <rect x="0" y="0" width="800" height="85" rx="10" fill="${C.ink}" stroke="${C.bg}" stroke-width="3"/>
            <text x="400" y="56" fill="#FAF7F0" font-size="44" font-family="Anton" text-anchor="middle" letter-spacing="3">THE THREE CRICKET BALL MAJORS</text>
          </g>

          <!-- 3 DYNAMIC HERO SPOTLIGHTS (Each shows Cricketer + Ball + Specs) -->
          <!-- 1. AUSTRALIA: Pat Cummins + Kookaburra -->
          <g id="s2_row_koo" class="heavy-cut" transform="translate(60, 200)">
            <rect x="0" y="0" width="960" height="290" rx="16" fill="${C.parchment}" stroke="${C.ausGreen}" stroke-width="4"/>
            <rect x="12" y="12" width="200" height="266" rx="10" fill="${C.ausGreen}"/>
            <text x="112" y="150" fill="${C.ausGold}" font-size="58" font-family="Anton" text-anchor="middle">🇦🇺 AUS</text>
            <!-- Cummins Mini Character Face -->
            ${cricketerRig("s2_cummins_mini", 310, -10, 0.44, { name: "PAT", flag: "", cap: C.ausGreen, badge: C.ausGold, vest: C.ausGreen, mouth: "smirk" })}
            <!-- Kookaburra Ball -->
            ${createPaperBall("s2_b_koo", "koo", 150, 460, 145)}
            <text x="560" y="80" fill="${C.ink}" font-size="54" font-family="Anton">KOOKABURRA TURF</text>
            <text x="560" y="135" fill="${C.ausGreen}" font-size="30" font-family="Anton">MACHINE-STITCHED • LOW EMBEDDED SEAM</text>
            <text x="560" y="190" fill="${C.inkSub}" font-size="28" font-family="Anton">Australia • South Africa • New Zealand</text>
            <rect x="560" y="215" width="370" height="38" rx="6" fill="#E8F5E9"/>
            <text x="745" y="242" fill="${C.ausGreen}" font-size="22" font-family="Anton" text-anchor="middle">FIERCE SWING FIRST 15-20 OVERS</text>
          </g>

          <!-- 2. INDIA: Virat Kohli + SG -->
          <g id="s2_row_sg" class="heavy-cut" transform="translate(60, 520)">
            <rect x="0" y="0" width="960" height="290" rx="16" fill="${C.parchment}" stroke="${C.indNavy}" stroke-width="4"/>
            <rect x="12" y="12" width="200" height="266" rx="10" fill="${C.indNavy}"/>
            <text x="112" y="150" fill="${C.indOrange}" font-size="58" font-family="Anton" text-anchor="middle">🇮🇳 IND</text>
            ${cricketerRig("s2_kohli_mini", 310, -10, 0.44, { name: "VIRAT", flag: "", cap: C.indNavy, badge: C.indOrange, vest: C.indNavy, beard: true, mouth: "teeth" })}
            ${createPaperBall("s2_b_sg", "sg", 150, 460, 145)}
            <text x="560" y="80" fill="${C.ink}" font-size="54" font-family="Anton">SG TEST (SANSPAREILS)</text>
            <text x="560" y="135" fill="${C.sgMaroon}" font-size="30" font-family="Anton">PROMINENT HAND SEAM • THICK THREAD</text>
            <text x="560" y="190" fill="${C.inkSub}" font-size="28" font-family="Anton">Exclusively used on abrasive Indian soil</text>
            <rect x="560" y="215" width="370" height="38" rx="6" fill="#FFF3E0"/>
            <text x="745" y="242" fill="${C.sgMaroon}" font-size="22" font-family="Anton" text-anchor="middle">SPIN GRIP & LATE DEADLY REVERSE</text>
          </g>

          <!-- 3. ENGLAND: Jimmy Anderson + Dukes -->
          <g id="s2_row_dukes" class="heavy-cut" transform="translate(60, 840)">
            <rect x="0" y="0" width="960" height="290" rx="16" fill="${C.parchment}" stroke="${C.dukesBurgundy}" stroke-width="4"/>
            <rect x="12" y="12" width="200" height="266" rx="10" fill="${C.dukesBurgundy}"/>
            <text x="112" y="150" fill="${C.gold}" font-size="58" font-family="Anton" text-anchor="middle">🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG</text>
            ${cricketerRig("s2_anderson_mini", 310, -10, 0.44, { name: "JIMMY", flag: "", cap: C.engNavy, badge: C.gold, vest: C.engNavy, stubble: true, mouth: "smirk" })}
            ${createPaperBall("s2_b_dukes", "dukes", 150, 460, 145)}
            <text x="560" y="80" fill="${C.ink}" font-size="54" font-family="Anton">DUKES SPECIAL MATCH</text>
            <text x="560" y="135" fill="${C.dukesBurgundy}" font-size="30" font-family="Anton">RAISED 6-ROW SEAM • GREASE LACQUER</text>
            <text x="560" y="190" fill="${C.inkSub}" font-size="28" font-family="Anton">England & West Indies Test Series</text>
            <rect x="560" y="215" width="370" height="38" rx="6" fill="#FCE4EC"/>
            <text x="745" y="242" fill="${C.dukesBurgundy}" font-size="22" font-family="Anton" text-anchor="middle">SWINGS & SEAMS UP TO 70+ OVERS</text>
          </g>

          <!-- Turf Base -->
          <rect x="0" y="1720" width="1080" height="200" fill="${C.turfGreen}"/>
          <line x1="0" y1="1720" x2="1080" y2="1720" stroke="#FAF7F0" stroke-width="8" stroke-dasharray="25,15"/>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 3: PITCH RULES & BALL BEHAVIOR (14.10 - 29.40s)
      // ----------------------------------------------------------
      s3.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${C.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid1)"/>

          <!-- Top Law Card (y=80 to y=230) -->
          <g id="s3_law_card" class="heavy-cut" transform="translate(70, 80)">
            <rect x="0" y="0" width="940" height="150" rx="14" fill="${C.parchment}" stroke="${C.stampRed}" stroke-width="5"/>
            <text x="470" y="55" fill="${C.stampRed}" font-size="38" font-family="Anton" text-anchor="middle">ICC TEST REGULATION</text>
            <text x="470" y="115" fill="${C.ink}" font-size="54" font-family="Anton" text-anchor="middle">"THE HOST BOARD CHOOSES THE BALL"</text>
          </g>

          <!-- Stamp: VISITING TEAMS STRUGGLE! (y=250) -->
          <g id="s3_struggle_stamp" class="cut" transform="translate(190, 245) rotate(2.5)">
            <rect x="0" y="0" width="700" height="80" rx="10" fill="${C.ink}" stroke="#FAF7F0" stroke-width="3"/>
            <text x="350" y="54" fill="${C.ausGold}" font-size="40" font-family="Anton" text-anchor="middle" letter-spacing="3">THAT'S WHY TOURING TEAMS STRUGGLE!</text>
          </g>

          <!-- HERO INTERACTIVE ACTION STAGE (y=340 to y=1160) -->
          <!-- 1. KOOKABURRA: Early Swing -> Flattens Soft -->
          <g id="s3_action_koo" class="heavy-cut" transform="translate(60, 345)">
            <rect x="0" y="0" width="960" height="255" rx="14" fill="${C.creamCard}" stroke="${C.ausGreen}" stroke-width="4"/>
            ${cricketerRig("s3_cummins_bowl", 120, -5, 0.42, { name: "CUMMINS", cap: C.ausGreen, badge: C.ausGold, vest: C.ausGreen, mouth: "teeth" })}
            ${createPaperBall("s3_ball_k", "koo", 140, 260, 130)}
            <text x="360" y="65" fill="${C.ausGreen}" font-size="44" font-family="Anton">KOOKABURRA: EARLY FIRE, THEN SOFT</text>
            <text x="360" y="115" fill="${C.ink}" font-size="30" font-family="Anton">Deadly swing in first 20 overs.</text>
            <rect x="360" y="135" width="560" height="32" rx="6" fill="#DDD2BE"/>
            <rect x="360" y="135" width="180" height="32" rx="6" fill="${C.ausGold}"/>
            <text x="375" y="158" fill="${C.ink}" font-size="18" font-family="Anton">SWINGS EARLY</text>
            <text x="640" y="158" fill="${C.inkSub}" font-size="18" font-family="Anton">OVERS 20-80: SEAM FLATTENS & GOES SOFT</text>
            <text x="360" y="210" fill="${C.stampRed}" font-size="26" font-family="Anton">➜ Batters feast once the ball loses hardness!</text>
          </g>

          <!-- 2. SG: Spinners Grip & Reverse Swing -->
          <g id="s3_action_sg" class="heavy-cut" transform="translate(60, 620)">
            <rect x="0" y="0" width="960" height="255" rx="14" fill="${C.creamCard}" stroke="${C.sgMaroon}" stroke-width="4"/>
            ${cricketerRig("s3_kohli_cheer", 120, -5, 0.42, { name: "KOHLI", cap: C.indNavy, badge: C.indOrange, vest: C.indNavy, beard: true, mouth: "roar" })}
            ${createPaperBall("s3_ball_s", "sg", 140, 260, 130)}
            <text x="360" y="65" fill="${C.sgMaroon}" font-size="44" font-family="Anton">SG: SPIN GRIP & REVERSE WEAPON</text>
            <text x="360" y="115" fill="${C.ink}" font-size="30" font-family="Anton">Prominent seam bites dry Indian wickets.</text>
            <rect x="360" y="135" width="560" height="32" rx="6" fill="#DDD2BE"/>
            <rect x="520" y="135" width="400" height="32" rx="6" fill="${C.sgMaroon}"/>
            <text x="375" y="158" fill="${C.inkSub}" font-size="18" font-family="Anton">SPINNER GRIP</text>
            <text x="660" y="158" fill="#FAF7F0" font-size="18" font-family="Anton">OVERS 30-80: WICKED REVERSE SWING!</text>
            <text x="360" y="210" fill="${C.indNavy}" font-size="26" font-family="Anton">➜ Indian pacers & spinners ambush visitors!</text>
          </g>

          <!-- 3. DUKES: The Swing Engine That Never Dies -->
          <g id="s3_action_dukes" class="heavy-cut" transform="translate(60, 895)">
            <rect x="0" y="0" width="960" height="255" rx="14" fill="${C.creamCard}" stroke="${C.dukesBurgundy}" stroke-width="4"/>
            ${cricketerRig("s3_anderson_bowl", 120, -5, 0.42, { name: "JIMMY", cap: C.engNavy, badge: C.gold, vest: C.engNavy, mouth: "smirk" })}
            ${createPaperBall("s3_ball_d", "dukes", 140, 260, 130)}
            <text x="360" y="65" fill="${C.dukesBurgundy}" font-size="44" font-family="Anton">DUKES: RELENTLESS SWING & SEAM</text>
            <text x="360" y="115" fill="${C.ink}" font-size="30" font-family="Anton">Hand-stitched spine keeps seam standing up.</text>
            <rect x="360" y="135" width="560" height="32" rx="6" fill="${C.dukesBurgundy}"/>
            <text x="640" y="158" fill="${C.gold}" font-size="18" font-family="Anton" text-anchor="middle">SWING & SEAM MOVEMENT LASTS 60-70+ OVERS NON-STOP</text>
            <text x="360" y="210" fill="${C.stampRed}" font-size="26" font-family="Anton">➜ Visiting openers get unpicked by English nip!</text>
          </g>

          <!-- Turf Base -->
          <rect x="0" y="1720" width="1080" height="200" fill="${C.turfGreen}"/>
          <line x1="0" y1="1720" x2="1080" y2="1720" stroke="#FAF7F0" stroke-width="8" stroke-dasharray="25,15"/>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 4: WHAT IF ONE BALL? (29.40 - 44.20s)
      // ----------------------------------------------------------
      s4.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${C.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid1)"/>

          <!-- Top Question Card (y=80 to y=250) -->
          <g id="s4_question_card" class="heavy-cut" transform="translate(70, 80)">
            <rect x="0" y="0" width="940" height="160" rx="16" fill="${C.parchment}" stroke="${C.ink}" stroke-width="5"/>
            <rect x="10" y="10" width="920" height="140" rx="10" fill="none" stroke="${C.goldDark}" stroke-width="2.5" stroke-dasharray="10,6"/>
            <text x="470" y="60" fill="${C.inkSub}" font-size="36" font-family="Anton" text-anchor="middle">STANDARDIZING WORLD CRICKET</text>
            <text x="470" y="125" fill="${C.stampRed}" font-size="62" font-family="Anton" text-anchor="middle">SO WHAT IF EVERYONE USED ONE BALL?</text>
          </g>

          <!-- HERO CHARACTERS DILEMMA STAGE (y=260 to y=1180) -->
          <!-- The Batter Relief vs Home Edge Scales -->
          <g id="s4_scale_group" transform="translate(0, 0)">
            <!-- Left Card: Visiting Batters Fair Trial -->
            <g id="s4_card_left" class="cut" transform="translate(60, 260)">
              <rect x="0" y="0" width="460" height="320" rx="16" fill="${C.parchment}" stroke="${C.ink}" stroke-width="4"/>
              <rect x="0" y="0" width="460" height="55" rx="12" fill="#E8F5E9"/>
              <text x="230" y="38" fill="#2E7D32" font-size="28" font-family="Anton" text-anchor="middle">PRO: VISITING BATTERS</text>
              <!-- Batter Character Mini -->
              ${batterRig("s4_batter_mini", 120, 90, 0.38)}
              <text x="290" y="130" fill="${C.ink}" font-size="38" font-family="Anton">NO SUDDEN</text>
              <text x="290" y="175" fill="${C.stampRed}" font-size="44" font-family="Anton">AMBUSH!</text>
              <text x="290" y="225" fill="${C.inkSub}" font-size="22" font-family="Anton">Familiar seam height</text>
              <text x="290" y="255" fill="${C.inkSub}" font-size="22" font-family="Anton">and swing pattern</text>
            </g>

            <!-- Right Card: Home Advantage Shrinks -->
            <g id="s4_card_right" class="cut" transform="translate(560, 260)">
              <rect x="0" y="0" width="460" height="320" rx="16" fill="${C.parchment}" stroke="${C.ink}" stroke-width="4"/>
              <rect x="0" y="0" width="460" height="55" rx="12" fill="#FFF3E0"/>
              <text x="230" y="38" fill="#E65100" font-size="28" font-family="Anton" text-anchor="middle">CON: HOME FORTRESS</text>
              <!-- Cummins Mini Shocked -->
              ${cricketerRig("s4_cummins_shock", 360, 80, 0.38, { name: "HOME", flag: "", cap: C.ausGreen, badge: C.ausGold, vest: C.ausGreen, mouth: "o" })}
              <text x="170" y="130" fill="${C.ink}" font-size="38" font-family="Anton">HOME EDGE</text>
              <text x="170" y="175" fill="${C.indNavy}" font-size="44" font-family="Anton">WOULD SHRINK!</text>
              <text x="170" y="225" fill="${C.inkSub}" font-size="22" font-family="Anton">Familiarity everywhere</text>
              <text x="170" y="255" fill="${C.inkSub}" font-size="22" font-family="Anton">kills secret tactics</text>
            </g>
          </g>

          <!-- Pitches & Weather Postcard (y=600 to y=850) -->
          <g id="s4_pitch_card" class="heavy-cut" transform="translate(70, 605)">
            <rect x="0" y="0" width="940" height="235" rx="16" fill="${C.creamCard}" stroke="${C.ink}" stroke-width="4"/>
            <!-- Weather / Pitch icons -->
            <text x="470" y="60" fill="${C.ink}" font-size="42" font-family="Anton" text-anchor="middle">BUT PITCHES & WEATHER STILL REIGN SUPREME!</text>
            <text x="470" y="130" fill="${C.goldDark}" font-size="56" font-family="Anton" text-anchor="middle">TURF CRACKS • HUMIDITY • RAIN CLOUDS</text>
            <text x="470" y="190" fill="${C.inkSub}" font-size="30" font-family="Anton" text-anchor="middle">Perth bounce, Lord's slope & Kanpur dust still decide matches!</text>
          </g>

          <!-- Soul of Cricket Certificate (y=860 to y=1140) -->
          <g id="s4_soul_card" class="heavy-cut" transform="translate(70, 860)">
            <rect x="0" y="0" width="940" height="255" rx="16" fill="#1C1A17" stroke="${C.gold}" stroke-width="5"/>
            <rect x="12" y="12" width="916" height="231" rx="10" fill="none" stroke="${C.gold}" stroke-width="2" stroke-dasharray="8,6"/>
            <!-- 3 Mini balls side by side -->
            ${createPaperBall("s4_b1", "koo", 85, 120, 125)}
            ${createPaperBall("s4_b2", "sg", 85, 470, 125)}
            ${createPaperBall("s4_b3", "dukes", 85, 820, 125)}
            <text x="470" y="60" fill="${C.gold}" font-size="36" font-family="Anton" text-anchor="middle" letter-spacing="3">CRICKET'S SOUL & HERITAGE</text>
            <text x="470" y="195" fill="#FAF7F0" font-size="54" font-family="Anton" text-anchor="middle">"THE BALL IS PART OF CRICKET'S CHARACTER!"</text>
            <text x="470" y="235" fill="#D5CBBF" font-size="26" font-family="Anton" text-anchor="middle">Different crafts, different skills, distinct masteries.</text>
          </g>

          <!-- Turf Base -->
          <rect x="0" y="1720" width="1080" height="200" fill="${C.turfGreen}"/>
          <line x1="0" y1="1720" x2="1080" y2="1720" stroke="#FAF7F0" stroke-width="8" stroke-dasharray="25,15"/>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 5: THE BIG VERDICT & CTA (44.20 - 49.95s)
      // ----------------------------------------------------------
      s5.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${C.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid1)"/>

          <!-- Top Question Card -->
          <g id="s5_vote_title" class="heavy-cut" transform="translate(70, 90)">
            <rect x="0" y="0" width="940" height="170" rx="16" fill="${C.parchment}" stroke="${C.ink}" stroke-width="5"/>
            <text x="470" y="65" fill="${C.stampRed}" font-size="44" font-family="Anton" text-anchor="middle">WHAT IS YOUR VERDICT?</text>
            <text x="470" y="135" fill="${C.ink}" font-size="62" font-family="Anton" text-anchor="middle">SHOULD TEST CRICKET USE ONE BALL?</text>
          </g>

          <!-- HERO VOTING BALLOTS WITH CHARACTERS (y=280 to y=1180) -->
          <!-- OPTION A: ONE BALL EVERYWHERE (Pat Cummins & Jimmy Anderson Endorse) -->
          <g id="s5_btn_one" class="heavy-cut" transform="translate(60, 290)">
            <rect x="0" y="0" width="960" height="240" rx="16" fill="${C.parchment}" stroke="${C.indNavy}" stroke-width="5"/>
            <!-- Cummins Mini endorsement -->
            ${cricketerRig("s5_cummins_vote", 100, -15, 0.38, { name: "CUMMINS", cap: C.ausGreen, badge: C.ausGold, vest: C.ausGreen, mouth: "smirk" })}
            <circle cx="210" cy="120" r="50" fill="${C.indNavy}"/>
            <text x="210" y="137" fill="#FAF7F0" font-size="48" font-family="Anton" text-anchor="middle">A</text>
            <text x="300" y="95" fill="${C.indNavy}" font-size="60" font-family="Anton">ONE BALL EVERYWHERE</text>
            <text x="300" y="150" fill="${C.ink}" font-size="32" font-family="Anton">Standardize global test matches (Equal ground)</text>
            <rect x="300" y="175" width="220" height="36" rx="6" fill="${C.indNavy}"/>
            <text x="410" y="201" fill="#FAF7F0" font-size="22" font-family="Anton" text-anchor="middle">UNIFIED RULES</text>
          </g>

          <!-- OPTION B: KEEP THE CHAOS! (Virat Kohli Endorses) -->
          <g id="s5_btn_chaos" class="heavy-cut" transform="translate(60, 560)">
            <rect x="0" y="0" width="960" height="240" rx="16" fill="${C.parchment}" stroke="${C.stampRed}" stroke-width="5"/>
            <!-- Kohli Mini endorsement -->
            ${cricketerRig("s5_kohli_vote", 100, -15, 0.38, { name: "VIRAT", cap: C.indNavy, badge: C.indOrange, vest: C.indNavy, beard: true, mouth: "roar" })}
            <circle cx="210" cy="120" r="50" fill="${C.stampRed}"/>
            <text x="210" y="137" fill="#FAF7F0" font-size="48" font-family="Anton" text-anchor="middle">B</text>
            <text x="300" y="95" fill="${C.stampRed}" font-size="60" font-family="Anton">KEEP THE CHAOS!</text>
            <text x="300" y="150" fill="${C.ink}" font-size="32" font-family="Anton">Preserve heritage, pitch quirks & craft</text>
            <rect x="300" y="175" width="220" height="36" rx="6" fill="${C.stampRed}"/>
            <text x="410" y="201" fill="#FAF7F0" font-size="22" font-family="Anton" text-anchor="middle">PURE TRADITION</text>
          </g>

          <!-- Interactive Voting Card (Strictly above y=1180!) -->
          <g id="s5_cta_card" class="heavy-cut" transform="translate(70, 830)">
            <rect x="0" y="0" width="940" height="240" rx="16" fill="#1C1A17" stroke="${C.gold}" stroke-width="5"/>
            <rect x="14" y="14" width="912" height="212" rx="10" fill="none" stroke="${C.gold}" stroke-width="2" stroke-dasharray="10,6"/>
            <!-- Pulsing pointer indicator -->
            <polygon points="470,40 500,85 440,85" fill="${C.gold}"/>
            <text x="470" y="140" fill="#FAF7F0" font-size="64" font-family="Anton" text-anchor="middle">COMMENT: A OR B?</text>
            <text x="470" y="200" fill="${C.gold}" font-size="36" font-family="Anton" text-anchor="middle" letter-spacing="3">WHICH CRICKET BALL DO YOU PREFER?</text>
          </g>

          <!-- Turf Base -->
          <rect x="0" y="1720" width="1080" height="200" fill="${C.turfGreen}"/>
          <line x1="0" y1="1720" x2="1080" y2="1720" stroke="#FAF7F0" stroke-width="8" stroke-dasharray="25,15"/>
        </svg>
      `;

      // ==========================================================
      // GSAP MASTER TIMELINE ORCHESTRATION
      // ==========================================================
      const tl = gsap.timeline({ paused: true });

      // STRICT SCENE VISIBILITY CONTROLLER
      const sceneList = [
        { id: "#s1", start: 0.00, end: 7.50 },
        { id: "#s2", start: 7.50, end: 14.10 },
        { id: "#s3", start: 14.10, end: 29.40 },
        { id: "#s4", start: 29.40, end: 44.20 },
        { id: "#s5", start: 44.20, end: 49.95 },
      ];

      sceneList.forEach((sc) => {
        tl.set(sc.id, { display: "block", autoAlpha: 1, zIndex: 3 }, sc.start);
        tl.set(sc.id, { display: "none", autoAlpha: 0, zIndex: 1 }, sc.end);
      });

      // SCENE TRANSITION WIPES
      const wipeTimes = [7.45, 14.05, 29.35, 44.15];
      wipeTimes.forEach((wt) => {
        tl.fromTo("#wipeCut", { y: -2200 }, { y: 2200, duration: 0.45, ease: "power2.inOut" }, wt);
      });

      // ----------------------------------------------------------
      // ANIMATION: SCENE 1 (0.00s - 7.50s)
      // ----------------------------------------------------------
      tl.from("#s1_header", { y: -100, opacity: 0, duration: 0.45, ease: "back.out(2)" }, 0.08);
      tl.from("#s1_title", { scale: 0.8, opacity: 0, duration: 0.55, ease: "back.out(1.8)" }, 0.22);

      // Cricketers Drop Down onto Stage
      tl.from("#s1_cummins", { y: -500, rotation: -12, duration: 0.65, ease: "bounce.out" }, 0.45);
      tl.from("#s1_kohli", { y: -500, rotation: 8, duration: 0.65, ease: "bounce.out" }, 0.65);
      tl.from("#s1_anderson", { y: -500, rotation: -10, duration: 0.65, ease: "bounce.out" }, 0.85);

      // Balls Appear in Hands
      tl.from("#s1_koo_ball", { scale: 0, duration: 0.4, ease: "back.out(2.5)" }, 0.90);
      tl.from("#s1_sg_ball", { scale: 0, duration: 0.4, ease: "back.out(2.5)" }, 1.10);
      tl.from("#s1_dukes_ball", { scale: 0, duration: 0.4, ease: "back.out(2.5)" }, 1.30);

      // Eye & Pupil Movement (Looking between each other)
      tl.to("#s1_kohli .pupil", { x: -8, duration: 0.3 }, 2.00);
      tl.to("#s1_cummins .pupil", { x: 8, duration: 0.3 }, 2.50);
      tl.to("#s1_anderson .pupil", { x: -8, duration: 0.3 }, 3.00);

      // Stamp SLAM: "CHANGES EVERYTHING!"
      tl.fromTo("#s1_stamp", { scale: 2.8, opacity: 0, rotation: -28 }, { scale: 1, opacity: 1, rotation: -6, duration: 0.35, ease: "power4.in" }, 4.95);
      tl.to("#s1 .cam", { scale: 1.03, y: 15, duration: 0.12, yoyo: true, repeat: 1 }, 5.30);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 2 (7.50s - 14.10s)
      // ----------------------------------------------------------
      tl.from("#s2_header", { y: -70, opacity: 0, duration: 0.4, ease: "back.out(1.8)" }, 7.55);

      // 1. Australia / Cummins Spotlight
      tl.from("#s2_row_koo", { x: -850, rotation: -6, opacity: 0, duration: 0.55, ease: "back.out(1.6)" }, 7.80);
      tl.from("#s2_b_koo", { rotation: -180, scale: 0.5, duration: 0.5, ease: "back.out(2)" }, 8.05);

      // 2. India / Kohli Spotlight
      tl.from("#s2_row_sg", { x: 850, rotation: 6, opacity: 0, duration: 0.55, ease: "back.out(1.6)" }, 9.95);
      tl.from("#s2_b_sg", { rotation: 180, scale: 0.5, duration: 0.5, ease: "back.out(2)" }, 10.20);

      // 3. England / Anderson Spotlight
      tl.from("#s2_row_dukes", { x: -850, rotation: -6, opacity: 0, duration: 0.55, ease: "back.out(1.6)" }, 12.05);
      tl.from("#s2_b_dukes", { rotation: -180, scale: 0.5, duration: 0.5, ease: "back.out(2)" }, 12.30);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 3 (14.10s - 29.40s)
      // ----------------------------------------------------------
      tl.from("#s3_law_card", { scale: 0.8, opacity: 0, duration: 0.45, ease: "back.out(1.8)" }, 14.15);
      tl.fromTo("#s3_struggle_stamp", { scale: 2.2, opacity: 0, rotation: 18 }, { scale: 1, opacity: 1, rotation: 2.5, duration: 0.4, ease: "power4.in" }, 17.65);
      tl.to("#s3 .cam", { scale: 1.025, y: -10, duration: 0.12, yoyo: true, repeat: 1 }, 17.95);

      // Action Breakdown Cards with Bowler Rigs
      tl.from("#s3_action_koo", { x: -800, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 19.85);
      tl.from("#s3_ball_k", { scale: 0.2, rotation: -120, duration: 0.4, ease: "back.out(2)" }, 20.10);

      tl.from("#s3_action_sg", { x: 800, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 22.75);
      tl.from("#s3_ball_s", { scale: 0.2, rotation: 120, duration: 0.4, ease: "back.out(2)" }, 23.00);

      tl.from("#s3_action_dukes", { x: -800, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 26.60);
      tl.from("#s3_ball_d", { scale: 0.2, rotation: -120, duration: 0.4, ease: "back.out(2)" }, 26.85);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 4 (29.40s - 44.20s)
      // ----------------------------------------------------------
      tl.from("#s4_question_card", { scale: 0.75, opacity: 0, duration: 0.5, ease: "back.out(2)" }, 29.45);

      // Scales of Dilemma (Batter relief vs Home edge)
      tl.from("#s4_card_left", { x: -400, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 32.25);
      tl.from("#s4_card_right", { x: 400, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 35.25);
      tl.to("#s4_card_left", { y: -15, duration: 1.2, yoyo: true, repeat: 1, ease: "sine.inOut" }, 33.00);
      tl.to("#s4_card_right", { y: 15, duration: 1.2, yoyo: true, repeat: 1, ease: "sine.inOut" }, 33.00);

      // Pitches & Weather
      tl.from("#s4_pitch_card", { y: 100, opacity: 0, duration: 0.5, ease: "power2.out" }, 37.25);

      // Soul Card
      tl.from("#s4_soul_card", { scale: 0.85, opacity: 0, duration: 0.5, ease: "back.out(1.8)" }, 41.75);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 5 (44.20s - 49.95s)
      // ----------------------------------------------------------
      tl.from("#s5_vote_title", { y: -80, opacity: 0, duration: 0.4, ease: "back.out(1.8)" }, 44.25);
      tl.from("#s5_btn_one", { x: -650, opacity: 0, duration: 0.45, ease: "back.out(1.7)" }, 44.40);
      tl.from("#s5_btn_chaos", { x: 650, opacity: 0, duration: 0.45, ease: "back.out(1.7)" }, 47.25);
      tl.from("#s5_cta_card", { scale: 0.82, opacity: 0, duration: 0.4, ease: "back.out(2)" }, 48.90);

      // Button pulse loops
      tl.to("#s5_btn_one", { scale: 1.025, duration: 0.6, yoyo: true, repeat: -1, ease: "sine.inOut" }, 45.00);
      tl.to("#s5_btn_chaos", { scale: 1.025, duration: 0.6, yoyo: true, repeat: -1, ease: "sine.inOut" }, 47.80);

      // ----------------------------------------------------------
      // CAPTION TIMELINE (STRICT ZERO-OVERLAP GUARANTEE)
      // ----------------------------------------------------------
      const caps = document.querySelectorAll(".cap");
      caps.forEach((cap) => {
        const start = parseFloat(cap.dataset.start);
        const dur = parseFloat(cap.dataset.duration);
        const end = start + dur;

        tl.fromTo(
          cap,
          { opacity: 0, scale: 0.82, y: 35 },
          { opacity: 1, scale: 1, y: 0, duration: 0.22, ease: "back.out(2.2)" },
          start
        );
        tl.to(
          cap,
          { opacity: 0, scale: 0.88, y: -20, duration: 0.16, ease: "power2.in" },
          Math.max(start + 0.22, end - 0.18)
        );
      });

      // EXPOSE INTERFACES FOR FAST_RENDER
      window.__timelines = { main: tl };
      window.seekFrame = (t) => { tl.seek(t); };
      tl.seek(0);
    </script>
  </body>
</html>
'''

full_html = html_content.replace("__FONT_B64__", font_b64).replace("__GSAP_CODE__", gsap_code)

standalone_path = base_dir / "standalone.html"
index_path = base_dir / "index.html"

standalone_path.write_text(full_html, encoding="utf-8")
index_path.write_text(full_html, encoding="utf-8")

print(f"Generated standalone.html ({len(full_html)/1024:.1f} KB)")
print(f"Generated index.html ({len(full_html)/1024:.1f} KB)")
