from pronunciation_engine.normalizer import normalize_instruction
from pronunciation_engine.tts_engine import text_to_speech_file


instruction = "Turn left onto NH 44 after 500m"

normalized = normalize_instruction(instruction)

print("Normalized:", normalized)

audio = text_to_speech_file(normalized)

print("Audio generated:", audio)