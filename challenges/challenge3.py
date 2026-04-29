import csv
from collections import Counter
from pathlib import Path

input_path = Path(__file__).resolve().parent.parent / "part1" / "favorites.csv"
output_path = Path(__file__).resolve().parent / "language_summary.csv"

counts = Counter()

with open(input_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        language = row["language"].strip()
        counts[language] += 1

total_votes = sum(counts.values())

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["language", "votes", "percentage"])
    writer.writeheader()

    for language, votes in counts.most_common():
        percentage = (votes / total_votes) * 100
        writer.writerow({
            "language": language,
            "votes": votes,
            "percentage": f"{percentage:.2f}"
        })

print("Saved to language_summary.csv")