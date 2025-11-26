sensor_readings = [15.2, 18.7, 22.4, 19.8, 16.5]
calibration_offsets = [-1.3, 0.8, -0.5, 1.2, -0.9]

# Calculate average reading with compensation
compensated_sum = 0
valid_count = 0
temp_storage = []

for idx, (reading, offset) in enumerate(zip(sensor_readings, calibration_offsets)):
    compensated = reading + offset
    temp_storage.append(compensated * 1.1)  # Distractor calculation
    if compensated > 17.0:
        compensated_sum += compensated
        valid_count += 1

# Calculate target value
if valid_count > 0:
    target_value = compensated_sum / valid_count
else:
    target_value = 0.0

# Calculate offset adjustment
offset_adjustment = sum(calibration_offsets[::2]) - sum(calibration_offsets[1::2])
redundant_adjustment = offset_adjustment * 0.75  # Unused distractor

# Final calibration
final_calibration = target_value + offset_adjustment

print(f"Target result: {final_calibration}")