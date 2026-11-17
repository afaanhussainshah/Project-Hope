import math
import os
import random
import struct
import wave
import subprocess
import imageio_ffmpeg

SR = 44100
DUR = 40.36
N = int(SR * DUR)
buf = [0.0] * N

def add(t, s, vol=1.0):
    start = int(t * SR)
    for i, v in enumerate(s):
        idx = start + i
        if 0 <= idx < N:
            buf[idx] += v * vol

def thud(d=0.35, f0=95, f1=38):
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

def rip(d=0.45):
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

def wood_knock(d=0.22, f=280):
    L = int(SR * d)
    out = []
    p = 0.0
    for i in range(L):
        frac = i / L
        p += 2 * math.pi * f / SR
        env = math.exp(-frac * 28)
        noise = random.uniform(-0.25, 0.25) * math.exp(-frac * 35)
        out.append((math.sin(p) * 0.8 + noise) * env)
    return out

def bat_crack(d=0.3):
    L = int(SR * d)
    out = []
    p = 0.0
    for i in range(L):
        frac = i / L
        p += 2 * math.pi * 1400 / SR
        env = math.exp(-frac * 20)
        noise = random.uniform(-0.5, 0.5) * math.exp(-frac * 25)
        out.append((math.sin(p) * 0.7 + noise) * env)
    return out

def wood_snap(d=0.5):
    L = int(SR * d)
    out = []
    for i in range(L):
        frac = i / L
        env = (1.0 - frac) ** 1.5
        n1 = random.uniform(-1, 1) if (i % 8 < 4) else random.uniform(-0.3, 0.3)
        out.append(n1 * env)
    return out

def cannon_boom(d=0.7):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        f = 130 * math.exp(-frac * 6) + 32
        phase += 2 * math.pi * f / SR
        env = (1.0 - frac) ** 1.6
        noise = random.uniform(-0.3, 0.3) * math.exp(-frac * 8)
        out.append((math.sin(phase) + noise) * env)
    return out

def riser(d=2.5):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        f = 140 + 600 * (frac ** 2)
        phase += 2 * math.pi * f / SR
        env = frac ** 1.5
        out.append(math.sin(phase) * env * 0.5)
    return out

# Place SFX:
# Scene 1: Money Waste Hook (0 - 4.8s)
add(0.1, whoosh(0.3), 0.5)
add(2.0, rip(0.4), 0.7)                    # Price tag rips!
add(2.8, thud(0.4, 110, 35), 0.9)          # Wasting money stamp

# Scene 2: Grade 1 & Myth or Fact (4.8 - 12.8s)
add(4.8, whoosh(0.35), 0.6)
add(5.2, thud(0.3, 90, 42), 0.6)           # 12 Grains card
add(10.8, thud(0.35, 120, 40), 0.95)       # MYTH stamp
add(11.9, thud(0.35, 130, 38), 1.0)        # FACT stamp

# Scene 3: Tree Rings (12.8 - 16.2s)
add(12.8, whoosh(0.4), 0.6)
add(13.2, wood_knock(0.25, 220), 0.7)

# Scene 4: 12 Grains Brittle & Crack (16.2 - 24.2s)
add(16.2, whoosh(0.35), 0.6)
add(19.4, bat_crack(0.35), 1.1)            # Explosive ball ping
add(21.5, wood_snap(0.55), 1.2)            # Crack splits the toe!
add(21.8, thud(0.4, 100, 35), 0.8)         # Warning stamp

# Scene 5: 6 Grains Flexible Cannon (24.2 - 33.2s)
add(24.2, whoosh(0.35), 0.6)
# Knocking mallet hits
add(25.4, wood_knock(0.22, 260), 0.9)
add(26.2, wood_knock(0.22, 275), 0.9)
add(27.0, wood_knock(0.22, 290), 0.9)
add(27.8, riser(2.2), 0.6)
add(29.8, cannon_boom(0.8), 1.2)           # Cannon boom!
add(30.4, thud(0.45, 115, 35), 1.0)        # 2X Lifespan stamp

# Scene 6: Stop Counting Lines & CTA (33.2 - 40.36s)
add(33.2, whoosh(0.4), 0.7)
add(33.8, thud(0.5, 125, 32), 1.1)         # STOP COUNTING LINES stamp
add(38.2, whoosh(0.3), 0.5)
add(38.5, wood_knock(0.2, 320), 0.8)

# Normalize & write WAV
peak = max(abs(s) for s in buf) or 1.0
scale = 0.90 / peak
raw = bytearray()
for s in buf:
    v = max(-32768, min(32767, int(s * scale * 32767)))
    raw.extend(struct.pack("<h", v))

out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\bat-grains-myth\assets"
out_wav = os.path.join(out_dir, "sfx.wav")
with wave.open(out_wav, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(raw)

print(f"Generated {out_wav} ({DUR}s, {len(raw)} bytes)")

# Mix with voiceover into renders/full_audio_mix.wav
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
renders_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\bat-grains-myth\renders"
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
