import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

#year_group = 11
cursor.execute(
    "SELECT year_group, name FROM students ORDER BY year_group"
)

rows = cursor.fetchall()
for year_group, name in rows:
    print(f"Year {year_group}: {name}")

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]
print("Total students:", total_students)

connection.close()

#python SQLOnboarding-main/examples/lesson4_filter.py