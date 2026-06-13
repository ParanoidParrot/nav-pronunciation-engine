import json
import re
from pathlib import Path

ALIASES_PATH = Path(__file__).resolve().parent / "pronunciation_aliases.json"

with open(ALIASES_PATH, "r", encoding="utf-8") as f:
    PRONUNCIATION_ALIASES = json.load(f)


def apply_pronunciation_hints(text: str) -> str:
    """
    Applies speech-only pronunciation aliases.

    This should be used before TTS generation, not necessarily for display.
    Example:
        hosakere halli -> hosa kere halli
    """
    result = text.lower()

    # Replace longer phrases first so "hosakere halli" wins before "halli"
    aliases = sorted(
        PRONUNCIATION_ALIASES.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    )

    for source, target in aliases:
        pattern = r"\b" + re.escape(source.lower()) + r"\b"
        result = re.sub(pattern, target.lower(), result)

    # Clean extra whitespace
    result = re.sub(r"\s+", " ", result).strip()

    return result