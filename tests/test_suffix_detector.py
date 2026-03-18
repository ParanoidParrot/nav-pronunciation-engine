from pronunciation_engine.suffix_detector import detect_suffix


def test_detect_halli():
    assert detect_suffix("hosakerehalli") == "halli"


def test_detect_nagar():
    assert detect_suffix("rajajinagar") == "nagar"


def test_detect_puram():
    assert detect_suffix("anantapuram") == "puram"


def test_detect_wadi():
    assert detect_suffix("bidarwadi") == "wadi"