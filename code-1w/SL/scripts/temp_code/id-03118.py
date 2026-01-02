from itertools import compress

# Simulate daily system load measurements over a week
base_loads = [120, 135, 160, 145, 170, 185, 150]
drift_compensation = 5

# Apply time-based decay correction to earlier readings
corrected_loads = [load - (drift_compensation * i) for i, load in enumerate(base_loads)]

# Identify days with high volatility (above 140 after correction)
high_load_threshold = 140
is_high_load_day = [load > high_load_threshold for load in corrected_loads]

# Filter valid high-load days using compress
daily_loads_filtered = list(compress(corrected_loads, is_high_load_day))

# Calculate peak operational capacity during high-usage days
peak_capacity = max(daily_loads_filtered)

# Irrelevant metric (distractor)
avg_load = sum(corrected_loads) / len(corrected_loads)

print(f"Result: {peak_capacity}")