# 📰 Automated News Aggregator & Summarizer

A Python-based News Aggregator that collects articles from multiple RSS feeds, stores them in a SQLite database, provides REST APIs for searching and filtering news, generates summaries, and supports automated email digest delivery.

---

## 🚀 Features

- 📰 Aggregate news from multiple sources using RSS feeds
- 🔍 Search articles by keyword
- 📄 Retrieve article summaries
- 🗄️ Store articles in SQLite database
- 🌐 REST API built with Flask
- 📧 Automated email digest using SMTP
- ⏰ Scheduled news updates and email delivery
- 🏷️ Filter news by source
- 📊 News statistics endpoint

---

## 🛠️ Tech Stack

- Python
- Flask
- SQLite
- Feedparser
- BeautifulSoup
- SMTP
- Schedule

---

## 📂 Project Structure

```text
news_aggregator/
│
├── app.py
├── scraper.py
├── database.py
├── summarizer.py
├── email_sender.py
├── digest.py
├── scheduler.py
├── load_data.py
├── requirements.txt
├── news.db
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Automated-News-Aggregator.git
cd Automated-News-Aggregator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Load News Articles

```bash
python load_data.py
```

### Start Flask Server

```bash
python app.py
```

Server will run on:

```text
http://127.0.0.1:5000
```

---

## 📌 API Endpoints

### Get All News

```http
GET /news
```

Example:

```text
http://127.0.0.1:5000/news
```

---

### Search News

```http
GET /search?keyword=<keyword>
```

Example:

```text
http://127.0.0.1:5000/search?keyword=technology
```

---

### Get Article Summary

```http
GET /summary/<id>
```

Example:

```text
http://127.0.0.1:5000/summary/1
```

---

### Filter by Source

```http
GET /source/<source>
```

Example:

```text
http://127.0.0.1:5000/source/bbc
```

---

### Statistics

```http
GET /stats
```

Returns the number of articles collected from each source.

---

## 📧 Email Digest Configuration

Update `email_sender.py`:

```python
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

For Gmail, use a Google App Password instead of your account password.

---

## ⏰ Automated Daily Digest

Run:

```bash
python scheduler.py
```

This automatically sends a daily news digest email at the configured time.

---

## 🗃️ Database Schema

```sql
CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    summary TEXT,
    url TEXT UNIQUE,
    source TEXT
);
```

---

## 🔮 Future Improvements

- AI-powered summarization using Hugging Face Transformers
- News categorization (Technology, Sports, Business, etc.)
- User authentication
- Personalized news feeds
- Web dashboard frontend
- Docker deployment
- Cloud deployment on Render

---

## 📸 Sample Response

```json
[
  {
    "id": 1,
    "title": "Latest Technology Trends",
    "content": "Article content...",
    "summary": "Short summary...",
    "url": "https://example.com/article",
    "source": "techcrunch"
  }
]
```

---

## 🎯 Learning Outcomes

- REST API Development with Flask
- RSS Feed Processing
- SQLite Database Management
- Email Automation using SMTP
- Python Backend Development
- API Design and Testing

---

## 👨‍💻 Author

Satyam 

GitHub: https://github.com/Satyam0212s

---

## 📜 License

This project is open-source and available under the MIT License.
