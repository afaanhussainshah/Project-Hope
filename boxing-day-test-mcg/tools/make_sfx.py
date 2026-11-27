import math
import wave
import struct
import numpy as np
from pathlib import Path

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\boxing-day-test-mcg")
assets = base / "assets"
renders = base / "renders"
renders.mkdir(parents=True, exist_ok=True)

vo_path = assets / "voiceover.wav"
if not vo_path.exists():
    raise FileNotFoundError("voiceover.wav not found!")

with wave.open(str(vo_path), "rb") as wf:
    sample_rate = wf.getframerate()
    n_channels = wf.getnchannels()
    n_frames = wf.getnframes()
    raw = wf.readframes(n_frames)

if n_channels == 1:
    vo_audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
else:
    vo_audio = np.frombuffer(raw, dtype=np.int16).reshape(-1, n_channels)[:, 0].astype(np.float32) / 32768.0

duration = len(vo_audio) / sample_rate
total_samples = int(duration * sample_rate)
print(f"Loaded voiceover: {duration:.3f}s ({total_samples} samples @ {sample_rate}Hz)")

# Master SFX buffer (stereo)
sfx_left = np.zeros(total_samples, dtype=np.float32)
sfx_right = np.zeros(total_samples, dtype=np.float32)

def add_tone(t_start, dur, freq_start, freq_end, amp, decay="exp", pan=0.0):
    start_idx = int(t_start * sample_rate)
    n = int(dur * sample_rate)
    if start_idx >= total_samples or n <= 0:
        return
    end_idx = min(start_idx + n, total_samples)
    actual_n = end_idx - start_idx
    t = np.linspace(0, dur, n)[:actual_n]
    phase = 2 * np.pi * (freq_start * t + 0.5 * (freq_end - freq_start) * (t**2 / dur))
    wave_data = np.sin(phase)
    if decay == "exp":
        env = np.exp(-4.5 * (t / dur))
    elif decay == "linear":
        env = 1.0 - (t / dur)
    elif decay == "bell":
        env = np.sin(np.pi * (t / dur))
    else:
        env = np.ones_like(t)
    sig = wave_data * env * amp
    l_gain = np.sqrt(0.5 * (1.0 - pan))
    r_gain = np.sqrt(0.5 * (1.0 + pan))
    sfx_left[start_idx:end_idx] += sig * l_gain
    sfx_right[start_idx:end_idx] += sig * r_gain

def add_thud(t_start, amp=0.36, pan=0.0):
    add_tone(t_start, 0.16, 120, 35, amp, decay="exp", pan=pan)
    add_tone(t_start, 0.22, 58, 28, amp * 0.7, decay="exp", pan=pan)

def add_crowd_surge(t_start, dur=2.5, amp=0.25):
    start_idx = int(t_start * sample_rate)
    n = int(dur * sample_rate)
    if start_idx >= total_samples or n <= 0:
        return
    end_idx = min(start_idx + n, total_samples)
    actual_n = end_idx - start_idx
    t = np.linspace(0, dur, n)[:actual_n]
    env = np.sin(np.pi * (t / dur)) ** 1.5
    # Synthesize roaring frequencies (pink noise simulation via layered sine octaves)
    freqs = [90, 140, 220, 310, 440, 580, 720, 890, 1100]
    roar = np.zeros_like(t)
    for f in freqs:
        roar += np.sin(2 * np.pi * f * t + np.random.uniform(0, 2*np.pi)) * (1.0 / np.sqrt(f))
    roar = (roar / len(freqs)) * env * amp
    sfx_left[start_idx:end_idx] += roar * 0.9
    sfx_right[start_idx:end_idx] += roar * 1.1

def add_bat_crack(t_start, amp=0.45):
    add_tone(t_start, 0.05, 820, 240, amp, decay="exp", pan=0.1)
    add_tone(t_start + 0.01, 0.12, 190, 50, amp * 0.8, decay="exp", pan=-0.1)

def add_wickets_rattle(t_start, amp=0.40):
    add_tone(t_start, 0.04, 1400, 600, amp, decay="exp", pan=-0.2)
    add_tone(t_start + 0.02, 0.08, 900, 300, amp * 0.7, decay="exp", pan=0.2)

def add_whoosh(t_start, dur=0.28, amp=0.15, pan=0.0):
    start_idx = int(t_start * sample_rate)
    n = int(dur * sample_rate)
    if start_idx >= total_samples or n <= 0:
        return
    end_idx = min(start_idx + n, total_samples)
    actual_n = end_idx - start_idx
    t = np.linspace(0, dur, n)[:actual_n]
    env = np.sin(np.pi * (t / dur)) ** 2
    flutter = np.sin(2 * np.pi * 180 * t) * 0.5 + np.sin(2 * np.pi * 260 * t) * 0.3 + np.sin(2 * np.pi * 380 * t) * 0.2
    sig = flutter * env * amp
    l_gain = np.sqrt(0.5 * (1.0 - pan))
    r_gain = np.sqrt(0.5 * (1.0 + pan))
    sfx_left[start_idx:end_idx] += sig * l_gain
    sfx_right[start_idx:end_idx] += sig * r_gain

def add_chime(t_start, freq=587.33, amp=0.18, pan=0.0):
    add_tone(t_start, 0.40, freq, freq * 0.98, amp, decay="exp", pan=pan)
    add_tone(t_start, 0.30, freq * 2, freq * 1.96, amp * 0.35, decay="exp", pan=pan)

# Continuous Stadium Murmur (Very gentle subtle hum across entire 52s)
t_arr = np.linspace(0, duration, total_samples)
murmur = (
    np.sin(2 * np.pi * 65.41 * t_arr) * 0.015 +
    np.sin(2 * np.pi * 110.00 * t_arr) * 0.010 +
    np.sin(2 * np.pi * 164.81 * t_arr) * 0.008
)
sfx_left += murmur
sfx_right += murmur

# ----------------- TIMED SFX EVENTS -----------------
# 1. Opening Hook: 19 YEARS OLD & The Ramp Shot (0.00 - 6.69s)
add_thud(0.04, 0.38, 0.0)             # Big opening hit on 19 YEARS OLD
add_whoosh(3.30, 0.30, 0.18, -0.3)     # Bumrah running in whoosh
add_bat_crack(4.85, 0.48)             # AUDACIOUS RAMP CRACK!
add_crowd_surge(5.00, 2.5, 0.28)      # Crowd shock roar

# 2. 90,000 MCG Crowd Goes Wild (6.69 - 14.65s)
add_crowd_surge(6.70, 4.5, 0.42)      # MASSIVE 90,000 MCG ROAR
add_thud(11.11, 0.38, 0.0)            # "On Boxing Day" impact
add_chime(12.43, 440.0, 0.22, 0.0)    # "So what is Boxing Day cricket?" (Slows down for explainer)

# 3. MCG Tradition & History (15.17 - 28.95s)
add_whoosh(15.10, 0.35, 0.15, -0.2)
add_thud(15.20, 0.32, 0.1)            # 26th of December
add_whoosh(20.80, 0.30, 0.14, 0.2)    # Families skip leftovers
add_thud(24.53, 0.34, 0.0)            # Biggest days in world cricket
add_chime(27.23, 523.25, 0.25, 0.0)   # "It creates legends"

# 4. The Legends: Warne Hat-trick & Rahane 100 (29.00 - 45.03s)
add_whoosh(29.25, 0.28, 0.16, -0.2)
add_wickets_rattle(30.80, 0.45)       # SHANE WARNE HAT-TRICK TIMBER!
add_crowd_surge(31.00, 2.8, 0.35)
add_bat_crack(33.50, 0.40)            # RAHANE CENTURY SHOT
add_chime(34.00, 659.25, 0.22, 0.2)
add_whoosh(37.50, 0.30, 0.14, 0.0)    # So why Boxing Day?
add_thud(39.86, 0.30, -0.1)           # Public holiday

# 5. Grand Climax: TEST CRICKET & CTA (45.00 - 52.61s)
add_chime(45.40, 587.33, 0.20, -0.1)  # Christmas is for family
add_thud(47.30, 0.45, 0.0)            # BOXING DAY IS FOR TEST CRICKET!
add_crowd_surge(47.40, 3.5, 0.40)
add_chime(49.82, 523.25, 0.22, 0.0)   # Best moment?
add_thud(51.70, 0.38, 0.0)            # Comment below!

# Stereo mixdown
vo_gain = 1.05
sfx_gain = 0.85
master_left = vo_audio * vo_gain + sfx_left * sfx_gain
master_right = vo_audio * vo_gain + sfx_right * sfx_gain

# Soft peak limiter
max_peak = max(np.max(np.abs(master_left)), np.max(np.abs(master_right)))
if max_peak > 0.96:
    scale_fac = 0.96 / max_peak
    master_left *= scale_fac
    master_right *= scale_fac
    print(f"Limited master peaks by factor {scale_fac:.3f}")

master_stereo = np.column_stack((master_left, master_right))
out_wav = renders / "full_audio_mix.wav"

int16_audio = (master_stereo * 32767.0).clip(-32768, 32767).astype(np.int16)
with wave.open(str(out_wav), "wb") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(int16_audio.tobytes())

print(f"Master audio mix generated successfully: {out_wav} ({duration:.2f}s, 44100Hz stereo)")
