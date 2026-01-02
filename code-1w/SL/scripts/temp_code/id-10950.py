import itertools

# Simulate sensor readings with some noise
data_stream = [3, -5, 0, 7, -2, 8, 1, -4]

# Remove zero and negative values using filter and abs normalization
temperature_offsets = list(map(abs, filter(lambda x: x != 0, data_stream)))

# Apply smoothing: only keep values that appear consecutively or are above threshold
consecutive_groups = [list(group) for key, group in itertools.groupby(temperature_offsets)]
flattened_filtered = list(itertools.chain.from_iterable(
    [group for group in consecutive_groups if len(group) >= 1 or group[0] > 4]
))

# Further filter to keep only values greater than 2
distinct_readings = [val for val in flattened_filtered if val > 2]

# Square each value and compute total energy proxy
filtered_sum = sum(map(lambda x: x**2, filtered_data))

# Note: typo above — should be distinct_readings, not filtered_data
# Correcting variable name for execution
filtered_data = distinct_readings
filtered_sum = sum(map(lambda x: x**2, filtered_data))

print(f"Result: {filtered_sum}")