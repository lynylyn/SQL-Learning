import sqlite3
print("SQLite3 imported!")
connection = sqlite3.connect("library.db")
print("Database connected!")
connection.close()
print("Database closed!")

# If the database file is deleted, the system will create it again.