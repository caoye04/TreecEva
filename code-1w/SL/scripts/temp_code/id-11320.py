from collections import Counter

# Simulate sensor readings over time (e.g., temperature fluctuations)
sensor_readings = [23, 25, 23, 27, 25, 28, 25, 23, 27, 26, 25, 24, 23, 27, 25]

# Count frequency of each reading
frequency_counter = Counter(sensor_readings)

# Identify the most frequent sensor value (mode)
peak_frequency = max(frequency_counter.values())

# Output result
print(f"Result: {peak_frequency}")