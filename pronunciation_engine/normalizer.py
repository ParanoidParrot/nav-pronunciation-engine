from .abbreviations import ABBREVIATIONS

def normalize_instruction(text: str) -> str:
    words = text.split()
    normalized = []

    for w in words:
        key = w.lower().replace(".", "")
        if key in ABBREVIATIONS:
            normalized.append(ABBREVIATIONS[key])
        else:
            normalized.append(w)

    return " ".join(normalized)