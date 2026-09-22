import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

year_group = 11
cursor.execute(
    "SELECT name, year_group FROM students WHERE year_group = ? ORDER BY name",
    (year_group,)
)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]
print("Total students:", total_students)

connection.close()

#python SQLOnboarding-main/examples/lesson4_filter.py