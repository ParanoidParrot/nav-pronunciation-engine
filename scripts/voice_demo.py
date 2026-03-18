import os
#from pronunciation_engine.normalizer import normalize_instruction
from pronunciation_engine.normalizer import normalize
from pronunciation_engine.tts_engine import text_to_speech_file


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "audio_outputs")

# create folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

test_sentences = [
    "Turn left onto National Highway 44 after 500 meters",
    "Turn left at Hosakerehalli",
    "Continue to Rajajinagar",
    "Go to Anantapuram",
    "Head towards Bidarwadi",
    "Turn left to kaikondrahalli"

]

for i, text in enumerate(test_sentences):
    normalized = normalize(text)
    print(f"\nOriginal:   {text}")
    print(f"\nNormalized: {normalized}")

    safe_text = normalized.replace(" ", "_")[:30]
    filename =os.path.join(OUTPUT_DIR, f"{i}_{safe_text}.wav")
    text_to_speech_file(normalized, filename)

    print(f"Saved: {filename}")