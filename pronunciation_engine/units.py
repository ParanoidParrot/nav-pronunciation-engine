UNIT_MAP = {
    "ft": "feet",
    "ft.": "feet",
    "m": "meters",
    "m.": "meters",
    "km": "kilometers",
    "km.": "kilometers"
}


def expand_unit(token: str):
    token_lower = token.lower()

    if token_lower in UNIT_MAP:
        return UNIT_MAP[token_lower]

    return token