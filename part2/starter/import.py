import csv
import sqlite3
from pathlib import Path

# Ruta correcta al CSV
file_path = Path(__file__).resolve().parent.parent / "favorites.csv"

conn = sqlite3.connect("favorites.db")
db = conn.cursor()

db.execute("DROP TABLE IF EXISTS favorites")

db.execute("""
CREATE TABLE favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problem TEXT,
    language TEXT
)
""")

with open(file_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db.execute(
            "INSERT INTO favorites (problem, language) VALUES (?, ?)",
            (row["problem"].strip(), row["language"].strip())
        )

conn.commit()
conn.close()

print("Database created successfully.")