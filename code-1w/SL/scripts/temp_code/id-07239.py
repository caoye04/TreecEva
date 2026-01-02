def analyze_sensor_data(raw_readings):
    # Irrelevant preprocessing: string cleaning (distractor)
    formatted_logs = [log.strip().upper() for log in raw_readings if isinstance(log, str)]
    valid_count = len([x for x in raw_readings if isinstance(x, (int, float)) and x > 0])

    # Real data path: extract numeric sensor values
    sensor_values = [x for x in raw_readings if type(x) in (int, float)]

    # Bit manipulation on sensor ID (relevant but obscured)
    sensor_id = 0b1101101
    parity_check = bin(sensor_id).count('1') % 2
    calibration_offset = sensor_id ^ 0b1011001  # XOR-based calibration

    # Data transformation with set operations (required feature)
    baseline_set = {1, 2, 4, 8, 16, 32}
    observed_set = {int(abs(x)) for x in sensor_values if x < 100}
    overlap = baseline_set & observed_set  # Intersection
    enhancement_factor = len(overlap) ** 2 if overlap else 0

    # Complex conditional aggregation
    aggregate_score = 0
    for val in sensor_values:
        if val == 0:
            continue
        elif val < 0:
            aggregate_score -= int(abs(val) ** 0.5)
        else:
            if val % 2 == 0:
                aggregate_score += val // 3
            else:
                aggregate_score += val % 7

    # Decoy computation path (dead code - never executed)
    def legacy_compatibility_mode():
        return sum([x * 2 for x in sensor_values]) // len(sensor_values)

    # Dictionary-based state tracking (relevant)
    status_registry = {
        'active': True,
        'mode_flag': parity_check == 1,
        'timestamp': '2023-09-15',
        'version': '2.1.0'
    }

    # Conditional logic with short-circuiting (required paradigm)
    if status_registry['active'] and status_registry['mode_flag'] or enhancement_factor > 5:
        adjustment = enhancement_factor * 3
    else:
        adjustment = -1

    # Secondary irrelevant calculation (misleading intermediate)
    average_magnitude = sum(abs(x) for x in sensor_values) / len(sensor_values) if sensor_values else 0
    normalized_avg = round(average_magnitude, 2)

    # Key logic chain involving multiple concepts
    temp_buffer = []
    for i, v in enumerate(sensor_values):
        shifted = v >> 1  # Bit shift
        if i % 2 == 0:
            temp_buffer.append(shifted + calibration_offset)
        else:
            temp_buffer.append(shifted - len(formatted_logs))  # Uses distractor

    # Another red herring: unused dictionary transformation
    metadata_summary = {
        'entries': len(raw_readings),
        'strings': len(formatted_logs),
        'numbers': len(sensor_values),
        'diagnostics': {k: bool(v) for k, v in status_registry.items() if isinstance(v, (bool, int))}
    }

    # Core answer computation (buried in logic)
    correction_factor = adjustment + (calibration_offset & 0b111)  # Bitwise AND
    final_diagnostic = aggregate_score + correction_factor

    # Final red herring: string method chain with no effect
    diagnostic_tag = 'SensorDiagnostic'.lower().replace('s', 'X').title()

    return final_diagnostic

# Input data with mixed types (realistic scenario)
sensor_input = [
    '  log_entry_01  ', 8, -27, 16, 42, 'ERROR',
    7, -64, 3.14, 128, 9, 'retry', 0, -49
]

result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")