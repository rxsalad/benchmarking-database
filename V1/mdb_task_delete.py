from mdb_helper import mongo_db_client, benchmark_db
from datetime import datetime, timezone
from zoneinfo import ZoneInfo 

# Task ID of the document to delete
task_id_to_delete = "20260101-fai-node-1"

# Connect to the database
db = mongo_db_client[benchmark_db]

# Select the collection
tasks = db["tasks"]

# Delete the document
delete_result = tasks.delete_one({"task_id": task_id_to_delete})

# Check result
if delete_result.deleted_count == 1:
    print(f"Document with task_id '{task_id_to_delete}' was deleted.")
else:
    print(f"No document found with task_id '{task_id_to_delete}'.")
