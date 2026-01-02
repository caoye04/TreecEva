def analyze_sensor_data(raw_readings, thresholds):
    # Initialize various diagnostic metrics (some are red herrings)
    baseline = sum(raw_readings) / len(raw_readings)
    variance = sum((x - baseline) ** 2 for x in raw_readings) / len(raw_readings)
    normalized_scores = [abs(x - baseline) / (variance + 1e-5) for x in raw_readings]

    # Irrelevant transformation: frequency domain mock analysis
    freq_components = []
    for i in range(len(raw_readings)):
        component = 0
        for j in range(len(raw_readings)):
            component += raw_readings[j] * (i * j % 7)
        freq_components.append(component % 100)

    # Real processing begins: detect anomalies using threshold logic
    anomaly_flags = []
    for idx, val in enumerate(raw_readings):
        if val > thresholds.get('upper', 90) or val < thresholds.get('lower', 10):
            anomaly_flags.append((idx, True))
        else:
            anomaly_flags.append((idx, False))

    # Distractor: unused complex structure
    status_map = {i: {'raw': raw_readings[i], 'norm': normalized_scores[i], 
                      'freq': freq_components[i], 'flag': flag} 
                  for i, (_, flag) in enumerate(anomaly_flags)}

    # Real logic: count consecutive anomalies
    consecutive_count = 0
    max_consecutive = 0
    for _, is_anomalous in anomaly_flags:
        if is_anomalous:
            consecutive_count += 1
            max_consecutive = max(max_consecutive, consecutive_count)
        else:
            consecutive_count = 0

    # Another distractor: set operations with no impact
    unique_normalized = set(round(n, 2) for n in normalized_scores)
    high_freq_set = set(f for f in freq_components if f > 50)
    intersection_distract = unique_normalized & {f * 0.5 for f in high_freq_set}

    # Compute aggregate score using multiple steps
    base_penalty = max_consecutive * 10
    duration_bonus = len(raw_readings) // 10
    aggregate_score = base_penalty - duration_bonus

    # Correction factor based on specific pattern detection
    correction_factor = 0
    for i in range(1, len(raw_readings)):
        if raw_readings[i] > raw_readings[i-1] and anomaly_flags[i][1]:
            correction_factor += 3

    # Key execution point
    final_diagnostic = aggregate_score + correction_factor

    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Dead code path: never executed but looks important
    if False:
        backup_system = {"recovery": sum(freq_components) // len(freq_components)}
        return backup_system['recovery']

    return final_diagnostic

# Input data
readings = [8, 12, 95, 97, 99, 45, 10, 5, 96, 98]
limits = {'upper': 90, 'lower': 15}

# Execute
result = analyze_sensor_data(readings, limits)