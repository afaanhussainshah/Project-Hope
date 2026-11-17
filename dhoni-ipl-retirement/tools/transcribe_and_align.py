import speech_recognition as sr
import wave
import numpy as np

wav_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\dhoni-ipl-retirement\assets\voiceover.wav"

r = sr.Recognizer()

# Analyze speech intervals using energy
with wave.open(wav_path, "rb") as wf:
    sr_rate = wf.getframerate()
    audio_data = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

duration = len(audio_data) / sr_rate
print(f"Total duration: {duration:.3f}s")

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

thresh = 0.015
is_speech = energy > thresh

min_silence_frames = int(0.25 / 0.01)
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
            if end_t - start_t > 0.2:
                segments.append((start_t, end_t))

if in_speech:
    segments.append((start_t, times[-1]))

print(f"\nDetected {len(segments)} speech segments:")
for idx, (s, e) in enumerate(segments):
    with sr.AudioFile(wav_path) as source:
        audio_slice = r.record(source, offset=max(0, s-0.08), duration=min(duration-s, e-s+0.16))
        try:
            txt = r.recognize_google(audio_slice)
        except Exception:
            txt = "(unrecognized)"
    print(f"  [{s:.2f}s - {e:.2f}s] (dur: {e-s:.2f}s): {txt}")
