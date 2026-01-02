from itertools import compress

# Sensor readings with some noise
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.0, 24.3, 23.9, 25.1]

# Identify valid readings (within normal operating range)
is_valid = [(23.0 <= temp <= 25.5) for temp in temperature_readings]

# Extract only valid sensor data
filtered_data = list(compress(temperature_readings, is_valid))

# Apply calibration offset using lambda
calibrate = lambda x: round(x + 0.2, 1)
filtered_data = list(map(calibrate, filtered_data))

# Calculate total of calibrated valid readings
filtered_sum = sum(filtered_data)

# Irrelevant string processing (minor distraction)
diagnostic_msg = "System OK"
diagnostic_status = diagnostic_msg.lower().replace(" ", "_")

print(f"Result: {filtered_sum}")