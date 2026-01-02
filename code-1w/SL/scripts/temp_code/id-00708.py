def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing: normalize strings (distractor)
    normalized_labels = [label.strip().upper() for label in ['sensor_a', 'sensor_b ', ' SENSOR_C']]
    encoded_tags = [hash(label) % 100 for label in normalized_labels]

    # Actual data processing begins
    filtered_readings = []
    outlier_count = 0
    for val in raw_readings:
        if val < thresholds['min'] or val > thresholds['max']:
            outlier_count += 1
            if outlier_count > 2:
                break
        else:
            filtered_readings.append(val)

    # Distractor: unused statistical computation
    mean_value = sum(raw_readings) / len(raw_readings) if raw_readings else 0
    variance_proxy = sum((x - mean_value) ** 2 for x in raw_readings) / len(raw_readings) if raw_readings else 0

    # Real signal extraction using set operations (key concept)
    baseline_set = {i for i in range(10, 20)}
    detected_peaks = {i for i, x in enumerate(filtered_readings) if x > 85}
    active_zones = baseline_set.intersection(detected_peaks)

    # Another red herring: string-based event logging (irrelevant)
    log_entries = ['Event: START']
    for zone in sorted(active_zones):
        status_flag = 'ACTIVE' if zone > 12 else 'STANDBY'
        log_entries.append(f'Zone {zone}: {status_flag}')
    full_log = ' | '.join(log_entries)
    compressed_log = ''.join([c for c in full_log if c.isalnum() or c.isspace()])  # distractor

    # Core logic chain starts here — meaningful accumulation
    adjustment_sequence = []
    for i, reading in enumerate(filtered_readings):
        if i % 2 == 0:
            adjusted = reading * 0.95
        else:
            adjusted = reading + (i % 3)
        adjustment_sequence.append(round(adjusted))

    # Use of enumerate and zip (required Python feature)
    index_pairs = list(zip(enumerate(adjustment_sequence), enumerate(reversed(adjustment_sequence))))
    symmetry_score = 0
    for (i, a), (j, b) in index_pairs:
        if i == j:  # center element in palindrome-like check
            symmetry_score += a
        elif abs(a - b) <= 5:
            symmetry_score += 2

    # Key aggregation step
    aggregate_score = sum(adjustment_sequence) + symmetry_score

    # Correction based on zone activity (depends on earlier set operation)
    zone_influence = len(active_zones) * 7
    environmental_bias = -5 if 'STANDBY' in full_log else 0  # misleading since STANDBY always appears
    correction_factor = zone_influence + environmental_bias

    # Dead code path — never executed due to prior break condition
    recovery_mode = False
    backup_buffer = []
    for x in raw_readings:
        if x < 0:
            recovery_mode = True
            backup_buffer.append(abs(x))
    # This loop is irrelevant because raw_readings contains only positive values

    final_diagnostic = aggregate_score + correction_factor
    return final_diagnostic

# Simulate execution
readings = [92, 87, 95, 88, 70, 105, 90]  # 105 will be excluded as outlier, then loop breaks on next
limits = {'min': 80, 'max': 100}
diag = analyze_sensor_data(readings, limits)
print(f"Result: {diag}")