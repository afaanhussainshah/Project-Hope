import imageio_ffmpeg
import subprocess
from pathlib import Path

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base = Path(r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-31-for-4")
mp3_src = list(base.glob("ElevenLabs_*.mp3"))[0]
mp3_dst = base / "assets" / "voiceover.mp3"
wav_dst = base / "assets" / "voiceover.wav"

mp3_dst.write_bytes(mp3_src.read_bytes())
print(f"Copied MP3 to {mp3_dst}")

cmd = [
    ffmpeg, "-y",
    "-i", str(mp3_dst),
    "-ar", "44100",
    "-ac", "1",
    "-c:a", "pcm_s16le",
    str(wav_dst)
]
subprocess.run(cmd, check=True)
print(f"Converted to WAV: {wav_dst}")
