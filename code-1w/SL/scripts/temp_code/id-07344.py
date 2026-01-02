from collections import defaultdict

# Simulate sensor readings over time for energy monitoring
time_series_data = [12, 15, 22, 18, 25, 30, 28, 20, 19, 24]

# Auxiliary variable (irrelevant to final result)
baseline_offset = sum([x * 0.1 for x in time_series_data])

# Count frequency of readings above threshold using defaultdict
counter = defaultdict(int)
for value in time_series_data:
    if value > 20:
        counter['high'] += 1
    else:
        counter['low'] += 1

# Calculate dynamic efficiency based on high-frequency usage patterns
peak_readings = [val for val in time_series_data if val > 20]
efficiency_ratio = len(peak_readings) / len(time_series_data)

# Determine energy threshold using conditional expression
energy_threshold = 100 if efficiency_ratio > 0.5 else 75 + len(counter)

# Print result as required
print(f"Target result: {energy_threshold}")