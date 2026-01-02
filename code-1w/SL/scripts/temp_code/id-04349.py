from itertools import compress

# Simulate sensor readings with some noise
timestamps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
raw_readings = [23.1, 24.5, 19.8, 22.0, 25.3, 20.1, 21.4, 26.8, 23.9, 24.2]

# Normalize readings to baseline (22.0)
normalized_readings = [round(x - 22.0, 1) for x in raw_readings]

# Identify valid readings: within ±3.0 of baseline
clean_mask = [abs(val) <= 3.0 for val in normalized_readings]

# Extract clean readings using compress
filtered_values = list(compress(normalized_readings, clean_mask))

# Compute total of filtered values
filtered_sum = sum(filtered_values)

# Irrelevant auxiliary variable (minor distraction)
max_normalized = max(normalized_readings)

# Output result
print(f"Result: {filtered_sum}")