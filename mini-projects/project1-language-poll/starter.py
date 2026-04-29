import csv
from pathlib import Path

file_path = Path(__file__).resolve().parents[2] / "part1" / "favorites.csv"

counts = {}

with open(file_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"].strip()
        counts[language] = counts.get(language, 0) + 1

sorted_languages = sorted(counts, key=counts.get, reverse=True)

print("=== Language Popularity Report ===")
for rank, language in enumerate(sorted_languages, start=1):
    print(f"{rank}. {language:<8}: {counts[language]:>3} students")

print(f"\nTotal responses: {sum(counts.values())}")