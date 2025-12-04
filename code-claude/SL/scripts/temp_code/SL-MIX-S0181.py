# Temperature sensor readings processing

# Original sensor readings in Celsius
sensor_readings = [22.5, 19.8, -5.2, 24.3, 18.5, 100.7, -10.6, 23.1]

# Calibration factor for the sensor
calibration_offset = 0.5

# Apply calibration to all readings
calibrated_readings = [reading + calibration_offset for reading in sensor_readings]

# Filter out invalid readings (below -5°C or above 40°C)
filtered_readings = [reading for reading in calibrated_readings if -5 <= reading <= 40]

# Calculate the sum of valid readings
filtered_sum = sum(filtered_readings)

# Calculate average of valid readings
if len(filtered_readings) > 0:
    average_temp = filtered_sum / len(filtered_readings)
else:
    average_temp = 0

print(f"Result: {filtered_sum}")