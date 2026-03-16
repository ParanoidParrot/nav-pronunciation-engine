ORDINAL_MAP = {
    "1st": "first",
    "2nd": "second",
    "3rd": "third",
    "4th": "fourth",
    "5th": "fifth",
    "6th": "sixth",
    "7th": "seventh",
    "8th": "eighth",
    "9th": "ninth",
    "10th": "tenth",
    "11th": "eleventh",
    "12th": "twelfth",
    "13th": "thirteenth",
    "14th": "fourteenth",
    "15th": "fifteenth",
    "16th": "sixteenth",
    "17th": "seventeenth",
    "18th": "eighteenth",
    "19th": "nineteenth",
    "20th": "twentieth",
    "21st": "twenty first",
    "22nd": "twenty second",
    "23rd": "twenty third",
    "24th": "twenty fourth",
    "25th": "twenty fifth",
    "26th": "twenty sixth",
    "27th": "twenty seventh",
    "28th": "twenty eighth",
    "29th": "twenty ninth",
    "30th": "thirtieth",
    "31st": "thirty first",
    "32nd": "thirty second",
    "33rd": "thirty third",
    "34th": "thirty fourth",
    "35th": "thirty fifth",
    "36th": "thirty sixth",
    "37th": "thirty seventh",
    "38th": "thirty eighth",
    "39th": "thirty ninth",
    "40th": "fortieth"
}


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


def normalize_numbers(token: str):

    if token.isdigit():
        return number_to_words(int(token))

    token_lower = token.lower()

    if token_lower in ORDINAL_MAP:
        return ORDINAL_MAP[token_lower]

    return token