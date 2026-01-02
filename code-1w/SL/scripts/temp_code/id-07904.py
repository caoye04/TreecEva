from itertools import cycle

# Simulate sensor array phase calibration with noise filtering
def calibrate_sensor_phases(readings):
    base_offsets = [15, -7, 22, -13]
    filtered_readings = []
    noise_counter = 0

    for i, val in enumerate(readings):
        if abs(val - round(val)) > 0.1:
            noise_counter += 1
            continue
        if val < -50 or val > 50:
            continue
        filtered_readings.append(int(round(val)))

    # Irrelevant transformation (distractor)
    squared_norms = [x**2 for x in filtered_readings if x > 0]
    avg_square = sum(squared_norms) / len(squared_norms) if squared_norms else 0

    # Core logic: accumulate calibrated phase shifts
    cumulative_rotation = 0
    offset_cycle = cycle(base_offsets)

    for idx, (reading, offset) in enumerate(zip(filtered_readings, offset_cycle)):
        rotated = reading * 3 + offset
        if rotated % 4 == 0:
            cumulative_rotation += rotated // 4
        elif rotated > 0:
            cumulative_rotation += abs(rotated) // 10
        else:
            cumulative_rotation -= abs(rotated) // 20

    # Add dummy influence from average square (has negligible effect)
    cumulative_rotation += int(avg_square // 100)

    # Key execution point
    final_adjustment = cumulative_rotation % 360
    net_phase_shift = final_adjustment if final_adjustment >= 0 else final_adjustment + 360

    # Dead code path (red herring)
    if net_phase_shift == 0:
        backup_modes = [180, 90, -90]
        net_phase_shift = backup_modes[1]

    return net_phase_shift

# Input data sequence
data_stream = [12.1, 7.0, -3.0, 44.9, 100, -8.0, 15.0, 2.5, -22.0]

result = calibrate_sensor_phases(data_stream)
print(f"Result: {result}")