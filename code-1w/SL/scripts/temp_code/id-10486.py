from itertools import compress

# Sensor data validation and correction pipeline
timestamps = [1001, 1002, 1003, 1004, 1005, 1006]
sensor_readings = [23.7, 19.5, 25.1, 18.3, 24.9, 20.2]
validity_flags = [True, False, True, True, False, True]

deviation_from_mean = [abs(r - sum(sensor_readings) / len(sensor_readings)) for r in sensor_readings]
outlier_threshold = 2.0

# Identify non-outliers based on deviation
is_not_outlier = [dev < outlier_threshold for dev in deviation_from_mean]

# Combine validity and outlier filters
final_mask = [valid and not_outlier for valid, not_outlier in zip(validity_flags, is_not_outlier)]

cleaned_readings = list(compress(sensor_readings, final_mask))
filtered_sum = sum(cleaned_readings)
correction_factor = 1.05
result = filtered_sum * correction_factor

print(f"Result: {result}")