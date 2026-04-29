import sqlite3

conn = sqlite3.connect("favorites.db")
db = conn.cursor()

rows = db.execute("""
    SELECT language, COUNT(*) as count
    FROM favorites
    GROUP BY language
    ORDER BY count DESC
""").fetchall()

for language, count in rows:
    print(f"{language}: {count}")

conn.close()