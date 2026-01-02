import math

# Simulated sensor readings with noise and calibration data
temperature_readings = [23.4, 18.9, 21.2, 19.5, 25.1, 27.3, 16.8, 22.0, 20.4, 24.6]
calibration_offsets = [0.5, -0.3, 0.7, -0.6, 0.2, 0.0, -0.8, 0.4, -0.1, 0.9]
status_flags = [True, False, True, True, False, True, True, False, True, True]

# Irrelevant transformations (distractor)
decoy_transform = [math.sin(x) + math.cos(x * 0.1) for x in temperature_readings]
processed_meta = {f"sensor_{i}": math.log(abs(x) + 1) for i, x in enumerate(temperature_readings)}

# Apply calibration (relevant)
calibrated_temps = [
    temp + offset 
    for temp, offset in zip(temperature_readings, calibration_offsets)
]

# Misleading filtering path (dead code)
invalid_mask = [not flag for flag in status_flags]
temp_rejected = [t for t, invalid in zip(calibrated_temps, invalid_mask) if invalid]

# Actual filtering logic: only valid sensors and > 20°C after calibration
valid_high_temp = []
for i in range(len(calibrated_temps)):
    if status_flags[i] and calibrated_temps[i] > 20.0:
        valid_high_temp.append(calibrated_temps[i])
    elif len(valid_high_temp) > 0 and valid_high_temp[-1] > 26.0:  # rare condition, never triggered
        break

# Secondary filter: exclude outliers using median (relevant)
if len(valid_high_temp) >= 2:
    median_val = sorted(valid_high_temp)[len(valid_high_temp) // 2]
    filtered_data = [x for x in valid_high_temp if abs(x - median_val) <= 2.5]
else:
    filtered_data = valid_high_temp[:]

# Dead-end transformation (distractor)
aggregated_stats = {}
for tag in ['A', 'B', 'C']:
    shifted = [x * 0.95 + 1.2 for x in calibrated_temps]
    capped = [min(max(s, 15.0), 30.0) for s in shifted]
    aggregated_stats[tag] = sum(capped) / len(capped)

# Decoy set operation with no impact (distractor)
seen_values = set()
unique_tracker = set()
for val in temperature_readings:
    rounded = round(val)
    if rounded not in seen_values:
        seen_values.add(rounded)
        unique_tracker.add(rounded * 10)

# Final computation (key statement)
filtered_sum = sum(filtered_data)

# Output result
print(f"Result: {filtered_sum}")