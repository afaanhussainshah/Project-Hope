import math
import os
import random
import struct
import wave
import subprocess
import imageio_ffmpeg

SR = 44100
DUR = 34.43
N = int(SR * DUR)
buf = [0.0] * N

def add(t, s, vol=1.0):
    start = int(t * SR)
    for i, v in enumerate(s):
        idx = start + i
        if 0 <= idx < N:
            buf[idx] += v * vol

def thud(d=0.35, f0=90, f1=38):
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

def prison_clank(d=0.6):
    L = int(SR * d)
    out = []
    p1 = p2 = 0.0
    for i in range(L):
        frac = i / L
        p1 += 2 * math.pi * 320 / SR
        p2 += 2 * math.pi * 840 / SR
        env = math.exp(-frac * 7)
        s = 0.6 * math.sin(p1) + 0.4 * math.sin(p2)
        out.append(s * env)
    return out

def rip(d=0.45):
    L = int(SR * d)
    out = []
    for i in range(L):
        frac = i / L
        r = random.uniform(-1, 1)
        mod = math.sin(2 * math.pi * 30 * (i / SR))
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

def bat_edge(d=0.18):
    L = int(SR * d)
    out = []
    p = 0.0
    for i in range(L):
        frac = i / L
        p += 2 * math.pi * 1800 / SR
        env = math.exp(-frac * 24)
        noise = random.uniform(-0.4, 0.4)
        out.append((math.sin(p) * 0.7 + noise) * env)
    return out

def crowd_gasp(d=0.8):
    L = int(SR * d)
    out = []
    for i in range(L):
        frac = i / L
        env = math.sin(math.pi * frac)
        noise = random.uniform(-1, 1)
        out.append(noise * env * 0.5)
    return out

def drone(d=4.0, f=55):
    L = int(SR * d)
    out = []
    p = 0.0
    for i in range(L):
        frac = i / L
        p += 2 * math.pi * f / SR
        env = math.sin(math.pi * frac)
        out.append(math.sin(p) * env * 0.4)
    return out

def riser(d=3.0):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        f = 120 + 700 * (frac ** 2)
        phase += 2 * math.pi * f / SR
        env = frac ** 1.5
        noise = random.uniform(-0.15, 0.15) * frac
        out.append((math.sin(phase) + noise) * env * 0.6)
    return out

# Place SFX precisely aligned with detected speech events:
# 0.0s - 3.8s: Five years banned
add(0.0, drone(3.8, 55), 0.6)
add(0.5, prison_clank(0.5), 0.7)
add(0.6, thud(0.4, 110, 35), 0.9)          # 5 YEARS BANNED stamp
add(1.8, thud(0.35, 100, 35), 0.8)         # EXILED stamp

# 4.0s - 7.2s: In 2016 returned from shadows
add(3.9, rip(0.5), 0.8)                    # Paper rip to green
add(4.3, whoosh(0.4), 0.6)
add(5.5, thud(0.3, 85, 40), 0.5)

# 7.2s - 11.4s: The Oval / Terrifying Trio
add(7.2, whoosh(0.45), 0.7)                # Transition to Oval
add(7.5, thud(0.35, 95, 42), 0.6)          # Trio slam
add(9.5, whoosh(0.3), 0.4)

# 11.4s - 15.5s: Over one - Rohit Sharma trapped!
add(11.4, whoosh(0.35), 0.8)               # Amir run-up & release
add(12.5, whoosh(0.25), 0.6)               # Late swinging missile
add(13.5, thud(0.45, 140, 38), 1.0)        # LBW pad impact!
add(13.8, prison_clank(0.3), 0.6)          # Umpire finger raised!
add(14.2, thud(0.3, 80, 40), 0.7)          # Scorecard 0/1

# 15.5s - 18.0s: Over three - Kohli dropped!
add(15.5, whoosh(0.35), 0.7)
add(16.2, bat_edge(0.2), 0.9)              # Thick outside edge
add(16.5, crowd_gasp(0.7), 0.8)            # DROPPED gasp!
add(17.2, thud(0.25, 75, 45), 0.5)

# 18.0s - 22.2s: Next ball - Kohli gone!
add(18.0, whoosh(0.38), 0.9)               # Fast furious ball
add(19.2, bat_edge(0.25), 1.1)             # Leading edge CLICK!
add(19.6, thud(0.5, 130, 35), 1.1)         # Point catch & roar!
add(20.2, thud(0.4, 110, 35), 1.0)         # KOHLI GONE stamp!

# 22.2s - 24.8s: Dhawan sliced behind
add(22.2, whoosh(0.3), 0.7)
add(23.0, bat_edge(0.2), 0.9)              # Nick behind
add(23.3, thud(0.35, 100, 40), 0.8)        # Keeper catch

# 24.8s - 29.2s: Three wickets, 16 runs, demolished
add(24.8, thud(0.5, 150, 30), 1.1)         # Stumps cartwheeling
add(25.0, rip(0.4), 0.7)
add(26.5, thud(0.4, 90, 40), 0.9)          # Demolished stamp!

# 29.2s - 34.43s: Immortal Redemption
add(29.0, riser(3.0), 0.75)                # Triumphant orchestral riser
add(31.8, thud(0.65, 120, 30), 1.2)        # CONQUERED THE WORLD slam!
add(32.0, whoosh(0.5), 0.8)

# Normalize & write WAV
peak = max(abs(s) for s in buf) or 1.0
scale = 0.90 / peak
raw = bytearray()
for s in buf:
    v = max(-32768, min(32767, int(s * scale * 32767)))
    raw.extend(struct.pack("<h", v))

out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\amir-2017-ct\assets"
out_wav = os.path.join(out_dir, "sfx.wav")
with wave.open(out_wav, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(raw)

print(f"Generated {out_wav} ({DUR}s, {len(raw)} bytes)")

# Mix with voiceover into renders/full_audio_mix.wav
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
renders_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\amir-2017-ct\renders"
vo_path = os.path.join(out_dir, "voiceover.wav")
mix_path = os.path.join(renders_dir, "full_audio_mix.wav")

cmd_mix = [
    FFMPEG, "-y",
    "-i", vo_path,
    "-i", out_wav,
    "-filter_complex", "[0:a]volume=1.0[a0];[1:a]volume=0.38[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=2",
    mix_path
]
subprocess.run(cmd_mix, check=True)
print(f"Mixed full audio -> {mix_path}")
