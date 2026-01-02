from itertools import compress

# Simulate sensor readings with some noise
data_readings = [102, 105, 98, 103, 107, 95, 100, 108, 99, 104]

# Threshold filter: only values within normal operating range (100-106)
valid_range = [(100 <= x <= 106) for x in data_readings]

# Use itertools.compress to extract only valid readings
filtered_values = list(compress(data_readings, valid_range))

# Further refine: exclude any value immediately following a filtered-out value
if len(filtered_values) > 1:
    refined_mask = [True] + [filtered_values[i] - filtered_values[i-1] < 10 for i in range(1, len(filtered_values))]
    filtered_values = [v for i, v in enumerate(filtered_values) if refined_mask[i]]

# Compute final sum of cleaned data
filtered_sum = sum(filtered_values)

# Irrelevant auxiliary variable (minor distraction)
dummy_avg = sum(data_readings) / len(data_readings) if data_readings else 0

print(f"Result: {filtered_sum}")