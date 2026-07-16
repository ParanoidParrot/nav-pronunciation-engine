import json
import re
from pathlib import Path

from pronunciation_engine.acronym_speller import spell_acronyms_for_tts

ALIASES_PATH = Path(__file__).resolve().parent / "pronunciation_aliases.json"

with open(ALIASES_PATH, "r", encoding="utf-8") as f:
    PRONUNCIATION_ALIASES = json.load(f)


def apply_pronunciation_hints(text: str) -> str:
    """
    Applies speech-only pronunciation aliases.

    This should be used before TTS generation, not necessarily for display.

    Examples:
        hosakere halli -> hosa kere halli
        MG Marg -> M G Marg
    """
    result = text.strip()

    # Replace longer phrases first so phrase-level aliases win before word-level aliases.
    aliases = sorted(
        PRONUNCIATION_ALIASES.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    )

    for source, target in aliases:
        pattern = r"\b" + re.escape(source) + r"\b"
        result = re.sub(
            pattern,
            target,
            result,
            flags=re.IGNORECASE,
        )

    result = spell_acronyms_for_tts(result)
    result = re.sub(r"\s+", " ", result).strip()

    return result