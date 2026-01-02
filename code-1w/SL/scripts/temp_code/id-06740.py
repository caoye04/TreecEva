from itertools import compress

# Sensor data collected over time (in arbitrary units)
sensor_readings = [12, 7, 23, 45, 8, 19, 34, 27, 41, 11, 50, 3]

# Preprocessing: extract every second reading starting from index 1
sliced_data = sensor_readings[1::2]

# Threshold for significant activity
threshold = 20

# Filter values above threshold and compute sum
temp_mask = [x > threshold for x in sliced_data]
filtered_sum = sum(filter(lambda x: x > threshold, sliced_data))

# Irrelevant auxiliary computation (minimal distraction)
dummy_shift = [x << 1 for x in sliced_data if x < 10]

# Output result
print(f"Result: {filtered_sum}")