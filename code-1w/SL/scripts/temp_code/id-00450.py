sensor_offsets = [2, -1, 3, 0, 1]
base_temperatures = [25, 30, 35, 40, 45]

# Apply offsets to raw sensor data
calibrated_readings = [base_temperatures[i] + sensor_offsets[i] for i in range(len(base_temperatures))]

# Filter out any readings below 25 degrees
elevated_readings = [temp for temp in calibrated_readings if temp >= 25]

# Adjust by squaring values for non-linear response correction
adjusted_readings = [temp ** 2 for temp in elevated_readings]

# Final processing step: take square root of last adjusted reading
final_temperature = adjusted_readings[-1] ** 0.5

print(f"Result: {final_temperature}")