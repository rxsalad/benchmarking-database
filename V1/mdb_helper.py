import os
from xmlrpc import client
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

benchmark_db = os.getenv("MDB_BENCHMARK_DB", "benchmark_db")

username     = os.getenv("MDB_USERNAME", "")
password     = os.getenv("MDB_PASSWORD", "")
host         = os.getenv("MDB_HOST", "")
database     = os.getenv("MDB_DATABASE", "") # the database that stores the user credentials

# Build connection URI
uri = f"mongodb+srv://{username}:{password}@{host}/?tls=true&authSource={database}&retryWrites=true&w=majority"

# Connect to MongoDB
mongo_db_client = MongoClient(uri)

if __name__ == "__main__":

    # Select the database
    db = mongo_db_client[database]

    # Test connection, including authentication, TLS/SSL
    print(db.command("ping"))  # should return {'ok': 1.0} if successful