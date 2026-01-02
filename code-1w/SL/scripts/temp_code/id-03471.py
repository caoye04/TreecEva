from collections import defaultdict, Counter

# Simulated sensor network diagnostic system
def collect_diagnostics(raw_readings):
    base_metrics = {}
    temp_cache = []
    for key, values in raw_readings.items():
        avg_val = sum(values) / len(values)
        base_metrics[key] = round(avg_val, 3)
        temp_cache.append(avg_val * 0.1)  # Irrelevant transformation
    
    # Dead code path - never used
    if len(temp_cache) > 100:
        outlier_score = max(temp_cache) - min(temp_cache)
        return {'anomaly': outlier_score}
    
    return base_metrics

def filter_noisy_sensors(metrics, noise_floor=0.5):
    cleaned = {}
    for k, v in metrics.items():
        if abs(v) >= noise_floor:
            cleaned[k] = v * 1.05  # Slight gain adjustment
    return cleaned

def generate_signature(data_dict):
    # Creates a hash-like signature (not used in final result)
    sig_parts = []
    for k, v in data_dict.items():
        part = (hash(k) + int(abs(v))) % 17
        sig_parts.append(part)
    fake_checksum = sum(sig_parts) / len(sig_parts)
    return [x ^ int(fake_checksum) for x in sig_parts]  # Distractor computation

def integrate_system_logs(log_stream):
    # Simulates log parsing but returns dummy structure
    log_summary = defaultdict(int)
    priority_flags = []
    for entry in log_stream:
        components = entry.split(' ')
        for c in components:
            if c.isdigit():
                log_summary['count'] += int(c)
            elif 'ERR' in c:
                priority_flags.append(c)
    # This entire function is irrelevant to final answer
    return {'flags': priority_flags, 'summary': dict(log_summary)}
def preprocess_readings(sensor_data):
    # Extract and reshape data
    reshaped = defaultdict(list)
    for entry in sensor_data:
        node_id = entry['node']
        readings = entry['values']
        filtered_vals = [v for v in readings if v is not None]
        smoothed = [round((filtered_vals[i] + filtered_vals[min(i+1, len(filtered_vals)-1)]) / 2, 2)
                    for i in range(len(filtered_vals))]
        reshaped[node_id].extend(smoothed)
    return dict(reshaped)
def compute_variance_profile(dataset):
    # Compute variance per group (unused later)
    variances = {}
    for k, v in dataset.items():
        mean_v = sum(v) / len(v)
        var = sum((x - mean_v) ** 2 for x in v) / len(v)
        variances[k] = round(var, 4)
    return variances

def detect_patterns(sliced_data):
    # Analyze slices for repeating motifs (red herring)
    patterns = Counter()
    for k, v in sliced_data.items():
        for i in range(len(v) - 2):
            triplet = tuple(v[i:i+3])
            patterns[triplet] += 1
    top_pattern = patterns.most_common(1)
    return top_pattern[0][1] if top_pattern else 0
def normalize_readings(data):
    # Normalize each sequence between -1 and 1
    normalized = {}
    for k, v in data.items():
        if not v:
            continue
        max_val, min_val = max(v), min(v)
        range_val = max_val - min_val
        if range_val == 0:
            normalized[k] = [0 for _ in v]
        else:
            normalized[k] = [round(2 * (x - min_val) / range_val - 1, 3) for x in v]
    return normalized

def slice_and_aggregate(data, window_size=3):
    # Create sliding windows and compute means
    aggregated = {}
    for k, v in data.items():
        if len(v) < window_size:
            continue
        windows = [v[i:i+window_size] for i in range(len(v) - window_size + 1)]
        means = [round(sum(w) / len(w), 3) for w in windows]
        aggregated[k] = means
    return aggregated

def analyze_readings(processed_data, threshold_map):
    # Core analysis logic
    scores = []
    for node, readings in processed_data.items():
        if node not in threshold_map:
            continue
        high_threshold = threshold_map[node]['high']
        low_threshold = threshold_map[node]['low']
        count_high = sum(1 for r in readings if r > high_threshold)
        count_low = sum(1 for r in readings if r < low_threshold)
        net_anomaly_score = count_high * 2 - count_low
        scores.append(net_anomaly_score)
    return sum(scores) if scores else 0

# Main execution flow
if __name__ == '__main__':
    # Raw input data
    sensor_input = [
        {'node': 'A1', 'values': [1.2, 0.8, None, 1.5, 1.7, 0.9]},
        {'node': 'B2', 'values': [0.3, 0.1, 0.4, None, 0.2]},
        {'node': 'C3', 'values': [2.1, 2.3, 2.0, 2.4, 2.2]}
    ]
    
    system_logs = [
        'SYS INIT OK',
        'NODE A1 SYNC ERR01',
        'NODE B2 TEMP STABLE',
        'ERR_CRITICAL_RESET',
        'NODE C3 DATA STREAMING'
    ]
    
    # Step 1: Preprocess raw sensor data
    raw_collected = {entry['node']: entry['values'] for entry in sensor_input}
    base_diagnostics = collect_diagnostics(raw_collected)
    
    # Step 2: Filter out low-amplitude sensors
    filtered_diagnostics = filter_noisy_sensors(base_diagnostics, noise_floor=0.5)
    
    # Step 3: Preprocess full dataset
    preprocessed_raw = preprocess_readings(sensor_input)
    
    # Step 4: Normalize all readings
    normalized_data = normalize_readings(preprocessed_raw)
    
    # Step 5: Apply slicing for temporal pattern analysis
    sliced_data = slice_and_aggregate(normalized_data, window_size=3)
    
    # Step 6: Run irrelevant pattern detection (distractor)
    pattern_count = detect_patterns(sliced_data)
    
    # Step 7: Compute variance profile (not used in final result)
    variance_report = compute_variance_profile(preprocessed_raw)
    
    # Step 8: Generate signature (irrelevant)
    signature_code = generate_signature(filtered_diagnostics)
    
    # Step 9: Integrate logs (completely unrelated)
    log_analysis = integrate_system_logs(system_logs)
    
    # Step 10: Define thresholds for anomaly detection
    threshold_config = {
        'A1': {'high': 0.6, 'low': -0.5},
        'B2': {'high': 0.7, 'low': -0.4},
        'C3': {'high': 0.8, 'low': -0.6}
    }
    
    # Step 11: Perform final analysis using only sliced_data and threshold_config
    final_diagnostic = analyze_readings(sliced_data, threshold_config)
    
    # Output result
    print(f"Result: {final_diagnostic}")