import json
from pathlib import Path

LEXICON_PATH = Path(__file__).resolve().parent / "lexicon.json"

with open(LEXICON_PATH, "r", encoding="utf-8") as f:
    LEXICON = json.load(f)

SUFFIXES = sorted(LEXICON.keys(), key=len, reverse=True)


def detect_suffix(word: str):
    word = word.lower()

    for suffix in SUFFIXES:
        if word.endswith(suffix):
            return suffix

    return None