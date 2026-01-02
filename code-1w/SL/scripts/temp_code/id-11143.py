from itertools import groupby

# Simulate sensor readings over time (sorted by value)
sensor_readings = [10, 10, 10, 15, 15, 20, 20, 20, 20, 25, 30, 30, 30]

# Group consecutive identical readings and count occurrences
grouped = [(k, len(list(g))) for k, g in groupby(sensor_readings)]

# Create frequency map from groups
frequency_map = {key: count for key, count in grouped}

# Identify the most frequent reading value
peak_frequency = max(frequency_map.values())

# Print result
print(f"Target result: {peak_frequency}")