import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    year_group INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students (name, year_group) VALUES (?, ?)", ("Ava", 10))
cursor.execute("INSERT INTO students (name, year_group) VALUES (?, ?)", ("Leo", 11))

connection.commit()
connection.close()