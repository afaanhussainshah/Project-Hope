import os
import wave
import numpy as np
import json

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-31-for-4"
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
    # Intense sharp wooden ping + sub thud
    ping1 = np.sin(2 * np.pi * 1280 * t) * np.exp(-t * 40)
    ping2 = np.sin(2 * np.pi * 2150 * t) * np.exp(-t * 55) * 0.6
    sub = np.sin(2 * np.pi * 85 * np.exp(-t * 12) * t) * np.exp(-t * 14) * 0.8
    snap = rng.normal(0, 1, len(t)) * np.exp(-t * 65) * 0.85
    return ((ping1 + ping2 + sub + snap) * 0.6 * power).astype(np.float32)


def make_heartbeat(dur=0.32):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    # Double thump lub-dub
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
    # Envelope ramps up and sustains then decays
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 0.85
    noise = rng.normal(0, 1, len(t))
    # Low frequency rumble + mid roar
    low_rumble = np.sin(2 * np.pi * 68 * t) * 0.25
    cheer = (noise * 0.65 + low_rumble) * env * peak
    return cheer.astype(np.float32)


def make_firework_burst(dur=0.6):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    boom = np.sin(2 * np.pi * 80 * np.exp(-t * 15) * t) * np.exp(-t * 10) * 0.8
    crackle = rng.normal(0, 1, len(t)) * np.exp(-np.maximum(0, t - 0.08) * 8) * (t >= 0.08) * 0.4
    return (boom + crackle).astype(np.float32)


# -------------------------------------------------------------
# ASSEMBLE SFX TRACK
# -------------------------------------------------------------

# Act 1: The Dark Abyss (0.0s - 5.6s)
add_at(sfx, 0.05, make_whoosh(0.4, 250, 90), 0.5)
add_at(sfx, 0.15, make_stamp_thud(0.45), 0.85)      # "31 FOR 4"
add_at(sfx, 0.20, make_sub_drop(1.2, 110, 30), 0.75)
add_at(sfx, 4.20, make_whoosh(0.35, 120, 800), 0.45)
add_at(sfx, 4.30, make_stamp_thud(0.4), 0.8)        # "EXCEPT ONE MAN"

# Act 2: The MCG Crucible & Collapse (5.6s - 15.8s)
add_at(sfx, 5.80, make_crowd_swell(4.5, 0.25), 0.3)  # Distant Melbourne murmur
add_at(sfx, 10.10, make_wood_shatter(0.55), 0.85)    # Top order collapse / wickets tumble
add_at(sfx, 11.65, make_stamp_thud(0.42), 0.75)     # 160 TO CHASE
add_at(sfx, 13.70, make_sub_drop(1.4, 130, 34), 0.65) # Unbearable pressure

# Heartbeat rhythm during pressure (14s -> 24s)
heartbeat_times = [13.9, 14.8, 15.8, 16.9, 18.0, 19.1, 20.2, 21.2, 22.2, 23.1, 24.0, 24.8, 25.6, 26.3]
for idx, ht in enumerate(heartbeat_times):
    gain = 0.35 + 0.03 * idx
    add_at(sfx, ht, make_heartbeat(0.28), gain)

# Act 3: The 113-Run Stand & Rebuild (15.8s - 26.5s)
add_at(sfx, 16.05, make_whoosh(0.3, 150, 500), 0.35)
add_at(sfx, 17.55, make_stamp_thud(0.35), 0.6)      # "HE REBUILT"
add_at(sfx, 21.25, make_stamp_thud(0.45), 0.85)     # "113 RUN STAND"
add_at(sfx, 21.30, make_whoosh(0.4, 200, 950), 0.45)
add_at(sfx, 23.75, make_riser(2.8, 65, 320), 0.55)  # 19th over rising tension

# Act 4: The Shot That Broke A Stadium (26.5s - 36.4s)
add_at(sfx, 26.70, make_whoosh(0.5, 300, 1800), 0.7)  # Rauf 148 km/h express pace swoosh
add_at(sfx, 27.20, make_stamp_thud(0.4), 0.8)         # "HARIS RAUF"
# 28.60s - BALL 5: THE STRAIGHT SIX OVER RAUF'S HEAD!
add_at(sfx, 28.60, make_bat_crack(0.55, power=1.4), 1.0) # ICONIC BAT CRACK #1
add_at(sfx, 28.65, make_sub_drop(1.2, 160, 35), 0.85)
add_at(sfx, 28.70, make_whoosh(0.65, 450, 2400), 0.75)   # Ball soaring into night sky
add_at(sfx, 29.00, make_crowd_swell(6.0, 0.85), 0.8)     # MCG EXPLODES!

# 31.35s - BALL 6: THE FLICK OVER FINE LEG!
add_at(sfx, 31.35, make_bat_crack(0.5, power=1.2), 0.95)  # ICONIC BAT CRACK #2
add_at(sfx, 31.40, make_whoosh(0.55, 500, 2200), 0.7)
add_at(sfx, 32.10, make_stamp_thud(0.45), 0.9)          # "TWO SIXES"
add_at(sfx, 33.60, make_crowd_swell(6.5, 0.95), 0.9)    # DEAFENING ROAR
add_at(sfx, 33.70, make_sub_drop(1.5, 140, 30), 0.8)

# Act 5: Diwali Immortality & King of Kings (36.4s - 44.83s)
# 82* off 53
add_at(sfx, 36.65, make_stamp_thud(0.42), 0.85)
add_at(sfx, 38.10, make_stamp_thud(0.42), 0.85)
# Golden celebratory chords (D Major / A Major majesty)
add_at(sfx, 39.50, make_chord([293.66, 369.99, 440.00, 587.33], dur=3.8), 0.8) # D Major
# Diwali firework celebrations
add_at(sfx, 39.60, make_firework_burst(0.65), 0.75)
add_at(sfx, 40.20, make_firework_burst(0.55), 0.65)
add_at(sfx, 40.85, make_firework_burst(0.70), 0.7)
add_at(sfx, 41.50, make_firework_burst(0.60), 0.6)
# Final immortal chord
add_at(sfx, 42.40, make_chord([220.00, 277.18, 329.63, 440.00], dur=4.5), 0.75)
add_at(sfx, 42.50, make_stamp_thud(0.5), 0.9)  # Final verdict stamp

# Normalize SFX to prevent clipping
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
# Voiceover at 1.0 gain, SFX mixed at 0.78
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
