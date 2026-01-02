from collections import Counter

# Simulate sensor readings over time (e.g., temperature in tenths of °C)
sensor_readings = [234, 239, 241, 234, 230, 239, 234, 245, 241, 234]

# Count frequency of each reading
frequency_count = Counter(sensor_readings)

# Track derived metrics for system health
average_reading = sum(sensor_readings) / len(sensor_readings)
deviation_sum = sum(abs(x - average_reading) for x in sensor_readings)

# Identify the most frequent sensor value (potential thermal steady-state)
peak_frequency = max(frequency_count.values())

# Normalize deviation (irrelevant to peak_frequency but adds context)
normalized_deviation = deviation_sum / len(sensor_readings)

# Output target result
print(f"Result: {peak_frequency}")