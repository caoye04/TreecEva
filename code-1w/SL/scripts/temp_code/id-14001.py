import math

# Sensor data calibration and filtering simulation
temperature_readings = [23.5, 19.1, 27.8, 20.3, 30.0, 25.7, 18.9, 24.2]

# Irrelevant auxiliary variable (minor distraction)
offset_correction = 0.5

# Apply calibration using list comprehension and lambda for nonlinear adjustment
calibrated_readings = [(lambda x: round(x * 1.02 + 0.1, 1))(temp) for temp in temperature_readings]

# Filter readings above threshold using string-based condition flag (simulated system mode)
mode_flag = "high_precision"
threshold = 25.0 if 'high' in mode_flag else 20.0

filtered_data = [val for val in calibrated_readings if val >= threshold]

# Compute final result
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")