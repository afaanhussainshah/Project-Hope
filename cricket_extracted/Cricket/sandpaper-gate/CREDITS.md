# Sandpaper Gate reel: credits, sources and re-rendering

## What is in this folder

- `renders/sandpaper-gate-reel.mp4`: the reel, 1080×1920, 30 fps, 41 s, captions burned in, with the voiceover and sound effects.
- `renders/sandpaper-gate-reel-silent.mp4`: the same picture with no audio at all.
- `renders/sandpaper-gate-reel.srt`: the captions as a subtitle file.
- `renders/cover.png`: cover frame.
- `index.html`: the whole video as code (scenes, characters, captions, timing).
- `assets/voiceover.mp3`: the narration supplied for the reel (ElevenLabs).
- `tools/make_sfx.py`: generates `assets/sfx.wav`.

Every cut and caption is placed on the phrase boundaries of `assets/voiceover.mp3` (found by detecting the pauses in the recording). If the voiceover is replaced, the times in `index.html` need to be redone.

## Re-rendering

```bash
npm run render
```

To change when a caption appears, edit its `data-start` and `data-duration` in `index.html`.

## Voiceover script

One piece of sandpaper... shredded a nation's reputation.
Cape Town. 2018.
Cameras caught Cameron Bancroft rubbing the ball with something yellow... then desperately hiding it.
He said it was sticky tape.
It was sandpaper.
David Warner had devised the plan. And captain Steve Smith knew about it... but failed to stop it.
The punishment?
Smith and Warner: twelve months banned.
Bancroft: nine months.
Australia lost the series 3–1.
But the bigger loss... was its reputation.

## Fact sheet (every on-screen claim)

| Claim on screen | Basis |
|---|---|
| 3rd Test, day 3, 24 March 2018, series level 1–1 | 24 March 2018, Newlands, Cape Town; series was 1–1 going into the Test |
| TV cameras caught Bancroft rubbing the ball with a yellow object | Broadcast footage; he was also shown on the stadium big screen |
| He hid it | He was filmed putting the object down the front of his trousers |
| "Sticky tape" | His first explanation at the press conference that evening was yellow adhesive tape |
| It was sandpaper | Admitted after Cricket Australia's investigation |
| Warner's plan; Smith, the captain, let it happen | Cricket Australia's findings: Warner developed the plan; Smith knew and failed to stop it |
| Warner 12 months, Smith 12 months, Bancroft 9 months | Cricket Australia sanctions, 28 March 2018 |
| Series: South Africa 3, Australia 1 | Final series result |

The reel follows Cricket Australia's 2018 findings only. It makes no use of the disputed claims in Usman Khawaja's 2026 autobiography.

Sources:
- https://en.wikipedia.org/wiki/2018_Australian_ball-tampering_scandal
- https://www.cricket.com.au/news/player-sanctions-steve-smith-cameron-bancroft-david-warner-australia-cricket-ball-tampering/2018-03-28

## Assets and licences

- All artwork is original, drawn in code for this reel. The player figures are generic paper cutout characters, not likenesses, and no broadcast footage or photographs are used.
- Font: Anton, SIL Open Font License 1.1 (`assets/fonts/OFL-Anton.txt`).
- Voiceover: supplied by the project owner, generated with ElevenLabs; its licence follows that account's terms.
- Sound effects: synthesised by `tools/make_sfx.py`; no third-party samples or music.
- Built with HyperFrames 0.9.42 (Apache 2.0) and GSAP.
