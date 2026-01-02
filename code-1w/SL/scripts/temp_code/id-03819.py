from collections import defaultdict

# Simulate a sequence of sensor readings (e.g., temperature fluctuations)
readings = [23, 24, 25, 23, 24, 23, 26, 25, 24, 24, 27, 26, 24, 23, 24]

# Count frequency of each reading using defaultdict
default_val = 0
frequency_map = defaultdict(lambda: default_val)

for reading in readings:
    frequency_map[reading] += 1

# Identify the highest occurrence count
peak_frequency = max(frequency_map.values())

# Print result for verification
print(f"Result: {peak_frequency}")