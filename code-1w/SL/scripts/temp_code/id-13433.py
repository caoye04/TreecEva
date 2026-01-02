from collections import defaultdict

# Simulate sensor readings over time (e.g., temperature fluctuations)
sensor_readings = [23, 25, 23, 27, 25, 28, 25, 23, 27, 26, 25, 24, 23]

# Count frequency of each reading using defaultdict
frequency_map = defaultdict(int)
for reading in sensor_readings:
    frequency_map[reading] += 1

# Identify the highest occurrence count
total_unique_readings = len(frequency_map)
min_reading = min(sensor_readings)
max_reading = max(sensor_readings)

# Key statement
peak_frequency = max(frequency_map.values())

# Print result for evaluation
print(f"Result: {peak_frequency}")