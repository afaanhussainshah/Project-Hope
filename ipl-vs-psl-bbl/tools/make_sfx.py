import numpy as np
import wave
import subprocess
from pathlib import Path
import imageio_ffmpeg

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\ipl-vs-psl-bbl")
assets = base / "assets"
renders = base / "renders"
renders.mkdir(parents=True, exist_ok=True)

vo_path = assets / "voiceover.wav"
with wave.open(str(vo_path), "rb") as wf:
    sr_rate = wf.getframerate()
    n_frames = wf.getnframes()
    vo_data = np.frombuffer(wf.readframes(n_frames), dtype=np.int16).astype(np.float32) / 32768.0

duration = n_frames / sr_rate
print(f"Loaded voiceover: {duration:.3f}s @ {sr_rate}Hz")

sfx = np.zeros(n_frames, dtype=np.float32)

def add_tone(start_t, dur, f0, f1, vol=0.5, kind="sine"):
    start_i = int(start_t * sr_rate)
    end_i = min(n_frames, start_i + int(dur * sr_rate))
    if start_i >= n_frames:
        return
    length = end_i - start_i
    t = np.linspace(0, dur, length, endpoint=False)
    freq = np.linspace(f0, f1, length)
    phase = 2 * np.pi * np.cumsum(freq) / sr_rate
    if kind == "sine":
        sig = np.sin(phase)
    elif kind == "square":
        sig = np.sign(np.sin(phase))
    elif kind == "noise":
        sig = np.random.uniform(-1, 1, length)
    
    # envelope
    env = np.sin(np.pi * np.linspace(0, 1, length)) ** 0.5
    sfx[start_i:end_i] += sig * env * vol

def add_thud(start_t, vol=0.6):
    add_tone(start_t, 0.22, 120, 35, vol=vol, kind="sine")
    add_tone(start_t, 0.08, 300, 80, vol=vol * 0.7, kind="noise")

def add_swoosh(start_t, dur=0.35, vol=0.4):
    start_i = int(start_t * sr_rate)
    end_i = min(n_frames, start_i + int(dur * sr_rate))
    if start_i >= n_frames:
        return
    length = end_i - start_i
    noise = np.random.uniform(-1, 1, length)
    # Bandpass filter via modulation
    t = np.linspace(0, dur, length, endpoint=False)
    center_freq = np.linspace(600, 2200, length)
    carrier = np.sin(2 * np.pi * center_freq * t)
    env = (np.sin(np.pi * np.linspace(0, 1, length))) ** 2
    sfx[start_i:end_i] += noise * carrier * env * vol

def add_coin(start_t, vol=0.45):
    # bright ringing coin chime
    add_tone(start_t, 0.28, 2637, 2637, vol=vol * 0.6, kind="sine")
    add_tone(start_t + 0.03, 0.25, 3136, 3136, vol=vol * 0.5, kind="sine")
    add_tone(start_t, 0.04, 1800, 400, vol=vol * 0.4, kind="noise")

def add_sub_drop(start_t, dur=1.2, vol=0.7):
    add_tone(start_t, dur, 95, 28, vol=vol, kind="sine")

# Key events & SFX choreography
# Hook:
add_sub_drop(0.05, 1.0, 0.65)
add_swoosh(0.1, 0.3, 0.4)
add_thud(1.0, 0.5)   # IPL card snap
add_thud(1.8, 0.5)   # PSL card snap
add_thud(2.5, 0.5)   # BBL card snap
add_sub_drop(3.18, 1.2, 0.75) # "9 times more"
add_thud(3.4, 0.7)   # 9X stamp slam
add_coin(4.2, 0.5)
add_thud(6.76, 0.55) # "Guess which"

# Scene 2 (PSL):
add_swoosh(7.6, 0.35, 0.45)
add_thud(8.0, 0.5)
add_thud(9.9, 0.6)   # $1.6M purse
add_coin(10.2, 0.45)
add_thud(13.9, 0.6)  # Half a million player
add_coin(14.3, 0.5)

# Scene 3 (BBL):
add_swoosh(16.5, 0.35, 0.45)
add_thud(17.0, 0.55)
add_coin(19.2, 0.4)
add_thud(23.5, 0.5)  # Great cricket stamp
add_thud(24.9, 0.65) # But not huge money stamp

# Scene 4 (IPL & Pant):
add_swoosh(26.3, 0.4, 0.5)
add_sub_drop(26.56, 1.4, 0.8) # "Then comes the IPL"
add_thud(28.6, 0.65) # 120 Crore
add_coin(29.0, 0.6)
add_coin(29.15, 0.5)
add_coin(32.3, 0.55) # $14 Million
add_sub_drop(34.5, 1.2, 0.75)
add_thud(34.8, 0.7)  # Rishabh Pant 27 Crore
add_coin(35.2, 0.65)
add_coin(35.35, 0.55)
add_thud(38.8, 0.65) # Scale tipping
add_coin(39.5, 0.45)

# Scene 5 (Economy & CTA):
add_swoosh(42.6, 0.4, 0.5)
add_sub_drop(42.87, 1.5, 0.85) # "The IPL isn't just a league"
add_thud(44.98, 0.8) # "It's an ECONOMY"
add_sub_drop(45.0, 1.8, 0.8)
add_coin(45.2, 0.6)
add_coin(45.4, 0.5)
add_thud(46.3, 0.6)  # Best league ballot
add_thud(48.2, 0.6)  # Comment below arrow

# Normalize SFX to prevent clipping
max_sfx = np.max(np.abs(sfx))
if max_sfx > 0.85:
    sfx = sfx * (0.85 / max_sfx)

# Mixed audio (Voiceover + SFX + light ambient drone)
t_arr = np.linspace(0, duration, n_frames, endpoint=False)
bed = np.sin(2 * np.pi * 55 * t_arr) * 0.02 # subtle low warm vinyl rumble

full_mix = vo_data * 1.0 + sfx * 0.85 + bed
max_mix = np.max(np.abs(full_mix))
if max_mix > 0.95:
    full_mix = full_mix * (0.95 / max_mix)

# Write output WAV files
sfx_path = assets / "sfx.wav"
mix_path = renders / "full_audio_mix.wav"

def write_wav(path, data):
    int_data = (data * 32767.0).astype(np.int16)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr_rate)
        wf.writeframes(int_data.tobytes())

write_wav(sfx_path, sfx)
write_wav(mix_path, full_mix)
print(f"Generated SFX track: {sfx_path}")
print(f"Generated Full Audio Mix: {mix_path}")
