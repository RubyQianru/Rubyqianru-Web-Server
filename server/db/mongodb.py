from pymongo import MongoClient
from server.core.config import settings

MONGO_URL = settings.MONGO_URL

client = MongoClient(MONGO_URL)

crypto_db = client["crypto"]
crypto_collection = crypto_db["crypto"]

twitter_db = client["twitter"]
twitter_collection = twitter_db["twitter"]

report_db = client["report"]
report_collection = report_db["sentiment_report"]

