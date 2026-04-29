import csv
from pathlib import Path

folder = Path(__file__).resolve().parent
input_path = folder / "messy_data.csv"
output_path = folder / "cleaned_data.csv"

valid_languages = {"Python", "C", "Scratch", "JavaScript"}
seen_ids = set()

report = {
    "blank_rows": 0,
    "duplicate_ids": 0,
    "out_of_range_scores": 0,
    "unknown_languages": 0,
    "clean_rows": 0,
}

cleaned_rows = []

with open(input_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        student_id = row.get("student_id", "").strip()
        language = row.get("language", "").strip()
        score_text = row.get("score", "").strip()

        if not student_id and not language and not score_text:
            report["blank_rows"] += 1
            continue

        if student_id in seen_ids:
            report["duplicate_ids"] += 1
            continue

        try:
            score = int(score_text)
        except ValueError:
            report["out_of_range_scores"] += 1
            continue

        if score < 1 or score > 5:
            report["out_of_range_scores"] += 1
            continue

        if language not in valid_languages:
            report["unknown_languages"] += 1
            continue

        seen_ids.add(student_id)
        cleaned_rows.append({
            "student_id": student_id,
            "language": language,
            "score": score,
        })
        report["clean_rows"] += 1

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["student_id", "language", "score"])
    writer.writeheader()
    writer.writerows(cleaned_rows)

print("Cleaning report")
print("---------------")
for key, value in report.items():
    print(f"{key}: {value}")

print("Saved to cleaned_data.csv")