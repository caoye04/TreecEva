from collections import Counter

# Simulate sensor readings over time (e.g., temperature in tenths of °C)
sensor_readings = [215, 220, 215, 225, 230, 225, 215, 240, 230, 225, 220, 215]

# Count frequency of each reading
frequency_map = Counter(sensor_readings)

# Track total number of unique readings (irrelevant distractor for intervention)
unique_count = len(frequency_map)

# Calculate average reading (additional context, not directly needed)
mean_value = sum(sensor_readings) / len(sensor_readings)

# Find the highest frequency of any single reading
peak_frequency = max(frequency_map.values())

# Output result
print(f"Result: {peak_frequency}")