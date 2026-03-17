import json

INPUT_FILE = "indian_street_data/processed/suffix_counts.csv"
OUTPUT_FILE = "indian_street_data/processed/cleaned_suffixes.json"

# Manually curated groups (you can expand later)
SUFFIX_GROUPS = {
    "nagar": ["nagar", "agar"],
    "pur": ["pur", "pura", "puram", "apur", "apuram"],
    "halli": ["halli", "alli"],
    "wadi": ["wadi", "nwadi", "anwadi", "ganwadi"],
    "gaon": ["gaon", "aon"],
    "oor": ["oor", "uru"],
    "palle": ["palle", "alle"],
    "aram": ["aram"],
    "thanda": ["thanda"]
}

cleaned = {}

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        suffix, count = line.strip().split(",")
        count = int(count)

        for canonical, variants in SUFFIX_GROUPS.items():
            if suffix in variants:
                if canonical not in cleaned:
                    cleaned[canonical] = 0
                cleaned[canonical] += count

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    json.dump(cleaned, out, indent=2)

print(f"Saved cleaned suffixes to {OUTPUT_FILE}")