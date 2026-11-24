import base64
from pathlib import Path

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\follow-on-gamble")
assets = base / "assets"
renders = base / "renders"

font_path = assets / "fonts" / "Anton-Regular.ttf"
gsap_path = assets / "gsap.min.js"

font_b64 = base64.b64encode(font_path.read_bytes()).decode("utf-8")
gsap_code = gsap_path.read_text(encoding="utf-8")

raw_template = """<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script>
__GSAP_CODE__
    </script>
    <style>
      @font-face {
        font-family: "Anton";
        src: url("data:font/truetype;charset=utf-8;base64,__FONT_B64__") format("truetype");
        font-weight: 400;
        font-style: normal;
      }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #143d30; }
      #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: "Anton", sans-serif; }
      .scene { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: hidden; z-index: 1; }
      .cam, .cam svg { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; display: block; }
      .cut { filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.3)); }
      #wipe { position: absolute; left: 0; top: -190px; width: 1500px; height: 2300px; z-index: 5; pointer-events: none; }
      #grain {
        position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 8; opacity: 0.08; mix-blend-mode: multiply; pointer-events: none;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' seed='4'/><feColorMatrix values='0 0 0 0 .35  0 0 0 0 .3  0 0 0 0 .25  0 0 0 .9 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");
      }
      #vig { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 9; pointer-events: none; background: radial-gradient(ellipse at 50% 45%, rgba(0, 0, 0, 0) 55%, rgba(0, 0, 0, 0.32) 100%); }
      .cap { position: absolute; left: 50px; width: 980px; top: 1280px; height: 230px; z-index: 10; text-align: center; pointer-events: none; }
      .cap span {
        display: inline-block; max-width: 960px; padding: 14px 34px 20px; background: #f6f1e4; color: #1b1b1b;
        font-size: 88px; line-height: 1.06; letter-spacing: 1px; text-transform: uppercase;
        filter: drop-shadow(9px 11px 0 rgba(0, 0, 0, 0.35));
      }
      .cap b { font-weight: 400; color: #c1121f; }
      .cap i { font-style: normal; background: #e3b23c; padding: 0 12px; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="49.476" data-width="1080" data-height="1920">
      <!-- 5 SCENES -->
      <div id="s1" class="clip scene" data-start="0" data-duration="7.45" data-track-index="0"><div class="cam"></div></div>
      <div id="s2" class="clip scene" data-start="7.45" data-duration="9.05" data-track-index="0"><div class="cam"></div></div>
      <div id="s3" class="clip scene" data-start="16.50" data-duration="10.0" data-track-index="0"><div class="cam"></div></div>
      <div id="s4" class="clip scene" data-start="26.50" data-duration="15.5" data-track-index="0"><div class="cam"></div></div>
      <div id="s5" class="clip scene" data-start="42.00" data-duration="7.476" data-track-index="0"><div class="cam"></div></div>

      <audio id="master_audio" src="renders/full_audio_mix.wav" data-start="0" data-duration="49.476" data-volume="1" data-track-index="2"></audio>

      <div id="wipe"></div>
      <div id="grain"></div>
      <div id="vig"></div>

      <!-- CAPTIONS -->
      <div class="clip cap" data-start="0.03" data-duration="3.87" data-track-index="1"><span><b>99% OF CRICKET FANS</b> DON'T KNOW THIS</span></div>
      <div class="clip cap" data-start="4.14" data-duration="3.31" data-track-index="1"><span>COST AUSTRALIA <i>THE GREATEST STREAK</i></span></div>
      <div class="clip cap" data-start="7.74" data-duration="0.86" data-track-index="1"><span>HERE'S <b>THE RULE</b></span></div>
      <div class="clip cap" data-start="8.69" data-duration="3.31" data-track-index="1"><span>LEAD BY <b>200+ RUNS</b></span></div>
      <div class="clip cap" data-start="12.10" data-duration="2.10" data-track-index="1"><span>BAT AGAIN <i>STRAIGHT AWAY</i></span></div>
      <div class="clip cap" data-start="14.31" data-duration="2.19" data-track-index="1"><span>BUT IT'S <b>THEIR CHOICE</b></span></div>
      <div class="clip cap" data-start="16.67" data-duration="1.43" data-track-index="1"><span>AND THAT'S <i>THE GAMBLE</i></span></div>
      <div class="clip cap" data-start="18.20" data-duration="1.50" data-track-index="1"><span>BOWLERS GET <b>TIRED</b></span></div>
      <div class="clip cap" data-start="19.78" data-duration="2.72" data-track-index="1"><span>CHASE ON A <b>WORN PITCH</b></span></div>
      <div class="clip cap" data-start="22.67" data-duration="3.83" data-track-index="1"><span>ONLY <b>4 WINS EVER</b> IN HISTORY</span></div>
      <div class="clip cap" data-start="26.76" data-duration="1.84" data-track-index="1"><span>KOLKATA <b>2001</b></span></div>
      <div class="clip cap" data-start="28.76" data-duration="2.84" data-track-index="1"><span>AUSTRALIA: <b>16 WINS IN A ROW</b></span></div>
      <div class="clip cap" data-start="31.71" data-duration="3.19" data-track-index="1"><span>INDIA: <b>274 RUNS BEHIND</b></span></div>
      <div class="clip cap" data-start="35.10" data-duration="2.10" data-track-index="1"><span>ENFORCED <i>THE FOLLOW-ON</i></span></div>
      <div class="clip cap" data-start="37.33" data-duration="3.36" data-track-index="1"><span>LAXMAN & DRAVID <b>BATTED ALL DAY</b></span></div>
      <div class="clip cap" data-start="40.79" data-duration="1.01" data-track-index="1"><span>AND INDIA <b>WON!</b></span></div>
      <div class="clip cap" data-start="42.25" data-duration="1.85" data-track-index="1"><span>THE FOLLOW-ON IS A <b>WEAPON</b></span></div>
      <div class="clip cap" data-start="44.22" data-duration="1.98" data-track-index="1"><span>BUT SOMETIMES... <i>A TRAP</i></span></div>
      <div class="clip cap" data-start="46.45" data-duration="2.85" data-track-index="1"><span><b>FOLLOW</b> FOR CRICKET SECRETS</span></div>
    </div>

    <script>
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
        dgreen: "#143D30",
        green: "#174D3A",
        gold: "#E3B23C",
        red: "#B3261E",
        stamp: "#C1121F",
        ausGreen: "#004732",
        sky: "#BFD9E6",
        pitch: "#D9BC82",
        indiaBlue: "#0B4EA2",
        white: "#FFFFFF"
      };

      const svg = (inner, bg) => `<svg viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg"><rect width="1080" height="1920" fill="${bg}"/>${inner}</svg>`;
      const put = (id, html) => (document.querySelector("#" + id + " .cam").innerHTML = html);
      const tx = (x, y, s, str, fill, anc = "middle", ex = "") =>
        `<text x="${x}" y="${y}" font-family="Anton" font-size="${s}" fill="${fill}" text-anchor="${anc}" ${ex}>${str}</text>`;

      function torn(x, y, w, h, j = 10, step = 40) {
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
          s += `<polygon points="${cx},${cy} ${(cx + 1900 * Math.cos(a)).toFixed(0)},${(cy + 1900 * Math.sin(a)).toFixed(0)} ${(cx + 1900 * Math.cos(b)).toFixed(0)},${(cy + 1900 * Math.sin(b)).toFixed(0)}" fill="${c}"/>`;
        }
        return s + "</g>";
      };

      const scraps = (cls, cx, cy, n, cols) => {
        let s = "";
        for (let i = 0; i < n; i++) {
          const w = 30 + rnd() * 60;
          const col = cols[i % cols.length];
          s += `<polygon class="${cls}" points="${cx},${cy} ${(cx + w).toFixed(0)},${(cy + rnd() * 30).toFixed(0)} ${(cx + w * 0.6).toFixed(0)},${(cy + w * 0.8).toFixed(0)}" fill="${col}" opacity="0"/>`;
        }
        return s;
      };

      const drop = (cls, x, y, s = 1) =>
        `<path class="${cls}" d="M${x} ${y - 34 * s} Q${x + 24 * s} ${y + 4 * s} ${x} ${y + 22 * s} Q${x - 24 * s} ${y + 4 * s} ${x} ${y - 34 * s}Z" fill="#9AD0EC" opacity="0"/>`;

      // Character Helpers (Clean Paper Style)
      function captainSteve(id, x, y, s = 1) {
        return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})">
          <g class="cut">
            <path d="M-180 340 Q-180 180 -80 160 L80 160 Q180 180 180 340Z" fill="${C.paper}"/>
            <path d="M-50 160 L0 230 L50 160 L30 145 L-30 145Z" fill="#DDD5C0"/>
            <rect x="-35" y="110" width="70" height="70" rx="15" fill="#D69E73"/>
          </g>
          <g class="head cut">
            <ellipse cx="-110" cy="15" rx="20" ry="32" fill="#D69E73"/><ellipse cx="110" cy="15" rx="20" ry="32" fill="#D69E73"/>
            <rect x="-110" y="-130" width="220" height="260" rx="100" fill="#E9B990"/>
            <path d="M-120 -80 Q-120 -210 0 -210 Q120 -210 120 -80Z" fill="${C.ausGreen}"/>
            <path d="M-140 -80 Q0 -115 140 -80 Q155 -50 0 -60 Q-155 -50 -140 -80Z" fill="#0A3324"/>
            <circle cx="0" cy="-145" r="22" fill="${C.gold}"/>
            <g class="eye"><circle cx="-48" cy="5" r="26" fill="#fff"/><circle class="pupil" cx="-48" cy="5" r="12" fill="${C.ink}"/></g>
            <g class="eye"><circle cx="48" cy="5" r="26" fill="#fff"/><circle class="pupil" cx="48" cy="5" r="12" fill="${C.ink}"/></g>
            <rect class="browL" x="-78" y="-40" width="60" height="14" rx="5" fill="#4A3423"/>
            <rect class="browR" x="18" y="-40" width="60" height="14" rx="5" fill="#4A3423"/>
            <path d="M-8 25 Q-4 55 18 48" stroke="#D69E73" stroke-width="7" fill="none" stroke-linecap="round"/>
            <rect class="mouth" x="-32" y="86" width="64" height="12" rx="5" fill="#7A2E22"/>
          </g>
          <g id="pointHand" class="cut" transform="translate(140, 190) rotate(-15)">
            <rect x="0" y="-28" width="220" height="56" rx="22" fill="${C.paper}"/>
            <rect x="210" y="-35" width="80" height="70" rx="24" fill="#E9B990"/>
            <rect x="280" y="-28" width="110" height="34" rx="16" fill="#E9B990"/>
          </g>
        </g>`;
      }

      function indianHero(id, x, y, name, runs, s = 0.85) {
        return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})">
          <g class="cut">
            <path d="M-180 340 Q-180 180 -80 160 L80 160 Q180 180 180 340Z" fill="${C.white}"/>
            <path d="M-50 160 L0 230 L50 160 L30 145 L-30 145Z" fill="#DDD5C0"/>
            <rect x="-35" y="110" width="70" height="70" rx="15" fill="#C48E66"/>
            <circle cx="0" cy="245" r="28" fill="${C.indiaBlue}"/>
            <circle cx="0" cy="245" r="12" fill="${C.gold}"/>
          </g>
          <g class="head cut">
            <ellipse cx="-110" cy="15" rx="20" ry="32" fill="#C48E66"/><ellipse cx="110" cy="15" rx="20" ry="32" fill="#C48E66"/>
            <rect x="-110" y="-130" width="220" height="260" rx="100" fill="#D69E73"/>
            <path d="M-120 -80 Q-120 -200 0 -200 Q120 -200 120 -80Z" fill="${C.indiaBlue}"/>
            <path d="M-140 -80 Q0 -115 140 -80 Q155 -50 0 -60 Q-155 -50 -140 -80Z" fill="#072F66"/>
            <circle cx="0" cy="-140" r="18" fill="${C.gold}"/>
            <g class="eye"><circle cx="-48" cy="5" r="26" fill="#fff"/><circle cx="-48" cy="5" r="12" fill="${C.ink}"/></g>
            <g class="eye"><circle cx="48" cy="5" r="26" fill="#fff"/><circle cx="48" cy="5" r="12" fill="${C.ink}"/></g>
            <rect x="-78" y="-40" width="60" height="14" rx="5" fill="#222"/>
            <rect x="18" y="-40" width="60" height="14" rx="5" fill="#222"/>
            <path d="M-8 25 Q-4 55 18 48" stroke="#C48E66" stroke-width="7" fill="none" stroke-linecap="round"/>
            <path d="M-35 88 Q0 115 35 88" stroke="#7A2E22" stroke-width="10" fill="none" stroke-linecap="round"/>
          </g>
          <g class="cut" transform="translate(0, 390)">
            ${sheet(-190, -45, 380, 90, C.paper, 6)}
            ${tx(0, -6, 44, name, C.ink)}
            ${tx(0, 32, 42, runs, C.stamp)}
          </g>
        </g>`;
      }

      // ==================== SCENE 1 ART ====================
      reseed(111);
      // Hook: 99% don't know card + Ripped Australia Streak banner
      const s1_hookCard = `<g id="s1_card" class="cut">
        ${sheet(120, 240, 840, 380, C.paper, 10)}
        <rect x="150" y="270" width="780" height="320" fill="${C.ink}"/>
        ${tx(540, 350, 52, "CRICKET'S UNTOLD RULE", C.gold)}
        ${tx(540, 470, 118, "99% DON'T KNOW", C.stamp)}
        ${tx(540, 545, 46, "THE SECRET OF THE FOLLOW-ON", C.paper)}
      </g>`;

      // Australia streak banner ripping in half
      function ripBanner(id, x, y) {
        const w = 860, h = 200, m = x + w / 2;
        const zig = `${m - 30},${y - 20} ${m + 25},${y + 45} ${m - 20},${y + 95} ${m + 30},${y + 150} ${m - 15},${y + h + 20}`;
        const inner = `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${C.ausGreen}"/>
          <rect x="${x}" y="${y + 14}" width="${w}" height="10" fill="${C.gold}"/>
          <rect x="${x}" y="${y + h - 24}" width="${w}" height="10" fill="${C.gold}"/>
          ${tx(m, y + 95, 44, "GREATEST STREAK IN TEST HISTORY", C.paper)}
          ${tx(m, y + 155, 62, "AUSTRALIA: 16 WINS IN A ROW", C.gold)}`;
        return `<defs>
          <clipPath id="${id}cl"><polygon points="${x - 20},${y - 20} ${zig} ${x - 20},${y + h + 20}"/></clipPath>
          <clipPath id="${id}cr"><polygon points="${x + w + 20},${y - 20} ${zig} ${x + w + 20},${y + h + 20}"/></clipPath>
        </defs>
        <g id="${id}" class="cut">
          <g id="${id}L"><g clip-path="url(#${id}cl)">${inner}</g></g>
          <g id="${id}R"><g clip-path="url(#${id}cr)">${inner}</g></g>
        </g>`;
      }

      const s1_rip = ripBanner("streakBanner", 110, 720);
      const s1_scraps = scraps("scA", 540, 820, 16, [C.gold, C.ausGreen, C.stamp, C.paper]);

      const s1_costBadge = `<g id="s1_cost" class="cut">
        <g transform="rotate(-6 540 1060)">
          ${sheet(160, 990, 760, 130, C.stamp, 8)}
          ${tx(540, 1076, 78, "COST THEM EVERYTHING!", C.paper)}
        </g>
      </g>`;

      put("s1", svg(
        rays("r1", 540, 800, 20, "#1A4A3A") +
        s1_hookCard +
        s1_rip +
        s1_scraps +
        s1_costBadge,
        C.dgreen
      ));

      // ==================== SCENE 2 ART ====================
      reseed(222);
      const s2_stadium = `<rect width="1080" height="680" fill="${C.sky}"/>
        <rect y="580" width="1080" height="380" fill="#39424E"/>
        ${(() => {
          let crowd = "";
          const cols = [C.paper, C.gold, C.red, C.green, "#5FA8C9", "#FFF"];
          for (let r = 0; r < 5; r++)
            for (let c = 0; c < 20; c++)
              crowd += `<circle cx="${(c * 56 + (r % 2 ? 28 : 0) + rnd() * 8).toFixed(0)}" cy="${610 + r * 50}" r="18" fill="${cols[Math.floor(rnd() * cols.length)]}"/>`;
          return crowd;
        })()}
        <rect y="930" width="1080" height="990" fill="${C.green}"/>
        <rect y="930" width="1080" height="26" fill="#0D3024"/>`;

      const s2_ruleCard = `<g id="s2_rule" class="cut">
        ${sheet(120, 220, 840, 280, C.paper, 10)}
        <rect x="150" y="245" width="780" height="230" fill="#202A36"/>
        ${tx(540, 310, 42, "MCC LAWS OF CRICKET", C.gold)}
        ${tx(540, 385, 72, "LAW 14: THE FOLLOW-ON", C.paper)}
        ${tx(540, 440, 38, "FIVE-DAY TEST MATCH MANDATE", "#9DB7C4")}
      </g>`;

      const s2_leadBars = `<g id="s2_bars" class="cut">
        <!-- Team 1 -->
        <g id="barA">
          ${sheet(100, 540, 410, 380, C.paper, 8)}
          <rect x="120" y="560" width="370" height="120" fill="${C.ausGreen}"/>
          ${tx(305, 625, 46, "1ST INNINGS LEAD", C.gold)}
          ${tx(305, 670, 32, "TEAM BATTING FIRST", C.paper)}
          ${tx(305, 790, 110, "450", C.ink)}
          ${tx(305, 855, 44, "RUNS SCORED", C.green)}
        </g>
        <!-- Team 2 -->
        <g id="barB">
          ${sheet(570, 540, 410, 380, C.paper, 8)}
          <rect x="590" y="560" width="370" height="120" fill="${C.indiaBlue}"/>
          ${tx(775, 625, 46, "TRAILED BY", C.gold)}
          ${tx(775, 670, 32, "TEAM BATTING SECOND", C.paper)}
          ${tx(775, 790, 110, "250", C.ink)}
          ${tx(775, 855, 44, "RUNS SCORED", C.red)}
        </g>
        <!-- Margin Tag -->
        <g id="marginStamp" transform="rotate(-5 540 960)">
          ${sheet(240, 910, 600, 110, C.stamp, 8)}
          ${tx(540, 988, 62, "LEAD ≥ 200 RUNS", C.paper)}
        </g>
      </g>`;

      const s2_choiceStamp = `<g id="s2_choice" class="cut">
        <g transform="rotate(3 540 1100)">
          ${sheet(120, 1040, 840, 130, C.gold, 8)}
          ${tx(540, 1125, 64, "IT'S THEIR CHOICE · NOT FORCED!", C.ink)}
        </g>
      </g>`;

      put("s2", svg(s2_stadium + s2_ruleCard + s2_leadBars + s2_choiceStamp, "#22364A"));

      // ==================== SCENE 3 ART ====================
      reseed(333);
      const s3_crackedPitch = `<g id="s3_pitch" class="cut">
        <polygon points="120,680 960,680 1080,1920 0,1920" fill="${C.pitch}"/>
        <path d="M480 720 L520 950 L460 1150 L560 1450 L510 1800" stroke="#7A5228" stroke-width="14" fill="none" stroke-linecap="round"/>
        <path d="M680 800 L640 1020 L710 1280 L650 1600" stroke="#7A5228" stroke-width="12" fill="none" stroke-linecap="round"/>
        <path d="M320 900 L370 1100 L310 1350 L390 1700" stroke="#7A5228" stroke-width="10" fill="none" stroke-linecap="round"/>
        <g transform="rotate(-4 280 820)">
          ${sheet(140, 770, 360, 90, C.ink, 6)}
          ${tx(320, 832, 48, "WORN PITCH · DAY 5", C.gold)}
        </g>
      </g>`;

      const s3_tiredBowler = `<g id="tiredBowler" transform="translate(760, 780) scale(0.9)">
        <g class="cut">
          <path d="M-140 280 Q-140 150 -60 130 L60 130 Q140 150 140 280Z" fill="${C.paper}"/>
          <rect x="-25" y="80" width="50" height="60" rx="10" fill="#D69E73"/>
        </g>
        <g class="head cut">
          <rect x="-90" y="-100" width="180" height="210" rx="80" fill="#E9B990"/>
          <path d="M-100 -50 Q-100 -160 0 -160 Q100 -160 100 -50Z" fill="#3B2A1E"/>
          <ellipse cx="-40" cy="5" rx="22" ry="14" fill="#fff"/>
          <circle cx="-40" cy="8" r="8" fill="${C.ink}"/>
          <ellipse cx="40" cy="5" rx="22" ry="14" fill="#fff"/>
          <circle cx="40" cy="8" r="8" fill="${C.ink}"/>
          <rect x="-68" y="-28" width="50" height="12" rx="4" fill="#3B2A1E" transform="rotate(-18 -43 -22)"/>
          <rect x="18" y="-28" width="50" height="12" rx="4" fill="#3B2A1E" transform="rotate(18 43 -22)"/>
          <ellipse cx="0" cy="65" rx="24" ry="20" fill="#4A1410"/>
        </g>
        ${drop("swD", -85, -20, 0.9)}
        ${drop("swD", 90, -10, 0.9)}
        ${drop("swD", -50, 90, 0.7)}
        ${drop("swD", 55, 80, 0.7)}
      </g>`;

      const s3_historyCard = `<g id="s3_history" class="cut">
        ${sheet(140, 240, 800, 360, C.paper, 10)}
        <rect x="170" y="270" width="740" height="300" fill="${C.ink}"/>
        ${tx(540, 340, 48, "THE DANGEROUS GAMBLE", C.gold)}
        ${tx(540, 460, 118, "ONLY 4 WINS EVER", C.stamp)}
        ${tx(540, 525, 42, "AFTER FOLLOWING ON IN TEST HISTORY", C.paper)}
      </g>`;

      put("s3", svg(s3_crackedPitch + s3_tiredBowler + s3_historyCard, "#B8894E"));

      // ==================== SCENE 4 ART ====================
      reseed(444);
      const s4_edenGardens = `<rect width="1080" height="740" fill="#203348"/>
        <rect y="500" width="1080" height="320" fill="#141E28"/>
        ${(() => {
          let crowd = "";
          const cols = ["#FFF", C.gold, C.indiaBlue, "#E34A26", "#FFF", "#4682B4"];
          for (let r = 0; r < 6; r++)
            for (let c = 0; c < 22; c++)
              crowd += `<circle cx="${(c * 50 + (r % 2 ? 25 : 0) + rnd() * 8).toFixed(0)}" cy="${520 + r * 46}" r="16" fill="${cols[Math.floor(rnd() * cols.length)]}"/>`;
          return crowd;
        })()}
        <rect y="810" width="1080" height="1110" fill="${C.green}"/>
        <g id="s4_banner" class="cut">
          <g transform="rotate(-2 540 260)">
            ${sheet(120, 200, 840, 115, C.paper, 8)}
            ${tx(540, 278, 64, "KOLKATA · EDEN GARDENS 2001", C.indiaBlue)}
          </g>
        </g>
        <g id="s4_ausStreak" class="cut">
          <g transform="rotate(2 540 380)">
            ${sheet(180, 330, 720, 100, C.ausGreen, 8)}
            ${tx(540, 400, 54, "AUSTRALIA: 16 TEST WINS IN A ROW", C.gold)}
          </g>
        </g>
        <g id="s4_deficitTag" class="cut">
          <g transform="rotate(-4 540 490)">
            ${sheet(200, 445, 680, 95, C.stamp, 8)}
            ${tx(540, 515, 58, "INDIA: 274 RUNS BEHIND!", C.paper)}
          </g>
        </g>`;

      const s4_sunArc = `<g id="s4_sunGroup">
        <circle id="s4_sun" cx="200" cy="460" r="75" fill="${C.gold}"/>
        <path id="s4_sunPath" d="M150 500 Q540 220 930 500" stroke="rgba(246,241,228,0.4)" stroke-width="8" stroke-dasharray="20 14" fill="none"/>
        <g transform="rotate(-3 540 595)">
          ${sheet(300, 560, 480, 70, C.paper, 6)}
          ${tx(540, 610, 40, "DAY 4: BATTED ENTIRE DAY", C.ink)}
        </g>
      </g>`;

      const s4_heroes = `<g id="s4_heroesGroup">
        ${indianHero("heroLaxman", 320, 720, "V.V.S. LAXMAN", "281 RUNS", 0.9)}
        ${indianHero("heroDravid", 760, 720, "RAHUL DRAVID", "180 RUNS", 0.9)}
      </g>`;

      const s4_winStamp = `<g id="s4_win" class="cut">
        <g transform="rotate(-6 540 1020)">
          ${sheet(160, 940, 760, 160, C.stamp, 10)}
          ${tx(540, 1045, 96, "INDIA WINS BY 171 RUNS!", C.paper)}
        </g>
      </g>`;

      const s4_confetti = scraps("scConfetti", 540, 980, 24, [C.gold, C.indiaBlue, "#FFF", C.stamp, "#28A745"]);

      put("s4", svg(s4_edenGardens + s4_sunArc + s4_heroes + s4_winStamp + s4_confetti, "#174D3A"));

      // ==================== SCENE 5 ART ====================
      reseed(555);
      const s5_weapon = `<g id="s5_weapon" class="cut">
        ${sheet(80, 280, 420, 520, C.paper, 8)}
        <rect x="100" y="300" width="380" height="90" fill="${C.indiaBlue}"/>
        ${tx(290, 362, 54, "THE WEAPON", C.gold)}
        <g transform="translate(290, 570) rotate(-45)">
          <polygon points="-16,-180 0,-240 16,-180 14,80 -14,80" fill="#E8EDF2" stroke="#607285" stroke-width="4"/>
          <line x1="0" y1="-220" x2="0" y2="80" stroke="#607285" stroke-width="5"/>
          <rect x="-60" y="80" width="120" height="24" rx="8" fill="${C.gold}"/>
          <rect x="-14" y="104" width="28" height="60" rx="6" fill="#8B4513"/>
          <circle cx="0" cy="180" r="22" fill="${C.gold}"/>
        </g>
        ${tx(290, 750, 38, "FAST WIN · INNINGS DEFEAT", C.green)}
      </g>`;

      const s5_trap = `<g id="s5_trap" class="cut">
        ${sheet(580, 280, 420, 520, C.paper, 8)}
        <rect x="600" y="300" width="380" height="90" fill="${C.stamp}"/>
        ${tx(790, 362, 54, "THE TRAP", C.paper)}
        <g id="bearTrap" transform="translate(790, 570)">
          <ellipse cx="0" cy="30" rx="140" ry="45" fill="#3D454E"/>
          <g id="trapJawL">
            <path d="M-130 20 Q-110 -70 0 -70" stroke="#5A6570" stroke-width="20" fill="none" stroke-linecap="round"/>
            <polygon points="-100,5 -85,-35 -70,5" fill="#DDD"/>
            <polygon points="-60,-15 -45,-55 -30,-15" fill="#DDD"/>
            <polygon points="-20,-30 0,-68 15,-30" fill="#DDD"/>
          </g>
          <g id="trapJawR">
            <path d="M130 20 Q110 -70 0 -70" stroke="#5A6570" stroke-width="20" fill="none" stroke-linecap="round"/>
            <polygon points="100,5 85,-35 70,5" fill="#DDD"/>
            <polygon points="60,-15 45,-55 30,-15" fill="#DDD"/>
          </g>
          <circle cx="0" cy="30" r="32" fill="${C.gold}"/>
        </g>
        ${tx(790, 750, 38, "TIRED ARMS · CHOKE DEFENSE", C.stamp)}
      </g>`;

      const s5_questionBanner = `<g id="s5_question" class="cut">
        <g transform="rotate(-3 540 910)">
          ${sheet(140, 850, 800, 130, C.paper, 8)}
          ${tx(540, 935, 62, "WOULD YOU ENFORCE IT? 👇", C.ink)}
        </g>
      </g>`;

      const s5_followBanner = `<g id="s5_follow" class="cut">
        <g transform="rotate(2 540 1080)">
          ${sheet(100, 1020, 880, 130, C.gold, 8)}
          ${tx(540, 1105, 58, "FOLLOW FOR MORE CRICKET SECRETS", C.ink)}
        </g>
      </g>`;

      put("s5", svg(
        rays("r5", 540, 700, 20, "#1A4A3A") +
        s5_weapon +
        s5_trap +
        s5_questionBanner +
        s5_followBanner,
        C.dgreen
      ));

      // ==================== WIPE SETUP ====================
      reseed(999);
      document.getElementById("wipe").innerHTML = `<svg viewBox="0 0 1500 2300" width="1500" height="2300" xmlns="http://www.w3.org/2000/svg"><polygon id="wp" points="${torn(20, 20, 1460, 2260, 60, 90)}" fill="${C.paper}"/></svg>`;

      // ==================== GSAP TIMELINE ====================
      const tl = gsap.timeline({ paused: true });
      const CC = "50% 50%";

      // Initial settings
      gsap.set("#r1", { svgOrigin: "540 800" });
      gsap.set("#r5", { svgOrigin: "540 700" });
      gsap.set("#s1_card,#streakBannerL,#streakBannerR,#s1_cost,#s2_rule,#barA,#barB,#marginStamp,#s2_choice,#s3_history,#tiredBowler,#s4_banner,#s4_ausStreak,#s4_deficitTag,#s4_heroesGroup,#s4_win,#s5_weapon,#s5_trap,#s5_question,#s5_follow", { transformOrigin: CC });
      gsap.set("#trapJawL,#trapJawR", { transformOrigin: "0% 100%" });

      const pop = (sel, t, d = 0.22) => tl.fromTo(sel, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: d, ease: "back.out(2.2)" }, t);
      const slam = (sel, t, r = 0) => tl.fromTo(sel, { scale: 3.0, opacity: 0, rotation: r }, { scale: 1, opacity: 1, rotation: 0, duration: 0.16, ease: "power4.in" }, t);
      const shake = (sel, t, a = 20) =>
        tl.to(sel, { x: a, y: -a * 0.6, duration: 0.04 }, t)
          .to(sel, { x: -a * 0.8, y: a * 0.5, duration: 0.04 }, t + 0.04)
          .to(sel, { x: a * 0.4, y: a * 0.3, duration: 0.04 }, t + 0.08)
          .to(sel, { x: 0, y: 0, duration: 0.05 }, t + 0.12);
      const zoom = (id, t, d, from, to, origin = CC, ease = "none") => tl.fromTo(`#${id} svg`, { scale: from }, { scale: to, duration: d, ease, transformOrigin: origin }, t);
      const burst = (cls, t, sx, sy0, sy1) =>
        gsap.utils.toArray("." + cls).forEach((el) => {
          tl.fromTo(el, { x: 0, y: 0, rotation: 0, opacity: 1 }, { x: (rnd() - 0.5) * sx, y: sy0 + rnd() * (sy1 - sy0), rotation: (rnd() - 0.5) * 720, opacity: 0, duration: 0.8, ease: "power2.out", immediateRender: false }, t);
        });
      const sweat = (cls, t) => gsap.utils.toArray("." + cls).forEach((el, i) => tl.fromTo(el, { opacity: 0, y: -20 }, { opacity: 1, y: 0, duration: 0.1, immediateRender: false }, t + i * 0.08).to(el, { y: 90, opacity: 0, duration: 0.55, ease: "power1.in" }, t + i * 0.08 + 0.2));

      // Captions
      gsap.utils.toArray(".cap span").forEach((el, i) => {
        const t = +el.parentNode.dataset.start;
        tl.fromTo(el, { scale: 0.5, rotation: i % 2 ? 5 : -5, opacity: 0 }, { scale: 1, rotation: i % 2 ? -1.5 : 1.5, opacity: 1, duration: 0.14, ease: "back.out(2.6)" }, t);
      });

      // Wipes
      gsap.set("#wipe", { x: -1700 });
      [
        [7.45, C.paper, 1],
        [16.50, C.stamp, -1],
        [26.50, C.gold, 1],
        [42.00, C.paper, -1]
      ].forEach(([t, c, dir]) => {
        tl.set("#wp", { fill: c }, t - 0.19);
        tl.fromTo("#wipe", { x: dir > 0 ? -1700 : 1300 }, { x: dir > 0 ? 1300 : -1700, duration: 0.36, ease: "none" }, t - 0.18);
      });

      // -------------------- SCENE 1 (0.00s - 7.45s) --------------------
      tl.fromTo("#r1", { rotation: 0 }, { rotation: 32, duration: 7.45, ease: "none" }, 0);
      zoom("s1", 0, 7.45, 1, 1.08);
      slam("#s1_card", 0.08, -6);
      shake("#s1 .cam", 0.24, 22);

      tl.fromTo("#streakBanner", { y: 600, opacity: 0 }, { y: 0, opacity: 1, duration: 0.40, ease: "back.out(1.3)" }, 3.50);
      // Ripping the banner apart! (Exact sandpaper style)
      tl.to("#streakBannerL", { x: -140, y: 70, rotation: -12, duration: 0.45, ease: "power3.out" }, 4.15);
      tl.to("#streakBannerR", { x: 140, y: 90, rotation: 10, duration: 0.45, ease: "power3.out" }, 4.15);
      burst("scA", 4.15, 1000, -500, 400);
      shake("#s1 .cam", 4.15, 28);

      pop("#s1_cost", 5.20, 0.25);
      shake("#s1 .cam", 5.45, 18);

      // -------------------- SCENE 2 (7.45s - 16.50s) --------------------
      zoom("s2", 7.45, 9.05, 1, 1.06);
      tl.fromTo("#s2_rule", { y: -700, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.3)" }, 7.50);
      shake("#s2 .cam", 7.85, 16);

      tl.fromTo("#barA", { x: -600, opacity: 0 }, { x: 0, opacity: 1, duration: 0.32, ease: "back.out(1.4)" }, 8.70);
      tl.fromTo("#barB", { x: 600, opacity: 0 }, { x: 0, opacity: 1, duration: 0.32, ease: "back.out(1.4)" }, 9.00);
      slam("#marginStamp", 12.10, -6);
      shake("#s2 .cam", 12.26, 24);

      pop("#s2_choice", 14.35, 0.25);
      shake("#s2 .cam", 14.60, 20);

      // -------------------- SCENE 3 (16.50s - 26.50s) --------------------
      zoom("s3", 16.5, 10.0, 1, 1.10);
      slam("#s3_history", 16.65, -5);
      shake("#s3 .cam", 16.81, 24);

      tl.fromTo("#tiredBowler", { y: 500, opacity: 0 }, { y: 0, opacity: 1, duration: 0.40, ease: "back.out(1.2)" }, 18.20);
      sweat("swD", 18.50);
      sweat("swD", 21.00);

      tl.fromTo("#s3_pitch", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "power2.out" }, 19.80);
      shake("#s3 .cam", 20.15, 18);

      tl.to("#s3_history", { scale: 1.08, duration: 0.15, yoyo: true, repeat: 1 }, 22.70);
      shake("#s3 .cam", 22.85, 26);

      // -------------------- SCENE 4 (26.50s - 42.00s) --------------------
      zoom("s4", 26.5, 15.5, 1, 1.07);
      slam("#s4_banner", 26.75, -4);
      shake("#s4 .cam", 26.91, 20);

      pop("#s4_ausStreak", 28.75, 0.25);
      pop("#s4_deficitTag", 31.70, 0.25);
      shake("#s4 .cam", 31.95, 20);

      tl.fromTo("#s4_sun", { cx: 200, cy: 460 }, { cx: 880, cy: 460, duration: 5.0, ease: "sine.inOut" }, 35.10);

      tl.fromTo("#heroLaxman", { y: 800, opacity: 0 }, { y: 0, opacity: 1, duration: 0.36, ease: "back.out(1.4)" }, 37.30);
      tl.fromTo("#heroDravid", { y: 800, opacity: 0 }, { y: 0, opacity: 1, duration: 0.36, ease: "back.out(1.4)" }, 37.55);
      shake("#s4 .cam", 37.90, 20);

      slam("#s4_win", 40.75, -8);
      shake("#s4 .cam", 40.91, 32);
      burst("scConfetti", 40.91, 1100, -600, 450);

      // -------------------- SCENE 5 (42.00s - 49.48s) --------------------
      tl.fromTo("#r5", { rotation: 0 }, { rotation: 28, duration: 7.48, ease: "none" }, 42.0);
      zoom("s5", 42.0, 7.48, 1, 1.06);

      tl.fromTo("#s5_weapon", { x: -600, opacity: 0 }, { x: 0, opacity: 1, duration: 0.32, ease: "back.out(1.4)" }, 42.20);
      tl.fromTo("#s5_trap", { x: 600, opacity: 0 }, { x: 0, opacity: 1, duration: 0.32, ease: "back.out(1.4)" }, 44.15);

      tl.to("#trapJawL", { rotation: 40, duration: 0.06, ease: "power4.in" }, 44.20);
      tl.to("#trapJawR", { rotation: -40, duration: 0.06, ease: "power4.in" }, 44.20);
      shake("#s5 .cam", 44.26, 26);

      pop("#s5_question", 45.10, 0.22);
      pop("#s5_follow", 46.45, 0.22);
      shake("#s5 .cam", 46.68, 16);

      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = tl;
      window.seekFrame = (t) => tl.seek(t);
      tl.seek(0);
    </script>
  </body>
</html>
"""

html_final = raw_template.replace("__GSAP_CODE__", gsap_code).replace("__FONT_B64__", font_b64)

# Write index.html and standalone.html
index_file = base / "index.html"
standalone_file = base / "standalone.html"

index_file.write_text(html_final, encoding="utf-8")
standalone_file.write_text(html_final, encoding="utf-8")

print(f"Generated {index_file} ({len(html_final)} bytes)")
print(f"Generated {standalone_file}")
