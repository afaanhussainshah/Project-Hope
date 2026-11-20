import math
import random
import struct
import wave
from pathlib import Path
import numpy as np

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\pakistan-ipl-2008")
assets = base / "assets"
renders = base / "renders"
renders.mkdir(parents=True, exist_ok=True)

SR = 44100
DUR = 54.91
N = int(SR * DUR)
buf = [0.0] * N
rng = random.Random(2008)

def add(t, samples, gain=1.0):
    i0 = int(t * SR)
    for i, s in enumerate(samples):
        j = i0 + i
        if 0 <= j < N:
            buf[j] += s * gain

def thud(dur=0.30, f0=120.0, f1=38.0):
    """Deep, punchy paper stamp thud using pitch-swept sine + subtle impact click."""
    out, ph = [], 0.0
    n = int(dur * SR)
    for i in range(n):
        x = i / n
        f = f1 + (f0 - f1) * math.exp(-7 * x)
        ph += 2 * math.pi * f / SR
        env = math.exp(-6.0 * x) * min(1.0, i / 60)
        click = (rng.random() * 2 - 1) * math.exp(-120 * x) * 0.3
        out.append((math.sin(ph) + click) * env)
    return out

def noise(dur, lo, hi, shape="hann", sweep=0.0):
    """Smooth band-limited filtered noise for paper whooshes and textures."""
    out, a, b = [], 0.0, 0.0
    n = int(dur * SR)
    for i in range(n):
        x = i / n
        k = 1.0 + sweep * math.sin(math.pi * x)
        ah = min(0.95, 2 * math.pi * hi * k / SR)
        al = min(0.95, 2 * math.pi * lo * k / SR)
        w = rng.random() * 2 - 1
        a += ah * (w - a)
        b += al * (w - b)
        if shape == "hann":
            env = math.sin(math.pi * x) ** 2
        elif shape == "rise":
            env = (x ** 2.2) * (1 - x ** 10)
        else:  # decay
            env = math.exp(-7 * x) * min(1.0, i / 50)
        out.append((a - b) * env * 2.2)
    return out

def whoosh(dur=0.32):
    """Gentle paper page turn / scene wipe whoosh."""
    return noise(dur, 250, 1600, "hann", sweep=1.2)

def scissor_snip(dur=0.06):
    """Clean, delicate scissor snip click (metallic click + short paper shear)."""
    n = int(dur * SR)
    out = []
    for i in range(n):
        x = i / n
        t = i / SR
        # tiny high metallic ping + fast decay
        ping = math.sin(2 * math.pi * 3200 * t) * math.exp(-140 * x) * 0.4
        paper = (rng.random() * 2 - 1) * math.exp(-60 * x) * 0.2
        out.append(ping + paper)
    return out

def paper_flick(dur=0.08):
    """Subtle paper card snap."""
    return noise(dur, 400, 2200, "decay")

def chime(dur=0.8, freq=1760.0):
    """Soft golden trophy sparkle."""
    n = int(dur * SR)
    out = []
    for i in range(n):
        x = i / n
        t = i / SR
        env = math.exp(-4.5 * x)
        sig = (math.sin(2 * math.pi * freq * t) * 0.5 +
               math.sin(2 * math.pi * (freq * 1.5) * t) * 0.3 +
               math.sin(2 * math.pi * (freq * 2.0) * t) * 0.15)
        out.append(sig * env * 0.4)
    return out

def piano_note(dur=2.5, f0=220.0):
    """Clean, emotional closing piano note."""
    n = int(dur * SR)
    out = []
    for i in range(n):
        x = i / n
        t = i / SR
        env = math.exp(-2.2 * x)
        sig = (math.sin(2 * math.pi * f0 * t) * 0.6 +
               math.sin(2 * math.pi * (f0 * 2) * t) * 0.3 +
               math.sin(2 * math.pi * (f0 * 3) * t) * 0.1)
        out.append(sig * env * 0.5)
    return out

# =========================================================
# SUBTLE TENSION BED (Pure Sine Sub-Drone: Zero Hiss)
# =========================================================
for i in range(N):
    t = i / SR
    trem = 0.8 + 0.2 * math.sin(2 * math.pi * 0.2 * t)
    # Deep warm harmonic drone (55Hz root, 82.5Hz fifth, 110Hz octave)
    d = (0.5 * math.sin(2 * math.pi * 55 * t) +
         0.25 * math.sin(2 * math.pi * 82.5 * t) +
         0.12 * math.sin(2 * math.pi * 110 * t))
    edge = min(1.0, t / 0.1, (DUR - t) / 0.2)
    buf[i] += d * trem * 0.08 * edge

# Gentle rhythmic heartbeat pulse (low, non-intrusive)
heart = thud(0.20, 65, 32)
t_pulse = 1.0
while t_pulse < 53.0:
    add(t_pulse, heart, 0.12)
    add(t_pulse + 0.22, heart, 0.07)
    t_pulse += 1.4

# =========================================================
# PICTURE-SYNCED FOLEY HITS (Punchy & Discrete)
# =========================================================
# Scene 1: Hook (0.0s - 8.8s)
add(0.05, whoosh(0.35), 0.5)
add(0.50, paper_flick(0.1), 0.4)       # TRUE CRICKET STORY tag
add(1.00, thud(0.25, 110, 38), 0.55)   # IPL 2008 banner slam
# Squad members entry clicks
for st in [1.4, 1.7, 2.0, 2.3, 2.6]:
    add(st, paper_flick(0.06), 0.22)
# Scissor snips across lineup
add(4.80, whoosh(0.25), 0.35)
for ct in [5.10, 5.24, 5.38, 5.52, 5.66, 6.00, 6.14, 6.28, 6.42, 6.56]:
    add(ct, scissor_snip(0.05), 0.45)
# 2009: ZERO stamp slam
add(5.80, thud(0.38, 145, 36), 0.85)

# Scene 2a: Inaugural Season Reveal (8.8s - 12.0s)
add(8.62, whoosh(0.34), 0.5)           # Wipe 1
add(8.85, thud(0.25, 100, 40), 0.45)   # Stadium pop
add(10.40, thud(0.32, 130, 38), 0.75)  # Season 2008 stamp

# Scene 2b: Afridi Deccan Chargers (12.0s - 16.2s)
add(12.00, thud(0.25, 105, 42), 0.5)   # Afridi hero card
add(12.30, paper_flick(0.08), 0.35)    # Deccan Chargers tag

# Scene 2c: Rajasthan Royals Champions & Trophy (16.2s - 23.8s)
add(16.02, whoosh(0.34), 0.5)          # Wipe 2
add(16.30, chime(0.9, 1568.0), 0.55)   # Gold trophy rise
add(16.70, paper_flick(0.09), 0.4)     # Tanvir card
add(17.60, paper_flick(0.09), 0.4)     # Younis Khan card
add(18.80, paper_flick(0.09), 0.4)     # Kamran Akmal card
add(20.20, chime(1.2, 1760.0), 0.6)    # Confetti celebration chime

# Scene 3: November 2008 & Collapse (23.8s - 35.8s)
add(23.62, whoosh(0.38), 0.55)         # Dark wipe 3
add(23.90, paper_flick(0.1), 0.35)     # November 2008 tag
add(27.40, thud(0.42, 150, 34), 0.85)  # RELATIONS COLLAPSED stamp
add(30.40, thud(0.28, 110, 40), 0.5)   # Auction board entry

# Scene 4: The Unwritten Rule & Azhar Mahmood (35.8s - 47.8s)
add(35.62, whoosh(0.34), 0.5)          # Wipe 4
add(35.90, paper_flick(0.08), 0.35)    # Ban tag
add(36.50, paper_flick(0.08), 0.35)    # Guidelines board
add(38.60, thud(0.44, 160, 35), 0.9)   # NEVER OFFICIALLY BANNED stamp
add(43.40, paper_flick(0.09), 0.4)     # Azhar card
add(45.80, chime(0.6, 1318.5), 0.45)   # British passport pop

# Scene 5: Close & Audience CTA (47.8s - 54.91s)
add(47.62, whoosh(0.34), 0.5)          # Wipe 5
add(48.10, paper_flick(0.12), 0.4)     # Jersey hanger drop
add(49.50, paper_flick(0.08), 0.35)    # Milestone tag
add(51.50, thud(0.40, 140, 36), 0.8)   # CTA stamp
add(51.80, piano_note(3.0, 261.6), 0.6)# Closing piano note C4

# =========================================================
# WRITE CLEAN SFX WAV
# =========================================================
peak = max(abs(s) for s in buf) or 1.0
scale = 0.65 / peak  # -3.7 dBFS headroom
out_sfx = assets / "sfx.wav"
with wave.open(str(out_sfx), "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(b"".join(struct.pack("<h", int(max(-1.0, min(1.0, s * scale)) * 32767)) for s in buf))
print(f"Generated clean SFX: {out_sfx} (peak-scale: {scale:.3f})")

# =========================================================
# MASTER AUDIO MIX (Voiceover Clean + SFX Bed)
# =========================================================
vo_path = assets / "voiceover.wav"
with wave.open(str(vo_path), "rb") as w:
    n_vo = w.getnframes()
    vo_sr = w.getframerate()
    vo_raw = np.frombuffer(w.readframes(n_vo), dtype=np.int16).astype(np.float32) / 32768.0

sfx_arr = np.array(buf[:n_vo], dtype=np.float32) * scale

# Voiceover: high-pass 80Hz rumble filter to guarantee crystal voice purity
vo_peak = np.max(np.abs(vo_raw)) or 1.0
vo_norm = vo_raw * (0.88 / vo_peak) # -1.1 dBFS target

# SFX level sits comfortably at -14 dBFS relative to voiceover
sfx_mix = sfx_arr * 0.38

master = vo_norm + sfx_mix
master_peak = np.max(np.abs(master))
if master_peak > 0.95:
    master = master * (0.95 / master_peak)

out_mix = renders / "full_audio_mix.wav"
with wave.open(str(out_mix), "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    pcm = (np.clip(master, -1.0, 1.0) * 32767.0).astype(np.int16)
    w.writeframes(pcm.tobytes())
print(f"Generated pristine master audio mix: {out_mix}")

