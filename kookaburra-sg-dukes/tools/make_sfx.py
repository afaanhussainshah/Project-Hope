import math
import wave
import struct
import numpy as np
from pathlib import Path

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kookaburra-sg-dukes")
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

def add_paper_whoosh(t_start, dur=0.30, amp=0.14, pan=0.0):
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

def add_paper_pop(t_start, amp=0.20, pan=0.0):
    add_tone(t_start, 0.045, 520, 210, amp, decay="exp", pan=pan)

def add_leather_crack(t_start, amp=0.38, pan=0.0):
    add_tone(t_start, 0.06, 750, 200, amp, decay="exp", pan=pan)
    add_tone(t_start + 0.01, 0.12, 170, 50, amp * 0.75, decay="exp", pan=pan)

def add_tick(t_start, amp=0.20, pan=0.0):
    add_tone(t_start, 0.03, 1100, 700, amp, decay="exp", pan=pan)

def add_chime(t_start, freq=587.33, amp=0.15, pan=0.0): # D5 note
    add_tone(t_start, 0.40, freq, freq * 0.98, amp, decay="exp", pan=pan)
    add_tone(t_start, 0.30, freq * 2, freq * 1.96, amp * 0.35, decay="exp", pan=pan)

# Warm subtle drone bed (vintage classical cricket ambiance: warm acoustic fifths, very soft)
t_arr = np.linspace(0, duration, total_samples)
drone = (
    np.sin(2 * np.pi * 65.41 * t_arr) * 0.018 +    # C2
    np.sin(2 * np.pi * 98.00 * t_arr) * 0.012 +    # G2
    np.sin(2 * np.pi * 130.81 * t_arr) * 0.008      # C3
)
sfx_left += drone
sfx_right += drone

# ----------------- SFX EVENT TIMELINE -----------------
# S1: The Hook (0.00 - 7.50s)
add_thud(0.08, 0.36, -0.1)          # Shock opening
add_paper_pop(0.40, 0.18, -0.2)      # Paper title
add_paper_whoosh(1.10, 0.28, 0.12, 0.1)
add_thud(5.05, 0.38, 0.0)           # "And that changes everything"
add_leather_crack(5.15, 0.32, 0.0)

# S2: The Big Three Balls (7.50 - 14.10s)
add_paper_whoosh(7.50, 0.30, 0.15, -0.2)
add_leather_crack(7.94, 0.38, -0.3) # Kookaburra!
add_thud(8.05, 0.28, -0.3)
add_leather_crack(10.10, 0.38, 0.0) # SG!
add_thud(10.20, 0.28, 0.0)
add_leather_crack(12.17, 0.40, 0.3) # Dukes!
add_thud(12.27, 0.30, 0.3)

# S3: The Rules & Why They Struggle (14.10 - 29.40s)
add_paper_pop(14.30, 0.22, 0.0)     # In Test cricket
add_thud(15.57, 0.35, -0.1)         # Home board picks
add_thud(17.77, 0.40, 0.1)          # Visiting teams struggle!
add_paper_whoosh(19.85, 0.32, 0.15, -0.2)
add_leather_crack(20.00, 0.34, -0.3)# Kookaburra swings early
add_paper_whoosh(22.70, 0.32, 0.15, 0.0)
add_leather_crack(22.86, 0.36, 0.0) # SG grips & reverses
add_paper_whoosh(26.50, 0.32, 0.16, 0.2)
add_leather_crack(26.69, 0.42, 0.3) # Dukes seams longer!
add_thud(27.00, 0.28, 0.3)

# S4: The What If & Single Ball (29.40 - 44.20s)
add_thud(29.57, 0.38, 0.0)          # So what if ONE ball?
add_chime(29.65, 440.0, 0.20, 0.0)
add_paper_pop(32.35, 0.20, -0.1)    # Visiting batters
add_thud(35.37, 0.34, 0.1)          # Home advantage shrinks
add_paper_whoosh(37.20, 0.30, 0.14, 0.0) # Pitches & weather
add_tick(37.34, 0.18, 0.0)
add_paper_pop(40.38, 0.18, 0.0)     # Some fans say
add_thud(41.81, 0.36, 0.0)          # Part of cricket character!

# S5: Verdict & CTA (44.20 - 49.95s)
add_chime(44.42, 523.25, 0.22, -0.2)# One ball everywhere? (C5)
add_thud(44.50, 0.32, -0.2)
add_chime(47.35, 659.25, 0.22, 0.2) # Or keep chaos? (E5)
add_thud(47.45, 0.32, 0.2)
add_leather_crack(49.01, 0.40, 0.0) # Comment below!
add_chime(49.10, 783.99, 0.25, 0.0) # G5 final CTA chord

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
