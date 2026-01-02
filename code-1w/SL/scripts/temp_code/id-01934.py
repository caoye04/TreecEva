from itertools import compress

# Sensor readings from environmental monitoring stations
candidate_readings = [1024, 987, 1003, 995, 1012, 976, 1008]
quality_flags = [True, False, True, True, False, True, True]

# Filter valid readings using quality control mask
filtered_readings = list(compress(candidate_readings, quality_flags))

# Apply calibration adjustment for temperature drift
calibrated_readings = [r * 0.98 + 5 for r in filtered_readings]

# Compute derived metrics
computed_readings = []
for value in calibrated_readings:
    if value > 1000:
        computed_readings.append(value * 1.02)
    else:
        computed_readings.append(value * 0.99)

total_pressure = sum(computed_readings)
print(f"Result: {total_pressure}")