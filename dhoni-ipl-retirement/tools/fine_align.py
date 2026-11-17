import speech_recognition as sr
import wave
import numpy as np

wav_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\dhoni-ipl-retirement\assets\voiceover.wav"
r = sr.Recognizer()

with wave.open(wav_path, "rb") as wf:
    sr_rate = wf.getframerate()
    audio_data = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

duration = len(audio_data) / sr_rate

# Let's inspect sub-windows across the 47.7s to pinpoint exact phrase boundaries
slices = [
    (0.0, 5.0, "For five years straight..."),
    (5.0, 8.5, "Is this your last season in yellow?"),
    (8.5, 10.8, "And with that calm little smile, he always replied..."),
    (10.8, 12.5, "Definitely NOT."),
    (12.5, 14.5, "...Until today."),
    (14.5, 16.2, "Five trophies."),
    (16.0, 17.8, "Ten finals."),
    (17.5, 22.0, "The only captain alive who could take a game into the twentieth over..."),
    (21.5, 26.0, "...look a bowler dead in the eye, and win with pure mind games."),
    (25.8, 27.2, "Busted knees."),
    (27.0, 28.5, "Heavy strapping."),
    (28.3, 30.8, "Limping between the wickets..."),
    (30.8, 35.8, "...and yet, forty thousand people screamed his name until their voices bled."),
    (35.5, 37.8, "The IPL will survive."),
    (37.5, 40.5, "Chennai will find a new captain."),
    (40.2, 44.2, "...But cricket will never, EVER, see another Thala."),
    (44.0, 46.0, "End of an era."),
    (45.8, 47.73, "Thankyou, Number Seven.")
]

for s, e, target in slices:
    with sr.AudioFile(wav_path) as source:
        audio_slice = r.record(source, offset=s, duration=e-s)
        try:
            txt = r.recognize_google(audio_slice)
        except Exception as ex:
            txt = f"ERR: {ex}"
    print(f"[{s:4.1f}s - {e:4.1f}s] Target: {target}")
    print(f"               Heard:  {txt}\n")
