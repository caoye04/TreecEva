def analyze_sensor_data(raw_readings, config_params):
    # Irrelevant preprocessing: string-based metadata parsing
    device_tag = 'SENSOR-TEMP-X2'
    firmware_version = 'v2.1.8'
    calibration_notes = 'Last calibrated on 2023-11-05'.upper().replace(' ', '_')
    temp_log = [note for note in calibration_notes.split('_') if 'CALIBRATED' in note]

    # Distractor: unused complex list comprehension
    derived_flags = [x ** 0.5 for x in range(1, len(raw_readings) + 1) if x % 7 == 0]

    # Actual relevant: extract thresholds and baseline
    baseline = config_params.get('base', 0)
    safety_margin = config_params.get('margin', 5)
    critical_floor = baseline - safety_margin * 2

    # Distractor: dead code path (never executed due to condition)
    anomaly_report = []
    if len(anomaly_report) > 100:
        backup_snapshot = raw_readings[-10:]
        for val in backup_snapshot:
            shifted = (val + 3) << 2
            anomaly_report.append(shifted)

    # Relevant: filter readings below critical floor
    filtered_data = [x for x in raw_readings if x > critical_floor]

    # Distractor: irrelevant slicing and string operations
    sample_segment = device_tag[6:] + firmware_version[1:4]
    version_slice = sample_segment[::2]
    padding_chars = [c for c in version_slice if c.isdigit()]

    # Relevant: create set of high-sensitivity thresholds
    threshold_set = set()
    for i in range(3):
        threshold_set.add(baseline + (safety_margin * (i + 1)))

    # Distractor: unused set operations with no impact
    debug_tags = {'T1', 'T2', 'T3'}
    audit_trail = debug_tags.union({'T4'}).difference({'T1'})
    audit_trail.add('T1')  # Re-added, no net effect

    # Key function call containing answer computation
    final_diagnostic = process_readings(filtered_data, threshold_set)
    return final_diagnostic


def process_readings(data, thresholds):
    # Complex logic with multiple steps
    aggregate_score = 0
    
    for val in data:
        # Multiple conditional branches
        if val < 0:
            aggregate_score += abs(val) // 2
        elif val in thresholds:
            aggregate_score += val * 3
        else:
            # Nested logic with bit manipulation red herring
            temp_flag = (val ^ 15) & 7
            if temp_flag > 3:
                aggregate_score += val + 2
            else:
                aggregate_score += val
    
    # Distractor: unused bitwise chain
    checksum = 0
    for x in data:
        checksum ^= (x << 1) | 1
    final_checksum = checksum & 0xFFFF  # Never used

    # Real transformation: apply logarithmic weighting if conditions met
    if len(data) > 5 and aggregate_score > 100:
        import math
        aggregate_score = math.log(aggregate_score, 2) * 10
        # Further modification via string length distraction
        meta_weight = len('diagnostic_v2')  # Always 11
        aggregate_score += meta_weight
    
    # Final adjustment based on set size
    aggregate_score -= len(thresholds)

    return int(aggregate_score)

# Input data and parameters
readings = [12, -8, 15, 20, 9, -3, 18, 25]
params = {'base': 10, 'margin': 4}

# Execute main logic
result = analyze_sensor_data(readings, params)

# Output target result
print(f"Target result: {result}")