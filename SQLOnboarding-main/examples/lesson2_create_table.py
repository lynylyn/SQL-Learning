import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    year_group INTEGER,
    favourite_subject TEXT NOT NULL
)
""")

#IF NOT EXISTS ensures that a table has been created and the system isn't attempting to feed data into an empty database.

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students (name, year_group, favourite_subject) VALUES (?, ?, ?)", ("Terence", 10, "Software Engineering"))
cursor.execute("INSERT INTO students (name, year_group, favourite_subject) VALUES (?, ?, ?)", ("Leo", 11, "PDHPE"))
cursor.execute("INSERT INTO students (name, year_group, favourite_subject) VALUES (?, ?, ?)", ("Awdsa", 7, "Science"))
cursor.execute("INSERT INTO students (name, year_group, favourite_subject) VALUES (?, ?, ?)", ("Evelyn", 10, "Software Engineering"))

connection.commit()
connection.close()

#The first row is the primary key.