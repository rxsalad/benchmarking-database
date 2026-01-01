from bson import json_util
from mdb_helper import mongo_db_client, benchmark_db
import csv
from bson import ObjectId

task_id = "20260101-cai-llm-test-2"

# Connect to the database
db = mongo_db_client[benchmark_db]

# Select the collection
results = db["results"]

# Fetch all documents
all_results = list(results.find({"task_id": task_id}))
if not all_results:
    print("No results found in the collection.")
    exit(0)

print("\n" + 60 * "-" + "> " + f"Total documents in 'results': {len(all_results)}")

# Print each document
for result in all_results:
    print(result)    
    #print(json_util.dumps(result, indent=4))

# Generate the CSV headers
all_keys = set()
for doc in all_results:
    all_keys.update(doc.keys())
all_keys.discard("_id")
print(f"\nCSV Headers: {all_keys}")

# Write CSV
csv_file = f"../{task_id}.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_keys)
    writer.writeheader()

    for doc in all_results:
        row = {}
        for key in all_keys:
            value = doc.get(key, "")
            # Convert ObjectId or other BSON types to string
            if isinstance(value, ObjectId):
                value = str(value)
            elif isinstance(value, (dict, list)):
                # Convert nested dict/list to JSON string
                value = json_util.dumps(value)
            row[key] = value
        writer.writerow(row)

print(f"\nCSV file generated: {csv_file}")