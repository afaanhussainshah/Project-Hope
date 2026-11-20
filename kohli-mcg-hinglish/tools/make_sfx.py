import os
import wave
import numpy as np
import json

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-mcg-hinglish"
VO_WAV = os.path.join(PROJECT_DIR, "assets", "voiceover.wav")
SFX_WAV = os.path.join(PROJECT_DIR, "assets", "sfx.wav")
MIX_WAV = os.path.join(PROJECT_DIR, "renders", "full_audio_mix.wav")

SR = 44100

with wave.open(VO_WAV, "rb") as wf:
    vo_sr = wf.getframerate()
    vo_raw = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

assert vo_sr == SR, f"Expected {SR}Hz, got {vo_sr}Hz"
N = len(vo_raw)
DUR = N / SR
print(f"Loaded voiceover: {DUR:.3f}s ({N} samples)")

sfx = np.zeros(N, dtype=np.float32)
rng = np.random.default_rng(18)  # Kohli #18 seed


def add_at(buf, t_sec, clip, gain=1.0):
    i0 = int(round(t_sec * SR))
    if i0 >= len(buf) or i0 + len(clip) <= 0:
        return
    src_start = max(0, -i0)
    dst_start = max(0, i0)
    length = min(len(clip) - src_start, len(buf) - dst_start)
    if length > 0:
        buf[dst_start:dst_start + length] += clip[src_start:src_start + length] * gain


def make_whoosh(dur=0.38, f0=180, f1=1600):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    env = np.sin(np.pi * t / dur) ** 1.6
    noise = rng.normal(0, 1, len(t))
    freq = np.linspace(f0, f1, len(t))
    mod = np.sin(2 * np.pi * np.cumsum(freq) / SR)
    return (0.45 * noise * env + 0.3 * mod * env).astype(np.float32)


def make_stamp_thud(dur=0.42):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    freq = 150 * np.exp(-t * 14) + 36
    body = np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-t * 9.5)
    slap = rng.normal(0, 1, len(t)) * np.exp(-t * 45) * 0.7
    return (body * 0.95 + slap).astype(np.float32)


def make_sub_drop(dur=1.1, f_start=120, f_end=32):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    freq = f_start * (f_end / f_start) ** (t / dur)
    env = np.exp(-t * 2.8) * (1 - np.exp(-t * 70))
    return (np.sin(2 * np.pi * np.cumsum(freq) / SR) * env * 0.9).astype(np.float32)


def make_wood_shatter(dur=0.55):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    crack = rng.normal(0, 1, len(t)) * np.exp(-t * 32)
    knock1 = np.sin(2 * np.pi * 580 * t) * np.exp(-t * 24)
    knock2 = np.sin(2 * np.pi * 920 * t) * np.exp(-np.maximum(0, t - 0.035) * 22) * (t >= 0.035)
    knock3 = np.sin(2 * np.pi * 1420 * t) * np.exp(-np.maximum(0, t - 0.08) * 20) * (t >= 0.08)
    return (0.55 * crack + 0.45 * knock1 + 0.38 * knock2 + 0.3 * knock3).astype(np.float32)


def make_bat_crack(dur=0.48, power=1.0):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    ping1 = np.sin(2 * np.pi * 1280 * t) * np.exp(-t * 40)
    ping2 = np.sin(2 * np.pi * 2150 * t) * np.exp(-t * 55) * 0.6
    sub = np.sin(2 * np.pi * 85 * np.exp(-t * 12) * t) * np.exp(-t * 14) * 0.8
    snap = rng.normal(0, 1, len(t)) * np.exp(-t * 65) * 0.85
    return ((ping1 + ping2 + sub + snap) * 0.6 * power).astype(np.float32)


def make_heartbeat(dur=0.32):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    lub = np.sin(2 * np.pi * 65 * t) * np.exp(-t * 25)
    t2 = np.maximum(0, t - 0.11)
    dub = np.sin(2 * np.pi * 55 * t2) * np.exp(-t2 * 22) * (t >= 0.11) * 0.85
    return (lub + dub).astype(np.float32)


def make_riser(dur=3.2, f0=70, f1=340):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    freq = np.linspace(f0, f1, len(t))
    env = (t / dur) ** 2.2
    tone = np.sin(2 * np.pi * np.cumsum(freq) / SR) * 0.4
    shimmer = rng.normal(0, 0.18, len(t)) * env
    return ((tone + shimmer) * env).astype(np.float32)


def make_chord(freqs, dur=3.0):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    sig = np.zeros_like(t)
    for f in freqs:
        sig += np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2 * t)
    env = np.exp(-t * 1.6) * (1 - np.exp(-t * 40))
    return (sig / len(freqs) * env * 0.45).astype(np.float32)


def make_crowd_swell(dur=5.0, peak=0.7):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 0.85
    noise = rng.normal(0, 1, len(t))
    low_rumble = np.sin(2 * np.pi * 68 * t) * 0.25
    cheer = (noise * 0.65 + low_rumble) * env * peak
    return cheer.astype(np.float32)


def make_firework_burst(dur=0.6):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    boom = np.sin(2 * np.pi * 80 * np.exp(-t * 15) * t) * np.exp(-t * 10) * 0.8
    crackle = rng.normal(0, 1, len(t)) * np.exp(-np.maximum(0, t - 0.08) * 8) * (t >= 0.08) * 0.4
    return (boom + crackle).astype(np.float32)


# -------------------------------------------------------------
# ASSEMBLE SFX TRACK (TIMED TO HINGLISH SCRIPT)
# -------------------------------------------------------------

# Scene 1: Twenty-Eight Runs. Sirf Aath Balls. (0.0s - 7.8s)
add_at(sfx, 0.05, make_whoosh(0.35, 260, 90), 0.5)
add_at(sfx, 0.12, make_stamp_thud(0.42), 0.9)        # "TWENTY-EIGHT RUNS"
add_at(sfx, 1.76, make_stamp_thud(0.40), 0.9)        # "SIRF AATH BALLS"
add_at(sfx, 1.80, make_sub_drop(1.1, 120, 32), 0.7)
add_at(sfx, 3.48, make_whoosh(0.35, 140, 600), 0.4) # "WIN PREDICTOR"
add_at(sfx, 5.20, make_stamp_thud(0.48), 0.95)       # "LAGBHAG NAMUMKIN"
add_at(sfx, 5.25, make_sub_drop(1.4, 140, 28), 0.85)

# Scene 2: Melbourne. Pakistan. 90,000+ Crowd & 31/4 (7.8s - 23.4s)
add_at(sfx, 7.90, make_crowd_swell(4.8, 0.28), 0.35) # Melbourne murmur
add_at(sfx, 8.00, make_stamp_thud(0.35), 0.6)        # "MELBOURNE"
add_at(sfx, 8.98, make_stamp_thud(0.35), 0.6)        # "PAKISTAN"
add_at(sfx, 10.05, make_stamp_thud(0.42), 0.75)      # "90,000+ LOG"
add_at(sfx, 12.30, make_wood_shatter(0.55), 0.85)    # 31/4 wickets tumbling
add_at(sfx, 13.50, make_wood_shatter(0.45), 0.75)    # Wickets
add_at(sfx, 16.00, make_stamp_thud(0.45), 0.85)      # "SAB KEH RAHE THE"
add_at(sfx, 17.28, make_stamp_thud(0.45), 0.9)       # "AB TOH KHEL KHATAM"
add_at(sfx, 17.35, make_sub_drop(1.2, 110, 30), 0.7)
add_at(sfx, 18.84, make_whoosh(0.5, 100, 900), 0.5)  # "LEKIN EK AADMI NE..."
add_at(sfx, 22.30, make_stamp_thud(0.5), 0.95)       # "VIRAT KOHLI"
add_at(sfx, 22.35, make_chord([146.83, 220.00, 293.66], dur=3.0), 0.7) # Heroic tone

# Heartbeat tension rhythm during stand (23.5s -> 34.0s)
heartbeats = [23.6, 24.6, 25.6, 26.6, 27.8, 29.0, 30.1, 31.0, 31.9, 32.7, 33.4]
for idx, ht in enumerate(heartbeats):
    gain = 0.32 + 0.04 * idx
    add_at(sfx, ht, make_heartbeat(0.28), gain)

# Scene 3: Hardik & Kohli Partnership (23.4s - 33.9s)
add_at(sfx, 23.55, make_whoosh(0.35, 160, 550), 0.4)
add_at(sfx, 27.10, make_stamp_thud(0.48), 0.9)       # "113 RUNS PARTNERSHIP"
add_at(sfx, 27.15, make_sub_drop(1.1, 130, 36), 0.7)
add_at(sfx, 31.90, make_riser(2.5, 75, 360), 0.6)    # "TIME KHATAM HO RAHA THA"

# Scene 4: Haris Rauf & The Two Sixes (33.9s - 44.3s)
add_at(sfx, 34.05, make_whoosh(0.55, 350, 2000), 0.75) # 148 km/h express ball
add_at(sfx, 34.15, make_stamp_thud(0.42), 0.85)        # "HARIS RAUF"
add_at(sfx, 35.00, make_whoosh(0.4, 200, 1100), 0.5)  # "TEZ RAFTAAR"

# 38.00s - BALL 18.5: THE STRAIGHT SIX OVER RAUF'S HEAD!
add_at(sfx, 38.00, make_bat_crack(0.55, power=1.4), 1.0) # ICONIC WILLOW CRACK #1
add_at(sfx, 38.05, make_sub_drop(1.3, 160, 35), 0.85)
add_at(sfx, 38.10, make_whoosh(0.7, 480, 2600), 0.8)   # High launch trajectory
add_at(sfx, 38.30, make_crowd_swell(6.5, 0.9), 0.85)   # MCG EXPLOSION!

# 39.15s - BALL 18.6: THE FLICK OVER FINE LEG!
add_at(sfx, 39.15, make_bat_crack(0.5, power=1.2), 0.95) # ICONIC WILLOW CRACK #2
add_at(sfx, 39.20, make_whoosh(0.6, 520, 2400), 0.75)
add_at(sfx, 39.80, make_stamp_thud(0.45), 0.9)          # "PHIR EK AUR... SIX!"
add_at(sfx, 40.50, make_sub_drop(1.6, 140, 28), 0.85)
add_at(sfx, 42.10, make_crowd_swell(7.0, 0.95), 0.9)   # "MATCH WAPAS AA GAYA!"

# Scene 5: 82* off 53, Diwali & Immortality (44.3s - 53.16s)
add_at(sfx, 44.50, make_stamp_thud(0.45), 0.9)       # "82 NOT OUT"
add_at(sfx, 45.98, make_stamp_thud(0.45), 0.9)       # "53 BALLS"
add_at(sfx, 47.50, make_chord([293.66, 369.99, 440.00, 587.33], dur=4.5), 0.85) # D Major
# Diwali Fireworks
add_at(sfx, 47.60, make_firework_burst(0.7), 0.8)
add_at(sfx, 48.20, make_firework_burst(0.6), 0.7)
add_at(sfx, 48.85, make_firework_burst(0.75), 0.75)
add_at(sfx, 49.50, make_firework_burst(0.65), 0.7)
add_at(sfx, 50.15, make_chord([220.00, 277.18, 329.63, 440.00], dur=4.8), 0.8) # A Major majesty
add_at(sfx, 50.20, make_stamp_thud(0.52), 0.95)      # Final challenge CTA
add_at(sfx, 50.25, make_sub_drop(1.5, 120, 30), 0.75)

# Normalize SFX
peak = np.max(np.abs(sfx))
if peak > 0.92:
    sfx = sfx * (0.92 / peak)
    print(f"Normalized SFX (peak was {peak:.2f})")

# Write SFX WAV
sfx_int16 = (np.clip(sfx, -1.0, 1.0) * 32767.0).astype(np.int16)
with wave.open(SFX_WAV, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(sfx_int16.tobytes())
print(f"Saved SFX: {SFX_WAV}")

# Mix with Voiceover
mix = vo_raw * 1.0 + sfx * 0.78
mix_peak = np.max(np.abs(mix))
if mix_peak > 0.95:
    mix = mix * (0.95 / mix_peak)
    print(f"Normalized Mix (peak was {mix_peak:.2f})")

mix_int16 = (np.clip(mix, -1.0, 1.0) * 32767.0).astype(np.int16)
os.makedirs(os.path.dirname(MIX_WAV), exist_ok=True)
with wave.open(MIX_WAV, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(mix_int16.tobytes())
print(f"Saved Audio Mix: {MIX_WAV}")
