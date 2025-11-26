data_records = ["user_1:active:online", "user_2:inactive:offline", "user_3:active:online", "user_4:active:busy", "user_5:inactive:offline", "user_6:active:online"]

# Process the data records
status_list = []
for record in data_records:
    parts = record.split(":")
    status = parts[1]
    status_list.append(status)

# Create a copy for analysis (distractor operation)
backup_list = status_list.copy()

# Calculate temporary metrics (distractor variables)
temp_active = len([s for s in backup_list if s == "active"])
temp_inactive = len([s for s in backup_list if s == "inactive"])
ratio_analysis = temp_active / len(backup_list) if backup_list else 0

# Main processing - filter and count active records
processed_data = [status.upper() for status in status_list if status.startswith("a")]
final_count = processed_data.count("ACTIVE")

# Print result for verification
print(f"Result: {final_count}")