import re


def tokenize(text: str):
    """
    Regex tokenizer for navigation instructions.

    Handles:
    - words
    - ordinals (12th)
    - compact distance tokens (200m)
    - numbers
    """

    pattern = r"\d+(?:st|nd|rd|th)?|\d+(?:m|km|ft)|[A-Za-z]+"

    tokens = re.findall(pattern, text)

    return tokens