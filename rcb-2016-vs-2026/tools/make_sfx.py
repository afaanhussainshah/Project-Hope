import math
import wave
import struct
import numpy as np
from pathlib import Path

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\rcb-2016-vs-2026")
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

def add_thud(t_start, amp=0.35, pan=0.0):
    add_tone(t_start, 0.16, 120, 35, amp, decay="exp", pan=pan)
    add_tone(t_start, 0.22, 58, 28, amp * 0.7, decay="exp", pan=pan)

def add_paper_whoosh(t_start, dur=0.30, amp=0.12, pan=0.0):
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

def add_paper_pop(t_start, amp=0.18, pan=0.0):
    add_tone(t_start, 0.045, 520, 210, amp, decay="exp", pan=pan)

def add_bat_crack(t_start, amp=0.40):
    add_tone(t_start, 0.06, 680, 180, amp, decay="exp", pan=-0.1)
    add_tone(t_start + 0.01, 0.14, 160, 45, amp * 0.8, decay="exp", pan=0.1)

def add_stump_clatter(t_start, amp=0.35):
    add_tone(t_start, 0.05, 750, 250, amp, decay="exp", pan=0.2)
    add_tone(t_start + 0.02, 0.08, 480, 150, amp * 0.7, decay="exp", pan=-0.2)
    add_thud(t_start + 0.04, amp * 0.6)

# S1: Hook (0.00 - 6.00s)
add_thud(0.08, 0.38, -0.1)
add_paper_pop(0.40, 0.18, 0.2)
add_thud(3.90, 0.32, 0.0) # One Match
add_paper_whoosh(5.00, 0.28, 0.14, -0.2)
add_thud(5.05, 0.35, 0.2) # Who Wins?

# S2: Round 1 Batting (6.00 - 16.20s)
add_paper_whoosh(5.95, 0.32, 0.16, 0.2) # Wipe
add_thud(6.15, 0.36, -0.2) # Round 1
add_bat_crack(7.85, 0.42) # Gayle/AB/Kohli peak
add_bat_crack(9.20, 0.35)
add_thud(11.00, 0.32, 0.0) # Chinnaswamy 220
add_paper_pop(14.30, 0.22, 0.2) # Advantage 2016
add_thud(14.35, 0.38, 0.1)

# S3: Round 2 Bowling (16.20 - 28.60s)
add_paper_whoosh(16.10, 0.32, 0.16, -0.2) # Wipe
add_thud(16.35, 0.36, -0.2) # Round 2 Bowling
add_paper_pop(18.25, 0.18, 0.1)
add_stump_clatter(20.20, 0.38) # Bhuvi/Hazlewood
add_stump_clatter(24.90, 0.42) # Wickets fall!
add_thud(26.65, 0.38, 0.1) # Advantage 2026

# S4: Round 3 The Chase (28.60 - 38.80s)
add_paper_whoosh(28.50, 0.32, 0.16, 0.2) # Wipe
add_thud(28.75, 0.36, -0.2) # Round 3 Chase
add_bat_crack(32.75, 0.44) # Tim David 188 SR
add_thud(36.30, 0.38, 0.0) # Chases anything

# S5: Verdict & CTA (38.80 - 47.07s)
add_paper_whoosh(38.70, 0.34, 0.16, -0.2) # Wipe
add_thud(38.90, 0.36, 0.1) # My Pick: 2026
add_paper_pop(41.30, 0.20, -0.2)
add_thud(45.25, 0.40, 0.0) # Who wins? Comment!

# Gentle warm sub-drone (zero noise)
drone_t = np.linspace(0, duration, total_samples)
drone = (np.sin(2 * np.pi * 55.0 * drone_t) * 0.025 + np.sin(2 * np.pi * 82.5 * drone_t) * 0.015)
sfx_left += drone
sfx_right += drone

# Mix with voiceover
vo_level = 0.95
sfx_level = 0.85
mix_l = vo_audio * vo_level + sfx_left * sfx_level
mix_r = vo_audio * vo_level + sfx_right * sfx_level

max_val = max(np.max(np.abs(mix_l)), np.max(np.abs(mix_r)))
if max_val > 0.96:
    gain = 0.96 / max_val
    mix_l *= gain
    mix_r *= gain

out_wav = renders / "full_audio_mix.wav"
with wave.open(str(out_wav), "wb") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    interleaved = np.empty((total_samples * 2,), dtype=np.int16)
    interleaved[0::2] = np.clip(mix_l * 32767.0, -32768, 32767).astype(np.int16)
    interleaved[1::2] = np.clip(mix_r * 32767.0, -32768, 32767).astype(np.int16)
    wf.writeframes(interleaved.tobytes())

print(f"Generated clean stereo mix: {out_wav} ({duration:.3f}s)")
