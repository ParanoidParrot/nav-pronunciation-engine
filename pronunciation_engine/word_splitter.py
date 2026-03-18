from pronunciation_engine.suffix_detector import detect_suffix


def split_word(word: str):
    suffix = detect_suffix(word)

    if suffix:
        base = word[:-len(suffix)]

        if base:
            return f"{base} {suffix}"

    return word