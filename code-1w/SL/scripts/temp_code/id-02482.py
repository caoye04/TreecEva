from collections import Counter

# Simulate sensor readings over time (e.g., temperature in Celsius)
sensor_readings = [23, 25, 24, 23, 26, 25, 25, 24, 27, 23, 26, 25, 28, 24, 23]

# Count frequency of each reading
frequency_counter = Counter(sensor_readings)

# Identify the highest occurrence count
peak_frequency = max(frequency_counter.values())

# Output result
print(f"Result: {peak_frequency}")