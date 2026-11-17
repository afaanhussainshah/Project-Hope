import wave
import numpy as np

wav_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\amir-2017-ct\assets\voiceover.wav"
with wave.open(wav_path, "rb") as wf:
    sr = wf.getframerate()
    n_frames = wf.getnframes()
    raw = wf.readframes(n_frames)
    audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

duration = len(audio) / sr
print(f"Total duration: {duration:.3f}s")

# Compute RMS energy over 25ms windows
frame_len = int(sr * 0.025)
hop_len = int(sr * 0.010)

energy = []
times = []
for i in range(0, len(audio) - frame_len, hop_len):
    chunk = audio[i:i + frame_len]
    rms = np.sqrt(np.mean(chunk**2))
    energy.append(rms)
    times.append(i / sr)

energy = np.array(energy)
times = np.array(times)

# Threshold for speech
thresh = 0.02
is_speech = energy > thresh

# Find continuous segments of speech (min silence 0.3s)
min_silence_frames = int(0.3 / 0.01)
segments = []
in_speech = False
start_t = 0

for i, sp in enumerate(is_speech):
    if sp and not in_speech:
        in_speech = True
        start_t = times[i]
    elif not sp and in_speech:
        # Check if silence persists
        if i + min_silence_frames >= len(is_speech) or not np.any(is_speech[i:i + min_silence_frames]):
            in_speech = False
            end_t = times[i]
            if end_t - start_t > 0.3:
                segments.append((start_t, end_t))

if in_speech:
    segments.append((start_t, times[-1]))

print(f"\nDetected {len(segments)} distinct speech segments:")
for idx, (s, e) in enumerate(segments):
    print(f"  Segment {idx+1}: {s:.2f}s -> {e:.2f}s  (dur: {e-s:.2f}s)")
