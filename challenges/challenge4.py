import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent.parent / "part2" / "favorites.db"


def run_query(query, parameters=()):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchall()


while True:
    print("\n=== SQL Explorer ===")
    print("1. Count by language")
    print("2. Count by problem")
    print("3. Search by problem name")
    print("4. Top 5 problems overall")
    print("5. Quit")

    choice = input("Choice: ").strip()

    if choice == "1":
        rows = run_query("""
            SELECT language, COUNT(*)
            FROM favorites
            GROUP BY language
            ORDER BY COUNT(*) DESC
        """)
        for language, count in rows:
            print(f"{language}: {count}")

    elif choice == "2":
        rows = run_query("""
            SELECT problem, COUNT(*)
            FROM favorites
            GROUP BY problem
            ORDER BY COUNT(*) DESC
        """)
        for problem, count in rows:
            print(f"{problem}: {count}")

    elif choice == "3":
        search = input("Problem name: ").strip()
        rows = run_query("""
            SELECT problem, language
            FROM favorites
            WHERE problem LIKE ?
            ORDER BY problem
        """, (f"%{search}%",))

        if not rows:
            print("No results found.")
        else:
            for problem, language in rows:
                print(f"{problem} — {language}")

    elif choice == "4":
        rows = run_query("""
            SELECT problem, COUNT(*)
            FROM favorites
            GROUP BY problem
            ORDER BY COUNT(*) DESC
            LIMIT 5
        """)
        for problem, count in rows:
            print(f"{problem}: {count}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")