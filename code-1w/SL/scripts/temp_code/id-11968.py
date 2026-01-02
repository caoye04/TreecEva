def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant pre-processing: normalize data (not actually used in final result)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 3) for x in raw_readings]
    
    # Distractor: complex frequency analysis with unused result
    freq_map = {}
    for val in raw_readings:
        freq_map[val] = freq_map.get(val, 0) + 1
    dominant_frequency = max(freq_map.values()) if freq_map else 0

    # Real processing begins: identify out-of-bound readings
    anomalies = []
    rolling_window = []
    aggregate_score = 0
    
    for i, reading in enumerate(raw_readings):
        rolling_window.append(reading)
        if len(rolling_window) > 3:
            rolling_window.pop(0)
        
        # Conditional expression to flag spikes
        is_spike = reading > thresholds['upper'] or (i > 0 and abs(reading - raw_readings[i-1]) > 15)
        if is_spike:
            anomalies.append((i, reading))
            
        # Accumulate only readings within medium range
        if thresholds['lower'] + 5 < reading <= thresholds['upper'] - 10:
            aggregate_score += reading * 0.1

    # Dead code path: never executed due to condition always being False
    debug_override = False
    if debug_override and len(anomalies) > 10:
        aggregate_score = 999  # decoy assignment

    # Simulated ML-based anomaly classifier (distractor)
    predicted_labels = {i: 1 if i % 3 == 0 else 0 for i in range(len(raw_readings))}
    false_positives = sum(1 for idx, _ in anomalies if predicted_labels.get(idx, 0) == 0)

    # Unused statistical calculation (red herring)
    mean_val = sum(raw_readings) / len(raw_readings) if raw_readings else 0
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings) if raw_readings else 0
    std_dev = variance ** 0.5

    # Critical control flow with nested conditions
    base_correction = 0
    if len(anomalies) > 5:
        if false_positives == 0:
            base_correction = -7
        elif false_positives < 3:
            base_correction = -3
        else:
            base_correction = 2
    else:
        base_correction = 5

    # Bit manipulation decoy (irrelevant to final answer)
    encoded_diagnostic = 0
    for i, (pos, val) in enumerate(anomalies[:4]):
        encoded_diagnostic ^= (pos << 2) | (val & 0x3)
    
    # Slicing operation on sorted anomalies
    sorted_anomalies = sorted(anomalies, key=lambda x: x[1], reverse=True)
    top_slice = sorted_anomalies[:2]
    penalty_adjust = sum([val for _, val in top_slice]) // 10 if top_slice else 0

    # Key statement - target of question
    correction_factor = base_correction + (penalty_adjust // 2)
    final_diagnostic = aggregate_score + correction_factor * (len(anomalies) - false_positives)

    # More distractions: unused dictionary aggregation
    summary_report = {
        'total_readings': len(raw_readings),
        'anomaly_rate': round(len(anomalies) / len(raw_readings), 3),
        'critical_flags': len([v for _, v in anomalies if v > 85]),
        'encoded_flag': encoded_diagnostic
    }

    return final_diagnostic

# Main execution
sensor_input = [23, 45, 78, 92, 15, 8, 67, 89, 95, 41, 29, 77]
cut_offs = {'lower': 10, 'upper': 90}

result = analyze_sensor_data(sensor_input, cut_offs)
print(f"Target result: {result}")