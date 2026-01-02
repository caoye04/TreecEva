def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing: normalize data (not used in final result)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100) for x in raw_readings]
    
    # Distractor: complex-looking but unused frequency analysis
    freq_map = {}
    for val in raw_readings:
        freq_map[val] = freq_map.get(val, 0) + 1
    dominant_frequency = max(freq_map.values()) if freq_map else 0

    # Unused smoothing function (red herring)
    def smooth(data):
        return [sum(data[max(0, i-1):i+2]) / len(data[max(0, i-1):i+2]) for i in range(len(data))]
    
    # Real processing begins: filter anomalies
    anomalies = []
    for i, reading in enumerate(raw_readings):
        if reading > thresholds['upper'] or reading < thresholds['lower']:
            anomalies.append((i, reading))
    
    # Distractor: set operations with no impact
    index_set = set(i for i, _ in anomalies)
    all_indices = set(range(len(raw_readings)))
    missing_indices = all_indices - index_set  # unused

    # Conditional expression with actual relevance
    base_flag = 'critical' if len(anomalies) > 3 else 'moderate'

    # Actual signal extraction using zip and enumerate (key concepts)
    deviations = []
    for i, (reading, threshold) in enumerate(zip(raw_readings, thresholds['dynamic'])):
        if i % 2 == 0:  # only even indices contribute
            deviations.append(abs(reading - threshold))
    
    # Complex but partially irrelevant transformation
    transformed = []
    for d in deviations:
        temp_val = d ** 2 + 5
        if temp_val > 50:
            temp_val = temp_val // 3
        transformed.append(temp_val - 2)  # not used directly

    # Key computation chain starts here
    aggregate_score = 0
    for val in deviations:
        aggregate_score += int(val // 1.5)
    
    # Simulated anomaly offset based on position
    anomaly_offset = 0
    for pos, _ in anomalies:
        anomaly_offset += pos % 7

    # Correction factor determined by conditional logic
    if base_flag == 'critical':
        correction_factor = 3
    elif len(deviations) > 4:
        correction_factor = 2
    else:
        correction_factor = 1

    # Dead code path (distractor)
    backup_mode = False
    if sum(transformed) < 0:
        correction_factor *= -1
        backup_mode = True  # never reached due to data constraints

    # Critical assignment - target execution point
    final_diagnostic = aggregate_score + anomaly_offset * correction_factor

    # Redundant post-processing (irrelevant)
    diagnostic_log = []
    for _ in range(3):
        diagnostic_log.append('entry')  # meaningless logging

    # Output the required variable
    print(f"Result: {final_diagnostic}")

# Input data
readings = [12, 45, 67, 89, 12, 90, 44, 68]
limits = {
    'upper': 85,
    'lower': 15,
    'dynamic': [10, 50, 60, 80, 20, 88, 40, 70]
}

# Execute
analyze_sensor_data(readings, limits)