from itertools import compress

# Sensor data readings in mV, some corrupted (negative values)
sensor_readings = [1.2, -0.5, 2.3, -1.0, 4.5, 3.1, -0.2, 5.6]

# Validity mask: only non-negative readings are valid
valid_mask = [x >= 0 for x in sensor_readings]

# Extract valid readings using itertools.compress
filtered_data = list(compress(sensor_readings, valid_mask))

# Apply calibration factor using lambda
calibrate = lambda x: round(x * 1.08, 2)  # 8% signal amplification correction
filtered_data = [calibrate(x) for x in filtered_data]

# Remove duplicates while preserving order via dict trick
data_no_duplicates = list(dict.fromkeys(filtered_data))

# Final result: sum of cleaned and calibrated data
result = sum(data_no_duplicates)

print(f"Result: {result}")