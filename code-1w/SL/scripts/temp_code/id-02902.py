sensor_readings = [12.5, 8.3, 15.0, 23.1, 7.8]
fallback_value = 10
calibration_factor = 0.9

# Normalize readings
calibrated_readings = [r * calibration_factor for r in sensor_readings]

# Identify safe operational levels above threshold
safe_levels = [cr for cr in calibrated_readings if cr > 10]

# Determine final energy threshold based on safety check
energy_threshold = min(safe_levels) if all(reading > 0 for reading in sensor_readings) else fallback_value

Result: energy_threshold