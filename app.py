from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return "News Aggregator API Running"


@app.route("/news")
def get_news():

    conn = sqlite3.connect("news.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles")

    rows = cursor.fetchall()

    conn.close()

    return jsonify([dict(row) for row in rows])


@app.route("/search")
def search_news():

    keyword = request.args.get("keyword", "")

    conn = sqlite3.connect("news.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM articles WHERE title LIKE ?",
        (f"%{keyword}%",)
    )

    rows = cursor.fetchall()

    conn.close()

    return jsonify([dict(row) for row in rows])


@app.route("/summary/<int:id>")
def get_summary(id):

    conn = sqlite3.connect("news.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT title, summary FROM articles WHERE id=?",
        (id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return jsonify(dict(row))

    return jsonify({"error": "Article not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
    @app.route("/source/<source>")
def get_by_source(source):

    conn = sqlite3.connect("news.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM articles WHERE source=?",
        (source,)
    )

    rows = cursor.fetchall()

    conn.close()

    return jsonify([dict(row) for row in rows])