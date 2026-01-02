import itertools

# Simulate sensor readings with noise
temperature_readings = [23.5, 24.1, 19.8, 22.7, 25.3]
offset = 1.2
scale_factor = 3

# Apply calibration offset and filter anomalies below threshold
calibrated_readings = [(temp + offset) for temp in temperature_readings if temp > 20]

# Use itertools.chain to flatten hypothetical multi-sensor array (simulated)
sensor_grid = [calibrated_readings, [26.0 + offset]]
flattened_temps = list(itertools.chain.from_iterable(sensor_grid))

# Calculate adjusted sum using only values within normal operating range
adjusted_sum = sum(temp for temp in flattened_temps if 21 <= temp <= 27)

# Final calibrated average temperature
final_temperature = adjusted_sum / scale_factor

print(f"Result: {final_temperature}")