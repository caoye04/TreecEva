from collections import defaultdict

# Simulate server load monitoring over a week
daily_loads = [120, 150, 135, 167, 142, 189, 134, 178, 165, 141]
threshold = 130

# Filter days where load exceeds threshold
high_load_days = defaultdict(int)
for i, load in enumerate(daily_loads):
    if load > threshold:
        high_load_days[f'Day_{i}'] = load

# Analyze recent trend using slicing: last 6 high-load observations
daily_loads_sliced = list(high_load_days.values())[-6:]

# Calculate peak capacity in recent period
peak_capacity = max(daily_loads_sliced)

# Irrelevant auxiliary calculation (minor distraction)
total_capacity = sum(daily_loads_sliced)

Result: peak_capacity