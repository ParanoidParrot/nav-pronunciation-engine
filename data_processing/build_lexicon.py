import json

INPUT_FILE = "indian_street_data/processed/cleaned_suffixes.json"
OUTPUT_FILE = "pronunciation_engine/lexicon.json"

# Add linguistic metadata
LEXICON_META = {
    "nagar": {"lang": "sanskrit", "type": "town"},
    "pur": {"lang": "sanskrit", "type": "city"},
    "halli": {"lang": "kannada", "type": "village"},
    "wadi": {"lang": "marathi", "type": "settlement"},
    "gaon": {"lang": "hindi", "type": "village"},
    "oor": {"lang": "dravidian", "type": "place"},
    "palle": {"lang": "telugu", "type": "village"},
    "aram": {"lang": "tamil", "type": "area"},
    "thanda": {"lang": "tribal", "type": "settlement"}
}

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

lexicon = {}

for suffix in data:
    if suffix in LEXICON_META:
        lexicon[suffix] = LEXICON_META[suffix]

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    json.dump(lexicon, out, indent=2)

print(f"Lexicon saved to {OUTPUT_FILE}")