import sqlite3

def create_digest():

    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT title
    FROM articles
    ORDER BY id DESC
    LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    digest = ""

    for row in rows:
        digest += f"• {row[0]}\n"

    return digest