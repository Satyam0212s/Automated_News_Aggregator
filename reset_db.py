import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM articles")

conn.commit()
conn.close()

print("Database cleared")