from pronunciation_engine.acronyms import ACRONYM_MAP
from pronunciation_engine.numbers import normalize_numbers
from pronunciation_engine.units import expand_unit
from pronunciation_engine.highways import expand_highway
from pronunciation_engine.abbreviations import expand_abbreviation


def normalize_instruction(text: str):

    tokens = text.split()
    normalized = []

    for token in tokens:

        token = expand_highway(token)
        token = expand_abbreviation(token)
        token = normalize_numbers(token)
        token = expand_unit(token)

        normalized.append(token.lower())

    return " ".join(normalized)