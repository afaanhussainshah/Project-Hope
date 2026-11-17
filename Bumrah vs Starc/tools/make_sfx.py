import math
import os
import random
import struct
import wave
import subprocess
import imageio_ffmpeg

SR = 44100
DUR = 57.391
N = int(SR * DUR)
buf = [0.0] * N

def add(t, s, vol=1.0):
    start = int(t * SR)
    for i, v in enumerate(s):
        idx = start + i
        if 0 <= idx < N:
            buf[idx] += v * vol

def thud(d=0.4, f0=115, f1=34):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        f = f0 + (f1 - f0) * frac
        phase += 2 * math.pi * f / SR
        env = (1.0 - frac) ** 1.8
        out.append(math.sin(phase) * env)
    return out

def rip(d=0.4):
    L = int(SR * d)
    out = []
    for i in range(L):
        frac = i / L
        r = random.uniform(-1, 1)
        mod = math.sin(2 * math.pi * 32 * (i / SR))
        env = (1.0 - frac) ** 1.3
        out.append(r * (0.6 + 0.4 * mod) * env)
    return out

def whoosh(d=0.35):
    L = int(SR * d)
    out = []
    for i in range(L):
        frac = i / L
        env = math.sin(math.pi * frac) ** 2
        r = random.uniform(-1, 1)
        out.append(r * env)
    return out

def metallic_ding(d=0.5, f=1800):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        phase += 2 * math.pi * f / SR
        env = math.exp(-frac * 14)
        out.append(math.sin(phase) * env)
    return out

def stumps_clatter(d=0.55):
    L = int(SR * d)
    out = []
    for i in range(L):
        frac = i / L
        # high wood resonance
        f1 = 480 + 80 * math.sin(2 * math.pi * 45 * frac)
        f2 = 720 + 120 * math.cos(2 * math.pi * 30 * frac)
        w1 = math.sin(2 * math.pi * f1 * (i / SR))
        w2 = math.sin(2 * math.pi * f2 * (i / SR))
        click = random.uniform(-0.6, 0.6) if i < int(SR * 0.08) else 0.0
        env = math.exp(-frac * 9)
        out.append((w1 * 0.45 + w2 * 0.35 + click) * env)
    return out

def crowd_roar(d=2.8):
    L = int(SR * d)
    out = []
    lp = 0.0
    for i in range(L):
        frac = i / L
        r = random.uniform(-1, 1)
        lp = lp * 0.85 + r * 0.15
        env = math.sin(math.pi * frac) ** 1.2
        out.append(lp * env)
    return out

def sub_drop(d=0.75):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        f = 95 * (1.0 - frac * 0.75)
        phase += 2 * math.pi * f / SR
        env = (1.0 - frac) ** 1.5
        out.append(math.sin(phase) * env)
    return out

# =========================================================================
# EXACT MILLISECOND-ALIGNED SFX PLACEMENT
# =========================================================================

# Intro (0.0s - 10.8s): The Toe-to-Toe Hook
add(0.1, whoosh(0.35), 0.5)
add(7.9, sub_drop(0.8), 0.8)                 # "Bumrah versus Starc" (7.96s)
add(9.7, thud(0.4, 120, 35), 0.95)           # "Let's settle it" (9.70s) - WHO IS DEADLIER stamp slam
add(9.8, crowd_roar(2.0), 0.4)

# Round 1: Opening the Bowling (10.8s - 20.0s)
add(10.8, rip(0.35), 0.7)                    # Wipe transition to Round 1
add(11.1, sub_drop(0.6), 0.6)                # "Round one" (11.08s)
add(14.0, whoosh(0.25), 0.4)                 # Starc 25 avg
add(16.8, metallic_ding(0.4, 1600), 0.7)     # Bumrah 18.84 avg
add(19.0, thud(0.45, 125, 34), 1.0)          # "Point, Bumrah" (18.96s) - Stamp slam
add(19.1, metallic_ding(0.6, 1400), 0.8)     # Scoreboard 1 - 0
add(19.2, crowd_roar(2.5), 0.5)

# Round 2: First Ball of a Test (20.0s - 29.2s)
add(20.0, rip(0.35), 0.7)                    # Wipe transition to Round 2
add(20.3, sub_drop(0.6), 0.6)                # "Round two" (20.34s)
add(24.5, stumps_clatter(0.6), 1.0)          # "struck four times on ball one" (23.34s)
add(28.1, thud(0.45, 125, 34), 1.0)          # "Point, Starc" (28.09s) - Stamp slam
add(28.2, metallic_ding(0.6, 1700), 0.8)     # Scoreboard 1 - 1
add(28.3, crowd_roar(2.5), 0.5)

# Round 3: Pink Ball Under Lights (29.2s - 37.5s)
add(29.2, whoosh(0.35), 0.6)                 # Night floodlights turn on
add(29.5, sub_drop(0.6), 0.6)                # "Round three" (29.54s)
add(33.2, metallic_ding(0.8, 2000), 0.9)     # "89 wickets" (32.71s)
add(36.3, thud(0.45, 125, 34), 1.0)          # "Point, Starc" (36.32s) - Stamp slam
add(36.4, metallic_ding(0.6, 1900), 0.8)     # Scoreboard 1 - 2
add(36.5, crowd_roar(2.5), 0.5)

# Round 4: Head-to-Head vs Each Other (37.5s - 47.6s)
add(37.5, rip(0.35), 0.7)                    # Wipe transition to Round 4
add(37.8, sub_drop(0.6), 0.6)                # "Round four" (37.78s)
add(41.0, whoosh(0.25), 0.4)                 # Starc 36 vs IND
add(44.0, metallic_ding(0.4, 1500), 0.7)     # Bumrah 17 vs AUS
add(46.5, thud(0.5, 130, 32), 1.05)          # "Point, Bumrah" (46.46s) - Stamp slam
add(46.6, metallic_ding(0.6, 1600), 0.8)     # Scoreboard 2 - 2
add(46.7, crowd_roar(2.5), 0.6)

# Outro & Tiebreaker (47.6s - 57.39s)
add(47.6, whoosh(0.4), 0.6)                  # Transition to Tiebreaker
add(47.8, sub_drop(0.8), 0.8)                # "Two all" (47.81s)
add(50.2, metallic_ding(0.8, 1300), 0.7)     # "separated by point-two-two" (50.05s)
add(53.6, thud(0.4, 110, 35), 0.9)           # "So you decide" (53.64s)
add(54.8, crowd_roar(3.5), 0.5)              # Final CTA & Question

# Normalize & write WAV
peak = max(abs(s) for s in buf) or 1.0
scale = 0.90 / peak
raw = bytearray()
for s in buf:
    v = max(-32768, min(32767, int(s * scale * 32767)))
    raw.extend(struct.pack("<h", v))

out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\Bumrah vs Starc\assets"
out_wav = os.path.join(out_dir, "sfx.wav")
with wave.open(out_wav, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(raw)

print(f"Generated {out_wav} ({DUR}s, {len(raw)} bytes)")

# Mix with voiceover into renders/full_audio_mix.wav
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
renders_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\Bumrah vs Starc\renders"
vo_path = os.path.join(out_dir, "voiceover.wav")
mix_path = os.path.join(renders_dir, "full_audio_mix.wav")

cmd_mix = [
    FFMPEG, "-y",
    "-i", vo_path,
    "-i", out_wav,
    "-filter_complex", "[0:a]volume=1.0[a0];[1:a]volume=0.36[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=2",
    mix_path
]
subprocess.run(cmd_mix, check=True)
print(f"Mixed full audio -> {mix_path}")
