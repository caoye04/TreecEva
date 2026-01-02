from collections import defaultdict

# Simulate daily system load (in percentage) over a week
daily_loads = [85, 92, 78, 96, 88, 94, 91]

# Threshold for acceptable load
capacity_threshold = 80

# Irrelevant distractor: tracking days by category
day_category = defaultdict(str)
for i in range(7):
    day_category[i] = "weekday" if i < 5 else "weekend"

# Filter days where system load exceeds threshold
daily_loads_filtered = [load for load in daily_loads if load > capacity_threshold]

# Compute peak capacity from filtered days
peak_capacity = max(daily_loads_filtered)

# Print final result
print(f"Target result: {peak_capacity}")