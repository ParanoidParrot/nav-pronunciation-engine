import json
import re
from collections import Counter

suffix_counter = Counter()

with open("../indian_street_data/india_roads.json") as f:
    data = json.load(f)

for feature in data["features"]:
    props = feature.get("properties", {})
    name = props.get("name")

    if not name:
        continue

    tokens = re.findall(r"[a-zA-Z]+", name.lower())

    if len(tokens) > 1:
        suffix = tokens[-1]
        suffix_counter[suffix] += 1


for word, count in suffix_counter.most_common(50):
    print(word, count)