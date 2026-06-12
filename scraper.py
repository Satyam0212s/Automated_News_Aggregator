import feedparser

RSS_FEEDS = {
    "bbc": "https://feeds.bbci.co.uk/news/rss.xml",
    "techcrunch": "https://techcrunch.com/feed/",
    "reuters": "https://feeds.reuters.com/reuters/topNews"
}

def fetch_news():

    news = []

    for source, url in RSS_FEEDS.items():

        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:

            news.append({
                "title": entry.title,
                "content": getattr(entry, "summary", ""),
                "url": entry.link,
                "source": source
            })

    return news