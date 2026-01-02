from collections import Counter

# Simulate sensor readings over time (e.g., temperature fluctuations)
sensor_readings = [23, 25, 23, 27, 25, 23, 29, 27, 25, 25, 30, 27, 23]

# Count frequency of each reading
frequency_count = Counter(sensor_readings)

# Identify the highest occurrence count
peak_frequency = max(frequency_count.values())

# Irrelevant auxiliary variable (minimal distraction)
total_observations = len(sensor_readings)

# Output result
print(f"Result: {peak_frequency}")