from pronunciation_engine.normalizer import normalize_instruction


def test_highway_and_distance_expansion():
    text = "Turn left onto NH 44 after 500m"
    result = normalize_instruction(text)
    assert result == "turn left onto national highway forty four after five hundred meters"


def test_ordinal_and_road_expansion():
    text = "Turn right onto 12th Main Rd"
    result = normalize_instruction(text)
    assert result == "turn right onto twelfth main road"


def test_hosakerehalli_split_present():
    text = "Turn left at Hosakerehalli"
    result = normalize_instruction(text)
    assert "hosakere halli" in result


def test_rajajinagar_split_present():
    text = "Continue to Rajajinagar"
    result = normalize_instruction(text)
    assert "rajaji nagar" in result


def test_anantapuram_split_present():
    text = "Go to Anantapuram"
    result = normalize_instruction(text)
    assert "ananta puram" in result