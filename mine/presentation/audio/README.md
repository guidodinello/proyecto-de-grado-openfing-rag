# Audio narration of the thesis

`tesis-audio.mp3` is a full text-to-speech reading of the compiled PDF
(`mine/presentation/pdfs/Proyecto_de_Grado_INCO_InCo_FIng_UdelaR.pdf`), generated for listening
instead of reading. `tesis-audio.srt` has matching subtitles/timestamps.

Regenerate with the steps below if the PDF changes.

## 1. Install edge-tts (free, no API key, Microsoft Edge's TTS voices)

```bash
python3 -m venv /tmp/tts-venv
/tmp/tts-venv/bin/pip install edge-tts
```

## 2. Extract and clean the PDF text

```bash
pdftotext -layout Proyecto_de_Grado_INCO_InCo_FIng_UdelaR.pdf tesis.txt
python3 clean_text.py tesis.txt tesis_clean.txt
```

`clean_text.py` (in this folder) does three things `pdftotext -layout` leaves undone:
- drops lone page-number lines
- rejoins words hyphenated across a line break (`Recupera-\nción` → `Recuperación`)
- collapses wrapped lines back into paragraphs, so edge-tts doesn't pause at every line wrap

Known noise this doesn't strip: roman-numeral page numbers, the índice general / índice de
figuras / bibliografía are read verbatim (page numbers, citation lists). Harmless but skippable.

## 3. Synthesize speech

```bash
/tmp/tts-venv/bin/edge-tts --list-voices | grep '^es-'   # list Spanish voices
/tmp/tts-venv/bin/edge-tts \
  --voice es-UY-MateoNeural \
  --file tesis_clean.txt \
  --write-media tesis-audio-raw.mp3 \
  --write-subtitles tesis-audio.srt
```

`es-UY-MateoNeural` (Uruguayan Spanish, male) was picked for the closest accent match; the
female counterpart is `es-UY-ValentinaNeural`.

## 4. Loudness-normalize

The raw edge-tts output came out quiet (mean ≈ -21 dB, peaks ≈ -2 dB). Boosted it with
`ffmpeg`'s `loudnorm` filter (better than a flat gain — raises quiet parts without clipping the
peaks):

```bash
ffmpeg -i tesis-audio-raw.mp3 -af "loudnorm=I=-14:TP=-1.0:LRA=11" \
  -codec:a libmp3lame -b:a 128k tesis-audio-loud.mp3
```

Result: mean ≈ -15 dB, peaks ≈ -1.2 dB (no clipping).

## 5. Fix playback on some players

The `loudnorm`-filtered file played fine in `ffplay`/`ffprobe` but was silent in at least one
real player. Remuxing with a proper Xing header and ID3v2 tag fixed it:

```bash
ffmpeg -i tesis-audio-loud.mp3 -c copy -write_xing 1 -id3v2_version 3 tesis-audio.mp3
```

Do this remux step even if the loudnorm output "looks" fine in ffprobe — it's what actually
made it play on a real device.

## Notes

- These are large binary files; not committed to git (see repo `.gitignore` — add
  `mine/presentation/audio/*.mp3` there if it isn't already).
- Full re-run takes a few minutes for TTS synthesis plus a couple more for the loudnorm pass, on
  a ~28k-word / ~3h11m document.
