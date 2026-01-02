from collections import Counter

# Simulate sensor readings over time (in arbitrary units)
sensor_readings = [101, 102, 105, 101, 103, 102, 101, 104, 105, 102, 101, 103, 104, 105]

# Count frequency of each reading
frequency_count = Counter(sensor_readings)

# Find the highest occurrence count
total_unique_readings = len(frequency_count)
min_frequency = min(frequency_count.values())
peak_frequency = max(frequency_count.values())

# Additional derived metric (not directly used)
dominance_ratio = peak_frequency / len(sensor_readings) if sensor_readings else 0.0

# Output the target result
print(f"Result: {peak_frequency}")