import json
from pathlib import Path

import pytest

from pronunciation_engine.tts_engine import text_to_speech_file

FIXTURE_PATH = Path("tests/fixtures/multilingual_cases.json")
OUTPUT_DIR = Path("tests/tmp_tts_outputs")


def load_cases():
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

@pytest.mark.tts
@pytest.mark.parametrize("case", load_cases())
def test_tts_smoke_multilingual(case):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    lang = case["lang"]
    text = case["text"]
    filename = OUTPUT_DIR / f"{lang}.wav"

    result = text_to_speech_file(
        text=text,
        filename=str(filename),
        target_language_code=lang,
        speaker="anushka",
        use_cache=True,
    )

    assert result == str(filename)
    assert filename.exists()
    assert filename.stat().st_size > 0