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
        background: #F4EFE6; font-family: "Anton", sans-serif;
      }
      #root {
        position: relative; width: 1080px; height: 1920px; overflow: hidden;
        background: #F4EFE6;
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
        filter: drop-shadow(8px 12px 0 rgba(40, 25, 15, 0.18)) drop-shadow(2px 4px 0 rgba(0, 0, 0, 0.08));
      }
      .heavy-cut {
        filter: drop-shadow(12px 18px 0 rgba(40, 25, 15, 0.22)) drop-shadow(3px 6px 0 rgba(0, 0, 0, 0.12));
      }
      #wipe {
        position: absolute; left: 0; top: -190px; width: 1500px; height: 2300px; z-index: 5; pointer-events: none;
      }
      #grain {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 8;
        opacity: 0.09; mix-blend-mode: multiply; pointer-events: none;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' seed='7'/><feColorMatrix values='0 0 0 0 .3 0 0 0 0 .25 0 0 0 0 .2 0 0 0 .9 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");
      }
      #vig {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 9;
        pointer-events: none;
        background: radial-gradient(ellipse at 50% 50%, rgba(244, 239, 230, 0) 65%, rgba(160, 140, 115, 0.35) 100%);
      }
      /* ELEGANT CLASSIC LIGHT-MODE CAPTION CARDS */
      .cap {
        position: absolute; left: 50px; width: 980px; top: 1280px; height: 250px;
        z-index: 10; text-align: center; pointer-events: none;
        opacity: 0;
      }
      .cap span {
        display: inline-block; max-width: 960px; padding: 16px 36px 20px;
        background: #1B1B1B; color: #FAF7F0;
        font-size: 76px; line-height: 1.10; letter-spacing: 1px; text-transform: uppercase;
        border: 4px solid #F4EFE6;
        filter: drop-shadow(8px 12px 0 rgba(40, 25, 15, 0.35));
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
      // PALETTE & TEXTURE HELPERS (LIGHT CLASSIC VINTAGE THEME)
      // ==========================================================
      const P = {
        bg: "#F4EFE6",
        parchment: "#FAF7F0",
        creamCard: "#EFE8DC",
        kraftPaper: "#DBC8AC",
        ink: "#1C1B1A",
        inkSub: "#4A443E",
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
        tape: "rgba(225, 205, 170, 0.7)",
      };

      // PAPER BALL GENERATOR (Realistic papercut seam, highlights, logo stamp)
      function createPaperBall(id, type, size, cx, cy) {
        let baseColor = P.kooRed;
        let brandText = "KOOKABURRA";
        let subText = "TURF • AUS";
        let crestColor = P.ausGold;
        let seamStyle = "low"; // low machine seam
        
        if (type === "sg") {
          baseColor = P.sgMaroon;
          brandText = "SG TEST";
          subText = "HANDMADE • IND";
          crestColor = P.indOrange;
          seamStyle = "high"; // thick pronounced hand seam
        } else if (type === "dukes") {
          baseColor = P.dukesBurgundy;
          brandText = "DUKES";
          subText = "MATCH • ENG";
          crestColor = P.gold;
          seamStyle = "prominent"; // 6-row raised seam
        }

        const r = size / 2;
        // Seam stitch ticks
        let stitches = "";
        const numStitches = 14;
        for (let i = 0; i <= numStitches; i++) {
          const sy = cy - r * 0.82 + (i / numStitches) * (r * 1.64);
          const offset = Math.sin((i / numStitches) * Math.PI) * 4;
          const stitchW = seamStyle === "high" ? 14 : seamStyle === "prominent" ? 18 : 10;
          stitches += `<line x1="${cx - stitchW/2 + offset}" y1="${sy}" x2="${cx + stitchW/2 + offset}" y2="${sy}" stroke="${P.seamWhite}" stroke-width="${seamStyle==='low'?2.5:4}" stroke-linecap="round"/>`;
        }

        return `
          <g id="${id}" class="cut">
            <!-- Paper shadow layer -->
            <ellipse cx="${cx + 8}" cy="${cy + r + 25}" rx="${r * 0.75}" ry="18" fill="rgba(40,25,15,0.22)"/>
            
            <!-- Ball Body Cutout -->
            <circle cx="${cx}" cy="${cy}" r="${r}" fill="${baseColor}" stroke="#3D0B12" stroke-width="4"/>
            <!-- Quarter Panels Crease -->
            <path d="M${cx - r * 0.9} ${cy} C${cx - r * 0.4} ${cy - r * 0.6}, ${cx + r * 0.4} ${cy - r * 0.6}, ${cx + r * 0.9} ${cy}" fill="none" stroke="rgba(0,0,0,0.25)" stroke-width="3" stroke-dasharray="6,4"/>
            <path d="M${cx - r * 0.9} ${cy} C${cx - r * 0.4} ${cy + r * 0.6}, ${cx + r * 0.4} ${cy + r * 0.6}, ${cx + r * 0.9} ${cy}" fill="none" stroke="rgba(0,0,0,0.25)" stroke-width="3" stroke-dasharray="6,4"/>

            <!-- Main Central Seam -->
            <path d="M${cx} ${cy - r + 3} Q${cx + 8} ${cy} ${cx} ${cy + r - 3}" fill="none" stroke="${seamStyle==='prominent'?'#F7F2E7':'#E5DFD0'}" stroke-width="${seamStyle==='low'?7:seamStyle==='high'?10:13}" stroke-linecap="round"/>
            <path d="M${cx} ${cy - r + 3} Q${cx + 8} ${cy} ${cx} ${cy + r - 3}" fill="none" stroke="rgba(0,0,0,0.3)" stroke-width="2"/>
            ${stitches}

            <!-- Leather Gloss & Paper Texture Highlight -->
            <path d="M${cx - r * 0.6} ${cy - r * 0.65} A${r * 0.85} ${r * 0.85} 0 0 1 ${cx - r * 0.1} ${cy - r * 0.85}" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="8" stroke-linecap="round"/>
            <circle cx="${cx - r * 0.45}" cy="${cy - r * 0.5}" r="7" fill="rgba(255,255,255,0.6)"/>

            <!-- Gold Embossed Brand Crest Stamp -->
            <g transform="translate(${cx - 85}, ${cy - 38})">
              <rect x="0" y="0" width="170" height="76" rx="8" fill="rgba(25,10,12,0.4)" stroke="${crestColor}" stroke-width="2" stroke-dasharray="4,2"/>
              <text x="85" y="32" fill="${crestColor}" font-size="22" font-family="Anton" text-anchor="middle" letter-spacing="2">${brandText}</text>
              <text x="85" y="58" fill="#F4EFE6" font-size="16" font-family="Anton" text-anchor="middle" letter-spacing="3">${subText}</text>
            </g>
          </g>
        `;
      }

      // KRAFT PAPER CARD COMPONENT
      function createPaperCard(id, x, y, w, h, bg, borderCol, rotate=0) {
        return `
          <g id="${id}" class="cut" transform="translate(${x},${y}) rotate(${rotate})">
            <!-- Torn tape pieces on top-left and top-right -->
            <rect x="25" y="-14" width="70" height="28" fill="${P.tape}" transform="rotate(-6 60 0)" rx="2"/>
            <rect x="${w - 95}" y="-14" width="70" height="28" fill="${P.tape}" transform="rotate(7 ${w-60} 0)" rx="2"/>
            <!-- Main paper card -->
            <rect x="0" y="0" width="${w}" height="${h}" rx="14" fill="${bg}" stroke="${borderCol}" stroke-width="4"/>
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
            <path d="M-50 -50 L1550 -50 L1550 2000 L1400 2060 L1250 1980 L1100 2080 L950 2000 L800 2090 L650 2010 L500 2100 L350 2020 L200 2110 L50 2030 L-50 2120 Z" fill="${P.creamCard}" stroke="${P.ink}" stroke-width="6"/>
          </g>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 1: THE HOOK (0.00 - 7.50s)
      // ----------------------------------------------------------
      s1.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <!-- Background Grid / Graph Paper -->
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(180, 160, 135, 0.22)" stroke-width="1.5"/>
          </pattern>
          <rect width="1080" height="1920" fill="${P.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid)"/>

          <!-- Top Banner Tag -->
          <g id="s1_tag" class="cut" transform="translate(190, 120)">
            <rect x="0" y="0" width="700" height="85" rx="10" fill="#2C2523" stroke="#FAF7F0" stroke-width="3"/>
            <text x="350" y="56" fill="#FAF7F0" font-size="40" font-family="Anton" text-anchor="middle" letter-spacing="4">TEST CRICKET'S SECRET VARIABLE</text>
          </g>

          <!-- Headline Banner Card -->
          <g id="s1_title" class="heavy-cut" transform="translate(80, 240)">
            <rect x="0" y="0" width="920" height="260" rx="18" fill="${P.parchment}" stroke="${P.ink}" stroke-width="5"/>
            <!-- Stitched outline -->
            <rect x="14" y="14" width="892" height="232" rx="10" fill="none" stroke="${P.stampRed}" stroke-width="2.5" stroke-dasharray="10,6"/>
            <text x="460" y="95" fill="${P.ink}" font-size="64" font-family="Anton" text-anchor="middle">AUSTRALIA • INDIA • ENGLAND</text>
            <text x="460" y="175" fill="${P.stampRed}" font-size="78" font-family="Anton" text-anchor="middle">DON'T PLAY WITH THE SAME BALL!</text>
            <text x="460" y="228" fill="${P.inkSub}" font-size="34" font-family="Anton" text-anchor="middle" letter-spacing="3">THREE RED LEATHERS • THREE DIFFERENT GAMES</text>
          </g>

          <!-- 3 Balls Trio Hero Display -->
          <g id="s1_trio" transform="translate(0, 0)">
            <!-- Ball 1: Kookaburra -->
            <g id="s1_ball_koo">
              ${createPaperBall("s1_ball1", "koo", 280, 220, 770)}
              <g class="cut" transform="translate(110, 950)">
                <rect x="0" y="0" width="220" height="60" rx="8" fill="${P.ausGreen}" stroke="${P.seamWhite}" stroke-width="2"/>
                <text x="110" y="42" fill="${P.ausGold}" font-size="28" font-family="Anton" text-anchor="middle">KOOKABURRA (AUS)</text>
              </g>
            </g>

            <!-- Ball 2: SG -->
            <g id="s1_ball_sg">
              ${createPaperBall("s1_ball2", "sg", 280, 540, 750)}
              <g class="cut" transform="translate(430, 930)">
                <rect x="0" y="0" width="220" height="60" rx="8" fill="${P.indNavy}" stroke="${P.seamWhite}" stroke-width="2"/>
                <text x="110" y="42" fill="#FAF7F0" font-size="28" font-family="Anton" text-anchor="middle">SG (INDIA)</text>
              </g>
            </g>

            <!-- Ball 3: Dukes -->
            <g id="s1_ball_dukes">
              ${createPaperBall("s1_ball3", "dukes", 280, 860, 770)}
              <g class="cut" transform="translate(750, 950)">
                <rect x="0" y="0" width="220" height="60" rx="8" fill="${P.dukesBurgundy}" stroke="${P.seamWhite}" stroke-width="2"/>
                <text x="110" y="42" fill="${P.gold}" font-size="28" font-family="Anton" text-anchor="middle">DUKES (ENG)</text>
              </g>
            </g>
          </g>

          <!-- Giant Rubber Stamp: "CHANGES EVERYTHING!" -->
          <g id="s1_stamp" class="heavy-cut" transform="translate(180, 1070) rotate(-7)">
            <rect x="0" y="0" width="720" height="140" rx="14" fill="${P.stampRed}" stroke="#4A050B" stroke-width="6"/>
            <rect x="10" y="10" width="700" height="120" rx="8" fill="none" stroke="#FAF7F0" stroke-width="3" stroke-dasharray="12,6"/>
            <text x="360" y="92" fill="#FAF7F0" font-size="78" font-family="Anton" text-anchor="middle" letter-spacing="4">CHANGES EVERYTHING!</text>
          </g>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 2: THE BIG THREE (7.50 - 14.10s)
      // ----------------------------------------------------------
      s2.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${P.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid)"/>

          <!-- Top Scene Header -->
          <g id="s2_header" class="cut" transform="translate(140, 110)">
            <rect x="0" y="0" width="800" height="90" rx="10" fill="${P.ink}" stroke="${P.bg}" stroke-width="3"/>
            <text x="400" y="60" fill="#FAF7F0" font-size="46" font-family="Anton" text-anchor="middle" letter-spacing="3">THE THREE TITANS OF TEST CRICKET</text>
          </g>

          <!-- 3 Staggered Ball Showcase Cards -->
          <!-- 1. AUSTRALIA KOOKABURRA -->
          <g id="s2_card_koo" class="heavy-cut" transform="translate(70, 240)">
            <rect x="0" y="0" width="940" height="300" rx="16" fill="${P.parchment}" stroke="${P.ausGreen}" stroke-width="5"/>
            <rect x="12" y="12" width="220" height="276" rx="10" fill="${P.ausGreen}"/>
            <!-- Flag Badge -->
            <text x="122" y="155" fill="${P.ausGold}" font-size="64" font-family="Anton" text-anchor="middle">🇦🇺 AUS</text>
            <!-- Ball Mini Graphic -->
            ${createPaperBall("s2_mini_koo", "koo", 180, 360, 150)}
            <!-- Specs Text -->
            <text x="480" y="90" fill="${P.ink}" font-size="64" font-family="Anton">KOOKABURRA TURF</text>
            <text x="480" y="150" fill="${P.ausGreen}" font-size="34" font-family="Anton">MACHINE STITCHED • LOW EMBEDDED SEAM</text>
            <text x="480" y="210" fill="${P.inkSub}" font-size="30" font-family="Anton">AUSTRALIA, SOUTH AFRICA, NEW ZEALAND</text>
            <rect x="480" y="235" width="410" height="40" rx="6" fill="#E8F5E9"/>
            <text x="685" y="263" fill="${P.ausGreen}" font-size="24" font-family="Anton" text-anchor="middle">SWINGS FAST FOR 15-20 OVERS</text>
          </g>

          <!-- 2. INDIA SG -->
          <g id="s2_card_sg" class="heavy-cut" transform="translate(70, 580)">
            <rect x="0" y="0" width="940" height="300" rx="16" fill="${P.parchment}" stroke="${P.indNavy}" stroke-width="5"/>
            <rect x="12" y="12" width="220" height="276" rx="10" fill="${P.indNavy}"/>
            <text x="122" y="155" fill="${P.indOrange}" font-size="64" font-family="Anton" text-anchor="middle">🇮🇳 IND</text>
            ${createPaperBall("s2_mini_sg", "sg", 180, 360, 150)}
            <text x="480" y="90" fill="${P.ink}" font-size="64" font-family="Anton">SG TEST (SANSPAREILS)</text>
            <text x="480" y="150" fill="${P.sgMaroon}" font-size="34" font-family="Anton">PROMINENT HAND SEAM • THICK THREAD</text>
            <text x="480" y="210" fill="${P.inkSub}" font-size="30" font-family="Anton">EXCLUSIVELY USED IN INDIAN CONDITIONS</text>
            <rect x="480" y="235" width="410" height="40" rx="6" fill="#FFF3E0"/>
            <text x="685" y="263" fill="${P.sgMaroon}" font-size="24" font-family="Anton" text-anchor="middle">SPIN GRIP & DESTRUCTIVE REVERSE SWING</text>
          </g>

          <!-- 3. ENGLAND DUKES -->
          <g id="s2_card_dukes" class="heavy-cut" transform="translate(70, 920)">
            <rect x="0" y="0" width="940" height="300" rx="16" fill="${P.parchment}" stroke="${P.dukesBurgundy}" stroke-width="5"/>
            <rect x="12" y="12" width="220" height="276" rx="10" fill="${P.dukesBurgundy}"/>
            <text x="122" y="155" fill="${P.gold}" font-size="64" font-family="Anton" text-anchor="middle">🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG</text>
            ${createPaperBall("s2_mini_dukes", "dukes", 180, 360, 150)}
            <text x="480" y="90" fill="${P.ink}" font-size="64" font-family="Anton">DUKES SPECIAL MATCH</text>
            <text x="480" y="150" fill="${P.dukesBurgundy}" font-size="34" font-family="Anton">RAISED 6-ROW SEAM • GREASE LACQUER</text>
            <text x="480" y="210" fill="${P.inkSub}" font-size="30" font-family="Anton">ENGLAND & WEST INDIES TEST MATCHES</text>
            <rect x="480" y="235" width="410" height="40" rx="6" fill="#FCE4EC"/>
            <text x="685" y="263" fill="${P.dukesBurgundy}" font-size="24" font-family="Anton" text-anchor="middle">SWINGS & NIPS OFF SEAM FOR 60+ OVERS</text>
          </g>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 3: PHYSICS & HOME ADVANTAGE (14.10 - 29.40s)
      // ----------------------------------------------------------
      s3.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${P.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid)"/>

          <!-- Official ICC Rule Seal Card -->
          <g id="s3_rule_card" class="heavy-cut" transform="translate(80, 120)">
            <rect x="0" y="0" width="920" height="180" rx="14" fill="${P.parchment}" stroke="${P.stampRed}" stroke-width="5"/>
            <text x="460" y="65" fill="${P.stampRed}" font-size="44" font-family="Anton" text-anchor="middle">ICC STANDARD TEST REGULATIONS</text>
            <text x="460" y="135" fill="${P.ink}" font-size="62" font-family="Anton" text-anchor="middle">"THE HOST BOARD CHOOSES THE BALL"</text>
          </g>

          <!-- Why Visitors Struggle Stamp -->
          <g id="s3_struggle_stamp" class="cut" transform="translate(190, 320) rotate(3)">
            <rect x="0" y="0" width="700" height="85" rx="10" fill="${P.ink}" stroke="#F4EFE6" stroke-width="3"/>
            <text x="350" y="58" fill="#FFB703" font-size="42" font-family="Anton" text-anchor="middle" letter-spacing="3">THAT'S WHY TOURING TEAMS GET AMBUSHED!</text>
          </g>

          <!-- Physics Comparison Section: 3 Ball Mechanics in Action -->
          <!-- 1. Kookaburra Flattens -->
          <g id="s3_mech_koo" class="heavy-cut" transform="translate(70, 440)">
            <rect x="0" y="0" width="940" height="235" rx="14" fill="${P.creamCard}" stroke="${P.ausGreen}" stroke-width="4"/>
            ${createPaperBall("s3_b1", "koo", 150, 120, 118)}
            <text x="220" y="65" fill="${P.ausGreen}" font-size="48" font-family="Anton">KOOKABURRA: FAST WEAR-OUT</text>
            <text x="220" y="115" fill="${P.ink}" font-size="34" font-family="Anton">Fierce bounce & swing in first 15-20 overs.</text>
            <!-- Graphic Meter -->
            <rect x="220" y="140" width="670" height="34" rx="6" fill="#DDD2BE"/>
            <rect x="220" y="140" width="220" height="34" rx="6" fill="${P.ausGold}"/>
            <text x="235" y="165" fill="${P.ink}" font-size="20" font-family="Anton">OVERS 1-20 (DANGEROUS)</text>
            <text x="560" y="165" fill="${P.inkSub}" font-size="20" font-family="Anton">OVERS 21-80: SEAM GOES SOFT & FLATTENS</text>
            <text x="220" y="210" fill="${P.stampRed}" font-size="26" font-family="Anton">➜ Batters cash in once ball is soft!</text>
          </g>

          <!-- 2. SG Reverse Swing Monster -->
          <g id="s3_mech_sg" class="heavy-cut" transform="translate(70, 700)">
            <rect x="0" y="0" width="940" height="235" rx="14" fill="${P.creamCard}" stroke="${P.sgMaroon}" stroke-width="4"/>
            ${createPaperBall("s3_b2", "sg", 150, 120, 118)}
            <text x="220" y="65" fill="${P.sgMaroon}" font-size="48" font-family="Anton">SG: THE TURNING & REVERSING BEAST</text>
            <text x="220" y="115" fill="${P.ink}" font-size="34" font-family="Anton">Pronounced seam stays upright on dust tracks.</text>
            <!-- Graphic Meter -->
            <rect x="220" y="140" width="670" height="34" rx="6" fill="#DDD2BE"/>
            <rect x="420" y="140" width="470" height="34" rx="6" fill="${P.sgMaroon}"/>
            <text x="235" y="165" fill="${P.inkSub}" font-size="20" font-family="Anton">SPINNER GRIP</text>
            <text x="560" y="165" fill="#FAF7F0" font-size="20" font-family="Anton">OVERS 30-80: DEADLY REVERSE SWING!</text>
            <text x="220" y="210" fill="${P.indNavy}" font-size="26" font-family="Anton">➜ Indian pacers & spinners dominate visiting bats!</text>
          </g>

          <!-- 3. Dukes English Swing Engine -->
          <g id="s3_mech_dukes" class="heavy-cut" transform="translate(70, 960)">
            <rect x="0" y="0" width="940" height="235" rx="14" fill="${P.creamCard}" stroke="${P.dukesBurgundy}" stroke-width="4"/>
            ${createPaperBall("s3_b3", "dukes", 150, 120, 118)}
            <text x="220" y="65" fill="${P.dukesBurgundy}" font-size="48" font-family="Anton">DUKES: NEVER STOPS MOVING</text>
            <text x="220" y="115" fill="${P.ink}" font-size="34" font-family="Anton">Hand-stitched spine + grease wax stays rock-hard.</text>
            <!-- Graphic Meter -->
            <rect x="220" y="140" width="670" height="34" rx="6" fill="${P.dukesBurgundy}"/>
            <text x="460" y="165" fill="${P.gold}" font-size="20" font-family="Anton" text-anchor="middle">SWING & SEAM LASTS 60-70+ OVERS NON-STOP</text>
            <text x="220" y="210" fill="${P.stampRed}" font-size="26" font-family="Anton">➜ Visiting openers get sliced in English mist!</text>
          </g>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 4: WHAT IF ONE BALL? (29.40 - 44.20s)
      // ----------------------------------------------------------
      s4.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${P.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid)"/>

          <!-- Thought Bubble Card -->
          <g id="s4_question_card" class="heavy-cut" transform="translate(80, 120)">
            <rect x="0" y="0" width="920" height="200" rx="16" fill="${P.parchment}" stroke="${P.ink}" stroke-width="5"/>
            <!-- Stitched banner -->
            <rect x="12" y="12" width="896" height="176" rx="10" fill="none" stroke="${P.goldDark}" stroke-width="2.5" stroke-dasharray="10,6"/>
            <text x="460" y="75" fill="${P.inkSub}" font-size="38" font-family="Anton" text-anchor="middle">WHAT IF THE ICC STANDARDIZED EVERYTHING?</text>
            <text x="460" y="150" fill="${P.stampRed}" font-size="70" font-family="Anton" text-anchor="middle">WHAT IF CRICKET USED ONLY ONE BALL?</text>
          </g>

          <!-- Balance Scale Graphic -->
          <g id="s4_balance" class="cut" transform="translate(90, 350)">
            <!-- Left Pan: Visiting Batters -->
            <g id="s4_pan_left" class="cut" transform="translate(0, 0)">
              <rect x="0" y="0" width="430" height="280" rx="14" fill="${P.creamCard}" stroke="${P.ink}" stroke-width="4"/>
              <rect x="0" y="0" width="430" height="60" rx="10" fill="#E8F5E9"/>
              <text x="215" y="42" fill="#2E7D32" font-size="30" font-family="Anton" text-anchor="middle">PRO: FAIR TOURING</text>
              <text x="215" y="125" fill="${P.ink}" font-size="44" font-family="Anton" text-anchor="middle">BATTERS WON'T BE</text>
              <text x="215" y="180" fill="${P.stampRed}" font-size="52" font-family="Anton" text-anchor="middle">BLINDSIDED!</text>
              <text x="215" y="240" fill="${P.inkSub}" font-size="26" font-family="Anton" text-anchor="middle">No sudden unfamiliar seam</text>
            </g>

            <!-- Right Pan: Home Advantage Shrinks -->
            <g id="s4_pan_right" class="cut" transform="translate(470, 0)">
              <rect x="0" y="0" width="430" height="280" rx="14" fill="${P.creamCard}" stroke="${P.ink}" stroke-width="4"/>
              <rect x="0" y="0" width="430" height="60" rx="10" fill="#FFF3E0"/>
              <text x="215" y="42" fill="#E65100" font-size="30" font-family="Anton" text-anchor="middle">CON: REDUCED EDGE</text>
              <text x="215" y="125" fill="${P.ink}" font-size="44" font-family="Anton" text-anchor="middle">HOME ADVANTAGE</text>
              <text x="215" y="180" fill="${P.indNavy}" font-size="52" font-family="Anton" text-anchor="middle">WOULD SHRINK!</text>
              <text x="215" y="240" fill="${P.inkSub}" font-size="26" font-family="Anton" text-anchor="middle">Familiarity everywhere</text>
            </g>
          </g>

          <!-- Pitch & Weather Postcard -->
          <g id="s4_pitch_card" class="heavy-cut" transform="translate(80, 670)">
            <rect x="0" y="0" width="920" height="240" rx="16" fill="${P.parchment}" stroke="${P.ink}" stroke-width="4"/>
            <text x="460" y="65" fill="${P.ink}" font-size="44" font-family="Anton" text-anchor="middle">BUT DON'T FORGET THE REAL DECIDERS:</text>
            <text x="460" y="135" fill="${P.goldDark}" font-size="62" font-family="Anton" text-anchor="middle">PITCHES & WEATHER STILL RULE!</text>
            <text x="460" y="195" fill="${P.inkSub}" font-size="30" font-family="Anton" text-anchor="middle">English clouds • Perth cracks • Chennai dust will still bite!</text>
          </g>

          <!-- Soul of Cricket Certificate -->
          <g id="s4_soul_card" class="heavy-cut" transform="translate(80, 940)">
            <rect x="0" y="0" width="920" height="240" rx="16" fill="#2C2523" stroke="${P.gold}" stroke-width="5"/>
            <rect x="12" y="12" width="896" height="216" rx="10" fill="none" stroke="${P.gold}" stroke-width="2" stroke-dasharray="8,6"/>
            <text x="460" y="80" fill="${P.gold}" font-size="42" font-family="Anton" text-anchor="middle" letter-spacing="3">TRADITION & CHARM</text>
            <text x="460" y="150" fill="#FAF7F0" font-size="62" font-family="Anton" text-anchor="middle">"THE BALL IS CRICKET'S CHARACTER!"</text>
            <text x="460" y="202" fill="#E0D7CC" font-size="28" font-family="Anton" text-anchor="middle">Each ball tells the story of the land it was forged in.</text>
          </g>
        </svg>
      `;

      // ----------------------------------------------------------
      // SCENE 5: THE BIG VERDICT & CTA (44.20 - 49.95s)
      // ----------------------------------------------------------
      s5.innerHTML = `
        <svg viewBox="0 0 1080 1920" width="1080" height="1920">
          <rect width="1080" height="1920" fill="${P.bg}"/>
          <rect width="1080" height="1920" fill="url(#grid)"/>

          <!-- Top Question Banner -->
          <g id="s5_vote_title" class="heavy-cut" transform="translate(80, 140)">
            <rect x="0" y="0" width="920" height="180" rx="14" fill="${P.parchment}" stroke="${P.ink}" stroke-width="5"/>
            <text x="460" y="70" fill="${P.stampRed}" font-size="44" font-family="Anton" text-anchor="middle">WHAT IS YOUR VERDICT?</text>
            <text x="460" y="140" fill="${P.ink}" font-size="66" font-family="Anton" text-anchor="middle">SHOULD TEST CRICKET USE ONE BALL?</text>
          </g>

          <!-- Option 1: ONE BALL EVERYWHERE -->
          <g id="s5_btn_one" class="heavy-cut" transform="translate(80, 360)">
            <rect x="0" y="0" width="920" height="240" rx="16" fill="${P.creamCard}" stroke="${P.indNavy}" stroke-width="5"/>
            <!-- Stamped circle -->
            <circle cx="120" cy="120" r="70" fill="${P.indNavy}"/>
            <text x="120" y="138" fill="#FAF7F0" font-size="52" font-family="Anton" text-anchor="middle">A</text>
            <text x="240" y="95" fill="${P.indNavy}" font-size="62" font-family="Anton">ONE BALL EVERYWHERE</text>
            <text x="240" y="155" fill="${P.ink}" font-size="34" font-family="Anton">Standardize one global brand (Fairer Tests)</text>
            <rect x="240" y="180" width="220" height="36" rx="6" fill="${P.indNavy}"/>
            <text x="350" y="206" fill="#FAF7F0" font-size="22" font-family="Anton" text-anchor="middle">UNIFIED RULES</text>
          </g>

          <!-- Option 2: KEEP THE CHAOS -->
          <g id="s5_btn_chaos" class="heavy-cut" transform="translate(80, 640)">
            <rect x="0" y="0" width="920" height="240" rx="16" fill="${P.creamCard}" stroke="${P.stampRed}" stroke-width="5"/>
            <circle cx="120" cy="120" r="70" fill="${P.stampRed}"/>
            <text x="120" y="138" fill="#FAF7F0" font-size="52" font-family="Anton" text-anchor="middle">B</text>
            <text x="240" y="95" fill="${P.stampRed}" font-size="62" font-family="Anton">KEEP THE CHAOS!</text>
            <text x="240" y="155" fill="${P.ink}" font-size="34" font-family="Anton">Preserve heritage, pitch quirks & craft</text>
            <rect x="240" y="180" width="220" height="36" rx="6" fill="${P.stampRed}"/>
            <text x="350" y="206" fill="#FAF7F0" font-size="22" font-family="Anton" text-anchor="middle">PURE TRADITION</text>
          </g>

          <!-- Interactive Voting Card -->
          <g id="s5_cta_card" class="heavy-cut" transform="translate(80, 930)">
            <rect x="0" y="0" width="920" height="250" rx="16" fill="#2C2523" stroke="${P.gold}" stroke-width="5"/>
            <rect x="14" y="14" width="892" height="222" rx="10" fill="none" stroke="${P.gold}" stroke-width="2.5" stroke-dasharray="10,6"/>
            <!-- Pulsing pointer indicator -->
            <polygon points="460,50 490,95 430,95" fill="${P.gold}"/>
            <text x="460" y="145" fill="#FAF7F0" font-size="62" font-family="Anton" text-anchor="middle">COMMENT: A OR B?</text>
            <text x="460" y="205" fill="${P.gold}" font-size="38" font-family="Anton" text-anchor="middle" letter-spacing="3">WHICH CRICKET BALL IS YOUR FAVORITE?</text>
          </g>
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

      sceneList.forEach((sc, i) => {
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
      tl.from("#s1_tag", { y: -120, opacity: 0, duration: 0.5, ease: "back.out(2)" }, 0.08);
      tl.from("#s1_title", { scale: 0.75, opacity: 0, duration: 0.6, ease: "back.out(1.8)" }, 0.25);
      // Trio balls drop in with authentic stop-motion stagger
      tl.from("#s1_ball_koo", { y: -600, rotation: -25, duration: 0.7, ease: "bounce.out" }, 0.55);
      tl.from("#s1_ball_sg", { y: -600, rotation: 15, duration: 0.7, ease: "bounce.out" }, 0.75);
      tl.from("#s1_ball_dukes", { y: -600, rotation: -18, duration: 0.7, ease: "bounce.out" }, 0.95);

      // Subtle float oscillation
      tl.to("#s1_ball_koo", { y: "-=18", rotation: "+=3", duration: 1.8, yoyo: true, repeat: 2, ease: "sine.inOut" }, 1.30);
      tl.to("#s1_ball_sg", { y: "-=22", rotation: "-=4", duration: 1.6, yoyo: true, repeat: 2, ease: "sine.inOut" }, 1.40);
      tl.to("#s1_ball_dukes", { y: "-=16", rotation: "+=3", duration: 1.7, yoyo: true, repeat: 2, ease: "sine.inOut" }, 1.50);

      // Stamp SLAM
      tl.fromTo("#s1_stamp", { scale: 2.8, opacity: 0, rotation: -25 }, { scale: 1, opacity: 1, rotation: -7, duration: 0.35, ease: "power4.in" }, 5.05);
      tl.to("#s1 .cam", { scale: 1.03, y: 15, duration: 0.12, yoyo: true, repeat: 1 }, 5.40);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 2 (7.50s - 14.10s)
      // ----------------------------------------------------------
      tl.from("#s2_header", { y: -80, opacity: 0, duration: 0.45, ease: "back.out(1.8)" }, 7.55);
      // Card 1: Kookaburra
      tl.from("#s2_card_koo", { x: -800, rotation: -8, opacity: 0, duration: 0.55, ease: "back.out(1.6)" }, 7.80);
      tl.from("#s2_mini_koo", { rotation: -180, scale: 0.5, duration: 0.55, ease: "back.out(2)" }, 8.05);

      // Card 2: SG
      tl.from("#s2_card_sg", { x: 800, rotation: 8, opacity: 0, duration: 0.55, ease: "back.out(1.6)" }, 9.95);
      tl.from("#s2_mini_sg", { rotation: 180, scale: 0.5, duration: 0.55, ease: "back.out(2)" }, 10.20);

      // Card 3: Dukes
      tl.from("#s2_card_dukes", { x: -800, rotation: -8, opacity: 0, duration: 0.55, ease: "back.out(1.6)" }, 12.05);
      tl.from("#s2_mini_dukes", { rotation: -180, scale: 0.5, duration: 0.55, ease: "back.out(2)" }, 12.30);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 3 (14.10s - 29.40s)
      // ----------------------------------------------------------
      tl.from("#s3_rule_card", { scale: 0.8, opacity: 0, duration: 0.5, ease: "back.out(1.8)" }, 14.15);
      tl.fromTo("#s3_struggle_stamp", { scale: 2.2, opacity: 0, rotation: 18 }, { scale: 1, opacity: 1, rotation: 3, duration: 0.4, ease: "power4.in" }, 17.65);
      tl.to("#s3 .cam", { scale: 1.025, y: -10, duration: 0.12, yoyo: true, repeat: 1 }, 17.95);

      // Kookaburra breakdown
      tl.from("#s3_mech_koo", { x: -750, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 19.85);
      tl.from("#s3_b1", { scale: 0.3, rotation: -90, duration: 0.4, ease: "back.out(2)" }, 20.10);

      // SG breakdown
      tl.from("#s3_mech_sg", { x: 750, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 22.75);
      tl.from("#s3_b2", { scale: 0.3, rotation: 90, duration: 0.4, ease: "back.out(2)" }, 23.00);

      // Dukes breakdown
      tl.from("#s3_mech_dukes", { x: -750, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 26.60);
      tl.from("#s3_b3", { scale: 0.3, rotation: -90, duration: 0.4, ease: "back.out(2)" }, 26.85);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 4 (29.40s - 44.20s)
      // ----------------------------------------------------------
      tl.from("#s4_question_card", { scale: 0.75, opacity: 0, duration: 0.55, ease: "back.out(2)" }, 29.45);
      // Balance Scale Left/Right
      tl.from("#s4_pan_left", { x: -350, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 32.25);
      tl.from("#s4_pan_right", { x: 350, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 35.25);
      // Tilting scale animation
      tl.to("#s4_pan_left", { y: -15, duration: 1.2, yoyo: true, repeat: 1, ease: "sine.inOut" }, 33.00);
      tl.to("#s4_pan_right", { y: 15, duration: 1.2, yoyo: true, repeat: 1, ease: "sine.inOut" }, 33.00);

      // Pitches & Weather
      tl.from("#s4_pitch_card", { y: 120, opacity: 0, duration: 0.5, ease: "power2.out" }, 37.25);

      // Soul Card
      tl.from("#s4_soul_card", { scale: 0.85, opacity: 0, duration: 0.55, ease: "back.out(1.8)" }, 41.75);

      // ----------------------------------------------------------
      // ANIMATION: SCENE 5 (44.20s - 49.95s)
      // ----------------------------------------------------------
      tl.from("#s5_vote_title", { y: -80, opacity: 0, duration: 0.4, ease: "back.out(1.8)" }, 44.25);
      tl.from("#s5_btn_one", { x: -600, opacity: 0, duration: 0.45, ease: "back.out(1.7)" }, 44.40);
      tl.from("#s5_btn_chaos", { x: 600, opacity: 0, duration: 0.45, ease: "back.out(1.7)" }, 47.25);
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

      // EXPOSE INTERFACES FOR SCRIPTS AND FAST_RENDER
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
