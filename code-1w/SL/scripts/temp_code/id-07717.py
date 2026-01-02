def analyze_sensor_stream(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize timestamps (not used in final result)
    timestamps = [r[0] for r in raw_readings]
    avg_time = sum(timestamps) / len(timestamps)
    normalized_times = [(t - avg_time) * 1.5 for t in timestamps]

    # Relevant data extraction: extract sensor values and types
    sensor_values = [r[1] for r in raw_readings]
    sensor_types = [r[2] for r in raw_readings]

    # Distractor: complex but unused frequency analysis
    freq_analysis = {}
    for s_type in set(sensor_types):
        counts = sensor_types.count(s_type)
        freq_analysis[s_type] = counts / len(sensor_types)

    # Misleading intermediate transformation (looks important but unused)
    transformed = []
    for i, val in enumerate(sensor_values):
        if i % 2 == 0:
            transformed.append(val ** 0.5 * calibration_factor)
        else:
            transformed.append(val / (calibration_factor + 1))

    # Actual relevant logic begins: filter valid numeric readings
    valid_entries = []
    for val, s_type in zip(sensor_values, sensor_types):
        if isinstance(val, (int, float)) and val > 0 and s_type in ['TEMP', 'PRES']:
            valid_entries.append((val, s_type))

    # Slicing to take only middle portion (critical step)
    mid_index = len(valid_entries) // 3
    filtered_data = valid_entries[mid_index:2*mid_index + 1]

    # Build threshold map based on enumerated positions (correct path)
    base_thresholds = [12.5, 18.9, 22.1]
    threshold_map = {i+1: base_thresholds[i % 3] for i in range(3)}

    # Dead code path: complex dictionary transformation (unused)
    decoy_map = {}
    for idx, (value, stype) in enumerate(valid_entries):
        key = f'{stype}_{idx*2}X'
        decoy_map[key] = value * (idx + 1) // (idx + 1)

    # Conditional override that never triggers (red herring)
    if len(decoy_map) > 100:
        threshold_map = {k: v * 0.1 for k, v in threshold_map.items()}

    # Critical function call (answer depends on this)
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic


def process_readings(data, thresholds):
    accumulator = 0
    type_weights = {'TEMP': 3, 'PRES': 5}
    for reading, r_type in data:
        # Bit manipulation as part of calculation
        weighted_val = (reading * type_weights[r_type]) ^ 7
        if r_type == 'TEMP':
            bound = thresholds[1] if reading < thresholds[2] else thresholds[3]
            if reading < bound:
                accumulator += int(weighted_val / 2)
            else:
                accumulator -= int(weighted_val / 4)
        elif r_type == 'PRES':
            accumulator += int(weighted_val % thresholds[1])
    # Final adjustment using logical operations
    flag = len(data) > 0 and all(r[0] > 0 for r in data)
    accumulator = accumulator + 5 if flag else accumulator - 5
    return accumulator

# Simulated input data
readings = [
    (1623456000, 25.3, 'TEMP'),
    (1623456060, 101.8, 'PRES'),
    (1623456120, 18.9, 'TEMP'),
    (1623456180, 98.4, 'PRES'),
    (1623456240, 22.1, 'TEMP'),
    (1623456300, -5.2, 'TEMP'),  # invalid due to negative
    (1623456360, 103.1, 'PRES'),
    (1623456420, 26.7, 'TEMP'),
    (1623456480, 0.0, 'TEMP'),   # invalid due to zero
    (1623456540, 99.3, 'PRES')
]

calibration = 1.7

# Entry point
result = analyze_sensor_stream(readings, calibration)
final_diagnostic = result
print(f'Result: {final_diagnostic}')