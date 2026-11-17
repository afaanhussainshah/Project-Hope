import os
import wave
import numpy as np

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\imran-khan-two-legends"
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
rng = np.random.default_rng(42)


def add_at(buf, t_sec, clip, gain=1.0):
    i0 = int(round(t_sec * SR))
    if i0 >= len(buf) or i0 + len(clip) <= 0:
        return
    src_start = max(0, -i0)
    dst_start = max(0, i0)
    length = min(len(clip) - src_start, len(buf) - dst_start)
    if length > 0:
        buf[dst_start:dst_start + length] += clip[src_start:src_start + length] * gain


def make_whoosh(dur=0.35, f0=220, f1=1400):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    env = np.sin(np.pi * t / dur) ** 1.5
    noise = rng.normal(0, 1, len(t))
    # Simple moving average bandpass feel
    freq = np.linspace(f0, f1, len(t))
    mod = np.sin(2 * np.pi * np.cumsum(freq) / SR)
    return (0.45 * noise * env + 0.25 * mod * env).astype(np.float32)


def make_stamp_thud(dur=0.38):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    freq = 140 * np.exp(-t * 14) + 38
    body = np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-t * 10)
    slap = rng.normal(0, 1, len(t)) * np.exp(-t * 48) * 0.65
    return (body * 0.9 + slap).astype(np.float32)


def make_sub_drop(dur=0.95, f_start=110, f_end=34):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    freq = f_start * (f_end / f_start) ** (t / dur)
    env = np.exp(-t * 3.0) * (1 - np.exp(-t * 80))
    return (np.sin(2 * np.pi * np.cumsum(freq) / SR) * env).astype(np.float32)


def make_wood_shatter(dur=0.45):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    crack = rng.normal(0, 1, len(t)) * np.exp(-t * 35)
    knock1 = np.sin(2 * np.pi * 620 * t) * np.exp(-t * 28)
    knock2 = np.sin(2 * np.pi * 980 * t) * np.exp(-np.maximum(0, t - 0.04) * 25) * (t >= 0.04)
    knock3 = np.sin(2 * np.pi * 1350 * t) * np.exp(-np.maximum(0, t - 0.09) * 22) * (t >= 0.09)
    return (0.5 * crack + 0.4 * knock1 + 0.35 * knock2 + 0.25 * knock3).astype(np.float32)


def make_bat_tap(dur=0.14):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    tone = (np.sin(2 * np.pi * 520 * t) + 0.5 * np.sin(2 * np.pi * 1080 * t)) * np.exp(-t * 42)
    click = rng.normal(0, 0.3, len(t)) * np.exp(-t * 90)
    return (tone * 0.7 + click).astype(np.float32)


def make_ding(freq=880, dur=0.55):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    sig = (
        np.sin(2 * np.pi * freq * t)
        + 0.45 * np.sin(2 * np.pi * freq * 2.0 * t)
        + 0.2 * np.sin(2 * np.pi * freq * 3.0 * t)
    )
    env = np.exp(-t * 6.5) * (1 - np.exp(-t * 220))
    return (sig * env * 0.5).astype(np.float32)


def make_riser(dur=4.5):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    freq = np.linspace(75, 290, len(t))
    env = (t / dur) ** 2.1
    tone = np.sin(2 * np.pi * np.cumsum(freq) / SR) * 0.45
    shimmer = rng.normal(0, 0.15, len(t)) * env
    return ((tone + shimmer) * env).astype(np.float32)


def make_chord(freqs, dur=2.2):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    sig = np.zeros_like(t)
    for f in freqs:
        sig += np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * f * 2 * t)
    sig /= len(freqs)
    env = (1 - np.exp(-t * 14)) * np.exp(-t * 1.4)
    return (sig * env).astype(np.float32)


def make_crowd_swell(dur=3.2):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    noise = rng.normal(0, 1, len(t))
    # Smooth noise for distant stadium roar
    kernel = np.ones(18) / 18.0
    roar = np.convolve(noise, kernel, mode="same")
    env = np.sin(np.pi * t / dur) ** 1.3
    return (roar * env * 0.55).astype(np.float32)


# --- Subtle Warm Ambient Pad Bed ---
t_all = np.linspace(0, DUR, N, endpoint=False)
bed = (
    0.018 * np.sin(2 * np.pi * 65.41 * t_all)   # C2
    + 0.012 * np.sin(2 * np.pi * 98.00 * t_all) # G2
    + 0.008 * np.sin(2 * np.pi * 130.81 * t_all) # C3
)
fade_in = np.minimum(1.0, t_all / 1.5)
fade_out = np.minimum(1.0, (DUR - t_all) / 1.5)
sfx += (bed * fade_in * fade_out).astype(np.float32)

# --- ACT 1: Trick Question Hook (0.0s - 10.10s) ---
add_at(sfx, 0.05, make_whoosh(0.32, 300, 900), 0.28)
add_at(sfx, 5.28, make_stamp_thud(), 0.72)
add_at(sfx, 5.28, make_sub_drop(0.85, 115, 36), 0.50)

# --- Wipe -> ACT 2: Bumrah (10.10s - 19.75s) ---
add_at(sfx, 9.95, make_whoosh(0.36, 200, 1500), 0.45)
add_at(sfx, 11.95, make_whoosh(0.24, 500, 2200), 0.40)  # Yorker swoosh
add_at(sfx, 12.18, make_wood_shatter(), 0.65)           # Stumps shattered!
add_at(sfx, 13.60, make_ding(740, 0.45), 0.35)          # ~20 Stat card pop
add_at(sfx, 17.50, make_stamp_thud(), 0.70)             # SURVIVAL MODE stamp

# --- Wipe -> ACT 3: Steve Smith (19.75s - 30.35s) ---
add_at(sfx, 19.60, make_whoosh(0.36, 1500, 220), 0.45)
add_at(sfx, 21.30, make_bat_tap(), 0.45)                # Smith fidget tap 1
add_at(sfx, 22.10, make_bat_tap(), 0.42)                # Smith fidget tap 2
add_at(sfx, 22.90, make_bat_tap(), 0.45)                # Smith fidget tap 3
add_at(sfx, 24.00, make_ding(880, 0.48), 0.36)          # 55+ Stat card pop
add_at(sfx, 28.55, make_bat_tap(), 0.65)                # Clean willow strike
add_at(sfx, 28.60, make_stamp_thud(), 0.68)             # UNSTOPPABLE stamp

# --- Wipe -> ACT 4: The Fusion (30.35s - 35.60s) ---
add_at(sfx, 30.20, make_whoosh(0.36, 250, 1200), 0.42)
add_at(sfx, 30.65, make_riser(4.95), 0.48)              # Suspense build to reveal
add_at(sfx, 32.45, make_ding(587.33, 0.45), 0.35)       # Bumrah's fire lock
add_at(sfx, 33.85, make_ding(659.25, 0.45), 0.35)       # Batter's backbone lock

# --- Wipe -> ACT 5: IMRAN KHAN REVEAL (35.60s - 46.65s) ---
add_at(sfx, 35.55, make_sub_drop(1.2, 130, 32), 0.65)   # Iconic reveal boom
add_at(sfx, 35.65, make_chord([261.63, 329.63, 392.00, 523.25], 2.5), 0.34)  # Heroic C-major shimmer
add_at(sfx, 37.08, make_ding(880, 0.55), 0.44)          # 362 Test Wickets
add_at(sfx, 40.00, make_ding(1046.5, 0.55), 0.44)       # 3,800+ Test Runs
add_at(sfx, 42.80, make_crowd_swell(3.5), 0.42)         # 1992 World Cup roar
add_at(sfx, 44.50, make_stamp_thud(), 0.72)             # CHAMPION CAPTAIN stamp

# --- Wipe -> ACT 6: Finale (46.65s - 52.61s) ---
add_at(sfx, 46.50, make_whoosh(0.36, 1300, 240), 0.42)
add_at(sfx, 46.92, make_ding(523.25, 0.35), 0.25)       # Bumrah
add_at(sfx, 47.75, make_ding(587.33, 0.35), 0.25)       # Smith
add_at(sfx, 50.65, make_stamp_thud(), 0.78)             # CARRIED BOTH stamp
add_at(sfx, 50.65, make_chord([196.00, 246.94, 293.66, 392.00], 2.0), 0.34)
add_at(sfx, 50.65, make_crowd_swell(1.95), 0.30)

# Normalize SFX gently
sfx_peak = np.max(np.abs(sfx)) + 1e-6
sfx = np.clip(sfx / max(1.0, sfx_peak * 1.15), -0.95, 0.95)

# Mix with voiceover (voiceover clear & dominant at 1.0, SFX bed at 0.36)
mix = vo_raw * 0.96 + sfx * 0.36
mix_peak = np.max(np.abs(mix)) + 1e-6
if mix_peak > 0.96:
    mix = mix * (0.96 / mix_peak)


def save_wav(path, arr):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pcm = np.clip(arr * 32767.0, -32768, 32767).astype(np.int16)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(pcm.tobytes())


save_wav(SFX_WAV, sfx)
save_wav(MIX_WAV, mix)
print(f"Saved SFX: {SFX_WAV}")
print(f"Saved Mix: {MIX_WAV} ({os.path.getsize(MIX_WAV) / 1024:.1f} KB)")
