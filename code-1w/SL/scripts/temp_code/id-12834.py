def analyze_sensor_data(raw_readings, calibration_sequence):
    aggregate_score = 0
    temp_buffer = []
    offset_map = {i: val % 7 for i, val in enumerate(calibration_sequence)}
    
    # Irrelevant transformation - dead path
    shadow_copy = [x * 2 for x in raw_readings if x < 500]
    decoy_sum = sum(shadow_copy) // 3 if len(shadow_copy) > 5 else 0
    scaling_factor = 0  # Unused variable (red herring)

    for idx, reading in enumerate(raw_readings):
        if idx % 2 == 0 and reading > 100:
            transformed = (reading ^ idx) & 15
            temp_buffer.append(transformed)
        else:
            adjusted = reading // 3 + (idx | 4)
            temp_buffer.append(adjusted % 25)

    # Misleading intermediate aggregation
    phantom_metric = sum(temp_buffer[i] * 2 for i in range(0, len(temp_buffer), 3))
    phantom_metric = phantom_metric // 2 if phantom_metric > 100 else phantom_metric * 3

    # Real computation begins
    base_accumulator = 0
    for i, val in enumerate(temp_buffer):
        if i in offset_map:
            base_accumulator += val ^ offset_map[i]
        else:
            base_accumulator += val % 9

    # Conditional expression with distractor variables
    correction_factor = len([x for x in temp_buffer if x > 10]) if base_accumulator > 50 else len(temp_buffer) // 2
    
    # String manipulation red herring
    status_log = "SensorOK" * len(raw_readings)
    char_count = {c: status_log.count(c) for c in set(status_log)}
    decoy_threshold = char_count['O'] + char_count['K']  # Unused

    # Key assignment statement
    final_diagnostic = base_accumulator + correction_factor

    # Multiple data structures with cross-reference (distractor)
    audit_trail = dict(zip(range(len(temp_buffer)), temp_buffer))
    validation_check = all(audit_trail[k] >= v for k, v in offset_map.items())  # Not used

    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Inputs
sensor_input = [120, 85, 200, 95, 300, 415, 180, 75]
calib_seq = [14, 28, 42, 56, 70]

result = analyze_sensor_data(sensor_input, calib_seq)