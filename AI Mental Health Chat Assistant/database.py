import os
import sqlite3

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/chat.db")


import sqlite3

conn = sqlite3.connect("database/chat.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS chat(

id INTEGER PRIMARY KEY AUTOINCREMENT,

message TEXT,

response TEXT

)

""")

conn.commit()

conn.close()

print("Database Created Successfully")