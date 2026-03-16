HIGHWAY_MAP = {
    "nh": "national highway",
    "sh": "state highway"
}


def expand_highway(token: str):
    token_lower = token.lower()

    if token_lower in HIGHWAY_MAP:
        return HIGHWAY_MAP[token_lower]

    return token