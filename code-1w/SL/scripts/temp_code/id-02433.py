import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
REFERENCE_VOLTAGE = 3.3
TEMP_CORRECTION_FACTOR = 1.05

# Irrelevant sensor metadata
device_info = {
    'model': 'SEN-X2000',
    'firmware': 'v2.1.7',
    'location_id': 4051,
    'installation_date': '2023-05-17'
}

# Simulated raw sensor readings (some will be discarded)
raw_readings = [
    102, 98, 107, 113, 99, 101, 105, 103, 111, 115,
    97, 104, 108, 110, 106, 100, 109, 102, 114, 96
]

# Noise floor and outlier thresholds (partially irrelevant)
noise_floor = 95
spike_threshold = 120

# Mapping of severity levels to actions (only keys used in logic)
severity_map = {
    'critical': {'action': 'shutdown', 'priority': 1},
    'high': {'action': 'alert', 'priority': 2},
    'moderate': {'action': 'log', 'priority': 3},
    'normal': {'action': 'monitor', 'priority': 4}
}

# Threshold configuration for analysis (this is critical)
threshold_map = {
    'low': 100,
    'medium': 105,
    'high': 110
}

# Auxiliary function - appears important but only one path matters
def apply_calibration(value, temp_factor=TEMP_CORRECTION_FACTOR):
    calibrated = value * (1 + CALIBRATION_OFFSET)
    corrected = calibrated * temp_factor
    return round(corrected, 2)

# Another decoy function that's never called
def legacy_compatibility_mode(data):
    return [x * REFERENCE_VOLTAGE / 1024 for x in data]

# Data transformation with red herring operations
def preprocess_readings(raw_data):
    processed = []
    outliers = []
    total_adjustment = 0.0

    for i, val in enumerate(raw_data):
        # Simulate position-based distortion (distractor)
        if i % 7 == 0:
            distorted = val * 0.98
        elif i % 5 == 0:
            distorted = val * 1.02
        else:
            distorted = val

        # Apply calibration (seems important, but rounding negates effect)
        calibrated = apply_calibration(distorted)

        # Only filter by noise floor; spike threshold is a red herring
        if calibrated >= noise_floor:
            processed.append(int(round(calibrated)))
        else:
            outliers.append(calibrated)

        # Accumulate meaningless statistic
        total_adjustment += abs(calibrated - val)

    # Dead code path - debugging artifact
    if len(outliers) > 10:
        fallback = [x for x in raw_data if x >= 100]
        return sorted(fallback, reverse=True)

    return processed  # This is what actually gets used

# Core analysis logic with conditional branching
def analyze_readings(data, thresholds):
    count_low = 0
    count_medium = 0
    count_high = 0

    # Real processing occurs here
    for reading in data:
        if reading < thresholds['low']:
            continue  # Below baseline
        elif reading < thresholds['medium']:
            count_low += 1
        elif reading < thresholds['high']:
            count_medium += 1
        else:
            count_high += 1

    # Complex-looking aggregation with distractor variables
    weighted_score = (
        count_low * 1.0 +
        count_medium * 2.5 +
        count_high * 5.0
    )

    total_valid = len(data)
    average_count = weighted_score / (total_valid or 1)

    # Secondary metric (unused)
    peak_ratio = count_high / (count_low or 1)

    # Determine diagnostic level using nested logic
    if count_high > 5:
        level = 'critical'
    elif count_medium > 8:
        level = 'high'
    elif count_low > 10:
        level = 'moderate'
    else:
        level = 'normal'

    # Final computation chain
    base_diagnostic = severity_map[level]['priority']
    adjustment_factor = 0.0

    # Conditional correction based on statistical profile
    if peak_ratio > 0.8 and average_count > 2.0:
        adjustment_factor = 1.2
    elif average_count > 1.5:
        adjustment_factor = 0.8
    else:
        adjustment_factor = 1.0  # This will be selected

    # The actual answer depends only on this calculation
    final_value = int(base_diagnostic * 729)  # 729 = 9^3, deterministic

    # Dead assignment - misleading
    final_value = final_value - 728 if level == 'unknown' else final_value

    return final_value

# Execution flow
processed_data = preprocess_readings(raw_readings)

# Irrelevant post-processing step (data inspection)
if len(processed_data) > 15:
    sample_variance = sum((x - 105) ** 2 for x in processed_data[:10]) / 10
    normalized_data = [x / 105.0 for x in processed_data]

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Additional distraction: unused summary object
diagnostic_report = {
    'timestamp': '2023-11-09T14:22:30Z',
    'readings_count': len(processed_data),
    'distribution': {
        'mean': sum(processed_data) / len(processed_data),
        'range': (min(processed_data), max(processed_data))
    },
    'status_code': final_diagnostic,
    'version': device_info['firmware']
}

Result: {final_diagnostic}