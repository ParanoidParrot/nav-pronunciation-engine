import re

from pronunciation_engine.numbers import number_to_words

def number_to_words(num: int):

    ones = {
        0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen"
    }

    tens = {
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety"
    }

    if num < 20:
        return ones[num]

    if num < 100:
        t = (num // 10) * 10
        r = num % 10
        if r == 0:
            return tens[t]
        return tens[t] + " " + ones[r]

    if num < 1000:
        h = num // 100
        r = num % 100

        if r == 0:
            return ones[h] + " hundred"

        return ones[h] + " hundred " + number_to_words(r)

    return str(num)

def normalize_distance(token: str):

    pattern = r"^(\d+)(m|km|ft)$"

    match = re.match(pattern, token.lower())

    if not match:
        return token

    number = int(match.group(1))
    unit = match.group(2)

    number_words = number_to_words(number)

    unit_map = {
        "m":"meters",
        "km":"kilometers",
        "ft":"feet"
    }

    return number_words + " " + unit_map[unit]