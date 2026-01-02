from itertools import compress

# Simulated daily system load (in percentage) over a week
daily_loads = [78, 92, 85, 96, 77, 88, 91]

# Threshold for high-load days
threshold = 85

# Identify days where load exceeded threshold
days_exceeding_threshold = [load > threshold for load in daily_loads]

# Extract high-load values using compress
daily_loads_filtered = list(compress(daily_loads, days_exceeding_threshold))

# Determine peak capacity required on high-load days
if daily_loads_filtered:
    peak_capacity = max(daily_loads_filtered)
else:
    peak_capacity = 0

# Print final result
print(f"Result: {peak_capacity}")