import re


KNOWN_ACRONYMS = {
    # Road / navigation acronyms
    "MG",
    "NH",
    "SH",
    "ORR",
    "IRR",
    "NHAI",

    # Common Bengaluru / Indian area acronyms
    "BTM",
    "JP",
    "KR",
    "HSR",
    "CBD",
    "JPN",
    "RT",
    "CV",
    "RMV",

    # Common institutional acronyms that may appear in roads/areas
    "IISc",
    "IISC",
    "IIT",
    "IIM",
    "AIIMS",
    "HAL",
    "BEL",
    "BHEL",
    "ISRO",
    "DRDO",

    # Transport acronyms
    "BMTC",
    "KSRTC",
    "MMTS",
    "MRTS",
    "NMMT",
    "BEST",
}


def _split_trailing_punctuation(token: str) -> tuple[str, str]:
    """
    Splits token into alphanumeric core and trailing punctuation.

    Examples:
        "MG" -> ("MG", "")
        "MG," -> ("MG", ",")
        "NH-44" remains untouched by this function and should be handled elsewhere.
    """
    match = re.match(r"^([A-Za-z]+)([^A-Za-z]*)$", token)

    if not match:
        return token, ""

    return match.group(1), match.group(2)


def spell_acronyms_for_tts(text: str) -> str:
    """
    Turns known acronyms into spaced letters so TTS does not read them as words.

    Examples:
        MG Marg -> M G Marg
        JP Nagar -> J P Nagar
        BTM Layout -> B T M Layout
    """
    output = []

    for token in text.split():
        core, trailing = _split_trailing_punctuation(token)
        canonical = core.upper()

        if canonical in {item.upper() for item in KNOWN_ACRONYMS}:
            output.append(" ".join(canonical) + trailing)
        else:
            output.append(token)

    return " ".join(output)