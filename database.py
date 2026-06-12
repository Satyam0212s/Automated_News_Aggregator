cursor.execute("""
CREATE TABLE IF NOT EXISTS articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    summary TEXT,
    url TEXT UNIQUE,
    source TEXT
)
""")