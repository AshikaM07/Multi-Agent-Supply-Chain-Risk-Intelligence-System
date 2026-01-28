import os
import requests
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

from analyzer import analyze_news

load_dotenv()

# -------- ENV CONFIG --------
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = os.getenv(
    "NEWS_API_URL",
    "https://newsapi.org/v2/everything"  # safe default
)

if not NEWS_API_KEY:
    raise RuntimeError("NEWS_API_KEY missing in .env")

# -------- QUERY CONFIG --------
KEYWORDS = ["fire", "strike", "shutdown"]

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2))
def fetch_news():
    params = {
        "q": " OR ".join(KEYWORDS),
        "language": "en",
        "pageSize": 50,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("articles", [])


def fetch_and_store_news():
    articles = fetch_news()

    for article in articles:
        analyze_news(article)
