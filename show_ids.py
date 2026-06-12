import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("SELECT id, title FROM articles")

for row in cursor.fetchall():
    print(row)

conn.close()