def calculate_remaining(capacities, logs):
    total_used = 0
    peak_usage = 0
    temp_buffer = []
    adjustment_factor = 1.0

    for entry in logs:
        device_id, usage, timestamp = entry
        if usage > 50:
            peak_usage += 1
        total_used += usage
        temp_buffer.append(usage * 0.1)

    # Irrelevant averaging computation (distractor)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    scaled_peak = peak_usage * adjustment_factor

    # Core logic: capacity analysis with slicing and conditional logic
    active_capacities = capacities[1:-1]  # Exclude first and last
    filtered = [c for c in active_capacities if c > 75]

    base_capacity = sum(filtered)
    redundancy_pool = base_capacity * 0.2

    # Simulate conditional reallocation
    if len(filtered) >= 3:
        bonus_allocation = 15
    else:
        bonus_allocation = 5

    # Final calculation
    final_capacity = base_capacity + bonus_allocation - total_used

    # Dead code path (misleading)
    if scaled_peak > 100:
        final_capacity += 10  # Never reached in this setup

    return final_capacity

# System configuration data
node_capacities = [120, 85, 90, 60, 95, 70, 110]
usage_records = [
    (101, 20, '2023-01-01T10:00'),
    (102, 55, '2023-01-01T10:05'),
    (103, 30, '2023-01-01T10:10'),
    (104, 45, '2023-01-01T10:15'),
    (105, 65, '2023-01-01T10:20')
]

# Initialize tracking variables (some irrelevant)
overall_utilization = sum(u for _, u, _ in usage_records)
diagnostic_checksum = sum([len(str(u)) for u in node_capacities])

# Key execution point
final_capacity = calculate_remaining(node_capacities, usage_records)

# Output result
print(f"Result: {final_capacity}")