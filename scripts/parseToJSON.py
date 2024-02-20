import re
import json
import uuid
import sys
import os.path
import time

# Function to parse the text and return JSON
def parse_text_to_json(text):
    # Find all bandwidth numbers in the text
    bandwidth_values = re.findall(r'\d+\.\d+', text)

    # Remove known non-bandwidth values (e.g., buffer size)
    known_non_bandwidth_values = {'100.000', '3.11'}
    bandwidth_values = [value for value in bandwidth_values if value not in known_non_bandwidth_values]
    
    # Generate a current timestamp and a UUID for instance
    timestamp = str(int(time.time()))  # Use time.time() to get current timestamp
    instance_uuid = str(uuid.uuid4())
    
    # Create the JSON structure
    data = {
        "timestamp": timestamp,
        "system_type": "numa_node",
        "node_type": "numa_node",
        "instance_UUID": instance_uuid,
        "bandwidths": []
    }
    
    # Assume unit_id and node_id are both 0 for this example
    for i, bandwidth in enumerate(bandwidth_values):
        data["bandwidths"].append({
            "instance_UUID": instance_uuid,
            "unit_id": 0,
            "node_id": 0,
            "bandwidth": float(bandwidth)
        })
    
    return data

# Read the contents of temp.txt into a variable
with open('temp.txt', 'r') as file:
    text = file.read()

# Saving file to mlc-exporter/examples/ directory
directory_path = "../examples" # examples directory is exposed to exporter
file_name = "sample.json"

if not os.path.exists(directory_path):
    print("Created /examples directory at root of mlc-exporter")
    os.mkdir(directory_path)

file_path = os.path.join(directory_path, file_name)

# Parse the text to JSON
parsed_json = parse_text_to_json(text)

# Write the JSON data to a file
with open(file_path, 'w') as file:
    json.dump([parsed_json], file, indent=2)

print("JSON data has been written to", os.path.abspath(file_path))
