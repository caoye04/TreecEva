def analyze_sensor_data(raw_readings, calibration_log):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in raw_readings if x > 0]
    outliers = [x for x in normalized if x > 95]
    filtered = [x for x in normalized if x <= 95]

    # Key data structures (mixed relevance)
    stats = {
        'count': len(filtered),
        'sum': sum(filtered),
        'max_val': max(filtered),
        'min_val': min(filtered)
    }

    # Decoy statistical analysis (dead path)
    mean_val = stats['sum'] / stats['count']
    variance_proxy = sum((x - mean_val) ** 2 for x in filtered) / stats['count']
    stability_index = 1 / (1 + variance_proxy)  # Not actually used

    # String-based calibration validation (semi-relevant distractor)
    valid_entries = 0
    for entry in calibration_log:
        if 'CAL' in entry and entry.strip().endswith('OK'):
            valid_entries += 1
    compliance_rate = valid_entries / len(calibration_log)

    # Fake reliability adjustment (misleading intermediate)
    if compliance_rate >= 0.8:
        temp_adjustment = 1.1
    else:
        temp_adjustment = 0.9  # Never used

    # Core logic buried in noise
    trigger_threshold = 42
    activation_count = 0
    for val in raw_readings:
        if val >= trigger_threshold:
            activation_count += 1  # Counts readings >= 42

    # Secondary counter with string method interference
    flagged_events = 0
    for log in calibration_log:
        if log.count('ERR') >= 2:
            flagged_events += 1

    # Complex but irrelevant transformation chain
    encoded_sequence = ''
    for i, val in enumerate(filtered):
        encoded_sequence += chr(97 + (i % 26))
    checksum = sum(ord(c) for c in encoded_sequence) % 100  # Unused

    # Actual signal extraction (hidden in middle)
    signal_strength = stats['sum'] * (activation_count + 1)
    noise_floor = len(calibration_log) * 3 + flagged_events * 5

    # Real computation masked by distractions
    aggregate_score = signal_strength - noise_floor
    reliability_factor = stats['count'] - len(outliers)

    # Critical statement
    final_diagnostic = aggregate_score // reliability_factor

    # Red herring output
    debug_info = f"Diag:{final_diagnostic},Stab:{stability_index:.2f},Compliance:{compliance_rate:.2f}"
    print(f"Debug: {debug_info}")

    # Only relevant output
    print(f"Result: {final_diagnostic}")

# Inputs
sensor_readings = [34, 45, 56, 78, 89, 42, 67, 76, 88, 91, 0, -5, 44]
calibration_records = [
    'CAL#001:OK',
    'CAL#002:OK',
    'CAL#003:ERR SEQUENCE ERR',
    'CAL#004:OK',
    'CAL#005:ERR ERR FAILED',  # 2 ERRs
    'CAL#006:OK'
]

# Execution
analyze_sensor_data(sensor_readings, calibration_records)