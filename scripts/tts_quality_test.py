from pathlib import Path

from pronunciation_engine.pronunciation_hints import apply_pronunciation_hints
from pronunciation_engine.tts_engine import text_to_speech_file

SAMPLES = [
    "Continue to MG Marg",
    "Turn left onto NH 44 after 500m near Hosakerehalli",
    "Continue to Rajajinagar",
    "Take the next right near Basavanagudi",
    "Head towards Marathahalli bridge",
    "Continue to Ranganathan Theru",
    "Continue to Ameerpet Veedhi",
    "Continue to Shivaji Peth",
    "Continue to Rashbehari Sarani",
    "Continue to Mandvi ni Pol",
]

SPEAKERS = [
    "simran"
]

OUT_DIR = Path("scripts/audio_outputs/quality_tests")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def slugify(value: str) -> str:
    return (
        value.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace(".", "")
        .replace(",", "")
    )[:60]


def main() -> None:
    for speaker in SPEAKERS:
        for i, original in enumerate(SAMPLES, start=1):
            speech_text = apply_pronunciation_hints(original)

            output_file = OUT_DIR / f"{i:02d}_{speaker}_{slugify(original)}.wav"

            print("\nSample:", i)
            print("Speaker:", speaker)
            print("Original:", original)
            print("Speech:", speech_text)
            print("Output:", output_file)

            try:
                text_to_speech_file(
                    text=speech_text,
                    filename=str(output_file),
                    target_language_code="en-IN",
                    speaker=speaker,
                    use_cache=False,
                    pace=0.9,
                    temperature=0.2,
                )
            except Exception as exc:
                print("FAILED:", exc)


if __name__ == "__main__":
    main()