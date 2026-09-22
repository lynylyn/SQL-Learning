import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()

#python SQLOnboarding-main/examples/lesson3_select.py