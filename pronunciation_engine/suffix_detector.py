import json

with open("pronunciation_engine/lexicon.json", "r", encoding="utf-8") as f:
    LEXICON = json.load(f)

SUFFIXES = list(LEXICON.keys())


def detect_suffix(word: str):
    word = word.lower()

    for suffix in sorted(SUFFIXES, key=len, reverse=True):
        if word.endswith(suffix):
            return suffix

    return None