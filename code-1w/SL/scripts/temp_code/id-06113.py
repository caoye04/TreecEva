def analyze_sensor_grid(raw_input, calibration_factor):
    readings = raw_input.split(',')
    calibrated_values = [float(x.strip()) * calibration_factor for x in readings]
    
    # Irrelevant transformation: text-based analysis (distractor)
    label_stats = {}
    labels = ['S1', 'S2', 'S3', 'S4', 'S5']
    for i, lbl in enumerate(labels):
        label_stats[lbl] = len(lbl) + i

    # Misleading intermediate normalization (dead path)
    normalized = []
    total = sum(calibrated_values)
    for val in calibrated_values:
        if total != 0:
            normalized.append(round(val / total, 4))
        else:
            normalized.append(0.0)

    # Actual filtering logic (relevant)
    valid_range = lambda x: 10 <= x <= 100
    filtered_data = [x for x in calibrated_values if valid_range(x)]

    # Decoy statistical summary (distractor)
    avg_val = sum(calibrated_values) / len(calibrated_values) if calibrated_values else 0
    outlier_count = len([x for x in calibrated_values if x > 110 or x < 5])

    # Complex data structure manipulation (mix of relevant and irrelevant)
    status_flags = {i: ('high' if v > 50 else 'low') for i, v in enumerate(filtered_data)}
    flag_summary = ''.join(status_flags.values()).count('high')

    # Dummy dictionary operations (irrelevant but plausible)
    metadata_log = {}
    metadata_log['version'] = '2.1'
    metadata_log['nodes'] = len(labels)
    metadata_log['active'] = True
    metadata_log['checksum'] = sum(ord(c) for c in metadata_log['version'])

    # Threshold map construction — actually used later (critical!)
    base_thresholds = {'t1': 15, 't2': 30, 't3': 45}
    dynamic_adjust = len(filtered_data) % 3
    threshold_map = {k: v + dynamic_adjust for k, v in base_thresholds.items()}

    # Red herring: unused function definition (distractor)
    def diagnose_anomaly(seq, factor):
        return [x for x in seq if x % factor == 0]

    # Another red herring: complex string operation with no downstream use
    diagnostic_tag = '-'.join([f'{k}{v}' for k, v in status_flags.items() if v == 'high']).lower()
    reversed_tag = diagnostic_tag[::-1]
    tag_entropy = sum([reversed_tag.count(c) for c in set(reversed_tag)])

    # Key assignment: this function is actually called
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic


def process_readings(data, thresholds):
    # Actual computation path
    t1, t2, t3 = thresholds['t1'], thresholds['t2'], thresholds['t3']
    count_a = len([x for x in data if x >= t1])
    count_b = len([x for x in data if x >= t2])
    count_c = len([x for x in data if x >= t3])
    
    # Multi-step arithmetic combination
    score_component_1 = count_a * 7
    score_component_2 = count_b * 12
    score_component_3 = count_c * 5
    
    # Final diagnostic calculation (answer depends on input)
    result = (score_component_1 + score_component_2 - score_component_3) * 2
    
    # Dead code branch (misleading)
    if result < 0:
        result = abs(result) + 100  # never reached in this case
    
    return result

# Simulate sensor input and execute
input_stream = "12.0, 45.5, 67.3, 105.0, 8.2, 53.1, 99.9, 23.4, 76.8"
calibration_multiplier = 1.1

# Execute main analysis
final_diagnostic = analyze_sensor_grid(input_stream, calibration_multiplier)
print(f"Result: {final_diagnostic}")