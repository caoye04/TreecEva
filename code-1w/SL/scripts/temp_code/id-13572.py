from itertools import compress

# Simulate sensor readings with some noise
timestamps = [100, 101, 102, 103, 104, 105]
sensor_values = [0.8, 1.2, 0.9, 1.5, 1.1, 0.7]
threshold_mask = [x >= 1.0 for x in sensor_values]

# Extract high-confidence readings
clean_readings = list(compress(sensor_values, threshold_mask))

# Apply calibration factor and round to 2 decimal places
calibrated_readings = [round(x * 0.95, 2) for x in clean_readings]

# Unrelated utility variable (minor distraction)
status_message = "Processing complete"

# Main computation chain
delta = timestamps[-1] - timestamps[0]
scale_factor = delta / len(clean_readings)
adjusted_readings = [x * scale_factor for x in calibrated_readings]
processed_data = [int(x * 10) / 10 for x in adjusted_readings]  # Truncate to 1 decimal
result = sum(processed_data)
print(f"Result: {result}")