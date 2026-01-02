from itertools import compress

# Simulate sensor readings with timestamps
timestamps = list(range(10, 100, 3))
sensor_readings = [t * 0.3 + ((t ^ 15) & 7) for t in timestamps]

# Identify valid readings: above baseline and occurring at even-indexed positions
even_index_mask = [(i % 2 == 0) for i in range(len(sensor_readings))]
baseline_filter = [(x > 20) for x in sensor_readings]
valid_readings = list(compress(sensor_readings, [a and b for a, b in zip(even_index_mask, baseline_filter)]))

# Process only the first half of valid readings using slicing
midpoint = len(valid_readings) // 2
sliced_data = valid_readings[:midpoint] if midpoint > 0 else [0]

# Final computation step
delta = sensor_readings[5] - sensor_readings[2]
scaling_factor = 1.0  # Placeholder for potential calibration
filtered_sum = sum(sliced_data)
print(f"Result: {filtered_sum}")