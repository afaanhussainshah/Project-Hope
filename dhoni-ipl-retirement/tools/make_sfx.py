import math
import os
import random
import struct
import wave
import subprocess
import imageio_ffmpeg

SR = 44100
DUR = 47.73
N = int(SR * DUR)
buf = [0.0] * N

def add(t, s, vol=1.0):
    start = int(t * SR)
    for i, v in enumerate(s):
        idx = start + i
        if 0 <= idx < N:
            buf[idx] += v * vol

def thud(d=0.4, f0=110, f1=34):
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

def whistle(d=0.6, f=2400):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        vib = math.sin(2 * math.pi * 18 * (i / SR)) * 80
        phase += 2 * math.pi * (f + vib) / SR
        env = math.sin(math.pi * frac) ** 1.5
        noise = random.uniform(-0.15, 0.15)
        out.append((math.sin(phase) * 0.85 + noise) * env)
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

def crowd_cheer(d=3.0):
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

def sub_drop(d=0.8):
    L = int(SR * d)
    out = []
    phase = 0.0
    for i in range(L):
        frac = i / L
        f = 90 * (1.0 - frac * 0.7)
        phase += 2 * math.pi * f / SR
        env = (1.0 - frac) ** 1.5
        out.append(math.sin(phase) * env)
    return out

# =========================================================================
# EXACT MILLISECOND-ALIGNED SFX PLACEMENT
# =========================================================================

# Scene 1: The Question & "Definitely Not" (0.0s - 12.8s)
add(0.2, whoosh(0.3), 0.4)
add(5.3, whistle(0.4, 2200), 0.5)
add(8.5, crowd_cheer(2.5), 0.35)
add(11.0, thud(0.45, 120, 35), 0.95)         # DEFINITELY NOT stamp slam (voice: 11.01s)
add(11.2, crowd_cheer(2.5), 0.6)

# Scene 2: The Shock & Silence (12.8s - 14.8s)
add(12.8, rip(0.35), 0.75)                   # Red line strikes through Definitely Not
add(13.1, sub_drop(0.9), 1.0)                # Heartbreak bass drop (...Until today at 13.10s)
add(13.2, thud(0.4, 95, 30), 0.85)           # UNTIL TODAY stamp slam

# Scene 3: The 5 Trophies Dynasty (14.8s - 25.8s)
add(14.8, whoosh(0.35), 0.5)
# 5 rapid trophy dings (voice says "Five trophies" 14.87s - 15.65s, "Ten finals" 16.26s - 17.34s)
add(14.9, metallic_ding(0.4, 1200), 0.8)     # Trophy 1 (2010)
add(15.3, metallic_ding(0.4, 1400), 0.8)     # Trophy 2 (2011)
add(15.7, metallic_ding(0.4, 1600), 0.8)     # Trophy 3 (2018)
add(16.3, metallic_ding(0.4, 1800), 0.8)     # Trophy 4 (2021)
add(16.8, metallic_ding(0.5, 2000), 0.9)     # Trophy 5 (2023)
add(17.0, thud(0.5, 130, 36), 1.0)           # 5 IPL TROPHIES stamp slam
add(17.2, crowd_cheer(3.5), 0.6)

# Scene 4: Busted Knees, Warrior Heart (25.8s - 35.8s)
add(25.8, whoosh(0.35), 0.5)
add(26.1, thud(0.3, 85, 40), 0.5)            # Heavy limping step (voice: "Busted knees" 26.09s)
add(27.4, thud(0.3, 85, 40), 0.5)            # Heavy limping step (voice: "Heavy strapping" 27.34s)
add(28.6, whistle(0.4, 2100), 0.4)           # "Limping between wickets" 28.56s
add(31.2, crowd_cheer(4.5), 0.85)            # "40,000 voices screamed his name" (voice: 31.18s)
add(31.5, whistle(0.6, 2500), 0.75)          # Whistle Podu roar
add(32.0, whistle(0.5, 2300), 0.65)
add(31.4, thud(0.45, 115, 34), 0.95)         # WARRIOR IN YELLOW stamp slam

# Scene 5: Never Another Thala (35.8s - 44.0s)
add(35.8, whoosh(0.4), 0.6)
add(36.6, metallic_ding(0.8, 1100), 0.7)     # Crown landing on jersey collar
add(40.5, thud(0.5, 125, 32), 1.0)           # NEVER ANOTHER THALA stamp (voice: 40.50s)
add(40.7, crowd_cheer(3.2), 0.5)

# Scene 6: The Farewell (44.0s - 47.73s)
add(44.0, whoosh(0.35), 0.5)
add(44.3, thud(0.5, 120, 30), 1.0)           # END OF AN ERA stamp (voice: 44.43s)
add(46.1, metallic_ding(0.9, 980), 0.75)     # Chime on "Thank you, Number Seven" (voice: 46.15s)
add(46.1, thud(0.55, 135, 28), 1.05)         # THANK YOU #7 stamp
add(46.3, crowd_cheer(3.0), 0.45)

# Normalize & write WAV
peak = max(abs(s) for s in buf) or 1.0
scale = 0.90 / peak
raw = bytearray()
for s in buf:
    v = max(-32768, min(32767, int(s * scale * 32767)))
    raw.extend(struct.pack("<h", v))

out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\dhoni-ipl-retirement\assets"
out_wav = os.path.join(out_dir, "sfx.wav")
with wave.open(out_wav, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(raw)

print(f"Generated {out_wav} ({DUR}s, {len(raw)} bytes)")

# Mix with voiceover into renders/full_audio_mix.wav
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
renders_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\dhoni-ipl-retirement\renders"
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
