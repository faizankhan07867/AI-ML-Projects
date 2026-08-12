import sqlite3

conn = sqlite3.connect("database/college.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS faq(

id INTEGER PRIMARY KEY AUTOINCREMENT,

question TEXT,

answer TEXT

)
""")

data = [

("What is college timing?",
"College timing is 9 AM to 5 PM."),

("Where is library?",
"The library is located in Block A."),

("How to apply scholarship?",
"You can apply through the scholarship portal."),

("What is hostel fee?",
"The hostel fee is ₹50,000 per year."),

("Where is IT Department?",
"The IT Department is in Block C.")

]

cursor.executemany(

"INSERT INTO faq(question,answer) VALUES(?,?)",

data

)

conn.commit()

conn.close()

print("Database Created Successfully")