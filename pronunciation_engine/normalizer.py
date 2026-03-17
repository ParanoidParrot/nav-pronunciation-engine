from pronunciation_engine.acronyms import ACRONYM_MAP
from pronunciation_engine.numbers import normalize_numbers
from pronunciation_engine.units import expand_unit
from pronunciation_engine.highways import expand_highway
from pronunciation_engine.abbreviations import expand_abbreviation
from pronunciation_engine.distance import normalize_distance
from pronunciation_engine.tokenizer import tokenize
from pronunciation_engine.word_splitter import split_word

def normalize_instruction(text: str):

    tokens = tokenize(text)
    normalized = []

    for token in tokens:

        token = normalize_distance(token)
        token = expand_highway(token)
        token = expand_abbreviation(token)
        token = normalize_numbers(token)
        token = expand_unit(token)

        normalized.append(token.lower())

    return " ".join(normalized)

def normalize(text: str):
    words = text.lower().split()

    processed = []
    for word in words:
        split = split_word(word)
        processed.append(split)

    return " ".join(processed)