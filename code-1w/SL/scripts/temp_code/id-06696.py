def analyze_signal(samples, config):
    # Irrelevant preprocessing (distractor)
    normalized = [x * config.get('gain', 1.0) + 10 for x in samples]
    filtered = [x for x in normalized if x > 5]
    
    # Decoy analysis path
    peak = max(normalized) if normalized else 0
    avg_val = sum(normalized) / len(normalized) if normalized else 0
    deviation_score = (peak - avg_val) * config.get('sensitivity', 0.5)

    # Real signal extraction (less obvious)
    windowed = [sum(samples[i:i+3]) for i in range(0, len(samples)-2)]
    trend_data = []
    for i, w in enumerate(windowed):
        if w % 2 == 0:
            trend_data.append(w * (i + 1))
        else:
            trend_data.append(w - i)

    # Dead code path (misleading)
    anomaly_flags = []
    for val in windowed:
        if val > 100:
            anomaly_flags.append(True)
        else:
            anomaly_flags.append(False)
    # Unused function call
    def compute_entropy(seq):
        from math import log
        freq = {}
        for item in seq:
            freq[item] = freq.get(item, 0) + 1
        entropy = 0
        total = len(seq)
        for count in freq.values():
            p = count / total
            entropy -= p * log(p, 2)
        return entropy
    
    # Distractor: unused dictionary
    metadata_summary = {
        'source': 'sensor_7A',
        'calibration': [0.1, 0.3, 0.2, 0.4],
        'version': 'v2.1',
        'entropy': compute_entropy(samples)  # Computed but not used
    }

    # Real logic: threshold mapping with slicing distraction
    thresholds = [15, 25, 40, 60, 80]
    labels = ['A', 'B', 'C', 'D', 'E']
    threshold_map = {lbl: thresholds[i] for i, lbl in enumerate(labels)}

    # Bit manipulation decoy
    encoded_state = 0
    for i, sample in enumerate(samples[:8]):
        if sample % 3 == 0:
            encoded_state |= (1 << i)
    
    # Actual aggregation function (depends only on trend_data and threshold_map)
    def aggregate_metrics(data, limits):
        count_c = 0
        total = 0
        for val in data:
            # Only values mapped to 'C' are relevant
            if val < limits['D'] and val >= limits['C']:
                count_c += 1
                total += val
        return total // (count_c if count_c > 0 else 1)

    # Key computation
    final_diagnostic = aggregate_metrics(trend_data, threshold_map)
    
    # Another red herring: string-based status
    status_log = []
    for i, (original, norm) in enumerate(zip(samples, normalized)):
        status_log.append(f"Sample{i}:[{original}->{norm:.1f}]")
    summary_string = " | ".join(status_log[:5])
    
    # Output the target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
sensor_readings = [8, 7, 10, 12, 5, 18, 4, 9, 11, 13]
settings = {'gain': 1.2, 'sensitivity': 0.7, 'mode': 'active'}

# Execute
analyze_signal(sensor_readings, settings)