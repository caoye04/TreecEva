from itertools import compress

# Sensor data calibration and noise filtering
defect_flags = [False, True, False, False, True]
raw_readings = [105.2, 98.7, 102.3, 99.8, 101.0]
bias_correction = [0.8, -1.2, 0.5, 0.3, -0.9]

# Apply bias correction to raw sensor readings
calibrated_values = [raw_readings[i] + bias_correction[i] for i in range(len(raw_readings))]

# Filter out defective sensor readings
good_readings = list(compress(calibrated_values, [not x for x in defect_flags]))

# Normalize readings relative to mean before weighting
mean_value = sum(good_readings) / len(good_readings)
normalized_deviation = [abs(val - mean_value) for val in good_readings]

# Assign dynamic weights based on deviation from mean
base_weights = [1.0 - min(dev/10, 0.3) for dev in normalized_deviation]
adjusted_weights = [w * 1.1 for w in base_weights]  # Systematic gain adjustment

total_weight = sum(adjusted_weights)
print(f"Result: {total_weight}")