import csv

scores = []
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

highest = {"name": "", "score": -1}
lowest = {"name": "", "score": 101}

with open("grades.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"].strip()
        score = int(row["score"])

        scores.append(score)

        if score > highest["score"]:
            highest = {"name": name, "score": score}

        if score < lowest["score"]:
            lowest = {"name": name, "score": score}

        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"

        grade_counts[letter] += 1

average = round(sum(scores) / len(scores), 1)

print("=== Quiz Grade Summary ===")
print(f"Students assessed : {len(scores)}")
print(f"Average score     : {average}")
print(f"Highest score     : {highest['score']}  ({highest['name']})")
print(f"Lowest score      : {lowest['score']}  ({lowest['name']})")

print("\nGrade Distribution:")
print(f"  A (90-100) : {grade_counts['A']} students")
print(f"  B (80-89)  : {grade_counts['B']} students")
print(f"  C (70-79)  : {grade_counts['C']} students")
print(f"  D (60-69)  : {grade_counts['D']} students")
print(f"  F ( 0-59)  : {grade_counts['F']} students")