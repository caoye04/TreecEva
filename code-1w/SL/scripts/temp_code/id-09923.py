def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize timestamps (not used in final result)
    timestamps = [r[0] for r in raw_readings]
    normalized_times = [(t - timestamps[0]) / 3600 for t in timestamps]

    # Distractor: complex frequency analysis with unused result
    frequency_domain = []
    for i in range(1, len(timestamps)):
        delta_t = timestamps[i] - timestamps[i-1]
        if delta_t > 0:
            frequency_domain.append(1 / delta_t)
    avg_frequency = sum(frequency_domain) / len(frequency_domain) if frequency_domain else 0

    # Actual relevant data extraction
    readings_only = [r[1] for r in raw_readings]

    # Misleading smoothing filter (partially used)
    smoothed = []
    for i, val in enumerate(readings_only):
        if i == 0:
            smoothed.append(val * calibration_factor)
        else:
            smoothed.append(0.7 * val + 0.3 * smoothed[i-1])

    # Dead code path: entropy calculation never used
    def calculate_entropy(data):
        from math import log
        counts = {}
        for d in data:
            counts[d] = counts.get(d, 0) + 1
        total = len(data)
        entropy = 0
        for count in counts.values():
            p = count / total
            entropy -= p * log(p) if p > 0 else 0
        return entropy
    
    signal_entropy = calculate_entropy(readings_only[:10])  # Unused

    # Relevant: detect anomalies above dynamic threshold
    baseline = sum(smoothed[:5]) / 5
    dynamic_threshold = baseline * 1.8
    anomalies = [i for i, s in enumerate(smoothed) if s > dynamic_threshold]

    # Distractor: secondary anomaly detection with different method (unused)
    rolling_avg = []
    window_size = 3
    for i in range(len(smoothed)):
        start = max(0, i - window_size + 1)
        roll_avg = sum(smoothed[start:i+1]) / (i - start + 1)
        rolling_avg.append(roll_avg)
    spike_indices = [i for i, (s, r) in enumerate(zip(smoothed, rolling_avg)) if s > r * 2.5]  # Unused

    # Critical: filter data based on primary anomalies
    filtered_data = [readings_only[i] for i in anomalies if i < len(readings_only)]

    # Complex distractor: build multi-layer status map (partially irrelevant)
    status_map = {}
    for i, orig in enumerate(raw_readings):
        sensor_id = f'S{i:02d}'
        temp_class = 'HIGH' if orig[1] > 80 else 'LOW'
        time_class = 'PEAK' if orig[0] % 86400 > 60000 else 'OFF_PEAK'
        status_map[sensor_id] = {'temp': temp_class, 'time': time_class, 'raw': orig[1]}

    # Unused nested structure
    diagnostic_tree = {
        'root': {
            'branch_a': {f'S{i}': {'status': 'alert'} for i in spike_indices},
            'branch_b': {f'T{i}': {'value': timestamps[i]} for i in range(0, len(timestamps), 5)}
        }
    }

    # Relevant: create threshold mapping using baseline
    threshold_map = {}
    for i in anomalies:
        key = f'ANOM_{i}'
        # Only this part matters: exponential decay of importance
        weight = 0.9 ** i
        threshold_map[key] = dynamic_threshold * weight

    # Critical function call embedded in distraction
    metadata_summary = {
        'total_sensors': len(raw_readings),
        'active_zones': [z for z in status_map if status_map[z]['temp'] == 'HIGH'],
        'calibration_used': calibration_factor
    }

    # Key statement: process only filtered data and threshold map
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Dead function - looks important but unused
    def generate_report(data, meta):
        return {"full": True, "data_len": len(data), "meta_keys": len(meta)}
    
    # Another red herring: bit manipulation on indices
    encoded_flags = 0
    for idx in anomalies[:4]:
        encoded_flags ^= (idx << (idx % 8))  # Complex but irrelevant
    
    # Final output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


def process_readings(data, thresholds):
    # Use enumerate and zip
    indexed = list(enumerate(data))
    weights = [0.5 ** i for i in range(len(data))]
    weighted_sum = sum(d * w for d, w in zip(data, weights))
    
    # Dictionary operation
    threshold_values = [v for k, v in thresholds.items()]
    adjustment = sum(threshold_values) / len(threshold_values) if threshold_values else 0
    
    # List comprehension with filtering
    significant = [x for x in data if x > adjustment * 0.7]
    
    # Final computation
    result = weighted_sum - adjustment + len(significant) * 0.1
    return round(result, 6)

# Simulated input data
sensor_input = [
    (1623456000, 45.2), (1623456060, 47.1), (1623456120, 82.3), (1623456180, 88.9),
    (1623456240, 53.4), (1623456300, 91.2), (1623456360, 76.8), (1623456420, 94.5),
    (1623456480, 68.0), (1623456540, 83.1)
]

# Execute
final_diagnostic = analyze_sensor_array(sensor_input, calibration_factor=1.05)