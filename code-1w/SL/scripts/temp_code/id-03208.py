from itertools import combinations

# Sensor data validation and fusion system
sensor_a_readings = {9, 15, 21, 33, 39, 45}
sensor_b_readings = {21, 33, 45, 51, 57}
baseline_thresholds = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45}

# Extract valid synchronized measurements present in both sensors and above baseline
common_readings = sensor_a_readings & sensor_b_readings
valid_common = common_readings.intersection(baseline_thresholds)

# Compute sum of valid intersecting readings
intersection_sum = sum(valid_common)

dummy_counter = 0
for pair in combinations(valid_common, 2):
    dummy_counter += 1  # Irrelevant operation: counts all 2-element combinations

scaling_factor = 2.5
result = intersection_sum * scaling_factor

print(f"Result: {result}")