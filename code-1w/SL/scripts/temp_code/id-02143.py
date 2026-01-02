from itertools import compress

# Simulated sensor readings for system load over a week
daily_loads = [87.3, 91.2, 88.7, 94.1, 89.5, 96.8, 92.4]
threshold = 90.0

# Identify days where load exceeds threshold
elevated_days = [load > threshold for load in daily_loads]

# Filter loads to only include elevated days
daily_loads_filtered = list(compress(daily_loads, elevated_days))

# Calculate average and peak capacity from filtered data
avg_load = sum(daily_loads_filtered) / len(daily_loads_filtered)
peak_capacity = max(daily_loads_filtered)

# Print final result
print(f"Target result: {peak_capacity}")