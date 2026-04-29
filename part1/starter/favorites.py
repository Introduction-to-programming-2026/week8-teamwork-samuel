import csv
from collections import Counter
from pathlib import Path

# Ruta correcta al CSV
file_path = Path(__file__).resolve().parent.parent / "favorites.csv"

counts = Counter()

with open(file_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        language = row["language"].strip()
        counts[language] += 1

for language, votes in counts.most_common():
    print(f"{language}: {votes}")