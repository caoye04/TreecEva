data_entries = ["active", "inactive", "active", "pending", "active", "completed"]
status_counts = {"active": 0, "inactive": 0, "pending": 0, "completed": 0}

for entry in data_entries:
    status_counts[entry] = status_counts.get(entry, 0) + 1

filtered_data = list(filter(lambda x: x in ["active", "pending"], data_entries))
processed_count = filtered_data.count("active")

print(f"Result: {processed_count}")