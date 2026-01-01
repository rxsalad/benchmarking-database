# Results — test data is usually consistent per task, but consistency is not required.

from mdb_helper import mongo_db_client, benchmark_db
from datetime import datetime, timezone
from zoneinfo import ZoneInfo 

task_id = "20260101-cai-llm-test-2"

# Connect to the database
db = mongo_db_client[benchmark_db]

# Select the collection
results = db["results"]

for x in range(1800, 1820):
    new_result = {
        "task_id": task_id,
        "timestamp":            datetime.now(timezone.utc),                                # For global 
        "date":                 str(datetime.now(ZoneInfo("America/Los_Angeles")).date()), # Only for me
        "worker_name":          f"node_{x-1800:02d}",
        "customer":             "cai",
        "region":               "atl1", 
        "physical_server_name": f"server_{x-1800:02d}",
        "rocm":                 "7.0",
        "gpu_tpye":             "MI325X",
        "gpu_number":           8,
        "downloading_s":        x,
        "loading_s":            x - 1790
    }

    result = results.insert_one(new_result)
    print("Inserted document ID:", result.inserted_id)


