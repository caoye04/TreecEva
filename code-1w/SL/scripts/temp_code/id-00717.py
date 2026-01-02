from collections import Counter

# Simulate daily server load (in requests per second) over a workweek
daily_loads = [120, 150, 135, 160, 142]

# Calculate average load
avg_load = sum(daily_loads) / len(daily_loads)

# Identify peak load during the week
peak_load = max(daily_loads)

# Extra: Count frequency of rounded tens digit
load_tens = [x // 10 for x in daily_loads]
tens_counter = Counter(load_tens)

# Secondary metric: variability index
variability_index = (max(daily_loads) - min(daily_loads)) / avg_load

# Print final result
print(f"Result: {peak_load}")