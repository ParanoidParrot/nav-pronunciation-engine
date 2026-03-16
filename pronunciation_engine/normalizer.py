from .abbreviations import ABBREVIATIONS
from .numbers import normalize_numbers
from .acronyms import ACRONYM_MAP


def normalize_instruction(text: str):

    tokens = text.split()
    normalized = []

    for token in tokens:
        clean = token.lower().replace(".", "")

        if clean in ABBREVIATIONS:
            normalized.append(ABBREVIATIONS[clean])
            continue

        if clean in ACRONYM_MAP:
            normalized.append(ACRONYM_MAP[clean])
            continue

        token = normalize_numbers(clean)

        normalized.append(token)

    return " ".join(normalized)