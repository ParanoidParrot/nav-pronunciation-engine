from pronunciation_engine.normalizer import normalize_instruction

def test_road_expansion():
    assert normalize_instruction("Dr Rajkumar Rd") == "doctor rajkumar road"

def test_number_normalization():
    assert normalize_instruction("BTM 2nd Stage") == "btm second stage"