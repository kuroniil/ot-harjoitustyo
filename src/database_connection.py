import os
import sqlite3
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    print("No .env file found")

db_env = os.getenv("APP_ENV") or "development"

connection = sqlite3.connect(os.path.join(dirname, "..", "data", \
                                "scores.sqlite" if db_env == "development" \
                                else "tests.sqlite"))

def get_database_connection():
    return connection
