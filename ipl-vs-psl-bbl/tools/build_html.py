import base64
from pathlib import Path

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\ipl-vs-psl-bbl")
font_path = base / "assets" / "fonts" / "Anton-Regular.ttf"
font_b64 = base64.b64encode(font_path.read_bytes()).decode("ascii")

gsap_path = base / "assets" / "gsap.min.js"
gsap_code = gsap_path.read_text(encoding="utf-8")

def get_html(inline_gsap=True):
    gsap_script = f"<script>{gsap_code}</script>" if inline_gsap else '<script src="assets/gsap.min.js"></script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>IPL vs PSL vs BBL - The Cricket Economy</title>
  {gsap_script}
  <style>
    @font-face {{
      font-family: 'Anton';
      src: url(data:font/ttf;base64,{font_b64}) format('truetype');
      font-weight: 400;
      font-style: normal;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      width: 1080px; height: 1920px;
      overflow: hidden;
      background: #F4EBD9;
      font-family: 'Anton', Impact, sans-serif;
      -webkit-font-smoothing: antialiased;
    }}
    #root {{
      position: relative;
      width: 1080px; height: 1920px;
      overflow: hidden;
      background: #F4EBD9;
    }}

    /* Paper Cutout Drop Shadows */
    .cut {{
      filter: drop-shadow(8px 11px 0 rgba(0, 0, 0, 0.28));
    }}
    .cut-lg {{
      filter: drop-shadow(12px 15px 0 rgba(0, 0, 0, 0.32));
    }}
    .cut-sm {{
      filter: drop-shadow(5px 7px 0 rgba(0, 0, 0, 0.22));
    }}

    /* Real Paper Grain Overlay */
    #grain {{
      position: absolute; left: 0; top: 0; width: 1080px; height: 1920px;
      pointer-events: none; z-index: 90;
      opacity: 0.25; mix-blend-mode: multiply;
      background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.75' numOctaves='3' seed='19'/><feColorMatrix values='0 0 0 0 .35 0 0 0 0 .3 0 0 0 0 .25 0 0 0 .9 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");
    }}

    /* Subtle Paper Vignette */
    #vignette {{
      position: absolute; left: 0; top: 0; width: 1080px; height: 1920px;
      pointer-events: none; z-index: 91;
      background: radial-gradient(ellipse at 50% 50%, rgba(0, 0, 0, 0) 62%, rgba(50, 35, 15, 0.22) 100%);
    }}

    /* Fullscreen Scene Containers */
    .scene {{
      position: absolute; left: 0; top: 0; width: 1080px; height: 1920px;
      overflow: hidden;
      opacity: 0; visibility: hidden;
    }}
    .scene svg {{
      position: absolute; left: 0; top: 0; width: 1080px; height: 1920px;
      display: block;
    }}

    /* Standardized Perfect Subtitle Caption Box */
    #captions-box {{
      position: absolute;
      left: 60px;
      top: 1420px;
      width: 960px;
      height: 220px;
      z-index: 80;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: none;
    }}
    .cap-strip {{
      display: inline-block;
      max-width: 920px;
      padding: 16px 36px 20px;
      background: #FAF8F2;
      color: #1B1B1B;
      font-size: 52px;
      line-height: 1.15;
      text-align: center;
      text-transform: uppercase;
      letter-spacing: 1px;
      filter: drop-shadow(8px 11px 0 rgba(0, 0, 0, 0.30));
      border: 3px solid #1B1B1B;
      border-radius: 4px;
    }}
    .cap-strip b {{
      color: #C1121F;
      font-weight: 400;
    }}
    .cap-strip i {{
      font-style: normal;
      background: #E3B23C;
      color: #1B1B1B;
      padding: 2px 10px;
      border-radius: 3px;
    }}
    .cap-strip u {{
      text-decoration: none;
      color: #165B33;
    }}
    .cap-strip .blue {{
      color: #0A2240;
    }}
  </style>
</head>
<body>
  <div id="root">
    <!-- ============================================================ -->
    <!-- SCENE 1: HOOK (Three Leagues & 9X Gap) -->
    <!-- ============================================================ -->
    <div id="s1" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <rect width="1080" height="1920" fill="#F5EEDB"/>
        <!-- Background paper sunburst -->
        <g opacity="0.12">
          <polygon points="540,750 0,0 200,0" fill="#D9C9A8"/>
          <polygon points="540,750 400,0 600,0" fill="#D9C9A8"/>
          <polygon points="540,750 800,0 1080,0" fill="#D9C9A8"/>
          <polygon points="540,750 1080,300 1080,500" fill="#D9C9A8"/>
          <polygon points="540,750 1080,800 1080,1100" fill="#D9C9A8"/>
          <polygon points="540,750 800,1500 1080,1500" fill="#D9C9A8"/>
          <polygon points="540,750 300,1500 600,1500" fill="#D9C9A8"/>
          <polygon points="540,750 0,1500 200,1500" fill="#D9C9A8"/>
          <polygon points="540,750 0,800 0,1100" fill="#D9C9A8"/>
          <polygon points="540,750 0,300 0,500" fill="#D9C9A8"/>
        </g>

        <!-- Top Scene Header Badge -->
        <g transform="translate(540, 220)">
          <g id="s1_header" class="cut">
            <polygon points="-385,-48 385,-44 378,48 -382,45" fill="#1B1B1B"/>
            <rect x="-365" y="-36" width="730" height="72" fill="#E3B23C"/>
            <text x="0" y="16" font-size="44" fill="#1B1B1B" text-anchor="middle" letter-spacing="3">CRICKET FINANCE COMPARISON</text>
          </g>
        </g>

        <!-- Center 3 League Cards -->
        <g id="s1_cards">
          <!-- Card 1: IPL -->
          <g transform="translate(230, 680) rotate(-6)">
            <g id="s1_card_ipl" class="cut">
              <polygon points="-142,-232 142,-236 144,232 -140,236" fill="#FAF8F2"/>
              <rect x="-125" y="-215" width="250" height="340" fill="#0A2240"/>
              <polygon points="0,-185 75,-145 75,-50 0,30 -75,-50 -75,-145" fill="#E3B23C"/>
              <polygon points="0,-172 62,-137 62,-55 0,18 -62,-55 -62,-137" fill="#0A2240"/>
              <circle cx="0" cy="-90" r="38" fill="#E3B23C"/>
              <text x="0" y="-76" font-size="40" fill="#0A2240" text-anchor="middle">IPL</text>
              <text x="0" y="-25" font-size="24" fill="#E3B23C" text-anchor="middle" letter-spacing="2">INDIA</text>
              <rect x="-125" y="135" width="250" height="85" fill="#FAF8F2"/>
              <text x="0" y="174" font-size="34" fill="#0A2240" text-anchor="middle">THE GIANT</text>
              <text x="0" y="204" font-size="22" fill="#888888" text-anchor="middle">EST. 2008</text>
              <polygon points="-130,-240 -80,-245 -65,-215 -115,-210" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
            </g>
          </g>

          <!-- Card 2: PSL -->
          <g transform="translate(540, 660)">
            <g id="s1_card_psl" class="cut">
              <polygon points="-142,-236 142,-232 140,236 -144,232" fill="#FAF8F2"/>
              <rect x="-125" y="-215" width="250" height="340" fill="#165B33"/>
              <circle cx="0" cy="-115" r="55" fill="#FAF8F2"/>
              <circle cx="16" cy="-120" r="48" fill="#165B33"/>
              <polygon points="12,-115 18,-96 2,-104 22,-104 6,-96" fill="#FAF8F2" transform="scale(1.1) translate(4,-15)"/>
              <text x="0" y="-25" font-size="52" fill="#FAF8F2" text-anchor="middle">PSL</text>
              <text x="0" y="12" font-size="24" fill="#E3B23C" text-anchor="middle" letter-spacing="2">PAKISTAN</text>
              <rect x="-125" y="135" width="250" height="85" fill="#FAF8F2"/>
              <text x="0" y="174" font-size="34" fill="#165B33" text-anchor="middle">FAST PACED</text>
              <text x="0" y="204" font-size="22" fill="#888888" text-anchor="middle">EST. 2016</text>
              <polygon points="-35,-245 35,-245 35,-215 -35,-215" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
            </g>
          </g>

          <!-- Card 3: BBL -->
          <g transform="translate(850, 680) rotate(6)">
            <g id="s1_card_bbl" class="cut">
              <polygon points="-142,-232 142,-236 144,236 -142,232" fill="#FAF8F2"/>
              <rect x="-125" y="-215" width="250" height="340" fill="#0E86D4"/>
              <circle cx="0" cy="-90" r="65" fill="#232B2B"/>
              <path d="M-30,-60 Q0,-130 35,-90 Q15,-65 18,-45 Q-10,-65 -30,-60Z" fill="#FAF8F2"/>
              <text x="0" y="0" font-size="50" fill="#FAF8F2" text-anchor="middle">BBL</text>
              <text x="0" y="32" font-size="24" fill="#E3B23C" text-anchor="middle" letter-spacing="2">AUSTRALIA</text>
              <rect x="-125" y="135" width="250" height="85" fill="#FAF8F2"/>
              <text x="0" y="174" font-size="34" fill="#0E86D4" text-anchor="middle">SUMMER FEST</text>
              <text x="0" y="204" font-size="22" fill="#888888" text-anchor="middle">EST. 2011</text>
              <polygon points="65,-245 115,-240 100,-210 50,-215" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
            </g>
          </g>
        </g>

        <!-- Big Slamming Stamp: 9X PAY GAP -->
        <g transform="translate(540, 1080) rotate(-7)">
          <g id="s1_stamp_9x" class="cut-lg">
            <polygon points="-425,-82 425,-78 420,82 -430,78" fill="#C1121F"/>
            <polygon points="-410,-68 410,-65 405,68 -415,65" fill="#FAF8F2"/>
            <text x="0" y="25" font-size="88" fill="#C1121F" text-anchor="middle" letter-spacing="4">9X PAY GAP!</text>
          </g>
        </g>

        <!-- Question Mark Badge: GUESS WHICH? -->
        <g transform="translate(540, 1260)">
          <g id="s1_guess_badge" class="cut">
            <rect x="-240" y="-45" width="480" height="90" rx="8" fill="#E3B23C"/>
            <rect x="-232" y="-38" width="464" height="76" rx="6" fill="#1B1B1B"/>
            <text x="-25" y="16" font-size="46" fill="#E3B23C" text-anchor="middle" letter-spacing="3">GUESS WHICH</text>
            <text x="140" y="18" font-size="52" fill="#FAF8F2" text-anchor="middle">?</text>
          </g>
        </g>
      </svg>
    </div>

    <!-- ============================================================ -->
    <!-- SCENE 2: PSL (Pakistan Super League) -->
    <!-- ============================================================ -->
    <div id="s2" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <rect width="1080" height="1920" fill="#F4EBD9"/>
        <polygon points="60,140 1020,130 1000,1360 80,1370" fill="#E8DEC8"/>

        <!-- Header Badge -->
        <g transform="translate(540, 220)">
          <g id="s2_header" class="cut">
            <polygon points="-385,-46 385,-48 378,48 -382,46" fill="#165B33"/>
            <rect x="-365" y="-34" width="730" height="68" fill="#FAF8F2"/>
            <text x="0" y="16" font-size="42" fill="#165B33" text-anchor="middle" letter-spacing="3">PAKISTAN SUPER LEAGUE</text>
          </g>
        </g>

        <!-- Initial PSL Intro Shield (Active 7.6s - 9.6s) -->
        <g transform="translate(540, 750)">
          <g id="s2_intro_badge" class="cut">
            <polygon points="-280,-160 280,-165 275,160 -285,155" fill="#FAF8F2"/>
            <rect x="-260" y="-140" width="520" height="280" fill="#165B33"/>
            <circle cx="0" cy="-35" r="75" fill="#FAF8F2"/>
            <circle cx="22" cy="-42" r="66" fill="#165B33"/>
            <polygon points="18,-35 26,-10 6,-20 30,-20 12,-10" fill="#FAF8F2" transform="scale(1.2) translate(5,-10)"/>
            <text x="0" y="80" font-size="54" fill="#FAF8F2" text-anchor="middle" letter-spacing="2">HBL PSL</text>
            <text x="0" y="118" font-size="24" fill="#E3B23C" text-anchor="middle" letter-spacing="2">PAKISTAN · EST. 2016</text>
          </g>
        </g>

        <!-- Main Card 1: Team Squad Budget ($1.6M) (Lands at 9.6s) -->
        <g transform="translate(540, 560)">
          <g id="s2_budget_card" class="cut">
            <polygon points="-432,-175 432,-180 428,175 -434,170" fill="#FAF8F2"/>
            <rect x="-415" y="-160" width="830" height="55" fill="#165B33"/>
            <text x="0" y="-122" font-size="30" fill="#FAF8F2" text-anchor="middle" letter-spacing="2">TEAM SQUAD PURSE (CAP)</text>

            <text x="0" y="30" font-size="115" fill="#1B1B1B" text-anchor="middle" letter-spacing="2">$1.6 MILLION</text>
            <text x="0" y="85" font-size="34" fill="#C1121F" text-anchor="middle">ROUGHLY ₹13.5 CRORE TOTAL PER SQUAD</text>
            <line x1="-350" y1="115" x2="350" y2="115" stroke="#E0D7C2" stroke-width="4"/>
            <text x="0" y="152" font-size="26" fill="#666666" text-anchor="middle">BUDGET SPLIT ACROSS 18–20 SQUAD CRICKETERS</text>

            <g transform="translate(320, -100) rotate(14)" class="cut-sm">
              <rect x="-80" y="-25" width="160" height="50" rx="4" fill="#FAF8F2" stroke="#165B33" stroke-width="5"/>
              <text x="0" y="9" font-size="24" fill="#165B33" text-anchor="middle">SALARY CAP</text>
            </g>
            <polygon points="-430,-190 -370,-190 -370,-160 -430,-160" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
          </g>
        </g>

        <!-- Mid Squad Lineup Visual (Active 9.6s - 13.7s) -->
        <g transform="translate(540, 920)">
          <g id="s2_squad_lineup" class="cut">
            <rect x="-410" y="-80" width="820" height="160" rx="8" fill="#FAF8F2"/>
            <text x="0" y="-30" font-size="28" fill="#666666" text-anchor="middle">ENTIRE ROSTER INCLUDED</text>
            <g transform="translate(-315, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
            <g transform="translate(-225, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
            <g transform="translate(-135, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
            <g transform="translate(-45, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
            <g transform="translate(45, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
            <g transform="translate(135, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
            <g transform="translate(225, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
            <g transform="translate(315, 20)">
              <circle cx="0" cy="-20" r="14" fill="#165B33"/><path d="M-18,25 Q-20,0 0,0 Q20,0 18,25Z" fill="#165B33"/>
            </g>
          </g>
        </g>

        <!-- Card 2: Highest Paid Player ($500K) (Slides in at 13.7s) -->
        <g transform="translate(540, 1020)">
          <g id="s2_player_card" class="cut">
            <polygon points="-432,-170 432,-175 428,170 -434,165" fill="#FAF8F2"/>
            <rect x="-395" y="-140" width="240" height="280" fill="#EAE0CC"/>
            <g transform="translate(-275, -10)">
              <circle cx="0" cy="-55" r="42" fill="#D69E73"/>
              <path d="M-44,-60 Q-46,-105 0,-105 Q46,-105 44,-60Z" fill="#165B33"/>
              <circle cx="0" cy="-78" r="12" fill="#E3B23C"/>
              <path d="M-65,85 Q-70,5 0,5 Q70,5 65,85Z" fill="#165B33"/>
              <polygon points="-25,5 0,35 25,5" fill="#FAF8F2"/>
            </g>
            <rect x="-375" y="95" width="200" height="35" fill="#1B1B1B"/>
            <text x="-275" y="120" font-size="20" fill="#FAF8F2" text-anchor="middle">PLATINUM CATEGORY</text>

            <text x="80" y="-85" font-size="32" fill="#666666" text-anchor="middle">HIGHEST-PAID STARS</text>
            <g transform="translate(80, -10)">
              <rect x="-240" y="-55" width="480" height="100" fill="#E3B23C" class="cut-sm"/>
              <text x="0" y="18" font-size="80" fill="#1B1B1B" text-anchor="middle">~$500,000</text>
            </g>
            <text x="80" y="95" font-size="34" fill="#C1121F" text-anchor="middle">AROUND HALF A MILLION $</text>
            <text x="80" y="130" font-size="24" fill="#888888" text-anchor="middle">(~₹4.1 CRORE RUPEES / SEASON)</text>
            <polygon points="370,-185 430,-185 430,-155 370,-155" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
          </g>
        </g>
      </svg>
    </div>

    <!-- ============================================================ -->
    <!-- SCENE 3: BBL (Big Bash League) -->
    <!-- ============================================================ -->
    <div id="s3" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <rect width="1080" height="1920" fill="#F4EBD9"/>
        <polygon points="60,140 1020,130 1000,1360 80,1370" fill="#E8DEC8"/>

        <!-- Header Badge -->
        <g transform="translate(540, 220)">
          <g id="s3_header" class="cut">
            <polygon points="-385,-46 385,-48 378,48 -382,46" fill="#0E86D4"/>
            <rect x="-365" y="-34" width="730" height="68" fill="#FAF8F2"/>
            <text x="0" y="16" font-size="42" fill="#0E86D4" text-anchor="middle" letter-spacing="3">BIG BASH LEAGUE · AUSTRALIA</text>
          </g>
        </g>

        <!-- Stadium paper collage graphic with floodlights & crowd -->
        <g transform="translate(540, 540)">
          <g id="s3_stadium_box" class="cut">
            <rect x="-430" y="-160" width="860" height="320" fill="#FAF8F2"/>
            <rect x="-410" y="-140" width="820" height="190" fill="#39424E"/>
            <g stroke="#FAF8F2" stroke-width="4" fill="none" opacity="0.6">
              <line x1="-360" y1="-140" x2="-360" y2="-40"/><line x1="-340" y1="-140" x2="-340" y2="-40"/><line x1="-360" y1="-140" x2="-340" y2="-40"/><line x1="-360" y1="-90" x2="-340" y2="-140"/>
              <line x1="360" y1="-140" x2="360" y2="-40"/><line x1="340" y1="-140" x2="340" y2="-40"/><line x1="360" y1="-140" x2="340" y2="-40"/><line x1="360" y1="-90" x2="340" y2="-140"/>
            </g>
            <g opacity="0.95">
              <circle cx="-300" cy="-100" r="16" fill="#F4EBD9"/><circle cx="-240" cy="-100" r="16" fill="#E3B23C"/><circle cx="-180" cy="-100" r="16" fill="#0E86D4"/><circle cx="-120" cy="-100" r="16" fill="#C1121F"/>
              <circle cx="-60" cy="-100" r="16" fill="#FAF8F2"/><circle cx="0" cy="-100" r="16" fill="#E3B23C"/><circle cx="60" cy="-100" r="16" fill="#0E86D4"/><circle cx="120" cy="-100" r="16" fill="#C1121F"/>
              <circle cx="180" cy="-100" r="16" fill="#FAF8F2"/><circle cx="240" cy="-100" r="16" fill="#E3B23C"/><circle cx="300" cy="-100" r="16" fill="#0E86D4"/>
              <circle cx="-330" cy="-55" r="16" fill="#0E86D4"/><circle cx="-270" cy="-55" r="16" fill="#FAF8F2"/><circle cx="-210" cy="-55" r="16" fill="#E3B23C"/><circle cx="-150" cy="-55" r="16" fill="#C1121F"/>
              <circle cx="-90" cy="-55" r="16" fill="#0E86D4"/><circle cx="-30" cy="-55" r="16" fill="#FAF8F2"/><circle cx="30" cy="-55" r="16" fill="#E3B23C"/><circle cx="90" cy="-55" r="16" fill="#C1121F"/>
              <circle cx="150" cy="-55" r="16" fill="#0E86D4"/><circle cx="210" cy="-55" r="16" fill="#FAF8F2"/><circle cx="270" cy="-55" r="16" fill="#E3B23C"/><circle cx="330" cy="-55" r="16" fill="#C1121F"/>
            </g>
            <rect x="-410" y="50" width="820" height="90" fill="#6F9A4B"/>
            <text x="0" y="105" font-size="34" fill="#FAF8F2" text-anchor="middle" letter-spacing="2">ICONIC AUSTRALIAN SUMMER BRAND</text>
          </g>
        </g>

        <!-- Top stars salary card -->
        <g transform="translate(540, 880)">
          <g id="s3_salary_card" class="cut">
            <polygon points="-432,-120 432,-125 428,120 -434,115" fill="#FAF8F2"/>
            <text x="0" y="-55" font-size="30" fill="#666666" text-anchor="middle" letter-spacing="1">TOP OVERSEAS & DOMESTIC STARS</text>
            <text x="0" y="30" font-size="82" fill="#1B1B1B" text-anchor="middle">A FEW HUNDRED THOUSAND $</text>
            <text x="0" y="85" font-size="30" fill="#0E86D4" text-anchor="middle">(TYPICALLY $250,000 – $420,000 / SEASON)</text>
            <polygon points="-430,-130 -370,-130 -370,-100 -430,-100" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
          </g>
        </g>

        <!-- Two Clashing Rubber Stamps -->
        <g transform="translate(540, 1090) rotate(-3)">
          <g id="s3_stamp_good" class="cut">
            <polygon points="-360,-45 360,-40 355,45 -365,40" fill="#FAF8F2" stroke="#165B33" stroke-width="6"/>
            <text x="0" y="16" font-size="44" fill="#165B33" text-anchor="middle" letter-spacing="2">GREAT CRICKET · GREAT ATMOSPHERE 🏏</text>
          </g>
        </g>

        <g transform="translate(540, 1220) rotate(4)">
          <g id="s3_stamp_bad" class="cut-lg">
            <polygon points="-320,-50 320,-45 315,50 -325,45" fill="#C1121F"/>
            <polygon points="-310,-40 310,-35 305,40 -315,35" fill="#FAF8F2"/>
            <text x="0" y="16" font-size="52" fill="#C1121F" text-anchor="middle" letter-spacing="3">BUT NOT HUGE MONEY ❌</text>
          </g>
        </g>
      </svg>
    </div>

    <!-- ============================================================ -->
    <!-- SCENE 4: IPL & RISHABH PANT (The Monster Economy) -->
    <!-- ============================================================ -->
    <div id="s4" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <rect width="1080" height="1920" fill="#F4EBD9"/>
        <polygon points="60,140 1020,130 1000,1360 80,1370" fill="#E8DEC8"/>

        <!-- Header Badge -->
        <g transform="translate(540, 220)">
          <g id="s4_header" class="cut">
            <polygon points="-385,-46 385,-48 378,48 -382,46" fill="#0A2240"/>
            <rect x="-365" y="-34" width="730" height="68" fill="#FAF8F2"/>
            <text x="0" y="16" font-size="42" fill="#0A2240" text-anchor="middle" letter-spacing="3">INDIAN PREMIER LEAGUE (IPL)</text>
          </g>
        </g>

        <!-- Initial Golden Trophy Intro Badge (Active 26.3s - 28.3s) -->
        <g transform="translate(540, 750)">
          <g id="s4_intro_trophy" class="cut">
            <polygon points="-280,-160 280,-165 275,160 -285,155" fill="#FAF8F2"/>
            <rect x="-260" y="-140" width="520" height="280" fill="#0A2240"/>
            <!-- Golden Trophy shifted up so text never touches -->
            <g transform="translate(0, -35)">
              <polygon points="0,-100 65,-65 45,5 18,35 18,65 45,75 45,85 -45,85 -45,75 -18,65 -18,35 -45,5 -65,-65" fill="#E3B23C"/>
              <circle cx="0" cy="-45" r="24" fill="#0A2240"/>
              <text x="0" y="-36" font-size="22" fill="#E3B23C" text-anchor="middle">TATA</text>
            </g>
            <text x="0" y="95" font-size="52" fill="#FAF8F2" text-anchor="middle" letter-spacing="5">IPL</text>
            <text x="0" y="125" font-size="22" fill="#E3B23C" text-anchor="middle" letter-spacing="3">INDIA · EST. 2008</text>
          </g>
        </g>

        <!-- Phase 1: Team Purse Card (120 Crore / $14M) (Lands at 28.3s) -->
        <g transform="translate(540, 540)">
          <g id="s4_purse_card" class="cut">
            <polygon points="-432,-170 432,-175 428,170 -434,165" fill="#FAF8F2"/>
            <rect x="-415" y="-155" width="830" height="55" fill="#0A2240"/>
            <text x="0" y="-117" font-size="30" fill="#E3B23C" text-anchor="middle" letter-spacing="2">EACH TEAM'S AUCTION PURSE</text>

            <text x="0" y="30" font-size="115" fill="#1B1B1B" text-anchor="middle" letter-spacing="2">₹120 CRORE</text>
            <g transform="translate(0, 95)">
              <rect x="-240" y="-35" width="480" height="65" rx="6" fill="#E3B23C" class="cut-sm"/>
              <text x="0" y="12" font-size="44" fill="#1B1B1B" text-anchor="middle">≈ $14 MILLION DOLLARS</text>
            </g>
            <text x="0" y="152" font-size="28" fill="#165B33" text-anchor="middle">NEARLY 9X THE ENTIRE PSL TEAM PURSE!</text>
            <polygon points="-430,-180 -370,-180 -370,-150 -430,-150" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
          </g>
        </g>

        <!-- Phase 2: Rishabh Pant Record Card (₹27 Crore) (Lands at 34.3s) -->
        <g transform="translate(540, 930)">
          <g id="s4_pant_card" class="cut-lg">
            <polygon points="-432,-165 432,-170 428,165 -434,160" fill="#FAF8F2"/>
            <rect x="-395" y="-135" width="240" height="265" fill="#D8E2EC"/>
            <g transform="translate(-275, -5)">
              <circle cx="0" cy="-55" r="42" fill="#D69E73"/>
              <path d="M-42,-65 Q-45,-105 0,-105 Q45,-105 42,-65Z" fill="#3B2A1E"/>
              <path d="M-38,-45 Q0,-25 38,-45 Q35,-30 0,-25 Q-35,-30 -38,-45Z" fill="#3B2A1E"/>
              <path d="M-45,-75 Q0,-115 45,-75 Q55,-60 0,-65 Q-55,-60 -45,-75Z" fill="#0A2240"/>
              <circle cx="0" cy="-85" r="8" fill="#E3B23C"/>
              <circle cx="-16" cy="-55" r="5" fill="#1B1B1B"/><circle cx="16" cy="-55" r="5" fill="#1B1B1B"/>
              <path d="M-18,-40 Q0,-22 18,-40" stroke="#1B1B1B" stroke-width="4" fill="none" stroke-linecap="round"/>
              <path d="M-65,80 Q-70,5 0,5 Q70,5 65,80Z" fill="#0A2240"/>
              <g transform="translate(50, -40) rotate(-25)">
                <rect x="-8" y="-70" width="16" height="120" rx="4" fill="#E3B23C" stroke="#B88A22" stroke-width="2"/>
                <rect x="-5" y="50" width="10" height="35" rx="3" fill="#FAF8F2"/>
              </g>
            </g>
            <rect x="-375" y="85" width="200" height="35" fill="#C1121F"/>
            <text x="-275" y="110" font-size="20" fill="#FAF8F2" text-anchor="middle">RECORD BUY</text>

            <text x="80" y="-85" font-size="34" fill="#666666" text-anchor="middle">ONE SINGLE CRICKETER</text>
            <text x="80" y="-35" font-size="52" fill="#0A2240" text-anchor="middle">RISHABH PANT</text>
            <g transform="translate(80, 45)">
              <rect x="-220" y="-50" width="440" height="90" fill="#C1121F" class="cut-sm"/>
              <text x="0" y="18" font-size="76" fill="#FAF8F2" text-anchor="middle">₹27 CRORE</text>
            </g>
            <text x="80" y="125" font-size="30" fill="#1B1B1B" text-anchor="middle">≈ $3.2 MILLION USD</text>
          </g>
        </g>

        <!-- Phase 3: The Shocking Truth Stamp (1 Player > Entire PSL Squad) (Slams at 38.5s) -->
        <g transform="translate(540, 1230) rotate(-4)">
          <g id="s4_shock_stamp" class="cut-lg">
            <polygon points="-420,-60 420,-55 415,60 -425,55" fill="#1B1B1B"/>
            <polygon points="-410,-50 410,-45 405,50 -415,45" fill="#E3B23C"/>
            <text x="0" y="18" font-size="46" fill="#1B1B1B" text-anchor="middle" letter-spacing="1">1 PLAYER > ENTIRE PSL TEAM'S BUDGET!</text>
          </g>
        </g>
      </svg>
    </div>

    <!-- ============================================================ -->
    <!-- SCENE 5: CONCLUSION & CTA (An Economy & Vote) -->
    <!-- ============================================================ -->
    <div id="s5" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <rect width="1080" height="1920" fill="#F4EBD9"/>
        <polygon points="60,140 1020,130 1000,1360 80,1370" fill="#E8DEC8"/>

        <!-- Header Badge -->
        <g transform="translate(540, 220)">
          <g id="s5_header" class="cut">
            <polygon points="-385,-46 385,-48 378,48 -382,46" fill="#1B1B1B"/>
            <rect x="-365" y="-34" width="730" height="68" fill="#E3B23C"/>
            <text x="0" y="16" font-size="44" fill="#1B1B1B" text-anchor="middle" letter-spacing="3">THE FINANCIAL VERDICT</text>
          </g>
        </g>

        <!-- Giant Economy Climax Banner -->
        <g transform="translate(540, 560)">
          <g id="s5_economy_box" class="cut-lg">
            <polygon points="-432,-180 432,-185 428,180 -434,175" fill="#FAF8F2"/>
            <text x="0" y="-95" font-size="44" fill="#666666" text-anchor="middle" letter-spacing="2">THE IPL ISN'T JUST A LEAGUE...</text>
            
            <g transform="translate(0, 15)">
              <rect x="-400" y="-80" width="800" height="150" rx="8" fill="#0A2240" class="cut-sm"/>
              <text x="0" y="26" font-size="94" fill="#E3B23C" text-anchor="middle" letter-spacing="4">IT'S AN ECONOMY!</text>
            </g>

            <text x="0" y="145" font-size="34" fill="#C1121F" text-anchor="middle">VALUED AT OVER $16 BILLION (₹1.3 LAKH CR)</text>
            <polygon points="-430,-190 -370,-190 -370,-160 -430,-160" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
          </g>
        </g>

        <!-- Phase 1.5: Grand Crown Illustration (Active 42.6s - 46.1s) -->
        <g transform="translate(540, 930)">
          <g id="s5_crown_emblem" class="cut">
            <rect x="-240" y="-80" width="480" height="160" rx="12" fill="#FAF8F2"/>
            <path d="M-80,30 L-100,-40 L-50,-10 L0,-50 L50,-10 L100,-40 L80,30 Z" fill="#E3B23C" stroke="#B88A22" stroke-width="4"/>
            <circle cx="-100" cy="-45" r="8" fill="#C1121F"/>
            <circle cx="0" cy="-55" r="10" fill="#0A2240"/>
            <circle cx="100" cy="-45" r="8" fill="#C1121F"/>
            <text x="0" y="62" font-size="28" fill="#0A2240" text-anchor="middle" letter-spacing="2">CRICKET'S SUPERPOWER</text>
          </g>
        </g>

        <!-- Phase 2: Which League is the Best Voting Ballot (Appears at 46.1s) -->
        <g transform="translate(540, 980)">
          <g id="s5_ballot_box" class="cut">
            <!-- Option 1: IPL -->
            <g transform="translate(-290, 0)">
              <polygon points="-125,-120 125,-125 120,120 -130,115" fill="#FAF8F2"/>
              <rect x="-115" y="-110" width="230" height="50" fill="#0A2240"/>
              <text x="0" y="-75" font-size="28" fill="#E3B23C" text-anchor="middle">OPTION 1</text>
              <text x="0" y="10" font-size="56" fill="#0A2240" text-anchor="middle">IPL</text>
              <text x="0" y="42" font-size="22" fill="#E3B23C" text-anchor="middle">INDIA</text>
              <text x="0" y="72" font-size="22" fill="#666666" text-anchor="middle">PURE EMPIRE</text>
              <text x="0" y="98" font-size="20" fill="#C1121F" text-anchor="middle">THE RICHEST</text>
              <polygon points="-30,-130 30,-130 30,-105 -30,-105" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
            </g>

            <!-- Option 2: PSL -->
            <g transform="translate(0, 0)">
              <polygon points="-125,-125 125,-120 125,120 -125,125" fill="#FAF8F2"/>
              <rect x="-115" y="-110" width="230" height="50" fill="#165B33"/>
              <text x="0" y="-75" font-size="28" fill="#FAF8F2" text-anchor="middle">OPTION 2</text>
              <text x="0" y="10" font-size="56" fill="#165B33" text-anchor="middle">PSL</text>
              <text x="0" y="42" font-size="22" fill="#165B33" text-anchor="middle">PAKISTAN</text>
              <text x="0" y="72" font-size="22" fill="#666666" text-anchor="middle">RAW PACE</text>
              <text x="0" y="98" font-size="20" fill="#165B33" text-anchor="middle">HIGH DRAMA</text>
              <polygon points="-30,-130 30,-130 30,-105 -30,-105" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
            </g>

            <!-- Option 3: BBL -->
            <g transform="translate(290, 0)">
              <polygon points="-125,-120 125,-125 120,120 -130,115" fill="#FAF8F2"/>
              <rect x="-115" y="-110" width="230" height="50" fill="#0E86D4"/>
              <text x="0" y="-75" font-size="28" fill="#FAF8F2" text-anchor="middle">OPTION 3</text>
              <text x="0" y="10" font-size="56" fill="#0E86D4" text-anchor="middle">BBL</text>
              <text x="0" y="42" font-size="22" fill="#0E86D4" text-anchor="middle">AUSTRALIA</text>
              <text x="0" y="72" font-size="22" fill="#666666" text-anchor="middle">ATMOSPHERE</text>
              <text x="0" y="98" font-size="20" fill="#0E86D4" text-anchor="middle">SUMMER FEST</text>
              <polygon points="-30,-130 30,-130 30,-105 -30,-105" fill="rgba(255,255,245,0.7)" stroke="rgba(210,200,180,0.5)"/>
            </g>
          </g>
        </g>

        <!-- CTA Paper Ribbon -->
        <g transform="translate(540, 1230)">
          <g id="s5_cta_ribbon" class="cut-lg">
            <polygon points="-420,-50 420,-45 415,50 -425,45" fill="#C1121F"/>
            <polygon points="-410,-40 410,-35 405,40 -415,35" fill="#FAF8F2"/>
            <text x="-20" y="16" font-size="44" fill="#C1121F" text-anchor="middle" letter-spacing="2">WHICH IS THE BEST? COMMENT BELOW!</text>
            <polygon points="340,3 365,3 352,22" fill="#C1121F"/>
          </g>
        </g>
      </svg>
    </div>

    <!-- Paper Grain and Vignette Elements -->
    <div id="grain"></div>
    <div id="vignette"></div>

    <!-- Standardized Subtitle / Caption Zone -->
    <div id="captions-box">
      <div id="cap-text" class="cap-strip">SAME SPORT. SAME FORMAT. <b>THREE LEAGUES.</b></div>
    </div>
  </div>

  <script>
    // Master GSAP Timeline mapped to speech segments
    const tl = gsap.timeline({{ paused: true }});

    // References
    const s1 = "#s1", s2 = "#s2", s3 = "#s3", s4 = "#s4", s5 = "#s5";

    // ==========================================
    // SCENE 1: THE HOOK (0.00s - 7.60s)
    // ==========================================
    tl.set(s1, {{ autoAlpha: 1 }}, 0);
    tl.from("#s1_header", {{ y: -180, autoAlpha: 0, duration: 0.5, ease: "back.out(1.4)" }}, 0.05);

    // Three cards drop in sequence
    tl.from("#s1_card_ipl", {{ y: 300, autoAlpha: 0, rotation: -25, duration: 0.6, ease: "back.out(1.5)" }}, 0.8);
    tl.from("#s1_card_psl", {{ y: 300, autoAlpha: 0, duration: 0.6, ease: "back.out(1.5)" }}, 1.5);
    tl.from("#s1_card_bbl", {{ y: 300, autoAlpha: 0, rotation: 25, duration: 0.6, ease: "back.out(1.5)" }}, 2.2);

    // 9X Stamp slams down!
    tl.from("#s1_stamp_9x", {{ scale: 2.8, autoAlpha: 0, rotation: 30, duration: 0.45, ease: "bounce.out" }}, 3.35);

    // Guess which badge
    tl.from("#s1_guess_badge", {{ scale: 0.2, autoAlpha: 0, duration: 0.4, ease: "back.out(2)" }}, 6.76);
    tl.to("#s1_guess_badge", {{ rotation: 4, yoyo: true, repeat: 3, duration: 0.1 }}, 7.0);

    // ==========================================
    // SCENE 2: PSL (7.60s - 16.50s)
    // ==========================================
    tl.to(s1, {{ autoAlpha: 0, duration: 0.25 }}, 7.60);
    tl.set(s2, {{ autoAlpha: 1 }}, 7.60);

    tl.from("#s2_header", {{ y: -150, autoAlpha: 0, duration: 0.45, ease: "power2.out" }}, 7.65);
    tl.from("#s2_intro_badge", {{ scale: 0.5, autoAlpha: 0, duration: 0.55, ease: "back.out(1.4)" }}, 7.75);

    // At 9.60s, transition into Team Budget Card ($1.6M) and Squad lineup
    tl.to("#s2_intro_badge", {{ autoAlpha: 0, scale: 0.8, duration: 0.3 }}, 9.50);
    tl.from("#s2_budget_card", {{ scale: 0.8, autoAlpha: 0, y: 80, duration: 0.55, ease: "back.out(1.4)" }}, 9.60);
    tl.from("#s2_squad_lineup", {{ autoAlpha: 0, y: 60, duration: 0.45, ease: "power2.out" }}, 9.80);

    // At 13.60s, squad lineup fades and Highest Paid Player ($500K) slides in!
    tl.to("#s2_squad_lineup", {{ autoAlpha: 0, duration: 0.25 }}, 13.50);
    tl.from("#s2_player_card", {{ x: -150, autoAlpha: 0, duration: 0.55, ease: "power3.out" }}, 13.70);

    // ==========================================
    // SCENE 3: BBL (16.50s - 26.30s)
    // ==========================================
    tl.to(s2, {{ autoAlpha: 0, duration: 0.25 }}, 16.50);
    tl.set(s3, {{ autoAlpha: 1 }}, 16.50);

    tl.from("#s3_header", {{ y: -150, autoAlpha: 0, duration: 0.45, ease: "power2.out" }}, 16.55);
    tl.from("#s3_stadium_box", {{ scale: 0.85, autoAlpha: 0, duration: 0.55, ease: "back.out(1.3)" }}, 16.70);

    // Top stars salary card
    tl.from("#s3_salary_card", {{ y: 80, autoAlpha: 0, duration: 0.5, ease: "power2.out" }}, 19.30);

    // Stamps: Great cricket vs Not huge money
    tl.from("#s3_stamp_good", {{ scale: 1.8, autoAlpha: 0, duration: 0.4, ease: "bounce.out" }}, 22.70);
    tl.from("#s3_stamp_bad", {{ scale: 2.2, autoAlpha: 0, rotation: -20, duration: 0.4, ease: "bounce.out" }}, 24.80);

    // ==========================================
    // SCENE 4: IPL & RISHABH PANT (26.30s - 42.60s)
    // ==========================================
    tl.to(s3, {{ autoAlpha: 0, duration: 0.25 }}, 26.30);
    tl.set(s4, {{ autoAlpha: 1 }}, 26.30);

    tl.from("#s4_header", {{ y: -150, autoAlpha: 0, duration: 0.45, ease: "power2.out" }}, 26.35);
    tl.from("#s4_intro_trophy", {{ scale: 0.5, autoAlpha: 0, duration: 0.55, ease: "back.out(1.4)" }}, 26.45);

    // At 28.20s, transition into Team Purse Card (₹120 Crore)
    tl.to("#s4_intro_trophy", {{ autoAlpha: 0, scale: 0.8, duration: 0.3 }}, 28.15);
    tl.from("#s4_purse_card", {{ scale: 0.75, autoAlpha: 0, duration: 0.6, ease: "back.out(1.5)" }}, 28.30);

    // Rishabh Pant 27 Crore Card
    tl.from("#s4_pant_card", {{ y: 150, scale: 0.85, autoAlpha: 0, duration: 0.6, ease: "back.out(1.4)" }}, 34.30);

    // Shocking truth stamp (1 Player > Entire PSL team budget)
    tl.from("#s4_shock_stamp", {{ scale: 2.5, autoAlpha: 0, duration: 0.45, ease: "bounce.out" }}, 38.50);

    // ==========================================
    // SCENE 5: CONCLUSION & CTA (42.60s - 49.08s)
    // ==========================================
    tl.to(s4, {{ autoAlpha: 0, duration: 0.25 }}, 42.60);
    tl.set(s5, {{ autoAlpha: 1 }}, 42.60);

    tl.from("#s5_header", {{ y: -150, autoAlpha: 0, duration: 0.45, ease: "power2.out" }}, 42.65);
    tl.from("#s5_economy_box", {{ scale: 0.8, autoAlpha: 0, duration: 0.6, ease: "back.out(1.4)" }}, 42.75);
    tl.from("#s5_crown_emblem", {{ scale: 0.5, autoAlpha: 0, duration: 0.5, ease: "back.out(1.5)" }}, 43.10);
    tl.to("#s5_economy_box", {{ scale: 1.05, yoyo: true, repeat: 1, duration: 0.25 }}, 45.0);

    // Which league is the best? At 46.10s, crown fades and ballot appears!
    tl.to("#s5_crown_emblem", {{ autoAlpha: 0, duration: 0.25 }}, 46.00);
    tl.from("#s5_ballot_box", {{ y: 120, autoAlpha: 0, duration: 0.5, ease: "power3.out" }}, 46.10);

    // Comment below ribbon
    tl.from("#s5_cta_ribbon", {{ scale: 0.5, autoAlpha: 0, duration: 0.4, ease: "back.out(2)" }}, 48.0);

    // ==========================================
    // 100% DETERMINISTIC CAPTIONS ARRAY
    // ==========================================
    const CAPTIONS = [
      {{ start: 0.00,  end: 3.10,  html: "SAME SPORT. SAME FORMAT. <b>THREE LEAGUES.</b>" }},
      {{ start: 3.10,  end: 6.65,  html: "ONE OF THEM PAYS <b>ABOUT 9 TIMES MORE</b> THAN ANOTHER." }},
      {{ start: 6.65,  end: 7.60,  html: "<i>GUESS WHICH?</i>" }},
      {{ start: 7.60,  end: 9.75,  html: "START WITH THE <u>PSL.</u>" }},
      {{ start: 9.75,  end: 13.70, html: "EACH TEAM HAS <b>$1.6 MILLION</b> TO BUILD A SQUAD." }},
      {{ start: 13.70, end: 16.50, html: "ITS HIGHEST-PAID PLAYERS EARN <i>AROUND HALF A MILLION.</i>" }},
      {{ start: 16.50, end: 19.40, html: "THE <b>BIG BASH</b> IS A HUGE BRAND IN AUSTRALIA..." }},
      {{ start: 19.40, end: 22.60, html: "ITS TOP STARS EARN A <b>FEW HUNDRED THOUSAND $</b> A SEASON." }},
      {{ start: 22.60, end: 24.75, html: "<i>GREAT CRICKET. GREAT ATMOSPHERE.</i>" }},
      {{ start: 24.75, end: 26.30, html: "BUT <b>NOT HUGE MONEY.</b> ❌" }},
      {{ start: 26.30, end: 28.45, html: "THEN COMES THE <span class='blue'>IPL.</span>" }},
      {{ start: 28.45, end: 32.15, html: "EACH TEAM CAN SPEND AROUND <b>₹120 CRORE RUPEES.</b>" }},
      {{ start: 32.15, end: 34.40, html: "THAT'S ABOUT <i>$14 MILLION DOLLARS!</i>" }},
      {{ start: 34.40, end: 38.55, html: "ONE PLAYER ALONE: <b>RISHABH PANT</b> WAS PAID <b>₹27 CRORE!</b>" }},
      {{ start: 38.55, end: 42.60, html: "ONE CRICKETER EARNING <b>MORE THAN A WHOLE PSL TEAM!</b>" }},
      {{ start: 42.60, end: 44.85, html: "THE IPL ISN'T JUST A LEAGUE..." }},
      {{ start: 44.85, end: 46.20, html: "<b>IT'S AN ECONOMY!</b> 📈👑" }},
      {{ start: 46.20, end: 48.10, html: "WHICH LEAGUE DO YOU THINK IS THE <b>BEST?</b>" }},
      {{ start: 48.10, end: 49.50, html: "<i>COMMENT BELOW!</i>" }}
    ];

    const capEl = document.getElementById("cap-text");

    // Global deterministic seek function for frame-by-frame rendering
    window.seekFrame = function(timeSeconds) {{
      tl.seek(timeSeconds);

      // Deterministically update caption text based on exact timestamp
      let found = null;
      for (let i = 0; i < CAPTIONS.length; i++) {{
        if (timeSeconds >= CAPTIONS[i].start && timeSeconds < CAPTIONS[i].end) {{
          found = CAPTIONS[i].html;
          break;
        }}
      }}
      if (found) {{
        if (capEl.innerHTML !== found) {{
          capEl.innerHTML = found;
        }}
      }}
    }};

    window.__timelines = {{
      main: {{
        seek: function(t) {{
          window.seekFrame(t);
        }}
      }}
    }};
  </script>
</body>
</html>
"""

# Write index.html with local link
(base / "index.html").write_text(get_html(inline_gsap=False), encoding="utf-8")
print(f"Generated {base / 'index.html'}")

# Write standalone.html with fully inlined gsap & font
(base / "standalone.html").write_text(get_html(inline_gsap=True), encoding="utf-8")
print(f"Generated {base / 'standalone.html'}")
