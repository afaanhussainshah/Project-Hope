import math
import wave
import struct
import numpy as np
from pathlib import Path

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\follow-on-gamble")
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
    add_tone(t_start, 0.16, 110, 35, amp, decay="exp", pan=pan)
    add_tone(t_start, 0.22, 55, 28, amp * 0.7, decay="exp", pan=pan)

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

def add_trap_snap(t_start, amp=0.42):
    add_tone(t_start, 0.08, 400, 80, amp, decay="exp", pan=0.0)
    add_tone(t_start + 0.012, 0.15, 95, 30, amp * 0.8, decay="exp", pan=0.0)

# Sound design timeline
# S1: Hook
add_thud(0.08, 0.34, -0.2)
add_paper_pop(0.40, 0.16, 0.2)
add_paper_whoosh(3.80, 0.32, 0.14, 0.1)
add_thud(4.15, 0.36, -0.1) # Streak rip

# S2: Wipe into The Rule
add_paper_whoosh(7.28, 0.36, 0.18, 0.2)
add_paper_pop(7.70, 0.16, -0.2)
add_thud(8.65, 0.30, 0.0)
add_paper_pop(12.05, 0.16, 0.2)
add_thud(14.28, 0.32, -0.1)

# S3: Wipe into The Gamble
add_paper_whoosh(16.35, 0.36, 0.18, -0.2)
add_thud(16.65, 0.35, 0.0)
add_paper_whoosh(18.15, 0.30, 0.12, 0.2)
add_thud(19.75, 0.32, -0.2)
add_thud(22.65, 0.40, 0.0) # 4 wins only stamp

# S4: Wipe into Kolkata 2001
add_paper_whoosh(26.35, 0.36, 0.20, 0.2)
add_thud(26.75, 0.35, -0.1)
add_paper_pop(28.70, 0.18, 0.2)
add_thud(31.68, 0.35, -0.2) # 274 behind
add_paper_pop(35.05, 0.18, 0.1)
add_paper_whoosh(37.28, 0.32, 0.12, 0.0)
add_thud(40.75, 0.44, 0.0) # India Won triumph thud

# S5: Wipe into Weapon vs Trap
add_paper_whoosh(41.85, 0.36, 0.18, -0.2)
add_thud(42.22, 0.35, -0.25) # Weapon
add_trap_snap(44.20, 0.48)   # Trap snap!
add_paper_pop(46.40, 0.18, 0.1)

# Warm ambient harmonic sub-drone (filtered low freqs, 0 hiss)
t_arr = np.linspace(0, duration, total_samples)
sub_drone = (np.sin(2 * np.pi * 55.0 * t_arr) * 0.032 +
             np.sin(2 * np.pi * 82.5 * t_arr) * 0.018 +
             np.sin(2 * np.pi * 110.0 * t_arr) * 0.014)
drone_env = np.minimum(t_arr / 1.0, 1.0) * np.minimum((duration - t_arr) / 1.5, 1.0)
sub_drone *= np.maximum(0, drone_env)

sfx_left += sub_drone
sfx_right += sub_drone

mix_left = vo_audio * 1.0 + sfx_left * 0.85
mix_right = vo_audio * 1.0 + sfx_right * 0.85

peak = max(np.max(np.abs(mix_left)), np.max(np.abs(mix_right)))
if peak > 0.96:
    scale = 0.96 / peak
    mix_left *= scale
    mix_right *= scale
    print(f"Applied soft scaling: {scale:.3f}")

out_wav = renders / "full_audio_mix.wav"
mix_stereo = np.column_stack((mix_left, mix_right))
int_data = (mix_stereo * 32767.0).astype(np.int16)

with wave.open(str(out_wav), "wb") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(int_data.tobytes())

print(f"Wrote master mix: {out_wav} ({len(int_data) / sample_rate:.3f}s)")
