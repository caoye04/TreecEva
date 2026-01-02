def analyze_sensor_data(raw_readings, calibration_map):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [0] * len(raw_readings)
    for i in range(len(raw_readings)):
        temp_buffer[i] = raw_readings[i] + 0.001  # Noise injection - unused

    # Actual processing begins
    filtered_readings = []
    for val in raw_readings:
        if val > 100 or val < -100:
            continue
        filtered_readings.append(val)

    # Distractor: complex but unused transformation
    normalized = set()
    base_offset = sum(filtered_readings) / len(filtered_readings)
    for idx, reading in enumerate(filtered_readings):
        normalized.add((reading - base_offset) * (idx + 1))

    # Another decoy: dictionary mapping with no downstream use
    diagnostic_codes = {}
    for i, r in enumerate(filtered_readings):
        code = f'D{i}{"H" if r > base_offset else "L"}'
        diagnostic_codes[r] = code

    # Real computation chain starts here
    moving_avg = []
    window_size = 3
    for i in range(len(filtered_readings) - window_size + 1):
        window = filtered_readings[i:i + window_size]
        moving_avg.append(sum(window) / window_size)

    # Compute volatility index
    volatility = 0
    for i in range(1, len(moving_avg)):
        volatility += abs(moving_avg[i] - moving_avg[i-1])

    # Anomaly detection using zip and enumerate (required feature)
    anomalies = []
    for idx, (current, next_val) in enumerate(zip(moving_avg, moving_avg[1:])):
        if abs(next_val - current) > 1.5:
            anomalies.append(idx)

    # Decoy analysis using set operations (required feature)
    unique_movements = set(moving_avg)
    large_shifts = set(anomalies)
    phantom_correlations = unique_movements.difference(large_shifts)  # Unused

    # Core logic buried among distractions
    baseline = moving_avg[0] if moving_avg else 0
    peak = max(moving_avg) if moving_avg else 0
    trend_ratio = (peak - baseline) / baseline if baseline != 0 else 0

    # Multi-step calculation with distractors
    stability_score = 100 - volatility
    anomaly_count = len(anomalies)
    anomaly_offset = anomaly_count ** 2

    # Dictionary-based weight lookup (used)
    severity_weights = {0: 0, 1: 5, 2: 12, 3: 20, 4: 30}
    weight = severity_weights.get(anomaly_count, 40)

    # Correction factor derived from trend
    correction_factor = 1.0
    if trend_ratio > 0.1:
        correction_factor = 0.8
    elif trend_ratio < -0.1:
        correction_factor = 1.2
    else:
        correction_factor = 1.0

    # Aggregate score with irrelevant terms included
    aggregate_score = stability_score - weight + 10  # +10 is fixed adjustment

    # Key statement: target variable
    final_diagnostic = aggregate_score + anomaly_offset * correction_factor

    # Dead code: further manipulation not affecting result
    if final_diagnostic > 100:
        final_diagnostic *= 0.95
    elif final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)

    return final_diagnostic

# Main execution
sensor_inputs = [105, -45, 30, 20, 10, 5, -5, -15, -25, 80, 90, 110]
calibration_profile = {'gain': 1.02, 'offset': -3.5}

result = analyze_sensor_data(sensor_inputs, calibration_profile)
print(f'Target result: {result}')