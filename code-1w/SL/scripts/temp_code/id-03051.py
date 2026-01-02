def transform_signal(raw_values, scale_factor):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    transformed = []
    for v in raw_values:
        if v < 0:
            transformed.append(-1 * (abs(v) ** 0.5))
        else:
            transformed.append(v ** 0.5)
    return [round(x * scale_factor, 3) for x in transformed]


def validate_checksum(data_str):
    """Compute ASCII checksum for data integrity (irrelevant but plausible)"""
    total = 0
    for char in data_str:
        total += ord(char)
    return total % 256


def extract_features(signal_sequence):
    """Extract statistical features from signal (mixed relevance)"""
    n = len(signal_sequence)
    mean_val = sum(signal_sequence) / n
    variance = sum((x - mean_val) ** 2 for x in signal_sequence) / n
    peak = max(abs(x) for x in signal_sequence)
    
    # Distractor: unused advanced metric
    entropy = 0
    for x in signal_sequence:
        prob = (x - min(signal_sequence) + 1) / (sum(signal_sequence) + len(signal_sequence))
        if prob > 0:
            entropy -= prob * __import__('math').log(prob, 2)
            
    return {
        'mean': round(mean_val, 4),
        'variance': round(variance, 4),
        'peak': peak,
        'range': max(signal_sequence) - min(signal_sequence)
    }


def filter_outliers(data_list, factor=1.5):
    """Remove outliers using IQR method (partially relevant)"""
    sorted_data = sorted(data_list)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    
    filtered = [x for x in data_list if lower_bound <= x <= upper_bound]
    outlier_count = len(data_list) - len(filtered)
    
    # Dead code path (never used)
    if outlier_count > 10:
        fallback = sorted_data[5:-5]
        return fallback
        
    return filtered


def aggregate_metrics(feature_maps):
    """Combine multiple feature sets into summary scores (red herring)"""
    combined_score = 0.0
    weights = {'mean': 0.1, 'variance': 0.3, 'peak': 0.4, 'range': 0.2}
    for fm in feature_maps:
        for key in weights:
            if key in fm:
                combined_score += fm[key] * weights[key]
    return round(combined_score, 3)


def analyze_readings(data_entries, config_map):
    """Core analysis logic: count valid high-frequency events above dynamic thresholds"""
    event_counter = 0
    
    # Real threshold logic
    base_threshold = config_map['primary']
    adaptive_boost = len([x for x in data_entries if x > config_map['secondary']]) // 3
    dynamic_limit = base_threshold + adaptive_boost
    
    # Actual critical logic
    for entry in data_entries:
        # Only positive odd values above dynamic limit trigger increment
        if entry > 0 and entry % 2 == 1 and entry > dynamic_limit:
            event_counter += 1
            
        # Early termination red herring (never triggered in this input)
        if entry == -999:
            return -1
    
    # Secondary rule: if counter is even, add bonus from metadata
    bonus_flag = config_map.get('bonus_active', False)
    if event_counter % 2 == 0 and bonus_flag:
        event_counter += config_map['bonus_value']
    
    return event_counter

# Main execution block
if __name__ == "__main__":
    # Simulated raw sensor input (distractor)
    raw_sensor_stream = [127, -45, 89, 201, 153, -67, 94, 112, 188, 203]
    scaled_signal = transform_signal(raw_sensor_stream, 1.732)
    
    # Checksum validation (completely irrelevant)
    stream_tag = "SENSOR_GROUP_7"
    checksum = validate_checksum(stream_tag)
    
    # Feature extraction chain
    features_list = []    
    for i in range(0, len(scaled_signal), 3):
        chunk = scaled_signal[i:i+3]
        if len(chunk) == 3:
            feat = extract_features(chunk)
            features_list.append(feat)
    
    # Filtering step with distractor
    flat_values = [v for d in features_list for k, v in d.items() if k in ['mean', 'peak']]
    cleaned_metrics = filter_outliers(flat_values, 2.0)
    
    # Irrelevant aggregation
    aggregated_diagnostic = aggregate_metrics(features_list)
    
    # Critical data preparation (real path)
    processed_data = []
    for val in raw_sensor_stream:
        if val > 0:
            processed_data.append(val % 100)  # map to 0-99
        else:
            processed_data.append(abs(val) % 25)  # different mapping
    
    # Configuration map with meaningful and decoy keys
    threshold_map = {
        'primary': 45,
        'secondary': 30,
        'bonus_active': True,
        'bonus_value': 3,
        'debug_mode': False,
        'retry_limit': 5,
        'timeout_ms': 250
    }
    
    # Final analysis - this is where the answer is computed
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    print(f"Result: {final_diagnostic}")