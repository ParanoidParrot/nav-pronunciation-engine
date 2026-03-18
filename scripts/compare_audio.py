import json
import os
import re
from pathlib import Path

from pronunciation_engine.normalizer import normalize
from pronunciation_engine.tts_engine import text_to_speech_file

TEST_SENTENCES = [
    "Turn left onto NH 44 after 500m",
    "Turn left at Hosakerehalli",
    "Continue to Rajajinagar",
    "Go to Anantapuram",
    "Head towards Bidarwadi",
]

BASE_DIR = Path(__file__).resolve().parent / "audio_outputs"
RAW_DIR = BASE_DIR / "raw"
NORMALIZED_DIR = BASE_DIR / "normalized"
METADATA_DIR = BASE_DIR / "metadata"

RAW_DIR.mkdir(parents=True, exist_ok=True)
NORMALIZED_DIR.mkdir(parents=True, exist_ok=True)
METADATA_DIR.mkdir(parents=True, exist_ok=True)


def slugify(text: str, max_len: int = 50) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text[:max_len] if text else "sample"


def main():
    all_metadata = []

    for i, original_text in enumerate(TEST_SENTENCES, start=1):
        normalized_text = normalize(original_text)

        slug = slugify(original_text)
        raw_file = RAW_DIR / f"{i:02d}_{slug}_raw.wav"
        normalized_file = NORMALIZED_DIR / f"{i:02d}_{slug}_normalized.wav"
        metadata_file = METADATA_DIR / f"{i:02d}_{slug}.json"

        text_to_speech_file(
            text=original_text,
            filename=str(raw_file),
            target_language_code="en-IN",
            speaker="anushka",
            use_cache=True,
        )

        text_to_speech_file(
            text=normalized_text,
            filename=str(normalized_file),
            target_language_code="en-IN",
            speaker="anushka",
            use_cache=True,
        )

        metadata = {
            "id": i,
            "original_text": original_text,
            "normalized_text": normalized_text,
            "raw_audio_file": str(raw_file),
            "normalized_audio_file": str(normalized_file),
            "language": "en-IN",
            "speaker": "anushka",
        }

        metadata_file.write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        all_metadata.append(metadata)

        print(f"\nSample {i}")
        print(f"Original:   {original_text}")
        print(f"Normalized: {normalized_text}")
        print(f"Raw audio:  {raw_file}")
        print(f"Norm audio: {normalized_file}")

    summary_file = METADATA_DIR / "summary.json"
    summary_file.write_text(
        json.dumps(all_metadata, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nSaved summary metadata to {summary_file}")


if __name__ == "__main__":
    main()