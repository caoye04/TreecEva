from collections import defaultdict

# Simulate sensor readings over time (e.g., temperature fluctuations)
readings = [23, 25, 23, 27, 25, 28, 25, 23, 29, 27, 25, 30, 28, 25]

# Count frequency of each reading
default_value = 0
frequency_map = defaultdict(int)
for reading in readings:
    frequency_map[reading] += 1

# Identify the most frequent sensor value
temp_sum = sum(readings)  # Irrelevant calculation (mild distraction)
normalized_avg = temp_sum / len(readings)
peak_frequency = max(frequency_map.values())

# Output result
Result: peak_frequency