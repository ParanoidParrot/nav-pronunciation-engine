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
    "40th": "fortieth",
}


CARDINAL_MAP = {
    "10": "ten",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
    "100": "hundred",
    "200": "two hundred",
}


def normalize_numbers(token: str):
    token_lower = token.lower()

    if token_lower in ORDINAL_MAP:
        return ORDINAL_MAP[token_lower]

    if token_lower in CARDINAL_MAP:
        return CARDINAL_MAP[token_lower]

    return token