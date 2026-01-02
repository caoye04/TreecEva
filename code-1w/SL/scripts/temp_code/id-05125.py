from itertools import compress

# Simulate sensor readings with some noise
timestamps = list(range(10))
raw_readings = [2.1, 3.5, -1.2, 4.8, 0.0, 5.2, -2.3, 6.1, 3.9, 4.4]

# Normalize readings and create mask for valid data (above threshold and not negative)
normalized = list(map(lambda x: round(x, 1), raw_readings))
valid_mask = [val > 3.0 and val >= 0 for val in normalized]

# Extract valid readings using compress
clean_readings = list(compress(normalized, valid_mask))

# Apply scaling only to values below 5.0
scaled_values = [v * 1.2 if v < 5.0 else v for v in clean_readings]

# Filter out any values that are now greater than 5.5
filtered_values = [v for v in scaled_values if v <= 5.5]
filtered_sum = sum(filtered_values)
print(f"Result: {filtered_sum}")