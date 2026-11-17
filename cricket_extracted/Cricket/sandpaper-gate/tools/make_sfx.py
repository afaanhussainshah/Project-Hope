"""Synthesises the reel's sound-effect bed (no samples, no downloads) -> assets/sfx.wav

Run from the project folder:  python tools/make_sfx.py
Voiceover is NOT included; it is added on top by the editor.
"""
import math, random, struct, wave, os

SR = 44100
DUR = 41.0
N = int(SR * DUR)
buf = [0.0] * N
rng = random.Random(2018)


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
        click = (rng.random() * 2 - 1) * math.exp(-90 * x) * 0.5
        out.append((math.sin(ph) + click) * env)
    return out


def noise(dur, lo, hi, shape="hann", sweep=0.0):
    """Band-limited noise: one-pole low-pass minus a slower low-pass. sweep moves the band."""
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
        else:  # decay
            env = math.exp(-6 * x) * min(1.0, i / 40)
        out.append((a - b) * env * 3.0)
    return out


def whoosh(dur=0.36):
    return noise(dur, 300, 2200, "hann", sweep=1.6)


def scratch(dur=0.08):
    return noise(dur, 1800, 7000, "hann")


def rip(dur=0.4):
    base = noise(dur, 900, 6000, "decay")
    gate, out = 1.0, []
    for i, s in enumerate(base):
        if i % 90 == 0:
            gate = 0.25 + rng.random()
        out.append(s * gate)
    return out


def click():
    out = noise(0.02, 2500, 9000, "decay")
    return out + [0.0] * int(0.045 * SR) + [s * 0.7 for s in noise(0.02, 2000, 8000, "decay")]


# --- tension bed: low drone + slow heartbeat ---
for i in range(N):
    t = i / SR
    trem = 0.75 + 0.25 * math.sin(2 * math.pi * 0.25 * t)
    d = 0.5 * math.sin(2 * math.pi * 55 * t) + 0.3 * math.sin(2 * math.pi * 82.5 * t) + 0.14 * math.sin(2 * math.pi * 110.3 * t)
    edge = min(1.0, t / 0.08, (DUR - t) / 0.08)
    buf[i] += d * trem * 0.11 * edge
beat = thud(0.22, 70, 38)
t = 0.5
while t < 40.4:
    add(t, beat, 0.2)
    add(t + 0.2, beat, 0.13)
    t += 1.0

# --- hits synced to the picture (kept light under the voiceover) ---
add(0.0, whoosh(0.4), 0.7)
add(0.4, thud(), 0.9)
for st in (2.2, 2.38, 2.51):
    add(st, scratch(0.13), 0.7)
add(2.62, rip(), 0.6)
add(2.62, thud(), 0.6)
for wt in (5.3, 15.9, 19.9, 27.45, 34.3):
    add(wt - 0.18, whoosh(), 0.6)
add(5.6, thud(0.2), 0.4)
add(6.99, thud(), 0.7)
add(9.05, thud(0.25), 0.55)
add(9.37, noise(0.3, 250, 2500, "rise", sweep=2.0), 0.65)
add(9.65, thud(0.25), 0.55)
for k in range(9):
    add(10.9 + k * 0.09, scratch(), 0.6)
add(11.9, thud(0.2), 0.4)
for k in range(5):
    add(12.94 + k * 0.07, scratch(0.065), 0.65)
add(13.62, thud(), 0.75)
add(13.75, noise(0.7, 500, 3000, "hann"), 0.3)
for ct in (16.0, 16.6, 17.3, 17.9, 18.5, 18.7, 19.0, 19.4):
    add(ct, click(), 0.45)
add(18.16, scratch(0.1), 0.5)
add(18.44, thud(0.45, 140, 36), 0.6)
add(20.0, whoosh(0.3), 0.45)
add(21.19, thud(), 0.7)
add(22.55, whoosh(0.3), 0.45)
add(25.47, thud(), 0.7)
add(27.68, thud(0.2), 0.4)
for wt in (28.8, 29.35, 32.39):
    add(wt, whoosh(0.28), 0.45)
for stp in (30.74, 31.14, 33.45):
    add(stp, thud(0.4, 150, 40), 0.9)
add(34.6, thud(), 0.75)
add(36.4, click(), 0.4)
add(36.72, click(), 0.4)
add(37.9, noise(0.7, 120, 700, "hann"), 0.45)
add(39.4, rip(), 0.5)
add(39.4, thud(), 0.5)
add(40.46, noise(0.52, 300, 2600, "rise", sweep=2.2), 0.8)

peak = max(abs(s) for s in buf) or 1.0
scale = 0.7 / peak  # about -3 dBFS
out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "sfx.wav")
with wave.open(out_path, "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(b"".join(struct.pack("<h", int(max(-1.0, min(1.0, s * scale)) * 32767)) for s in buf))
print("wrote", os.path.normpath(out_path), "peak-scale", round(scale, 3))
