import itertools

# Simulate hourly network bandwidth usage across multiple servers
hourly_ticks = list(range(24))
server_a_load = [120, 135, 140, 160, 180, 200, 220, 250, 240, 230, 210, 190, 
               170, 165, 167, 175, 195, 215, 235, 245, 255, 250, 230, 200]
server_b_load = [90, 95, 100, 110, 115, 125, 145, 170, 180, 175, 170, 160,
               150, 155, 160, 170, 185, 200, 210, 215, 220, 210, 190, 170]

# Combine loads using element-wise summation
combined_load = [a + b for a, b in zip(server_a_load, server_b_load)]

# Apply time-based weighting: peak hours (9-18) have higher impact
weighted_load = []
for hour, load in enumerate(combined_load):
    if 9 <= hour <= 18:
        weighted_load.append(load * 1.1)
    else:
        weighted_load.append(load * 0.9)

# Normalize values to simulate percentage of max capacity
max_theoretical = 500
normalized_load = [round((load / max_theoretical) * 100, 2) for load in weighted_load]

# Misleading computation: average usage (not needed for final answer)
dummy_avg = sum(normalized_load) / len(normalized_load)
dummy_variance_list = [(x - dummy_avg) ** 2 for x in normalized_load]
dummy_total_variance = sum(dummy_variance_list)

# Slice only business hours for anomaly detection (distractor operation)
business_hour_usage = normalized_load[9:18]
anomaly_threshold = 85
anomalies = [x for x in business_hour_usage if x > anomaly_threshold]

# Actual key computation path
usage_levels = []
for val in normalized_load:
    if val >= 75:
        usage_levels.append(val)

# Red herring: unused string processing with slicing
log_entry = "ERROR: HighLoad THRESHOLD breached"
error_code = log_entry[7:15]
status_flag = log_entry.lower().split(':')[0].title()

# Critical statement
peak_capacity = max(usage_levels)

# Distractor: itertools permutation of irrelevant data
fake_patterns = list(itertools.permutations([1, 2, 3], 2))

# Another red herring variable
effective_utilization = [x for x in usage_levels if x > 80]

# Final output
print(f"Result: {peak_capacity}")