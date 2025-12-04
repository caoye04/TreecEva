server_capacities = [120, 85, 200, 90, 150, 180, 75]
maintenance_flags = [False, True, False, True, False, False, True]

# Calculate total capacity before filtering
total_raw_capacity = sum(server_capacities)
print(f"Raw total capacity: {total_raw_capacity}")

# Filter out servers under maintenance
filtered_capacities = []
for i, (capacity, in_maintenance) in enumerate(zip(server_capacities, maintenance_flags)):
    if not in_maintenance:
        filtered_capacities.append(capacity)
    # Distractor: unused calculation
    temp_adjustment = capacity * 0.1

# Calculate average of available servers
if filtered_capacities:
    final_capacity = sum(filtered_capacities) // len(filtered_capacities)
else:
    final_capacity = 0

# Distractor: unused variable
backup_threshold = max(server_capacities) - 50

print(f"Result: {final_capacity}")