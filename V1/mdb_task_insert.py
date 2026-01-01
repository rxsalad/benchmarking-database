# Optional: keep the metadata of each task
# task_id of each task should be unique, such as "date-customer-purpose-id"
# task_id is used to extract test results for each task from the results collection

from mdb_helper import mongo_db_client, benchmark_db
from datetime import datetime, timezone
from zoneinfo import ZoneInfo 

# Connect to the database
db = mongo_db_client[benchmark_db]

# Select the collection
tasks = db["tasks"]

# 20260101-cai-llm-test-1, 20260101-cai-llm-test-2, 20260101-fai-node-1,

# Insert a task document
task = { "task_id":      "20260101-fai-node-1",                                     # Should be unique
         "timestamp":    datetime.now(timezone.utc),                                # For global 
         "date":         str(datetime.now(ZoneInfo("America/Los_Angeles")).date()), # Only for me
         "customer":     "fai",
         "sa":           "rshue",
         "model":        "meta-llama/Llama-3.1-70B-Instruct",
         "vllm_version": "rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103",
         "node_count":   20,
         "node_type":    "mixed-MI325X-MI350X",
         "region":       "atl1",
         "use_case":    "model downloading",
         "misc":         "" 
}

result = tasks.insert_one(task)
print("Inserted document ID:", result.inserted_id)
