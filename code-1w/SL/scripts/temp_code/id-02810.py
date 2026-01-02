def analyze_sensor_data(raw_readings):
    filtered_data = [x for x in raw_readings if x > -50 and x < 150]
    baseline = sum(filtered_data) / len(filtered_data)
    normalized = [round((x - baseline) * 1.05, 2) for x in filtered_data]

    # Irrelevant transformation: frequency simulation (distractor)
    freq_components = []
    for i in range(len(normalized)):
        component = 0
        for j in range(0, min(i+1, 5)):
            component += normalized[j] * (0.9 ** (i - j))
        freq_components.append(component)

    # Dead code path: never used (red herring)
    def calculate_entropy(data):
        from math import log
        counts = {}
        for d in data:
            counts[d] = counts.get(d, 0) + 1
        total = len(data)
        entropy = 0
        for count in counts.values():
            p = count / total
            entropy -= p * log(p)
        return entropy

    # Unused variable: misleading intermediate
    peak_magnitude = max(normalized) - min(normalized)
    temporal_drift = normalized[-1] - normalized[0]

    # Relevant logic begins here: signal integrity assessment
    anomalies = 0
    for val in normalized:
        if abs(val) > 25:
            anomalies += 1
    anomaly_ratio = anomalies / len(normalized)

    # Simulated hardware correction factor based on calibration history
    calibration_log = ['CAL_201', 'CAL_305', 'CAL_412']
    calibration_scores = []
    for entry in calibration_log:
        score = 0
        for char in entry:
            if char.isdigit():
                score += int(char)
        calibration_scores.append(score)
    avg_calibration_score = sum(calibration_scores) / len(calibration_scores)

    # Decoy aggregation: looks important but unused
    synthetic_index = (anomaly_ratio * 100) + avg_calibration_score

    # Core computation chain (nested logic)
    if anomaly_ratio < 0.3:
        if avg_calibration_score > 12:
            confidence_level = 0.9
        else:
            confidence_level = 0.65
    else:
        confidence_level = 0.4

    # Secondary irrelevant processing: text-based metadata parsing
    metadata_tags = ['SRC:A', 'VER:2.1', 'NODE:7', 'GRP:X']
    node_id = 0
    for tag in metadata_tags:
        if 'NODE:' in tag:
            try:
                node_id = int(tag.split(':')[-1])
            except:
                node_id = 5

    # Another decoy variable
    system_weight = node_id * 1.8

    # Actual signal quality metric (used later)
    signal_quality = 1 - anomaly_ratio

    # Complex derived measure with slicing distraction
    trend_sample = normalized[::2]  # Every other reading
    trend_rate = (trend_sample[-1] - trend_sample[0]) / len(trend_sample)

    # Redundant string operation (distractor)
    status_flag = 'OK' if signal_quality > 0.7 else 'WARN'
    status_code = ''.join([c.lower() for c in status_flag])

    # Critical path variables
    aggregate_measure = signal_quality * abs(trend_rate) * 1000
    correction_factor = confidence_level * (0.85 + (node_id * 0.01))
    offset_value = 17.4

    # Key assignment statement
    final_diagnostic = aggregate_measure * correction_factor + offset_value

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Return nothing; focus on side effect
    return None

# Input data (deterministic seed)
data_stream = [23.1, -15.7, 89.4, 101.2, -45.0, 12.8, 9.3, 110.0, -30.5, 7.0, 55.6, 67.8]
analyze_sensor_data(data_stream)