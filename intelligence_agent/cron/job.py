import logging
from ingestion.news_fetcher import fetch_and_store_news

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def main():
    logging.info("🚀 Ingestion job started")
    try:
        fetch_and_store_news()
        logging.info("✅ Ingestion job completed")
    except Exception:
        logging.exception("❌ Ingestion job failed")

if __name__ == "__main__":
    main()
