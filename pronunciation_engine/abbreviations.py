ABBREVIATION_MAP = {
    "rd": "road",
    "rd.": "road",
    "st": "street",
    "st.": "street",
    "ave": "avenue",
    "ave.": "avenue",
    "blvd": "boulevard",
    "blvd.": "boulevard",
    "ln": "lane",
    "ln.": "lane",
    "dr": "drive",
    "dr.": "drive"
}

def expand_abbreviation(token: str):
    token_lower = token.lower()

    if token_lower in ABBREVIATION_MAP:
        return ABBREVIATION_MAP[token_lower]

    return token