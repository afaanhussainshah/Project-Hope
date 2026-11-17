import speech_recognition as sr
import wave

r = sr.Recognizer()
wav_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\amir-2017-ct\assets\voiceover.wav"

# We know the segments from analyze_speech:
# Segment 1: 0.32s -> 1.55s
# Segment 2: 3.30s -> 3.68s
# Segment 3: 4.30s -> 7.28s
# Segment 4: 7.61s -> 11.19s
# Segment 5: 11.55s -> 15.41s
# Segment 6: 15.72s -> 17.73s
# Segment 7: 18.13s -> 21.92s
# Segment 8: 22.35s -> 29.09s
# Segment 9: 29.44s -> 34.12s

# Let's inspect by slicing with wave and transcribing each window:
slices = [
    (0.0, 4.0),
    (4.0, 7.5),
    (7.5, 11.5),
    (11.5, 15.5),
    (15.5, 18.0),
    (18.0, 22.2),
    (22.2, 29.2),
    (29.2, 34.43)
]

for idx, (s, e) in enumerate(slices):
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source, offset=s, duration=e-s)
        try:
            txt = r.recognize_google(audio)
            print(f"[{s:.2f}s - {e:.2f}s]: {txt}")
        except Exception:
            print(f"[{s:.2f}s - {e:.2f}s]: (unrecognized or silence)")
