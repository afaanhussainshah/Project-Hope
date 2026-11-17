import wave
import numpy as np

wav_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\amir-2017-ct\assets\voiceover.wav"
with wave.open(wav_path, "rb") as wf:
    sr = wf.getframerate()
    audio = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

# 10ms hop
hop = int(sr * 0.01)
win = int(sr * 0.02)
rms = [np.sqrt(np.mean(audio[i:i+win]**2)) for i in range(0, len(audio)-win, hop)]
times = [i / sr for i in range(0, len(audio)-win, hop)]

def find_bursts(t0, t1, thresh=0.035):
    sub_t = [t for t, r in zip(times, rms) if t0 <= t <= t1 and r > thresh]
    if sub_t:
        return min(sub_t), max(sub_t)
    return t0, t1

targets = [
    ("FIVE YEARS BANNED. EXILED. FORGOTTEN.", 0.2, 3.8),
    ("IN 2016, HE RETURNED FROM THE SHADOWS.", 4.0, 7.3),
    ("AND AT THE OVAL... CRICKET'S MOST TERRIFYING TRIO.", 7.4, 11.4),
    ("OVER ONE: LATE INSWING. ROHIT SHARMA FOR A DUCK!", 11.4, 15.6),
    ("OVER THREE: KOHLI DROPPED AT SLIP!", 15.6, 18.0),
    ("NEXT BALL... LEADING EDGE! CAUGHT! KOHLI GONE!", 18.0, 22.3),
    ("THEN DHAWAN SLICED BEHIND.", 22.3, 24.8),
    ("THREE WICKETS. SIXTEEN RUNS. DEMOLISHED.", 24.8, 29.2),
    ("FROM OUTCAST... TO IMMORTAL REDEMPTION.", 29.2, 31.8),
    ("MOHAMMAD AMIR CONQUERED THE WORLD.", 31.8, 34.3)
]

for label, s, e in targets:
    actual_s, actual_e = find_bursts(s, e)
    print(f"{actual_s:.2f}s - {actual_e:.2f}s (dur: {actual_e - actual_s:.2f}s): {label}")
