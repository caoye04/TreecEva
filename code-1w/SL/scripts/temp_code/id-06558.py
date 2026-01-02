from collections import defaultdict

# Simulate hourly system load with some noise
time_series_data = [105, 120, 135, 140, 137, 155, 160, 158, 150, 145, 142, 148]

# Apply threshold filter to exclude anomalous low values
minimum_threshold = 130
base_loads_filtered = [load for load in time_series_data if load >= minimum_threshold]

# Track frequency of loads using defaultdict (irrelevant but plausible)
load_frequency = defaultdict(int)
for load in time_series_data:
    load_frequency[load] += 1

# Compute peak operational load
peak_load = max(base_loads_filtered)

# Print final result
print(f"Result: {peak_load}")