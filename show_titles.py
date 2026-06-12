import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("SELECT title FROM articles")

for row in cursor.fetchall():
    print(row[0])

conn.close()