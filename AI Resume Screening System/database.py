import sqlite3

connection = sqlite3.connect("database/resumes.db")

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS candidates(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

email TEXT,

score INTEGER,

skills TEXT

)

""")

connection.commit()

connection.close()