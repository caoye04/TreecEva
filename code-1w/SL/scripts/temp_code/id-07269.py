import math

# Simulated sensor fusion system for environmental monitoring

def collect_sensor_data():
    raw_values = [144, 25, 49, 64, 121, 169, 81]
    timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
    return list(zip(timestamps, raw_values))

def filter_outliers(data):
    values = [v for t, v in data]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    threshold = 1.5 * std_dev
    filtered = [(t, v) for t, v in data if abs(v - mean) <= threshold]
    return filtered

def transform_scale(x):
    if x <= 0:
        return 0
    return int(math.log(x, 2))

def decode_signal(pattern):
    # Irrelevant bit manipulation red herring
    result = 0
    for i in range(len(pattern)):
        result |= (pattern[i] % 2) << i
    decoy_shift = (result ^ 0xFF) >> 2
    return result  # decoy_shift unused

def generate_checksum(seq):
    # Unused cryptographic decoy
    prime_mask = 104729
    chk = 0
    for s in seq:
        chk = (chk * 31 + s) % prime_mask
    return chk  # never used

def extract_features(log_entries):
    features = []
    for entry in log_entries:
        ts, val = entry
        root_val = int(math.sqrt(val))
        parity_flag = val & 1
        transformed = transform_scale(val)
        feature_code = (root_val << 4) | (transformed << 1) | parity_flag
        features.append(feature_code)
    return features

def build_lookup(features):
    # Distractor: builds a map but only one entry matters
    lookup = {}
    for idx, feat in enumerate(features):
        key = (feat % 89, idx % 17)
        lookup[key] = math.factorial(idx) if idx < 5 else 0
    # Critical value embedded at known position
    lookup[(features[3] % 89, 3 % 17)] = 4242  # planted signal
    return lookup

def detect_anomaly_set(feature_list):
    even_features = {f for f in feature_list if f % 2 == 0}
    multiples_of_3 = {f for f in feature_list if f % 3 == 0}
    # Complex set logic red herring
    decoy_intersection = even_features & multiples_of_3
    decoy_union = even_features | multiples_of_3
    decoy_diff = even_features - multiples_of_3
    # Actual relevant computation
    anomaly_candidates = {f for f in feature_list if bin(f).count('1') > 5}
    return anomaly_candidates if len(anomaly_candidates) > 0 else {0}

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p, 2) for p in probabilities if p > 0)
    return round(entropy, 6)

def temporal_correlation(times):
    # Unused time-series distraction
    diffs = [times[i+1] - times[i] for i in range(len(times)-1)]
    corr = 0
    for d in diffs:
        corr += math.sin(d) * math.cos(d)
    return corr  # never used

def process_diagnostics(anomalies, lookup_table, feature_count):
    base_score = len(anomalies) * 100
    try:
        bonus = lookup_table[(feature_count % 89, 3)]
    except KeyError:
        bonus = 10
    adjusted = base_score + bonus
    
    # Multi-step adjustment chain
    if adjusted > 500:
        adjusted = adjusted // 2
    if adjusted % 3 == 0:
        adjusted += 17
    if adjusted > 4000:
        adjusted -= 3000
    else:
        adjusted += 200  # triggers due to prior division
    return adjusted

def finalize_report(diagnostic_code):
    # Final obfuscation layer
    magic_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
    accumulator = diagnostic_code
    for shift in magic_sequence:
        accumulator = ((accumulator << 1) | (accumulator >> 15)) & 0xFFFF
        accumulator ^= shift
    return accumulator & 0x7FFF

def analyze_readings(sensor_log):
    # Main analysis pipeline
    processed = filter_outliers(sensor_log)
    features = extract_features(processed)
    lookup_map = build_lookup(features)
    anomalies = detect_anomaly_set(features)
    
    # Irrelevant entropy calculation (distraction)
    _ = compute_entropy([f for f in features])
    
    # Critical call
    intermediate_result = process_diagnostics(anomalies, lookup_map, len(features))
    final_diagnostic = finalize_report(intermediate_result)
    return final_diagnostic

# Execution sequence
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    raw_logs = collect_sensor_data()
    
    # Step 2: Filter noisy readings
    cleaned_logs = filter_outliers(raw_logs)
    
    # Step 3: Extract feature vectors
    extracted_features = extract_features(cleaned_logs)
    
    # Step 4: Build internal lookup (contains hidden value)
    feature_lookup = build_lookup(extracted_features)
    
    # Step 5: Detect anomalous patterns using set logic
    detected_anomalies = detect_anomaly_set(extracted_features)
    
    # Step 6: Compute irrelevant entropy (red herring)
    entropy_metric = compute_entropy([x for x in extracted_features if x > 10])
    
    # Step 7: Generate unused checksum
    test_pattern = [1, 2, 3, 4]
    signal = decode_signal(test_pattern)
    chksum = generate_checksum(test_pattern)
    
    # Step 8: Correlate timestamps (dead code path)
    log_times = [t for t, v in cleaned_logs]
    time_corr = temporal_correlation(log_times)
    
    # Step 9: Process through diagnostic engine
    temp_diagnostic = process_diagnostics(detected_anomalies, feature_lookup, len(extracted_features))
    
    # Step 10: Finalize with obfuscation
    final_diagnostic = finalize_report(temp_diagnostic)
    
    # Output target result
    print(f"Result: {final_diagnostic}")