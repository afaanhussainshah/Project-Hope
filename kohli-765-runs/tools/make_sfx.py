"""Synthesises the sound-effect bed for the 44.04-second Kohli Reel -> assets/sfx.wav
Aligned with your new 44.04s ElevenLabs narration.
"""
import math, random, struct, wave, os, subprocess
import imageio_ffmpeg

SR = 44100
DUR = 44.04
N = int(SR * DUR)
buf = [0.0] * N
rng = random.Random(2023)

def add(t, samples, gain=1.0):
    i0 = int(t * SR)
    for i, s in enumerate(samples):
        j = i0 + i
        if 0 <= j < N:
            buf[j] += s * gain

def thud(dur=0.32, f0=120.0, f1=42.0):
    out, ph = [], 0.0
    n = int(dur * SR)
    for i in range(n):
        x = i / n
        f = f1 + (f0 - f1) * math.exp(-6 * x)
        ph += 2 * math.pi * f / SR
        env = math.exp(-5.5 * x) * min(1.0, i / 60)
        click_val = (rng.random() * 2 - 1) * math.exp(-90 * x) * 0.5
        out.append((math.sin(ph) + click_val) * env)
    return out

def bat_crack():
    dur = 0.28
    n = int(dur * SR)
    out = []
    for i in range(n):
        x = i / n
        snap = (rng.random() * 2 - 1) * math.exp(-120 * x)
        wood = math.sin(2 * math.pi * 780 * (i / SR)) * math.exp(-22 * x)
        sub = math.sin(2 * math.pi * 140 * (i / SR)) * math.exp(-14 * x)
        out.append((snap * 0.85 + wood * 0.55 + sub * 0.4) * min(1.0, i / 30))
    return out

def noise(dur, lo, hi, shape="hann", sweep=0.0):
    out, a, b = [], 0.0, 0.0
    n = int(dur * SR)
    for i in range(n):
        x = i / n
        k = 1.0 + sweep * math.sin(math.pi * x)
        ah = min(0.99, 2 * math.pi * hi * k / SR)
        al = min(0.99, 2 * math.pi * lo * k / SR)
        w = rng.random() * 2 - 1
        a += ah * (w - a)
        b += al * (w - b)
        if shape == "hann":
            env = math.sin(math.pi * x) ** 2
        elif shape == "rise":
            env = x ** 2.5 * (1 - x ** 12)
        else:
            env = math.exp(-6 * x) * min(1.0, i / 40)
        out.append((a - b) * env * 3.0)
    return out

def whoosh(dur=0.36):
    return noise(dur, 300, 2200, "hann", sweep=1.6)

def click():
    out = noise(0.02, 2500, 9000, "decay")
    return out + [0.0] * int(0.045 * SR) + [s * 0.7 for s in noise(0.02, 2000, 8000, "decay")]

def rip(dur=0.4):
    base = noise(dur, 900, 6000, "decay")
    gate, out = 1.0, []
    for i, s in enumerate(base):
        if i % 90 == 0:
            gate = 0.25 + rng.random()
        out.append(s * gate)
    return out

# --- Tension Bed: Sub Drone ---
for i in range(N):
    t = i / SR
    # Dead silence drop on Ahmedabad silence (27.8s to 33.0s)
    if 27.8 <= t <= 33.0:
        continue
    trem = 0.75 + 0.25 * math.sin(2 * math.pi * 0.25 * t)
    d = 0.5 * math.sin(2 * math.pi * 55 * t) + 0.3 * math.sin(2 * math.pi * 82.5 * t) + 0.14 * math.sin(2 * math.pi * 110.3 * t)
    edge = min(1.0, t / 0.12, (DUR - t) / 0.12)
    buf[i] += d * trem * 0.10 * edge

# Continuous Heartbeat Pulse
beat = thud(0.22, 70, 38)
t = 0.5
while t < 43.5:
    if not (27.5 <= t <= 33.0):
        add(t, beat, 0.22)
        add(t + 0.2, beat, 0.14)
    t += 1.0

# Synchronized Cinematic Hits
add(0.0, whoosh(0.4), 0.7)
add(1.0, thud(0.35, 130, 42), 0.75)        # 95.62 AVG stamp
add(3.0, thud(0.30, 120, 45), 0.70)        # 90.31 SR stamp
add(4.5, thud(0.40, 140, 38), 0.85)        # 765 RUNS slam
add(11.6, rip(0.45), 0.8)                  # Destiny tear
add(13.8, whoosh(0.38), 0.8)               # Wipe 1
add(14.1, thud(0.40, 110, 40), 0.9)        # Kohli Reveal
add(16.5, bat_crack(), 0.95)               # 50th Century Shot
add(16.8, click(), 0.5)                    # Camera flash 1
add(17.2, click(), 0.5)                    # Camera flash 2
add(18.0, click(), 0.5)                    # Camera flash 3
add(21.0, whoosh(0.38), 0.85)              # Wipe 2 (Ahmedabad)
add(21.3, thud(0.35, 95, 42), 0.75)        # Ahmedabad final slam
add(25.8, whoosh(0.28), 0.8)               # Fast ball incoming
add(26.4, bat_crack(), 1.0)                # The Inside Edge!
add(26.8, thud(0.55, 150, 35), 1.1)        # Stumps shattered!
add(26.9, rip(0.5), 0.9)                   # Bails fly!
# (Dead silence 27.8s - 33.0s)
add(33.0, whoosh(0.42), 0.85)              # Wipe 3 (Heartbreak)
add(33.3, thud(0.30, 70, 35), 0.5)         # Solemn thud
add(36.5, whoosh(0.45), 0.9)               # Wipe 4 (Gold King)
add(37.0, noise(2.5, 200, 2800, "rise"), 0.5) # Triumphant rising swell
add(41.2, thud(0.65, 110, 32), 1.0)        # King slam
add(41.4, whoosh(0.5), 0.7)

# Normalize & write WAV
peak = max(abs(s) for s in buf) or 1.0
scale = 0.92 / peak
raw = bytearray()
for s in buf:
    v = max(-32768, min(32767, int(s * scale * 32767)))
    raw.extend(struct.pack("<h", v))

out_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\assets"
out_wav = os.path.join(out_dir, "sfx.wav")
with wave.open(out_wav, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(raw)

print(f"Generated {out_wav} (44.04s, {len(raw)} bytes)")

# Mix voiceover + SFX -> renders/full_audio_mix.mp3
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
renders_dir = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\renders"
vo_path = os.path.join(out_dir, "voiceover.mp3")
mix_path = os.path.join(renders_dir, "full_audio_mix.mp3")

cmd_mix = [
    FFMPEG, "-y",
    "-i", vo_path,
    "-i", out_wav,
    "-filter_complex", "[0:a]volume=1.0[a0];[1:a]volume=0.35[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=2",
    "-c:a", "libmp3lame",
    "-b:a", "192k",
    mix_path
]
subprocess.run(cmd_mix, check=True)
print(f"Mixed full audio -> {mix_path}")
