from itertools import compress

# Simulate sensor readings with timestamps
timestamps = list(range(100, 200, 2))
sensor_readings = [t * 0.3 + ((t % 7) ** 1.5) for t in timestamps]

# Identify valid windows where readings are within normal bounds (15.0 to 25.0)
normal_range_mask = [(15.0 <= val <= 25.0) for val in sensor_readings]

# Use compress to extract only readings in normal range
filtered_data = list(compress(sensor_readings, normal_range_mask))

# Apply post-processing: remove first and last 2 elements as buffer zones
trimmed_data = filtered_data[2:-2]

# Calculate final result on trimmed dataset
filtered_sum = sum(trimmed_data)

# Print result for verification
print(f"Result: {filtered_sum}")