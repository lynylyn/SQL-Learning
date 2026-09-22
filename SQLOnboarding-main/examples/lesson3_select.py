import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("SELECT name, year_group, favourite_subject FROM students")
rows = cursor.fetchall()

for name, year_group, favourite_subject in rows:
    print(f"{name} is in year {year_group}, and their favourite subject is {favourite_subject}.")

connection.close()

#python SQLOnboarding-main/examples/lesson3_select.py