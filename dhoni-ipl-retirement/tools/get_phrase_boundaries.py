import wave
import numpy as np

wav_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\dhoni-ipl-retirement\assets\voiceover.wav"

with wave.open(wav_path, "rb") as wf:
    sr = wf.getframerate()
    audio = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

# Calculate short-time RMS energy in 20ms windows with 5ms hop
win_len = int(sr * 0.02)
hop_len = int(sr * 0.005)

n_frames = (len(audio) - win_len) // hop_len
times = np.arange(n_frames) * (hop_len / sr)
rms = np.array([np.sqrt(np.mean(audio[i*hop_len : i*hop_len + win_len]**2)) for i in range(n_frames)])

ranges = [
    ("FOR FIVE YEARS STRAIGHT, EVERY COMMENTATOR ASKED...", 0.0, 5.0),
    ("“IS THIS YOUR LAST SEASON IN YELLOW?”", 5.0, 8.5),
    ("AND WITH THAT CALM LITTLE SMILE, HE ALWAYS REPLIED...", 8.5, 10.8),
    ("“DEFINITELY NOT.”", 10.8, 12.5),
    ("...UNTIL TODAY.", 12.5, 14.5),
    ("FIVE TROPHIES.", 14.5, 16.0),
    ("TEN FINALS.", 16.0, 17.5),
    ("THE ONLY CAPTAIN ALIVE...", 17.5, 21.5),
    ("...AND WIN WITH PURE MIND GAMES.", 21.5, 25.8),
    ("BUSTED KNEES.", 25.8, 27.2),
    ("HEAVY STRAPPING.", 27.2, 28.5),
    ("LIMPING BETWEEN THE WICKETS...", 28.5, 30.8),
    ("...YET 40,000 VOICES SCREAMED HIS NAME!", 30.8, 35.5),
    ("THE IPL WILL SURVIVE.", 35.5, 37.8),
    ("CHENNAI WILL FIND A NEW CAPTAIN.", 37.8, 40.5),
    ("...BUT CRICKET WILL NEVER, EVER, SEE ANOTHER THALA.", 40.5, 44.0),
    ("END OF AN ERA.", 44.0, 45.8),
    ("THANK YOU, NUMBER SEVEN. 💛", 45.8, 47.73)
]

print("=== EXACT SPEECH PHRASE BOUNDARIES ===")
for title, r0, r1 in ranges:
    mask = (times >= r0) & (times <= r1)
    r_times = times[mask]
    r_rms = rms[mask]
    
    # threshold for speech in this region
    th = max(0.012, np.max(r_rms) * 0.15)
    speech_indices = np.where(r_rms > th)[0]
    if len(speech_indices) > 0:
        start_t = r_times[speech_indices[0]]
        end_t = r_times[speech_indices[-1]]
    else:
        start_t, end_t = r0, r1
    print(f"{start_t:5.2f}s - {end_t:5.2f}s (dur: {end_t-start_t:4.2f}s): {title}")
