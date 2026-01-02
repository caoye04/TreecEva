from itertools import compress

# Simulate sensor readings with some invalid data points
temperature_readings = [23.5, 19.0, 27.3, 18.1, 30.2, 25.0, 17.9, 22.1]
valid_flags = [temp > 18.0 and temp < 28.0 for temp in temperature_readings]

# Extract only valid temperature readings using itertools.compress
valid_entries = list(compress(temperature_readings, valid_flags))

# Sort the valid entries to prepare for analysis
sorted_valid = sorted(valid_entries)

# Calculate summary statistics
count_valid = len(sorted_valid)
avg_valid = sum(sorted_valid) / count_valid if count_valid > 0 else 0.0

# Key computation: sum of filtered valid entries
filtered_sum = sum(valid_entries)

# Print result for verification
print(f"Result: {filtered_sum}")