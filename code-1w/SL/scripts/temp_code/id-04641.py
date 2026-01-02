def analyze_sensor_array(raw_readings, threshold=0.75, mode='strict'):
    # Irrelevant preprocessing: string-based metadata parsing (distractor)
    sensor_metadata = 'SN1234_TEMP|LOC_A|CALIB_2023'
    segments = sensor_metadata.split('|')
    calibration_year = int(segments[2].split('_')[1])
    location_code = segments[1].split('_')[1]

    # Decoy data transformation (dead path)
    temp_offset = 0.0
    if location_code == 'X':
        temp_offset = -2.5
    elif location_code == 'Y':
        temp_offset = 1.8

    # Real signal processing begins
    normalized = [x / max(raw_readings) for x in raw_readings]
    above_threshold = [i for i, val in enumerate(normalized) if val >= threshold]

    # Bit manipulation red herring (irrelevant to final result)
    bit_signature = 0
    for idx in above_threshold:
        bit_signature ^= (idx << 2) | 1

    # String method distraction: encoding index positions as hex strings
    encoded_indices = [hex(i)[2:].zfill(2) for i in above_threshold]
    valid_hex = [h for h in encoded_indices if h.startswith('a') or h.endswith('f')]

    # Actual filtering logic (core path)
    filtered_data = [raw_readings[i] for i in above_threshold]

    # Multiple assignment distractor
    (backup_mode, debug_level, _ignored) = (False, 3, 'unused_flag')

    # Complex nested function with closure (misleading recursion)
    def generate_corrector(factor):
        def correct(val):
            return val * (1 + factor / 100) if val > 0 else val
        return correct

    correction_applier = generate_corrector(2.0)  # Unused later

    # Spurious list transformations using zip and enumerate (distractor)
    paired_deltas = []
    for i, (a, b) in enumerate(zip(normalized, normalized[1:])):
        change = round(b - a, 6)
        if abs(change) > 0.1:
            paired_deltas.append((i, change))

    # Dummy statistical decoy
    mean_deviation = sum(abs(d[1]) for d in paired_deltas) / len(paired_deltas) if paired_deltas else 0.0

    # Conditional early exit red herring (never triggered due to data)
    if mode == 'debug' and debug_level > 5:
        return -999  # dead code

    # Core processing hidden among distractions
    calibration_factor = (calibration_year % 100) * 0.01  # evaluates to 0.23

    def process_readings(data, calib):
        if not data:
            return 0.0
        adjusted = [x * (1 + calib) for x in data]
        squared_sum = sum(x ** 2 for x in adjusted)
        root_mean_sq = (squared_sum / len(adjusted)) ** 0.5
        return round(root_mean_sq, 6)

    # Key execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)

    # Final decoy: unused bitwise aggregation
    aggregate_flag = 0
    for val in filtered_data:
        aggregate_flag |= int(val) & 7

    # Output required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data crafted to yield deterministic outcome
sensor_input = [18.4, 22.1, 9.3, 27.6, 14.8, 31.9, 8.2, 25.3]
analyze_sensor_array(sensor_input)