import random

ROAD_NAMES = [
    "MG Rd",
    "Brigade Rd",
    "12th Main Rd",
    "30th Cross",
    "5th Avenue",
    "Church St",
]

HIGHWAYS = [
    "NH 44",
    "NH 48",
    "NH 75"
]

DISTANCES = [
    "100m",
    "200m",
    "500m",
    "1km",
    "2km"
]

TURNS = [
    "Turn left onto",
    "Turn right onto",
]

CONTINUES = [
    "Continue for"
]


def generate_instruction():

    choice = random.choice(["turn", "continue", "highway"])

    if choice == "turn":

        turn = random.choice(TURNS)
        road = random.choice(ROAD_NAMES)

        return f"{turn} {road}"

    elif choice == "continue":

        dist = random.choice(DISTANCES)

        return f"Continue for {dist}"

    else:

        dist = random.choice(DISTANCES)
        highway = random.choice(HIGHWAYS)

        return f"Merge onto {highway} and continue for {dist}"