calibration_values = [15, 22, 8, 19, 31]
reference_points = [3, 7, 12, 5, 9]
combined_readings = []
for cal, ref in zip(calibration_values, reference_points):
    measurement = cal - ref
    combined_readings.append(measurement)

final_measurement = 0
for idx, val in enumerate(combined_readings):
    if idx % 2 == 0:
        final_measurement += val
    else:
        final_measurement -= val

print(f"Result: {final_measurement}")