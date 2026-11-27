import os
import json

def build():
    base_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\boxing-day-test-mcg"
    out_standalone = os.path.join(base_dir, "standalone.html")
    out_index = os.path.join(base_dir, "index.html")

    # Load speech segments
    with open(os.path.join(base_dir, "assets", "speech_segments.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    segments = data["segments"]

    # Caption definitions matched with the transcript
    captions = [
        {"start": 0.00, "end": 1.50, "html": "<span class='hl-gold'>19 YEARS OLD.</span> HIS TEST DEBUT."},
        {"start": 1.50, "end": 3.20, "html": "FIRST TIME ON THE <span class='hl-white'>BIGGEST STAGE</span>."},
        {"start": 3.20, "end": 6.69, "html": "JASPRIT BUMRAH RUNS IN... AND HE <span class='hl-red'>RAMP-SHOTS HIM!</span>"},
        {"start": 6.69, "end": 10.80, "html": "NEARLY <span class='hl-red'>90,000 PEOPLE</span> AT THE MCG WENT WILD!"},
        {"start": 10.80, "end": 12.40, "html": "ON <span class='hl-gold'>BOXING DAY.</span>"},
        {"start": 12.40, "end": 15.00, "html": "SO WHAT <span class='hl-blue'>IS</span> BOXING DAY CRICKET?"},
        {"start": 15.00, "end": 20.80, "html": "EVERY YEAR ON <span class='hl-gold'>DECEMBER 26</span>, AUSTRALIA STARTS AT THE <span class='hl-green'>MCG</span>."},
        {"start": 20.80, "end": 24.40, "html": "FAMILIES SKIP <span class='hl-gold'>CHRISTMAS LEFTOVERS</span>... AND FILL THE STADIUM."},
        {"start": 24.40, "end": 26.90, "html": "IT'S ONE OF THE <span class='hl-red'>BIGGEST DAYS</span> IN WORLD CRICKET."},
        {"start": 26.90, "end": 29.20, "html": "AND IT CREATES <span class='hl-gold'>LEGENDS</span>."},
        {"start": 29.20, "end": 32.20, "html": "<span class='hl-gold'>SHANE WARNE</span> TOOK A HAT-TRICK HERE AGAINST ENGLAND."},
        {"start": 32.20, "end": 37.50, "html": "IN 2020, <span class='hl-blue'>AJINKYA RAHANE</span> HIT 100 AND INDIA WON!"},
        {"start": 37.50, "end": 39.60, "html": "SO WHY <span class='hl-gold'>'BOXING DAY'</span>?"},
        {"start": 39.60, "end": 41.70, "html": "IT'S A <span class='hl-white'>PUBLIC HOLIDAY</span> IN AUSTRALIA."},
        {"start": 41.70, "end": 43.10, "html": "EVERYONE IS <span class='hl-gold'>OFF WORK</span>."},
        {"start": 43.10, "end": 45.20, "html": "SO EVERYONE GOES TO <span class='hl-green'>THE CRICKET</span>."},
        {"start": 45.20, "end": 47.10, "html": "CHRISTMAS IS FOR <span class='hl-red'>FAMILY</span>."},
        {"start": 47.10, "end": 49.50, "html": "BOXING DAY IS FOR <span class='hl-gold'>TEST CRICKET!</span>"},
        {"start": 49.50, "end": 51.50, "html": "BEST BOXING DAY MOMENT <span class='hl-white'>YOU'VE SEEN?</span>"},
        {"start": 51.50, "end": 52.61, "html": "DROP YOUR PICK IN THE <span class='hl-gold'>COMMENTS!</span>"}
    ]

    # HTML template with rich paper cutout SVG graphics
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Boxing Day Test at the MCG (Sam Konstas vs Bumrah)</title>
  <style>
    @font-face {{
      font-family: 'Anton';
      src: url('assets/fonts/Anton-Regular.ttf') format('truetype');
      font-weight: normal;
      font-style: normal;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }}
    body {{
      background: #0d131a;
      width: 1080px;
      height: 1920px;
      overflow: hidden;
      font-family: 'Anton', Impact, sans-serif;
    }}
    #stage {{
      position: relative;
      width: 1080px;
      height: 1920px;
      background: #143525;
      overflow: hidden;
    }}

    /* Paper texture & shadow styles */
    .paper-shadow {{
      filter: drop-shadow(0 14px 22px rgba(0, 0, 0, 0.45)) drop-shadow(0 4px 6px rgba(0, 0, 0, 0.3));
    }}
    .subtle-shadow {{
      filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.25));
    }}
    .glow-gold {{
      filter: drop-shadow(0 0 25px rgba(255, 209, 102, 0.6));
    }}
    .glow-red {{
      filter: drop-shadow(0 0 25px rgba(224, 49, 49, 0.7));
    }}

    /* Caption Pedestal Zone */
    #caption-zone {{
      position: absolute;
      left: 60px;
      right: 60px;
      top: 1260px;
      height: 220px;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      pointer-events: none;
    }}
    .caption-card {{
      position: absolute;
      background: #11141a;
      border: 4px solid #FAF7F0;
      border-radius: 20px;
      padding: 22px 36px;
      max-width: 960px;
      text-align: center;
      color: #FAF7F0;
      font-size: 50px;
      line-height: 1.25;
      letter-spacing: 2px;
      text-transform: uppercase;
      box-shadow: 0 16px 36px rgba(0,0,0,0.65), 0 0 0 4px rgba(0,0,0,0.4);
      opacity: 0;
      transform: scale(0.92);
      transition: none;
    }}
    .hl-gold {{ color: #FFD166; text-shadow: 0 0 12px rgba(255,209,102,0.4); }}
    .hl-red {{ color: #FF4D4D; text-shadow: 0 0 12px rgba(255,77,77,0.4); }}
    .hl-green {{ color: #52B788; text-shadow: 0 0 12px rgba(82,183,136,0.4); }}
    .hl-blue {{ color: #4CC9F0; text-shadow: 0 0 12px rgba(76,201,240,0.4); }}
    .hl-white {{ color: #FFFFFF; font-weight: bold; }}

    /* Scene layers */
    .scene {{
      position: absolute;
      top: 0;
      left: 0;
      width: 1080px;
      height: 1920px;
      visibility: hidden;
      opacity: 0;
    }}

    /* Overlay grain for classic paper aesthetic */
    #paper-grain {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 900;
      opacity: 0.08;
      background-image: radial-gradient(#fff 1px, transparent 1px), radial-gradient(#000 1px, transparent 1px);
      background-size: 8px 8px;
      background-position: 0 0, 4px 4px;
    }}
  </style>
  <script src="assets/gsap.min.js"></script>
</head>
<body>
  <div id="stage">
    <!-- Paper texture grain -->
    <div id="paper-grain"></div>

    <!-- ======================================================== -->
    <!-- SCENE 1: 19 YEARS OLD ON FIRST FRAME & RAMP SHOT (0 - 6.69s) -->
    <!-- ======================================================== -->
    <div id="scene1" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- Definitions for cut-out patterns and clips -->
        <defs>
          <filter id="drop-cut" x="-20%" y="-20%" width="150%" height="150%">
            <feDropShadow dx="0" dy="12" stdDeviation="8" flood-color="#000" flood-opacity="0.4"/>
          </filter>
          <pattern id="turf-stripes" width="1080" height="90" patternUnits="userSpaceOnUse">
            <rect y="0" width="1080" height="45" fill="#205c3c"/>
            <rect y="45" width="1080" height="45" fill="#1b4d32"/>
          </pattern>
        </defs>

        <!-- Stadium Sky & Floodlight Beams -->
        <rect width="1080" height="450" fill="#1d3557"/>
        <polygon points="120,40 280,450 0,450" fill="#f1faee" opacity="0.12"/>
        <polygon points="960,40 1080,450 800,450" fill="#f1faee" opacity="0.12"/>

        <!-- MCG Roof Canopy & Floodlight Towers -->
        <rect x="70" y="20" width="20" height="130" fill="#adb5bd"/>
        <polygon points="40,20 120,20 100,5 60,5" fill="#ced4da"/>
        <rect x="990" y="20" width="20" height="130" fill="#adb5bd"/>
        <polygon points="960,20 1040,20 1020,5 980,5" fill="#ced4da"/>

        <path d="M 0 120 Q 540 160 1080 120 L 1080 150 Q 540 190 0 150 Z" fill="#e9ecef" stroke="#adb5bd" stroke-width="4"/>

        <!-- MCG Grandstand Top Crowd Tier (Packed Melbourne spectators) -->
        <rect x="0" y="150" width="1080" height="140" fill="#102218"/>
        <!-- Multi-colored paper cutout crowd dots -->
        <g id="s1_crowd_dots">
          <!-- Row 1 -->
          <circle cx="50" cy="170" r="12" fill="#ffd166"/><circle cx="90" cy="170" r="12" fill="#ef476f"/><circle cx="130" cy="170" r="12" fill="#f8f9fa"/><circle cx="170" cy="170" r="12" fill="#06d6a0"/><circle cx="210" cy="170" r="12" fill="#ffd166"/><circle cx="250" cy="170" r="12" fill="#118ab2"/><circle cx="290" cy="170" r="12" fill="#f8f9fa"/><circle cx="330" cy="170" r="12" fill="#ef476f"/><circle cx="370" cy="170" r="12" fill="#ffd166"/><circle cx="410" cy="170" r="12" fill="#f8f9fa"/><circle cx="450" cy="170" r="12" fill="#06d6a0"/><circle cx="490" cy="170" r="12" fill="#ef476f"/><circle cx="530" cy="170" r="12" fill="#ffd166"/><circle cx="570" cy="170" r="12" fill="#118ab2"/><circle cx="610" cy="170" r="12" fill="#f8f9fa"/><circle cx="650" cy="170" r="12" fill="#ffd166"/><circle cx="690" cy="170" r="12" fill="#ef476f"/><circle cx="730" cy="170" r="12" fill="#06d6a0"/><circle cx="770" cy="170" r="12" fill="#ffd166"/><circle cx="810" cy="170" r="12" fill="#f8f9fa"/><circle cx="850" cy="170" r="12" fill="#118ab2"/><circle cx="890" cy="170" r="12" fill="#ef476f"/><circle cx="930" cy="170" r="12" fill="#ffd166"/><circle cx="970" cy="170" r="12" fill="#f8f9fa"/><circle cx="1010" cy="170" r="12" fill="#06d6a0"/>
          <!-- Row 2 -->
          <circle cx="70" cy="205" r="14" fill="#f8f9fa"/><circle cx="110" cy="205" r="14" fill="#ffd166"/><circle cx="150" cy="205" r="14" fill="#118ab2"/><circle cx="190" cy="205" r="14" fill="#ef476f"/><circle cx="230" cy="205" r="14" fill="#ffd166"/><circle cx="270" cy="205" r="14" fill="#06d6a0"/><circle cx="310" cy="205" r="14" fill="#f8f9fa"/><circle cx="350" cy="205" r="14" fill="#ffd166"/><circle cx="390" cy="205" r="14" fill="#ef476f"/><circle cx="430" cy="205" r="14" fill="#118ab2"/><circle cx="470" cy="205" r="14" fill="#ffd166"/><circle cx="510" cy="205" r="14" fill="#f8f9fa"/><circle cx="550" cy="205" r="14" fill="#06d6a0"/><circle cx="590" cy="205" r="14" fill="#ef476f"/><circle cx="630" cy="205" r="14" fill="#ffd166"/><circle cx="670" cy="205" r="14" fill="#118ab2"/><circle cx="710" cy="205" r="14" fill="#f8f9fa"/><circle cx="750" cy="205" r="14" fill="#ffd166"/><circle cx="790" cy="205" r="14" fill="#ef476f"/><circle cx="830" cy="205" r="14" fill="#06d6a0"/><circle cx="870" cy="205" r="14" fill="#ffd166"/><circle cx="910" cy="205" r="14" fill="#f8f9fa"/><circle cx="950" cy="205" r="14" fill="#118ab2"/><circle cx="990" cy="205" r="14" fill="#ef476f"/><circle cx="1030" cy="205" r="14" fill="#ffd166"/>
          <!-- Row 3 -->
          <circle cx="50" cy="245" r="15" fill="#ef476f"/><circle cx="90" cy="245" r="15" fill="#f8f9fa"/><circle cx="130" cy="245" r="15" fill="#ffd166"/><circle cx="170" cy="245" r="15" fill="#06d6a0"/><circle cx="210" cy="245" r="15" fill="#118ab2"/><circle cx="250" cy="245" r="15" fill="#ffd166"/><circle cx="290" cy="245" r="15" fill="#ef476f"/><circle cx="330" cy="245" r="15" fill="#f8f9fa"/><circle cx="370" cy="245" r="15" fill="#ffd166"/><circle cx="410" cy="245" r="15" fill="#06d6a0"/><circle cx="450" cy="245" r="15" fill="#ef476f"/><circle cx="490" cy="245" r="15" fill="#ffd166"/><circle cx="530" cy="245" r="15" fill="#f8f9fa"/><circle cx="570" cy="245" r="15" fill="#118ab2"/><circle cx="610" cy="245" r="15" fill="#ffd166"/><circle cx="650" cy="245" r="15" fill="#ef476f"/><circle cx="690" cy="245" r="15" fill="#06d6a0"/><circle cx="730" cy="245" r="15" fill="#f8f9fa"/><circle cx="770" cy="245" r="15" fill="#ffd166"/><circle cx="810" cy="245" r="15" fill="#118ab2"/><circle cx="850" cy="245" r="15" fill="#ef476f"/><circle cx="890" cy="245" r="15" fill="#ffd166"/><circle cx="930" cy="245" r="15" fill="#06d6a0"/><circle cx="970" cy="245" r="15" fill="#f8f9fa"/><circle cx="1010" cy="245" r="15" fill="#ffd166"/>
        </g>

        <!-- Stadium LED Boundary Ribbon -->
        <rect x="0" y="275" width="1080" height="42" fill="#c1121f"/>
        <text x="540" y="304" fill="#fff" font-size="24" font-family="Anton" letter-spacing="4" text-anchor="middle">MELBOURNE CRICKET GROUND • 90,000 STRONG • BOXING DAY TEST</text>

        <!-- MCG Outfield (Lush Mown Green Turf) -->
        <rect y="315" width="1080" height="1605" fill="url(#turf-stripes)"/>
        <!-- White boundary rope curve -->
        <path d="M 0 340 Q 540 375 1080 340" stroke="#fdf0d5" stroke-width="8" fill="none" opacity="0.8"/>

        <!-- Authentic Pitch Clay Center Strip -->
        <g transform="translate(320, 390)">
          <!-- Pitch dirt rectangle with paper texture edge -->
          <rect x="0" y="0" width="440" height="780" rx="12" fill="#d4a373" stroke="#b08968" stroke-width="4" filter="url(#drop-cut)"/>
          <!-- Pitch wear cracks and dry grass streaks -->
          <line x1="80" y1="120" x2="160" y2="180" stroke="#b08968" stroke-width="3" opacity="0.6"/>
          <line x1="280" y1="460" x2="350" y2="540" stroke="#b08968" stroke-width="3" opacity="0.6"/>
          <!-- Bowling crease and popping crease (Top end - Bumrah) -->
          <line x1="0" y1="110" x2="440" y2="110" stroke="#ffffff" stroke-width="6"/>
          <!-- Top Wickets & Bails -->
          <g transform="translate(195, 80)">
            <rect x="0" y="0" width="10" height="36" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
            <rect x="18" y="0" width="10" height="36" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
            <rect x="36" y="0" width="10" height="36" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
            <rect x="-3" y="-5" width="52" height="7" rx="2" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
          </g>
          <!-- Batting crease and popping crease (Bottom end - Konstas) -->
          <line x1="0" y1="670" x2="440" y2="670" stroke="#ffffff" stroke-width="6"/>
          <!-- Bottom Wickets & Bails -->
          <g transform="translate(195, 665)">
            <rect x="0" y="0" width="10" height="36" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
            <rect x="18" y="0" width="10" height="36" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
            <rect x="36" y="0" width="10" height="36" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
            <rect x="-3" y="-5" width="52" height="7" rx="2" fill="#fdf0d5" stroke="#333" stroke-width="2"/>
          </g>
        </g>

        <!-- ============================================== -->
        <!-- USER REQUIREMENT: "19 YEARS OLD" ON FIRST FRAME -->
        <!-- Visible immediately at t=0.00s! -->
        <!-- ============================================== -->
        <g id="s1_header_19yo" class="paper-shadow" transform="translate(90, 65)">
          <rect x="0" y="0" width="900" height="92" rx="16" fill="#c1121f" stroke="#FAF7F0" stroke-width="4"/>
          <text x="450" y="64" fill="#FAF7F0" font-size="52" font-family="Anton" letter-spacing="4" text-anchor="middle">⚡ 19 YEARS OLD • HIS TEST DEBUT</text>
        </g>

        <!-- Match clash banner -->
        <g id="s1_clash_badge" class="paper-shadow" transform="translate(140, 180)">
          <rect x="0" y="0" width="800" height="75" rx="12" fill="#FAF7F0" stroke="#11141a" stroke-width="4"/>
          <text x="400" y="52" fill="#11141a" font-size="38" font-family="Anton" letter-spacing="2" text-anchor="middle">JASPRIT BUMRAH <tspan fill="#c1121f">vs</tspan> SAM KONSTAS</text>
        </g>

        <!-- ============================================== -->
        <!-- CHARACTERS ON PITCH: BUMRAH & KONSTAS -->
        <!-- ============================================== -->
        <!-- Jasprit Bumrah (Left Bowler end, charging in) -->
        <g id="s1_bumrah_group" class="paper-shadow" transform="translate(130, 480)">
          <!-- India bowler body -->
          <path d="M 50 170 C 50 120, 150 120, 150 170 L 170 340 L 30 340 Z" fill="#f8f9fa" stroke="#111" stroke-width="5"/>
          <!-- India blue collar -->
          <polygon points="80,135 120,135 100,185" fill="#003566" stroke="#111" stroke-width="3"/>
          <!-- Bowling Arm with Ball -->
          <g id="s1_bumrah_arm" transform="translate(140, 145)">
            <!-- Arm angled backward in iconic sling action -->
            <rect x="0" y="-12" width="130" height="34" rx="16" fill="#c68b59" stroke="#111" stroke-width="4" transform="rotate(-35)"/>
            <!-- Cricket ball in hand -->
            <circle cx="115" cy="-75" r="22" fill="#c1121f" stroke="#111" stroke-width="4"/>
            <path d="M 98 -75 C 115 -85, 115 -65, 132 -75" stroke="#fff" stroke-width="3" fill="none"/>
          </g>
          <!-- Head with beard & navy headband -->
          <circle cx="100" cy="80" r="54" fill="#c68b59" stroke="#111" stroke-width="5"/>
          <!-- Blue India headband -->
          <path d="M 50 65 Q 100 55 150 65 L 148 45 Q 100 35 52 45 Z" fill="#003566" stroke="#111" stroke-width="3"/>
          <!-- Eyes & expressive mouth -->
          <ellipse cx="85" cy="78" rx="8" ry="10" fill="#fff" stroke="#111" stroke-width="2"/>
          <circle id="bumrah_pupil_l" cx="87" cy="78" r="4" fill="#111"/>
          <ellipse cx="115" cy="78" rx="8" ry="10" fill="#fff" stroke="#111" stroke-width="2"/>
          <circle id="bumrah_pupil_r" cx="117" cy="78" r="4" fill="#111"/>
          <ellipse cx="100" cy="104" rx="10" ry="6" fill="#331400"/>
          <!-- Name tag -->
          <rect x="15" y="325" width="170" height="42" rx="8" fill="#003566" stroke="#FAF7F0" stroke-width="3"/>
          <text x="100" y="354" fill="#ffd166" font-size="22" font-family="Anton" text-anchor="middle">JASPRIT BUMRAH</text>
        </g>

        <!-- Red Kookaburra Ball in delivery flight -->
        <g id="s1_match_ball" opacity="0" transform="translate(250, 410)">
          <circle cx="0" cy="0" r="20" fill="#c1121f" stroke="#111" stroke-width="4" filter="url(#drop-cut)"/>
          <line x1="-18" y1="0" x2="18" y2="0" stroke="#fff" stroke-width="3"/>
        </g>

        <!-- Sam Konstas (Right Batsman end, crouching into ramp) -->
        <g id="s1_konstas_group" class="paper-shadow" transform="translate(620, 720)">
          <!-- Aussie whites body -->
          <path d="M 60 170 C 60 110, 170 110, 170 170 L 190 350 L 40 350 Z" fill="#fdf0d5" stroke="#111" stroke-width="5"/>
          <!-- Green Aussie collar -->
          <polygon points="90,135 140,135 115,185" fill="#004b23" stroke="#111" stroke-width="3"/>
          <!-- Aussie Baggy Green Cap / Helmet -->
          <circle cx="115" cy="75" r="52" fill="#f1c095" stroke="#111" stroke-width="5"/>
          <path d="M 65 60 Q 115 25 165 60 L 175 75 Q 115 50 55 75 Z" fill="#004b23" stroke="#111" stroke-width="4"/>
          <circle cx="115" cy="50" r="9" fill="#ffd166"/>
          <!-- Aussie visor / grill -->
          <line x1="80" y1="90" x2="150" y2="90" stroke="#333" stroke-width="4"/>
          <!-- Eyes & determined look -->
          <ellipse cx="98" cy="72" rx="7" ry="9" fill="#fff" stroke="#111" stroke-width="2"/>
          <circle cx="99" cy="72" r="4" fill="#111"/>
          <ellipse cx="132" cy="72" rx="7" ry="9" fill="#fff" stroke="#111" stroke-width="2"/>
          <circle cx="133" cy="72" r="4" fill="#111"/>
          <!-- Bat & Arms (Ramp pose: bat angled high overhead over keeper) -->
          <g id="s1_konstas_bat" transform="translate(90, 130)">
            <!-- Arms holding handle -->
            <rect x="-10" y="-30" width="70" height="26" rx="12" fill="#f1c095" stroke="#111" stroke-width="4" transform="rotate(-40)"/>
            <!-- Bat blade angled upwards -->
            <g transform="translate(35, -45) rotate(-65)">
              <rect x="0" y="0" width="40" height="220" rx="8" fill="#e9c46a" stroke="#111" stroke-width="5"/>
              <!-- Green Kookaburra rubber grip -->
              <rect x="12" y="-90" width="16" height="95" rx="5" fill="#004b23" stroke="#111" stroke-width="3"/>
              <!-- Kookaburra logo stripe -->
              <rect x="5" y="40" width="30" height="40" fill="#004b23"/>
              <text x="20" y="66" fill="#ffd166" font-size="14" font-family="Anton" text-anchor="middle">KOOKA</text>
            </g>
          </g>
          <!-- Name tag -->
          <rect x="25" y="335" width="180" height="42" rx="8" fill="#004b23" stroke="#FAF7F0" stroke-width="3"/>
          <text x="115" y="364" fill="#ffd166" font-size="22" font-family="Anton" text-anchor="middle">SAM KONSTAS (19)</text>
        </g>

        <!-- Starburst Bat Crack on Ramp Shot -->
        <g id="s1_bat_crack" opacity="0" transform="translate(730, 710)">
          <polygon points="0,-45 14,-15 45,-20 22,5 40,35 10,22 -5,45 -18,18 -45,22 -22,-5 -35,-35 -8,-18" fill="#ffd166" stroke="#c1121f" stroke-width="5"/>
          <text x="0" y="10" fill="#c1121f" font-size="28" font-family="Anton" font-weight="bold" text-anchor="middle">CRACK!</text>
        </g>

        <!-- Ramp shot dotted flight trajectory arc -->
        <path id="s1_ramp_arc" d="M 730 710 Q 820 450 960 330" stroke="#ffd166" stroke-width="7" stroke-dasharray="14 10" fill="none" opacity="0"/>

        <!-- Bold comic action ribbon -->
        <g id="s1_action_stamp" class="paper-shadow" opacity="0" transform="translate(180, 1140)">
          <rect x="0" y="0" width="720" height="85" rx="14" fill="#ffd166" stroke="#11141a" stroke-width="5"/>
          <text x="360" y="58" fill="#11141a" font-size="44" font-family="Anton" letter-spacing="3" text-anchor="middle">🔥 AUDACIOUS RAMP OVER THIRD MAN!</text>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- SCENE 2: CUT TO 90,000 MCG CROWD WENT WILD! (6.69 - 12.4s) -->
    <!-- ======================================================== -->
    <div id="scene2" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- Sky & Massive Stadium Lighting -->
        <rect width="1080" height="1920" fill="#0f1f18"/>
        
        <!-- Giant Stadium Floodlights -->
        <g opacity="0.6">
          <circle cx="160" cy="80" r="70" fill="#fff" opacity="0.15"/>
          <circle cx="920" cy="80" r="70" fill="#fff" opacity="0.15"/>
        </g>

        <!-- 3 Tiers of Packed Grandstands (Great Southern Stand) -->
        <!-- Tier 3 (Top) -->
        <rect x="0" y="140" width="1080" height="260" fill="#1a382b" stroke="#000" stroke-width="4"/>
        <!-- Tier 2 (Middle) -->
        <rect x="0" y="400" width="1080" height="300" fill="#224838" stroke="#000" stroke-width="4"/>
        <!-- Tier 1 (Lower Bay 13) -->
        <rect x="0" y="700" width="1080" height="420" fill="#2d5e4a" stroke="#000" stroke-width="4"/>

        <!-- Massive Crowd Density: Animated Waves of Spectators -->
        <g id="s2_crowd_tier1">
          <!-- Spectators in Tier 1 with Australian flags, Indian flags, Bay 13 signs -->
          <!-- We render animated cheering paper cutout spectators -->
          <!-- Bay 13 Aussie Fans -->
          <g transform="translate(60, 720)">
            <!-- Fan 1 -->
            <circle cx="50" cy="80" r="28" fill="#f1c095" stroke="#111" stroke-width="3"/>
            <path d="M 20 80 Q 50 40 80 80 Z" fill="#ffd166"/>
            <rect x="25" y="105" width="50" height="90" rx="10" fill="#004b23"/>
            <!-- Waving flag -->
            <line x1="80" y1="110" x2="120" y2="40" stroke="#8d99ae" stroke-width="4"/>
            <rect x="120" y="25" width="60" height="36" fill="#004b23"/>
            <circle cx="150" cy="43" r="10" fill="#ffd166"/>
          </g>
          <!-- Fan 2: Indian supporter with Tiranga -->
          <g transform="translate(320, 710)">
            <circle cx="50" cy="80" r="28" fill="#c68b59" stroke="#111" stroke-width="3"/>
            <rect x="25" y="105" width="50" height="90" rx="10" fill="#003566"/>
            <!-- Indian Flag -->
            <line x1="10" y1="110" x2="-20" y2="30" stroke="#8d99ae" stroke-width="4"/>
            <rect x="-70" y="20" width="50" height="12" fill="#ff9933"/>
            <rect x="-70" y="32" width="50" height="12" fill="#ffffff"/>
            <rect x="-70" y="44" width="50" height="12" fill="#138808"/>
            <circle cx="-45" cy="38" r="4" fill="#000088"/>
          </g>
          <!-- Fan 3 & 4 with giant "BAY 13" Banner -->
          <g id="s2_bay13_banner" transform="translate(560, 750)" class="paper-shadow">
            <rect x="0" y="0" width="380" height="110" rx="14" fill="#ffd166" stroke="#111" stroke-width="5"/>
            <text x="190" y="72" fill="#111" font-size="62" font-family="Anton" letter-spacing="4" text-anchor="middle">BAY 13 GOES WILD!</text>
          </g>
        </g>

        <!-- Crowd Dot Grid for the remaining 90,000 visual density -->
        <g id="s2_dense_crowd" opacity="0.9">
          <!-- Rows of spectators filling Tier 2 & Tier 3 -->
          <rect x="40" y="200" width="1000" height="180" fill="#132c21" rx="8"/>
          <!-- Dynamic confetti & camera flashes -->
          <g id="s2_flashes">
            <circle cx="220" cy="240" r="14" fill="#fff" opacity="0.8"/>
            <circle cx="480" cy="310" r="18" fill="#fff" opacity="0.9"/>
            <circle cx="780" cy="220" r="16" fill="#fff" opacity="0.85"/>
            <circle cx="910" cy="290" r="20" fill="#fff" opacity="0.95"/>
            <circle cx="340" cy="460" r="16" fill="#fff" opacity="0.9"/>
            <circle cx="670" cy="520" r="18" fill="#fff" opacity="0.85"/>
          </g>
        </g>

        <!-- Giant Iconic MCG Scoreboard (Top Hero Element) -->
        <g id="s2_mcg_scoreboard" class="paper-shadow" transform="translate(80, 80)">
          <!-- Classic Dark Green & Yellow MCG Board -->
          <rect x="0" y="0" width="920" height="230" rx="18" fill="#0b291b" stroke="#ffd166" stroke-width="6"/>
          <!-- Header -->
          <rect x="0" y="0" width="920" height="60" rx="14" fill="#ffd166"/>
          <text x="460" y="44" fill="#0b291b" font-size="36" font-family="Anton" letter-spacing="4" text-anchor="middle">MELBOURNE CRICKET GROUND</text>
          <!-- Scoreboard Data -->
          <text x="460" y="125" fill="#FAF7F0" font-size="52" font-family="Anton" letter-spacing="3" text-anchor="middle">ATTENDANCE: <tspan fill="#ff4d4d">89,956</tspan></text>
          <text x="460" y="185" fill="#ffd166" font-size="44" font-family="Anton" letter-spacing="2" text-anchor="middle">BOXING DAY TEST • AUSTRALIA vs INDIA</text>
        </g>

        <!-- Giant 90,000 Roar Stamp in Center (Requested explicitly) -->
        <g id="s2_roar_card" class="paper-shadow" transform="translate(90, 480)">
          <rect x="0" y="0" width="900" height="200" rx="20" fill="#c1121f" stroke="#FAF7F0" stroke-width="6"/>
          <text x="450" y="90" fill="#ffd166" font-size="76" font-family="Anton" letter-spacing="4" text-anchor="middle">90,000 PEOPLE!</text>
          <text x="450" y="160" fill="#FAF7F0" font-size="48" font-family="Anton" letter-spacing="2" text-anchor="middle">THE LARGEST CROWD IN WORLD CRICKET</text>
        </g>

        <!-- Cheering Foreground Cutout Characters (Aussie & Indian Cricket Fans) -->
        <g id="s2_front_fans" transform="translate(100, 940)">
          <!-- Australian Fan with Aussie Flag & Bucket Hat -->
          <g transform="translate(80, 0)" class="paper-shadow">
            <circle cx="60" cy="60" r="38" fill="#f1c095" stroke="#111" stroke-width="4"/>
            <!-- Bucket hat -->
            <polygon points="10,50 110,50 95,20 25,20" fill="#ffd166" stroke="#111" stroke-width="3"/>
            <!-- Body -->
            <path d="M 20 100 L 100 100 L 115 220 L 5 220 Z" fill="#004b23" stroke="#111" stroke-width="4"/>
            <text x="60" y="160" fill="#ffd166" font-size="28" font-family="Anton" text-anchor="middle">AUS</text>
          </g>
          <!-- Indian Fan with Indian Tricolour Headband -->
          <g transform="translate(620, 0)" class="paper-shadow">
            <circle cx="60" cy="60" r="38" fill="#c68b59" stroke="#111" stroke-width="4"/>
            <!-- Saffron White Green Headband -->
            <rect x="22" y="38" width="76" height="18" fill="#ff9933" stroke="#111" stroke-width="2"/>
            <!-- Body -->
            <path d="M 20 100 L 100 100 L 115 220 L 5 220 Z" fill="#003566" stroke="#111" stroke-width="4"/>
            <text x="60" y="160" fill="#fff" font-size="28" font-family="Anton" text-anchor="middle">INDIA</text>
          </g>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- SCENE 3: WHAT IS BOXING DAY? & 26 DECEMBER MCG (12.4 - 20.8s) -->
    <!-- ======================================================== -->
    <div id="scene3" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- Summer Melbourne Sky & MCG Outfield -->
        <rect width="1080" height="650" fill="#4a90e2"/>
        <circle cx="900" cy="180" r="90" fill="#ffd166" opacity="0.85"/>
        <rect y="650" width="1080" height="1270" fill="url(#turf-stripes)"/>

        <!-- Question Hero Banner -->
        <g id="s3_hero_q" class="paper-shadow" transform="translate(100, 90)">
          <rect x="0" y="0" width="880" height="100" rx="16" fill="#11141a" stroke="#ffd166" stroke-width="5"/>
          <text x="440" y="68" fill="#ffd166" font-size="52" font-family="Anton" letter-spacing="4" text-anchor="middle">SO WHAT IS BOXING DAY CRICKET?</text>
        </g>

        <!-- Giant Vintage Flip Calendar Card (26 DECEMBER) -->
        <g id="s3_calendar_card" class="paper-shadow" transform="translate(240, 240)">
          <!-- Calendar top binder bar -->
          <rect x="0" y="0" width="600" height="70" rx="14" fill="#c1121f" stroke="#111" stroke-width="4"/>
          <!-- Calendar rings -->
          <rect x="90" y="-15" width="20" height="35" rx="6" fill="#adb5bd" stroke="#111" stroke-width="3"/>
          <rect x="290" y="-15" width="20" height="35" rx="6" fill="#adb5bd" stroke="#111" stroke-width="3"/>
          <rect x="490" y="-15" width="20" height="35" rx="6" fill="#adb5bd" stroke="#111" stroke-width="3"/>
          <text x="300" y="48" fill="#FAF7F0" font-size="34" font-family="Anton" letter-spacing="4" text-anchor="middle">DECEMBER 2026</text>
          <!-- Calendar date paper leaf -->
          <rect x="0" y="66" width="600" height="340" rx="12" fill="#FAF7F0" stroke="#111" stroke-width="4"/>
          <text x="300" y="270" fill="#c1121f" font-size="180" font-family="Anton" text-anchor="middle">26</text>
          <text x="300" y="360" fill="#11141a" font-size="44" font-family="Anton" letter-spacing="6" text-anchor="middle">BOXING DAY</text>
        </g>

        <!-- Iconic MCG Stadium Gate & Melbourne Tradition Card -->
        <g id="s3_mcg_tradition" class="paper-shadow" transform="translate(90, 720)">
          <rect x="0" y="0" width="900" height="380" rx="20" fill="#FAF7F0" stroke="#004b23" stroke-width="6"/>
          <!-- Top green header strip -->
          <rect x="0" y="0" width="900" height="80" rx="14" fill="#004b23"/>
          <text x="450" y="56" fill="#ffd166" font-size="44" font-family="Anton" letter-spacing="3" text-anchor="middle">AN UNBROKEN CRICKET TRADITION</text>
          <!-- Explainer details -->
          <text x="450" y="150" fill="#111" font-size="46" font-family="Anton" text-anchor="middle">EVERY YEAR SINCE 1980</text>
          <text x="450" y="210" fill="#c1121f" font-size="52" font-family="Anton" text-anchor="middle">AUSTRALIA HOSTS A TEST MATCH</text>
          <!-- Sub-badge -->
          <rect x="100" y="255" width="700" height="85" rx="12" fill="#e9f5ed" stroke="#004b23" stroke-width="3"/>
          <text x="450" y="312" fill="#004b23" font-size="38" font-family="Anton" letter-spacing="2" text-anchor="middle">AT THE CATHEDRAL OF CRICKET: THE MCG</text>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- SCENE 4: FAMILIES SKIP LEFTOVERS & BIGGEST DAYS (20.8 - 26.9s) -->
    <!-- ======================================================== -->
    <div id="scene4" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- Summer Ground & Festive Atmosphere -->
        <rect width="1080" height="1920" fill="#143525"/>
        <rect y="0" width="1080" height="400" fill="#2d6a4f"/>

        <!-- Top Header Badge -->
        <g id="s4_header_leftovers" class="paper-shadow" transform="translate(90, 80)">
          <rect x="0" y="0" width="900" height="95" rx="16" fill="#ffd166" stroke="#111" stroke-width="5"/>
          <text x="450" y="65" fill="#111" font-size="48" font-family="Anton" letter-spacing="3" text-anchor="middle">FAMILIES SKIP CHRISTMAS LEFTOVERS...</text>
        </g>

        <!-- Christmas Feast Table vs MCG Cricket Tickets (Split Card) -->
        <g id="s4_feast_card" class="paper-shadow" transform="translate(100, 215)">
          <rect x="0" y="0" width="880" height="400" rx="18" fill="#FAF7F0" stroke="#c1121f" stroke-width="5"/>
          <!-- Left: Christmas Leftovers Table -->
          <g transform="translate(40, 40)">
            <rect x="0" y="0" width="360" height="320" rx="12" fill="#f8edeb" stroke="#c1121f" stroke-width="3"/>
            <text x="180" y="55" fill="#c1121f" font-size="34" font-family="Anton" text-anchor="middle">CHRISTMAS ROAST</text>
            <!-- Turkey / Roast illustration -->
            <ellipse cx="180" cy="150" rx="80" ry="50" fill="#b07d62" stroke="#111" stroke-width="4"/>
            <rect x="160" y="180" width="40" height="20" rx="6" fill="#f1c095"/>
            <!-- Stamped text "LEFT IN FRIDGE!" -->
            <g transform="translate(40, 240) rotate(-6)">
              <rect x="0" y="0" width="280" height="50" rx="8" fill="#c1121f"/>
              <text x="140" y="36" fill="#fff" font-size="28" font-family="Anton" text-anchor="middle">STAYS IN THE FRIDGE!</text>
            </g>
          </g>
          <!-- Arrow pointing to the right -->
          <polygon points="425,180 455,200 425,220" fill="#111"/>
          <!-- Right: Melbourne Test Match Ticket -->
          <g transform="translate(480, 40)">
            <rect x="0" y="0" width="360" height="320" rx="12" fill="#e9f5ed" stroke="#004b23" stroke-width="3"/>
            <text x="180" y="55" fill="#004b23" font-size="34" font-family="Anton" text-anchor="middle">MCG ADMISSION</text>
            <rect x="40" y="80" width="280" height="140" rx="10" fill="#fff" stroke="#004b23" stroke-width="3" stroke-dasharray="8 6"/>
            <text x="180" y="130" fill="#004b23" font-size="38" font-family="Anton" text-anchor="middle">ADMIT ONE</text>
            <text x="180" y="175" fill="#c1121f" font-size="30" font-family="Anton" text-anchor="middle">BOXING DAY</text>
            <!-- Subtitle -->
            <rect x="40" y="240" width="280" height="50" rx="8" fill="#004b23"/>
            <text x="180" y="276" fill="#ffd166" font-size="26" font-family="Anton" text-anchor="middle">HEADING TO THE 'G!</text>
          </g>
        </g>

        <!-- Aussie Family Heading to the Cricket (Dad, Mum, Kid with Esky cooler) -->
        <g id="s4_family_group" class="paper-shadow" transform="translate(140, 670)">
          <!-- Dad with Esky cooler & floppy hat -->
          <g transform="translate(60, 0)">
            <circle cx="70" cy="70" r="42" fill="#f1c095" stroke="#111" stroke-width="4"/>
            <!-- Floppy sun hat -->
            <ellipse cx="70" cy="50" rx="65" ry="18" fill="#e9c46a" stroke="#111" stroke-width="3"/>
            <!-- Body -->
            <rect x="30" y="110" width="80" height="160" rx="12" fill="#ffd166" stroke="#111" stroke-width="4"/>
            <!-- Blue Esky Cooler Box in hand -->
            <g transform="translate(115, 170)">
              <rect x="0" y="0" width="95" height="85" rx="8" fill="#0077b6" stroke="#111" stroke-width="4"/>
              <rect x="-4" y="-8" width="103" height="16" rx="4" fill="#fff" stroke="#111" stroke-width="3"/>
              <text x="47" y="52" fill="#fff" font-size="22" font-family="Anton" text-anchor="middle">ESKY</text>
            </g>
          </g>
          <!-- Kid with Baggy Green cap holding mini bat -->
          <g transform="translate(320, 90)">
            <circle cx="50" cy="50" r="32" fill="#f1c095" stroke="#111" stroke-width="3"/>
            <path d="M 20 40 Q 50 15 80 40 Z" fill="#004b23"/>
            <rect x="25" y="80" width="50" height="100" rx="8" fill="#004b23" stroke="#111" stroke-width="3"/>
            <!-- Mini bat -->
            <rect x="80" y="70" width="16" height="90" rx="4" fill="#e9c46a" stroke="#111" stroke-width="3" transform="rotate(25)"/>
          </g>
          <!-- Mum with sunglasses & drink bottle -->
          <g transform="translate(500, 20)">
            <circle cx="60" cy="60" r="38" fill="#f1c095" stroke="#111" stroke-width="4"/>
            <!-- Sunglasses -->
            <rect x="35" y="52" width="22" height="14" rx="4" fill="#111"/>
            <rect x="63" y="52" width="22" height="14" rx="4" fill="#111"/>
            <rect x="25" y="95" width="70" height="145" rx="10" fill="#e76f51" stroke="#111" stroke-width="4"/>
          </g>
        </g>

        <!-- Big Card: "ONE OF THE BIGGEST DAYS IN WORLD CRICKET" -->
        <g id="s4_biggest_days_stamp" class="paper-shadow" transform="translate(90, 1070)">
          <rect x="0" y="0" width="900" height="100" rx="16" fill="#c1121f" stroke="#FAF7F0" stroke-width="5"/>
          <text x="450" y="68" fill="#FAF7F0" font-size="50" font-family="Anton" letter-spacing="3" text-anchor="middle">THE BIGGEST DAY IN WORLD CRICKET</text>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- SCENE 5A: SHANE WARNE'S 1994 HAT-TRICK (26.9 - 32.2s) -->
    <!-- ======================================================== -->
    <div id="scene5a" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- Melbourne Pitch & Stadium Atmosphere -->
        <rect width="1080" height="1920" fill="#1b4332"/>
        <rect y="0" width="1080" height="420" fill="#081c15"/>

        <!-- Top Legends Header -->
        <g id="s5a_legends_title" class="paper-shadow" transform="translate(100, 75)">
          <rect x="0" y="0" width="880" height="85" rx="14" fill="#ffd166" stroke="#111" stroke-width="5"/>
          <text x="440" y="60" fill="#111" font-size="50" font-family="Anton" letter-spacing="4" text-anchor="middle">AND IT CREATES LEGENDS...</text>
        </g>

        <!-- Match Banner: 1994 ASHES HAT-TRICK -->
        <g id="s5a_warne_badge" class="paper-shadow" transform="translate(100, 185)">
          <rect x="0" y="0" width="880" height="95" rx="16" fill="#c1121f" stroke="#FAF7F0" stroke-width="4"/>
          <text x="440" y="64" fill="#FAF7F0" font-size="48" font-family="Anton" letter-spacing="3" text-anchor="middle">1994: SHANE WARNE'S ASHES HAT-TRICK!</text>
        </g>

        <!-- Authentic Pitch Ground Scene -->
        <g transform="translate(200, 310)">
          <rect x="0" y="0" width="680" height="800" rx="16" fill="#d4a373" stroke="#b08968" stroke-width="4" filter="url(#drop-cut)"/>
          <line x1="0" y1="620" x2="680" y2="620" stroke="#fff" stroke-width="6"/>

          <!-- Shattered England Stumps Flying in the Air! -->
          <g id="s5a_shattered_stumps" transform="translate(320, 580)">
            <!-- Off stump flying left -->
            <rect x="-40" y="-80" width="12" height="70" rx="3" fill="#fdf0d5" stroke="#111" stroke-width="3" transform="rotate(-45)"/>
            <!-- Middle stump flattened -->
            <rect x="0" y="-10" width="12" height="70" rx="3" fill="#fdf0d5" stroke="#111" stroke-width="3" transform="rotate(25)"/>
            <!-- Leg stump sent cartwheeling right -->
            <rect x="60" y="-60" width="12" height="70" rx="3" fill="#fdf0d5" stroke="#111" stroke-width="3" transform="rotate(70)"/>
            <!-- Bails flying -->
            <rect x="-10" y="-120" width="28" height="6" fill="#fdf0d5" stroke="#111" stroke-width="2" transform="rotate(110)"/>
            <rect x="40" y="-100" width="28" height="6" fill="#fdf0d5" stroke="#111" stroke-width="2" transform="rotate(-85)"/>
          </g>
        </g>

        <!-- Shane Warne Full Character Rig (Blonde hair, white zinc, celebratory run) -->
        <g id="s5a_warne_hero" class="paper-shadow" transform="translate(360, 450)">
          <!-- Aussie whites body -->
          <path d="M 60 170 C 60 110, 180 110, 180 170 L 200 370 L 40 370 Z" fill="#fdf0d5" stroke="#111" stroke-width="5"/>
          <polygon points="95,135 145,135 120,185" fill="#004b23" stroke="#111" stroke-width="3"/>
          <!-- Arms spread wide in legendary celebration -->
          <g id="s5a_warne_arms">
            <!-- Left arm outstretched -->
            <rect x="-110" y="140" width="140" height="32" rx="14" fill="#f1c095" stroke="#111" stroke-width="4" transform="rotate(-20)"/>
            <!-- Right arm outstretched -->
            <rect x="160" y="140" width="140" height="32" rx="14" fill="#f1c095" stroke="#111" stroke-width="4" transform="rotate(20)"/>
          </g>
          <!-- Head with iconic blonde curly hair & zinc stripe -->
          <circle cx="120" cy="75" r="54" fill="#f1c095" stroke="#111" stroke-width="5"/>
          <!-- Blonde hair -->
          <path d="M 65 60 Q 120 15 175 60 Q 190 35 160 20 Q 120 5 80 20 Q 50 35 65 60 Z" fill="#ffd166" stroke="#111" stroke-width="4"/>
          <!-- White zinc cream on nose -->
          <rect x="115" y="65" width="10" height="22" rx="3" fill="#ffffff" stroke="#111" stroke-width="2"/>
          <!-- Wide ecstatic smile -->
          <path d="M 100 105 Q 120 125 140 105 Z" fill="#c1121f" stroke="#111" stroke-width="3"/>
          <!-- Name badge -->
          <rect x="25" y="350" width="190" height="44" rx="8" fill="#004b23" stroke="#FAF7F0" stroke-width="3"/>
          <text x="120" y="381" fill="#ffd166" font-size="24" font-family="Anton" text-anchor="middle">SHANE WARNE</text>
        </g>

        <!-- Hat-trick summary card -->
        <g id="s5a_hattrick_box" class="paper-shadow" transform="translate(100, 1070)">
          <rect x="0" y="0" width="880" height="110" rx="16" fill="#FAF7F0" stroke="#004b23" stroke-width="5"/>
          <text x="440" y="50" fill="#004b23" font-size="40" font-family="Anton" text-anchor="middle">3 ENGLISH WICKETS IN 3 BALLS!</text>
          <text x="440" y="95" fill="#c1121f" font-size="36" font-family="Anton" text-anchor="middle">FIRST ASHES HAT-TRICK AT MCG IN 90 YEARS</text>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- SCENE 5B: AJINKYA RAHANE'S 2020 CENTURY (32.2 - 37.5s) -->
    <!-- ======================================================== -->
    <div id="scene5b" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- MCG Stadium & India Comeback -->
        <rect width="1080" height="1920" fill="#0d2b45"/>
        <rect y="0" width="1080" height="420" fill="#001829"/>

        <!-- Top Header -->
        <g id="s5b_rahane_header" class="paper-shadow" transform="translate(90, 75)">
          <rect x="0" y="0" width="900" height="85" rx="14" fill="#0077b6" stroke="#FAF7F0" stroke-width="4"/>
          <text x="450" y="60" fill="#FAF7F0" font-size="46" font-family="Anton" letter-spacing="3" text-anchor="middle">2020: INDIA'S GREATEST COMEBACK</text>
        </g>

        <!-- MCG Scoreboard Card -->
        <g id="s5b_scoreboard" class="paper-shadow" transform="translate(90, 180)">
          <rect x="0" y="0" width="900" height="120" rx="16" fill="#11141a" stroke="#ffd166" stroke-width="4"/>
          <text x="450" y="55" fill="#ffd166" font-size="44" font-family="Anton" letter-spacing="2" text-anchor="middle">MELBOURNE TEST • CAPTAIN'S KNOCK</text>
          <text x="450" y="105" fill="#FAF7F0" font-size="42" font-family="Anton" letter-spacing="3" text-anchor="middle">AJINKYA RAHANE: <tspan fill="#4cc9f0">112</tspan> • INDIA WIN BY 8 WICKETS!</text>
        </g>

        <!-- Pitch Ground Scene -->
        <g transform="translate(200, 320)">
          <rect x="0" y="0" width="680" height="780" rx="16" fill="#d4a373" stroke="#b08968" stroke-width="4" filter="url(#drop-cut)"/>
          <line x1="0" y1="620" x2="680" y2="620" stroke="#fff" stroke-width="6"/>
        </g>

        <!-- Ajinkya Rahane Celebrating His 100 (Helmet off in left hand, Bat raised in right) -->
        <g id="s5b_rahane_hero" class="paper-shadow" transform="translate(370, 480)">
          <!-- India whites body -->
          <path d="M 50 170 C 50 110, 170 110, 170 170 L 190 370 L 30 370 Z" fill="#f8f9fa" stroke="#111" stroke-width="5"/>
          <polygon points="85,135 135,135 110,185" fill="#003566" stroke="#111" stroke-width="3"/>
          <!-- Left Arm holding Blue Helmet aloft -->
          <g id="s5b_left_arm" transform="translate(40, 150)">
            <rect x="-80" y="-80" width="30" height="100" rx="14" fill="#c68b59" stroke="#111" stroke-width="4" transform="rotate(-30)"/>
            <!-- India blue helmet held in fist -->
            <g transform="translate(-100, -110)">
              <circle cx="25" cy="25" r="28" fill="#003566" stroke="#111" stroke-width="3"/>
              <rect x="5" y="25" width="40" height="6" fill="#ffd166"/>
              <line x1="10" y1="35" x2="40" y2="35" stroke="#8d99ae" stroke-width="3"/>
            </g>
          </g>
          <!-- Right Arm holding Bat raised in triumph -->
          <g id="s5b_right_arm" transform="translate(180, 150)">
            <rect x="50" y="-80" width="30" height="100" rx="14" fill="#c68b59" stroke="#111" stroke-width="4" transform="rotate(30)"/>
            <!-- Cricket bat raised high -->
            <g transform="translate(60, -170)">
              <rect x="0" y="0" width="36" height="160" rx="6" fill="#e9c46a" stroke="#111" stroke-width="4"/>
              <rect x="10" y="160" width="16" height="70" rx="4" fill="#fff" stroke="#111" stroke-width="2"/>
              <rect x="4" y="30" width="28" height="40" fill="#003566"/>
              <text x="18" y="58" fill="#fff" font-size="18" font-family="Anton" text-anchor="middle">100</text>
            </g>
          </g>
          <!-- Head with beard & sweat -->
          <circle cx="110" cy="75" r="50" fill="#c68b59" stroke="#111" stroke-width="5"/>
          <!-- Black hair -->
          <path d="M 65 60 Q 110 30 155 60 Z" fill="#111" stroke="#111" stroke-width="3"/>
          <!-- Proud smile -->
          <path d="M 95 105 Q 110 120 125 105 Z" fill="#fff" stroke="#111" stroke-width="2"/>
          <!-- Name badge -->
          <rect x="15" y="350" width="190" height="44" rx="8" fill="#003566" stroke="#FAF7F0" stroke-width="3"/>
          <text x="110" y="381" fill="#ffd166" font-size="24" font-family="Anton" text-anchor="middle">AJINKYA RAHANE</text>
        </g>

        <!-- Comeback triumph banner -->
        <g id="s5b_comeback_stamp" class="paper-shadow" transform="translate(100, 1070)">
          <rect x="0" y="0" width="880" height="110" rx="16" fill="#FAF7F0" stroke="#003566" stroke-width="5"/>
          <text x="440" y="50" fill="#003566" font-size="40" font-family="Anton" text-anchor="middle">AFTER 36 ALL OUT IN ADELAIDE...</text>
          <text x="440" y="95" fill="#c1121f" font-size="38" font-family="Anton" text-anchor="middle">INDIA CAME BACK TO WIN AT THE MCG!</text>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- SCENE 6: PUBLIC HOLIDAY & BOXING DAY IS FOR TEST CRICKET (37.5 - 47.1s) -->
    <!-- ======================================================== -->
    <div id="scene6" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- Melbourne Summer Green Atmosphere -->
        <rect width="1080" height="1920" fill="#143525"/>
        <rect y="0" width="1080" height="480" fill="#1b4d3e"/>

        <!-- Top Header: SO WHY BOXING DAY? -->
        <g id="s6_q_badge" class="paper-shadow" transform="translate(100, 75)">
          <rect x="0" y="0" width="880" height="85" rx="14" fill="#ffd166" stroke="#111" stroke-width="5"/>
          <text x="440" y="60" fill="#111" font-size="50" font-family="Anton" letter-spacing="4" text-anchor="middle">SO WHY "BOXING DAY"?</text>
        </g>

        <!-- Public Holiday Stamp -->
        <g id="s6_holiday_stamp" class="paper-shadow" transform="translate(90, 185)">
          <rect x="0" y="0" width="900" height="130" rx="18" fill="#FAF7F0" stroke="#004b23" stroke-width="5"/>
          <text x="450" y="58" fill="#004b23" font-size="48" font-family="Anton" letter-spacing="3" text-anchor="middle">IT'S A PUBLIC HOLIDAY IN AUSTRALIA</text>
          <text x="450" y="112" fill="#c1121f" font-size="40" font-family="Anton" letter-spacing="2" text-anchor="middle">EVERYONE'S OFF WORK • EVERYONE GOES TO CRICKET!</text>
        </g>

        <!-- Dramatic Split Card: Christmas vs Boxing Day -->
        <g id="s6_versus_card" class="paper-shadow" transform="translate(80, 340)">
          <rect x="0" y="0" width="920" height="780" rx="22" fill="#0d1b1e" stroke="#FAF7F0" stroke-width="6"/>
          
          <!-- Top Half: Christmas is for Family -->
          <g transform="translate(40, 30)">
            <rect x="0" y="0" width="840" height="320" rx="16" fill="#2d6a4f" stroke="#FAF7F0" stroke-width="3"/>
            <!-- Christmas Tree Icon -->
            <polygon points="120,60 70,160 170,160" fill="#52b788" stroke="#111" stroke-width="3"/>
            <polygon points="120,110 50,220 190,220" fill="#40916c" stroke="#111" stroke-width="3"/>
            <rect x="105" y="220" width="30" height="40" fill="#774936"/>
            <circle cx="120" cy="50" r="14" fill="#ffd166"/>
            <!-- Text -->
            <text x="500" y="140" fill="#FAF7F0" font-size="52" font-family="Anton" letter-spacing="3" text-anchor="middle">DECEMBER 25:</text>
            <text x="500" y="210" fill="#ffd166" font-size="64" font-family="Anton" letter-spacing="3" text-anchor="middle">CHRISTMAS IS FOR FAMILY</text>
          </g>

          <!-- Bottom Half: Boxing Day is for Test Cricket -->
          <g transform="translate(40, 380)">
            <rect x="0" y="0" width="840" height="350" rx="16" fill="#c1121f" stroke="#ffd166" stroke-width="4"/>
            <!-- Giant Red Cricket Ball with Stitches -->
            <circle cx="120" cy="170" r="75" fill="#9e2a2b" stroke="#FAF7F0" stroke-width="5" filter="url(#drop-cut)"/>
            <path d="M 50 170 Q 120 130 190 170" stroke="#fff" stroke-width="5" stroke-dasharray="8 6" fill="none"/>
            <path d="M 50 170 Q 120 210 190 170" stroke="#fff" stroke-width="5" stroke-dasharray="8 6" fill="none"/>
            <!-- Text -->
            <text x="510" y="130" fill="#ffd166" font-size="50" font-family="Anton" letter-spacing="3" text-anchor="middle">DECEMBER 26:</text>
            <text x="510" y="215" fill="#FAF7F0" font-size="66" font-family="Anton" letter-spacing="4" text-anchor="middle">BOXING DAY IS FOR</text>
            <text x="510" y="295" fill="#ffd166" font-size="78" font-family="Anton" letter-spacing="6" text-anchor="middle">TEST CRICKET!</text>
          </g>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- SCENE 7: PINNED DEBATE COMMENT CARD & CALL TO ACTION (47.1 - 52.61s) -->
    <!-- USER REQUIREMENT: Pin a comment "Konstas vs Bumrah: best debut moment ever?" -->
    <!-- ======================================================== -->
    <div id="scene7" class="scene">
      <svg viewBox="0 0 1080 1920" width="1080" height="1920">
        <!-- Melbourne Ground Background with 4 Legends -->
        <rect width="1080" height="1920" fill="#143525"/>
        <rect y="0" width="1080" height="360" fill="#081c15"/>

        <!-- Top Header Banner -->
        <g id="s7_cta_header" class="paper-shadow" transform="translate(90, 75)">
          <rect x="0" y="0" width="900" height="85" rx="14" fill="#ffd166" stroke="#111" stroke-width="5"/>
          <text x="450" y="60" fill="#111" font-size="48" font-family="Anton" letter-spacing="4" text-anchor="middle">WHAT'S YOUR GREATEST BOXING DAY MEMORY?</text>
        </g>

        <!-- 4 Cricket Icons Lineup on MCG Turf -->
        <g id="s7_cricket_icons" class="paper-shadow" transform="translate(80, 180)">
          <!-- Icon 1: Sam Konstas -->
          <g transform="translate(40, 0)">
            <circle cx="50" cy="50" r="34" fill="#f1c095" stroke="#111" stroke-width="3"/>
            <path d="M 20 40 Q 50 15 80 40 Z" fill="#004b23"/>
            <rect x="25" y="80" width="50" height="80" rx="8" fill="#fdf0d5" stroke="#111" stroke-width="3"/>
            <text x="50" y="185" fill="#ffd166" font-size="20" font-family="Anton" text-anchor="middle">KONSTAS</text>
          </g>
          <!-- Icon 2: Jasprit Bumrah -->
          <g transform="translate(280, 0)">
            <circle cx="50" cy="50" r="34" fill="#c68b59" stroke="#111" stroke-width="3"/>
            <rect x="20" y="32" width="60" height="12" fill="#003566"/>
            <rect x="25" y="80" width="50" height="80" rx="8" fill="#f8f9fa" stroke="#111" stroke-width="3"/>
            <text x="50" y="185" fill="#4cc9f0" font-size="20" font-family="Anton" text-anchor="middle">BUMRAH</text>
          </g>
          <!-- Icon 3: Shane Warne -->
          <g transform="translate(520, 0)">
            <circle cx="50" cy="50" r="34" fill="#f1c095" stroke="#111" stroke-width="3"/>
            <path d="M 20 40 Q 50 10 80 40 Z" fill="#ffd166"/>
            <rect x="25" y="80" width="50" height="80" rx="8" fill="#fdf0d5" stroke="#111" stroke-width="3"/>
            <text x="50" y="185" fill="#ffd166" font-size="20" font-family="Anton" text-anchor="middle">WARNE</text>
          </g>
          <!-- Icon 4: Ajinkya Rahane -->
          <g transform="translate(760, 0)">
            <circle cx="50" cy="50" r="34" fill="#c68b59" stroke="#111" stroke-width="3"/>
            <path d="M 20 40 Q 50 20 80 40 Z" fill="#111"/>
            <rect x="25" y="80" width="50" height="80" rx="8" fill="#f8f9fa" stroke="#111" stroke-width="3"/>
            <text x="50" y="185" fill="#4cc9f0" font-size="20" font-family="Anton" text-anchor="middle">RAHANE</text>
          </g>
        </g>

        <!-- ============================================== -->
        <!-- USER REQUIREMENT: PINNED DEBATE COMMENT CARD   -->
        <!-- "Konstas vs Bumrah: best debut moment ever?"   -->
        <!-- ============================================== -->
        <g id="s7_pinned_comment_card" class="paper-shadow" transform="translate(70, 420)">
          <!-- Comment Box Frame -->
          <rect x="0" y="0" width="940" height="480" rx="22" fill="#FAF7F0" stroke="#c1121f" stroke-width="6"/>
          
          <!-- Top Pinned Tag Bar -->
          <g transform="translate(30, 25)">
            <rect x="0" y="0" width="240" height="45" rx="8" fill="#c1121f"/>
            <text x="120" y="32" fill="#fff" font-size="26" font-family="Anton" letter-spacing="2" text-anchor="middle">📌 PINNED DEBATE</text>
          </g>
          <!-- Social Handle & Verified Badge -->
          <circle cx="70" cy="115" r="32" fill="#004b23"/>
          <text x="70" y="126" fill="#ffd166" font-size="30" font-family="Anton" text-anchor="middle">🏏</text>
          <text x="120" y="115" fill="#111" font-size="32" font-family="Anton">CricketDebate</text>
          <circle cx="280" cy="105" r="10" fill="#0077b6"/>
          <text x="280" y="112" fill="#fff" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">✓</text>
          <text x="120" y="138" fill="#666" font-size="22" font-family="sans-serif">Pinned by Creator • 2h ago</text>

          <!-- Core Debated Question (Exact wording requested by user) -->
          <g transform="translate(40, 170)">
            <rect x="0" y="0" width="860" height="190" rx="14" fill="#fdf0d5" stroke="#b08968" stroke-width="3"/>
            <text x="430" y="70" fill="#c1121f" font-size="46" font-family="Anton" letter-spacing="2" text-anchor="middle">“KONSTAS VS BUMRAH:</text>
            <text x="430" y="125" fill="#111" font-size="48" font-family="Anton" letter-spacing="2" text-anchor="middle">BEST DEBUT MOMENT EVER?”</text>
            <text x="430" y="165" fill="#004b23" font-size="30" font-family="Anton" letter-spacing="2" text-anchor="middle">OR WARNE'S HAT-TRICK? RAHANE'S 100?</text>
          </g>

          <!-- Social Engagement Stats Bar -->
          <g transform="translate(50, 410)">
            <text x="0" y="30" fill="#555" font-size="28" font-family="Anton">❤️ 54.8K LIKES</text>
            <text x="320" y="30" fill="#555" font-size="28" font-family="Anton">💬 4,210 COMMENTS</text>
            <text x="700" y="30" fill="#c1121f" font-size="28" font-family="Anton">🔥 TOP DEBATE</text>
          </g>
        </g>

        <!-- Call To Action Arrow & Stamp -->
        <g id="s7_comment_cta" class="paper-shadow" transform="translate(100, 950)">
          <rect x="0" y="0" width="880" height="150" rx="20" fill="#ffd166" stroke="#11141a" stroke-width="6"/>
          <text x="440" y="65" fill="#11141a" font-size="52" font-family="Anton" letter-spacing="3" text-anchor="middle">👇 DROP YOUR PICK BELOW!</text>
          <text x="440" y="122" fill="#c1121f" font-size="40" font-family="Anton" letter-spacing="2" text-anchor="middle">WHAT'S YOUR FAVORITE BOXING DAY MOMENT?</text>
        </g>
      </svg>
    </div>

    <!-- ======================================================== -->
    <!-- CAPTION PEDESTAL ZONE (y = 1260 to 1480, ZERO OVERLAP) -->
    <!-- ======================================================== -->
    <div id="caption-zone">
      {"".join([f'<div id="cap_{i}" class="caption-card">{c["html"]}</div>' for i, c in enumerate(captions)])}
    </div>
  </div>

  <!-- GSAP Animation Engine -->
  <script>
    const tl = gsap.timeline({{ paused: true }});

    // Make seekFrame globally available for Playwright screenshotting
    window.seekFrame = function(timeInSeconds) {{
      tl.seek(timeInSeconds);
    }};

    // ----------------------------------------------------
    // SCENE TIMINGS & VISIBILITY
    // S1: 0.00s - 6.69s (19yo + Ramp Shot)
    // S2: 6.69s - 12.40s (90,000 MCG Crowd)
    // S3: 12.40s - 20.80s (What is Boxing Day + 26 Dec)
    // S4: 20.80s - 26.90s (Families skip leftovers)
    // S5A: 26.90s - 32.20s (Shane Warne 1994 Hat-trick)
    // S5B: 32.20s - 37.50s (Ajinkya Rahane 2020 100)
    // S6: 37.50s - 47.10s (Public Holiday + Test Cricket)
    // S7: 47.10s - 52.61s (Pinned Debate + Call to Action)
    // ----------------------------------------------------

    // Initialize initial state: SCENE 1 IS VISIBLE ON FIRST FRAME!
    gsap.set("#scene1", {{ autoAlpha: 1 }});
    // 19 YEARS OLD text is VISIBLE on Frame 1!
    gsap.set("#s1_header_19yo", {{ autoAlpha: 1, scale: 1 }});
    gsap.set("#s1_clash_badge", {{ autoAlpha: 1, y: 0 }});
    gsap.set("#s1_bumrah_group", {{ autoAlpha: 1, x: 0 }});
    gsap.set("#s1_konstas_group", {{ autoAlpha: 1, x: 0 }});

    // Scene Transitions
    tl.to("#scene1", {{ autoAlpha: 0, duration: 0.1 }}, 6.69);
    tl.to("#scene2", {{ autoAlpha: 1, duration: 0.1 }}, 6.69);

    tl.to("#scene2", {{ autoAlpha: 0, duration: 0.15 }}, 12.40);
    tl.to("#scene3", {{ autoAlpha: 1, duration: 0.15 }}, 12.40);

    tl.to("#scene3", {{ autoAlpha: 0, duration: 0.15 }}, 20.80);
    tl.to("#scene4", {{ autoAlpha: 1, duration: 0.15 }}, 20.80);

    tl.to("#scene4", {{ autoAlpha: 0, duration: 0.15 }}, 26.90);
    tl.to("#scene5a", {{ autoAlpha: 1, duration: 0.15 }}, 26.90);

    tl.to("#scene5a", {{ autoAlpha: 0, duration: 0.15 }}, 32.20);
    tl.to("#scene5b", {{ autoAlpha: 1, duration: 0.15 }}, 32.20);

    tl.to("#scene5b", {{ autoAlpha: 0, duration: 0.15 }}, 37.50);
    tl.to("#scene6", {{ autoAlpha: 1, duration: 0.15 }}, 37.50);

    tl.to("#scene6", {{ autoAlpha: 0, duration: 0.15 }}, 47.10);
    tl.to("#scene7", {{ autoAlpha: 1, duration: 0.15 }}, 47.10);

    // ----------------------------------------------------
    // DETAILED SCENE ANIMATIONS
    // ----------------------------------------------------
    // SCENE 1: High energy opener
    // Subtle breathing pulse for 19yo badge
    tl.to("#s1_header_19yo", {{ scale: 1.05, duration: 0.4, yoyo: true, repeat: 3, ease: "sine.inOut" }}, 0.2);
    // Bumrah charges forward
    tl.to("#s1_bumrah_group", {{ x: 40, duration: 2.2, ease: "power1.inOut" }}, 1.0);
    // Bumrah sling bowling action
    tl.to("#s1_bumrah_arm", {{ rotation: -80, duration: 0.45, ease: "power2.in" }}, 2.8);
    tl.to("#s1_bumrah_arm", {{ rotation: 30, duration: 0.18, ease: "power4.out" }}, 3.25);
    // Ball appears and hurtles toward Konstas
    tl.to("#s1_match_ball", {{ opacity: 1, duration: 0.05 }}, 3.3);
    tl.fromTo("#s1_match_ball", {{ x: 260, y: 440, scale: 0.7 }}, {{ x: 730, y: 710, scale: 1.1, duration: 0.85, ease: "power2.in" }}, 3.3);
    // Konstas crouches into ramp shot
    tl.to("#s1_konstas_bat", {{ rotation: 35, duration: 0.35, ease: "back.out(2)" }}, 3.8);
    // Bat crack starburst
    tl.to("#s1_bat_crack", {{ opacity: 1, scale: 1.4, duration: 0.12, ease: "back.out(3)" }}, 4.15);
    tl.to("#s1_bat_crack", {{ opacity: 0, scale: 0.8, duration: 0.3 }}, 4.45);
    // Ball ramps over keeper in parabolic arc
    tl.to("#s1_ramp_arc", {{ opacity: 0.9, duration: 0.2 }}, 4.15);
    tl.fromTo("#s1_match_ball", {{ x: 730, y: 710 }}, {{ x: 980, y: 310, duration: 0.9, ease: "power1.out" }}, 4.15);
    // Comic action stamp
    tl.fromTo("#s1_action_stamp", {{ opacity: 0, scale: 0.5, y: 50 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.4, ease: "back.out(2)" }}, 4.3);

    // SCENE 2: Cut to 90,000 crowd roar!
    tl.fromTo("#s2_roar_card", {{ scale: 0.6, opacity: 0, rotation: -3 }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }}, 6.75);
    tl.fromTo("#s2_mcg_scoreboard", {{ y: -100, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, 6.85);
    // Cheering spectator motion
    tl.to("#s2_front_fans", {{ y: -25, duration: 0.3, yoyo: true, repeat: 8, ease: "sine.inOut" }}, 6.9);
    tl.to("#s2_bay13_banner", {{ rotation: 4, duration: 0.35, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 6.9);

    // SCENE 3: What is Boxing Day explainer
    tl.fromTo("#s3_hero_q", {{ y: -60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "back.out(1.8)" }}, 12.45);
    tl.fromTo("#s3_calendar_card", {{ scale: 0.8, opacity: 0, rotation: 5 }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.55, ease: "back.out(2)" }}, 13.0);
    tl.fromTo("#s3_mcg_tradition", {{ y: 80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }}, 15.2);

    // SCENE 4: Families skip leftovers
    tl.fromTo("#s4_header_leftovers", {{ y: -50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "back.out(1.8)" }}, 20.85);
    tl.fromTo("#s4_feast_card", {{ scale: 0.85, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.5, ease: "power3.out" }}, 21.2);
    tl.fromTo("#s4_family_group", {{ x: -100, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 22.0);
    tl.fromTo("#s4_biggest_days_stamp", {{ scale: 0.7, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }}, 24.5);

    // SCENE 5A: Shane Warne 1994 Hat-trick
    tl.fromTo("#s5a_legends_title", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.5)" }}, 26.95);
    tl.fromTo("#s5a_warne_badge", {{ scale: 0.8, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }}, 27.5);
    tl.fromTo("#s5a_warne_hero", {{ scale: 0.85, opacity: 0, y: 50 }}, {{ scale: 1, opacity: 1, y: 0, duration: 0.55, ease: "power3.out" }}, 28.2);
    // Warne celebrations and jumping
    tl.to("#s5a_warne_hero", {{ y: -30, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }}, 28.8);
    tl.fromTo("#s5a_shattered_stumps", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(3)" }}, 29.5);
    tl.fromTo("#s5a_hattrick_box", {{ y: 60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.8)" }}, 30.2);

    // SCENE 5B: Ajinkya Rahane 2020 Century
    tl.fromTo("#s5b_rahane_header", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.5)" }}, 32.25);
    tl.fromTo("#s5b_scoreboard", {{ scale: 0.85, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "power3.out" }}, 32.7);
    tl.fromTo("#s5b_rahane_hero", {{ scale: 0.85, opacity: 0, y: 40 }}, {{ scale: 1, opacity: 1, y: 0, duration: 0.55, ease: "power3.out" }}, 33.3);
    // Rahane raising arms
    tl.fromTo("#s5b_left_arm", {{ rotation: -20 }}, {{ rotation: 0, duration: 0.4, ease: "back.out(2)" }}, 33.8);
    tl.fromTo("#s5b_right_arm", {{ rotation: 20 }}, {{ rotation: 0, duration: 0.4, ease: "back.out(2)" }}, 33.8);
    tl.fromTo("#s5b_comeback_stamp", {{ y: 60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.8)" }}, 34.6);

    // SCENE 6: Public Holiday & Boxing Day is for Test Cricket
    tl.fromTo("#s6_q_badge", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.5)" }}, 37.55);
    tl.fromTo("#s6_holiday_stamp", {{ scale: 0.85, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }}, 38.0);
    tl.fromTo("#s6_versus_card", {{ scale: 0.8, opacity: 0, y: 50 }}, {{ scale: 1, opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }}, 39.8);

    // SCENE 7: Pinned Debate Card & Final Call to Action
    tl.fromTo("#s7_cta_header", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.5)" }}, 47.15);
    tl.fromTo("#s7_cricket_icons", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "power2.out" }}, 47.6);
    tl.fromTo("#s7_pinned_comment_card", {{ scale: 0.7, opacity: 0, y: 80 }}, {{ scale: 1, opacity: 1, y: 0, duration: 0.6, ease: "back.out(2)" }}, 48.2);
    tl.fromTo("#s7_comment_cta", {{ scale: 0.8, opacity: 0, y: 40 }}, {{ scale: 1, opacity: 1, y: 0, duration: 0.5, ease: "back.out(2)" }}, 49.8);

    // ----------------------------------------------------
    // CAPTION SYNCHRONIZATION
    // ----------------------------------------------------
    const captionsData = {json.dumps(captions)};
    captionsData.forEach((cap, idx) => {{
      const elem = `#cap_${{idx}}`;
      const dur = cap.end - cap.start;
      
      // In-transition
      tl.fromTo(elem, 
        {{ opacity: 0, scale: 0.88, y: 15 }}, 
        {{ opacity: 1, scale: 1, y: 0, duration: 0.18, ease: "power2.out" }}, 
        cap.start
      );

      // Out-transition
      tl.to(elem, 
        {{ opacity: 0, scale: 0.95, duration: 0.12, ease: "power1.in" }}, 
        cap.end - 0.12
      );
    }});
  </script>
</body>
</html>
"""

    with open(out_standalone, "w", encoding="utf-8") as f:
        f.write(html)
    with open(out_index, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated standalone.html ({len(html)/1024:.1f} KB)")
    print(f"Successfully generated index.html ({len(html)/1024:.1f} KB)")

if __name__ == "__main__":
    build()
