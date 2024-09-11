import sqlite3

db = sqlite3.connect("quiz.db")
print("Opened database successfully")

cursor = db.cursor()

startup_file = open("quiz.sql", "r")
startup_script = startup_file.read()
startup_file

cursor.executescript(startup_script)

db.commit()
db.close()
print("Database created successfully")

