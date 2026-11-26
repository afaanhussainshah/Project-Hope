import os
import json
import wave
import subprocess
from pathlib import Path
import numpy as np
import speech_recognition as sr
import imageio_ffmpeg

base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-rohit-2027-wc")
assets = base / "assets"
assets.mkdir(parents=True, exist_ok=True)

# Find Elevenlabs mp3
mp3_files = list(base.glob("*.mp3")) + list(assets.glob("*.mp3"))
if not mp3_files:
    raise FileNotFoundError("No mp3 voiceover found in kohli-rohit-2027-wc!")

src_mp3 = mp3_files[0]
dst_mp3 = assets / "voiceover.mp3"
if src_mp3.resolve() != dst_mp3.resolve():
    dst_mp3.write_bytes(src_mp3.read_bytes())
    print(f"Copied {src_mp3.name} -> {dst_mp3.name}")

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
wav_path = assets / "voiceover.wav"

cmd = [
    ffmpeg, "-y",
    "-i", str(dst_mp3),
    "-ar", "44100",
    "-ac", "1",
    "-c:a", "pcm_s16le",
    str(wav_path)
]
subprocess.run(cmd, check=True, capture_output=True)
print(f"Converted to WAV: {wav_path}")

# Load audio
with wave.open(str(wav_path), "rb") as wf:
    sr_rate = wf.getframerate()
    audio_data = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

duration = len(audio_data) / sr_rate
print(f"Total Audio Duration: {duration:.3f} seconds")

# Speech segmentation
r = sr.Recognizer()
frame_len = int(sr_rate * 0.025)
hop_len = int(sr_rate * 0.010)

energy = []
times = []
for i in range(0, len(audio_data) - frame_len, hop_len):
    chunk = audio_data[i:i + frame_len]
    rms = np.sqrt(np.mean(chunk**2))
    energy.append(rms)
    times.append(i / sr_rate)

energy = np.array(energy)
times = np.array(times)

thresh = 0.008
is_speech = energy > thresh
min_silence_frames = int(0.20 / 0.01)

segments = []
in_speech = False
start_t = 0

for i, sp in enumerate(is_speech):
    if sp and not in_speech:
        in_speech = True
        start_t = times[i]
    elif not sp and in_speech:
        if i + min_silence_frames >= len(is_speech) or not np.any(is_speech[i:i + min_silence_frames]):
            in_speech = False
            end_t = times[i]
            if end_t - start_t > 0.15:
                segments.append((start_t, end_t))

if in_speech:
    segments.append((start_t, times[-1]))

print(f"Detected {len(segments)} speech segments. Transcribing...")
results = []
for idx, (s, e) in enumerate(segments):
    with sr.AudioFile(str(wav_path)) as source:
        audio_slice = r.record(source, offset=max(0, s - 0.08), duration=min(duration - max(0, s - 0.08), e - s + 0.16))
        try:
            txt = r.recognize_google(audio_slice)
        except Exception:
            txt = "(unrecognized)"
    print(f"  [{s:5.2f}s - {e:5.2f}s]: {txt}")
    results.append({"index": idx + 1, "start": round(s, 2), "end": round(e, 2), "text": txt})

out_json = assets / "speech_segments.json"
out_json.write_text(json.dumps({"duration": round(duration, 3), "segments": results}, indent=2), encoding="utf-8")
print(f"Saved segments to {out_json}")
