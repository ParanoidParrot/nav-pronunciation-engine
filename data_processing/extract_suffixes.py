import re
from collections import Counter

INPUT_FILE = "indian_street_data/named_roads.osm"
OUTPUT_FILE = "indian_street_data/processed/suffix_counts.csv"

MIN_SUFFIX_LEN = 3
MAX_SUFFIX_LEN = 8

suffix_counter = Counter()

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        if 'k="name"' not in line:
            continue

        match = re.search(r'v="([^"]+)"', line)
        if not match:
            continue

        name = match.group(1).lower()
        words = re.findall(r"[a-z]+", name)

        for word in words:
            if len(word) < 6:
                continue

            for i in range(MIN_SUFFIX_LEN, MAX_SUFFIX_LEN + 1):
                suffix = word[-i:]
                suffix_counter[suffix] += 1

# save to csv
with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for suffix, count in suffix_counter.most_common():
        out.write(f"{suffix},{count}\n")

print(f"Saved to {OUTPUT_FILE}")