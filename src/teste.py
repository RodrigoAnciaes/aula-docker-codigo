import sqlite3
import os

db = sqlite3.connect('quiz.db')

print('quiz.db' in os.listdir())

cursor = db.cursor()

startup_file = open('src/quiz.sql', 'r')
startup_script = startup_file.read()
startup_file.close()

cursor.executescript(startup_script)

