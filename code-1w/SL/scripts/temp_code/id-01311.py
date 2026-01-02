from collections import defaultdict, Counter

# Simulate sensor data aggregation and fault detection in a distributed system
def collect_sensor_readings():
    raw_readings = [
        (0, [3.2, 3.5, 3.1, 2.9]), (1, [4.0, 4.1, 3.8]), (2, [2.0, 1.8, 1.9, 2.1, 2.2]),
        (3, [5.5, 5.7, 5.6]), (4, [1.0, 0.9, 1.1]), (5, [3.3, 3.4]),
        (6, [2.7, 2.6, 2.8]), (7, [4.4, 4.5, 4.3]), (8, [1.5, 1.6]),
        (9, [3.9, 3.7])
    ]
    return raw_readings

# Irrelevant helper - looks useful but not used in final computation
def deprecated_normalizer(x):
    return [val / sum(x) for val in x]

# Misleading preprocessing that seems important but is bypassed
def legacy_filter(data):
    filtered = []
    for node_id, readings in data:
        if len(readings) > 3:
            filtered.append((node_id, [r for r in readings if r > 2.5]))
    return filtered

# Core processing: compute moving average over sliding window
def smooth_signal(signal, window=2):
    if len(signal) < window:
        return signal[:]
    smoothed = []
    for i in range(len(signal) - window + 1):
        smoothed.append(sum(signal[i:i+window]) / window)
    return smoothed

# Auxiliary function for noise estimation (distractor)
def estimate_noise_floor(signal):
    diffs = [abs(signal[i] - signal[i-1]) for i in range(1, len(signal))]
    return sum(diffs) / len(diffs) if diffs else 0.0

# Real preprocessing path - only this one is actually used
def preprocess_node_data(raw_entry):
    node_id, readings = raw_entry
    avg_base = sum(readings) / len(readings)
    
    # Apply smoothing
    smoothed = smooth_signal(readings)
    if not smoothed:
        smoothed = [avg_base]
    
    # Compute variance as stability metric
    variance = sum((x - avg_base) ** 2 for x in readings) / len(readings)
    
    # Generate enhanced feature set
    features = {
        'node': node_id,
        'base_avg': avg_base,
        'stability': variance,
        'peak': max(readings),
        'trend': smoothed[-1] - smoothed[0] if len(smoothed) > 1 else 0.0,
        'duration': len(readings)
    }
    
    return features

# Threshold configuration map (used in final analysis)
def build_threshold_profile():
    profile = defaultdict(dict)
    profile[0]['critical'] = 4.0
    profile[1]['critical'] = 4.2
    profile[2]['critical'] = 2.3
    profile[3]['critical'] = 5.6
    profile[4]['critical'] = 1.2
    profile[5]['critical'] = 3.6
    profile[6]['critical'] = 2.9
    profile[7]['critical'] = 4.6
    profile[8]['critical'] = 1.7
    profile[9]['critical'] = 4.0
    
    # Add unused categories as distractors
    for k in profile:
        profile[k]['warning'] = profile[k]['critical'] - 0.5
        profile[k]['info'] = profile[k]['critical'] - 1.0
    
    return profile

# Fault pattern recognizer (looks complex but only one output matters)
def detect_anomaly_patterns(features_list):
    patterns = Counter()
    for feat in features_list:
        if feat['stability'] > 0.3:
            patterns['high_variance'] += 1
        if feat['trend'] > 0.5:
            patterns['rising_risk'] += 1
        if feat['peak'] > 5.0:
            patterns['extreme_peak'] += 1
        if feat['duration'] < 3:
            patterns['insufficient_data'] += 1
    return dict(patterns)

# Main analyzer - uses threshold_map to classify anomalies
def analyze_signal(processed_features, thresholds):
    anomaly_count = 0
    severity_score = 0.0
    critical_nodes = []
    
    # Map node features to index for fast lookup
    feature_map = {f['node']: f for f in processed_features}
    
    # Cross-reference with thresholds
    for node_id, feat in enumerate(processed_features):
        expected_threshold = thresholds[node_id]['critical']
        observed_avg = feat['base_avg']
        
        # Only this condition contributes to final result
        if observed_avg > expected_threshold:
            anomaly_count += 1
            # Scoring logic: excess above threshold weighted by stability
            excess = observed_avg - expected_threshold
            stability_penalty = max(0.1, feat['stability'])
            severity_score += excess * (1.0 / stability_penalty)
            critical_nodes.append(node_id)
        
        # Dead code branch - never executed due to logic, but looks plausible
        if feat.get('computed_index', -1) > 100:
            severity_score *= 1.1
    
    # Final diagnostic is deterministic combination
    final_value = int((severity_score * 1000) + anomaly_count * 10 + len(critical_nodes))
    
    # Unused telemetry (distractor)
    telemetry_snapshot = {
        'timestamp': 1678886400,
        'source_nodes': 10,
        'processed_count': len(processed_features),
        'pattern_summary': detect_anomaly_patterns(processed_features)
    }
    
    return final_value

# Orchestration function with red herring calls
def run_diagnostics():
    # Step 1: Collect raw data
    raw_data = collect_sensor_readings()
    
    # Step 2: Preprocess each node (only this path is valid)
    processed_data = [preprocess_node_data(entry) for entry in raw_data]
    
    # Step 3: Build threshold map
    threshold_map = build_threshold_profile()
    
    # Step 4: Run legacy filter (result ignored - distraction)
    _ignored_filtered = legacy_filter(raw_data)
    
    # Step 5: Estimate noise (computation performed but not used)
    for _, readings in raw_data:
        noise_floor = estimate_noise_floor(readings)  # Computed but unused
    
    # Step 6: Analyze signal (key statement)
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Step 7: Print result as required
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    run_diagnostics()