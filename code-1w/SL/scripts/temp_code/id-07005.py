from collections import Counter

# Simulate sensor readings over time (e.g., temperature fluctuations)
readings = [23, 25, 23, 27, 25, 28, 25, 23, 24, 27, 25, 26, 25, 24, 23]

# Filter out values below threshold (noise reduction)
filtered_readings = [temp for temp in readings if temp >= 24]

# Count frequency of each reading
frequency_count = Counter(filtered_readings)

# Identify the highest occurrence count
peak_frequency = max(frequency_count.values())

print(f"Result: {peak_frequency}")