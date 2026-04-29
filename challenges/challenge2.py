# challenge2.py — Top N Languages
# Ask user for N and print top N most popular languages from favorites.csv

import csv
from collections import Counter
from pathlib import Path


def main():
    file_path = Path(__file__).resolve().parent.parent / "part1" / "favorites.csv"
    counts = Counter()

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            language = row["language"].strip()
            counts[language] += 1

    try:
        n = int(input("Top how many languages? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for language, votes in counts.most_common(n):
        print(f"{language}: {votes}")


if __name__ == "__main__":
    main()