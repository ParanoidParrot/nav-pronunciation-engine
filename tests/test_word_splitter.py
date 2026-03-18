from pronunciation_engine.word_splitter import split_word


def test_split_hosakerehalli():
    assert split_word("hosakerehalli") == "hosakere halli"


def test_split_rajajinagar():
    assert split_word("rajajinagar") == "rajaji nagar"


def test_split_anantapuram():
    assert split_word("anantapuram") == "ananta puram"


def test_split_bidarwadi():
    assert split_word("bidarwadi") == "bidar wadi"