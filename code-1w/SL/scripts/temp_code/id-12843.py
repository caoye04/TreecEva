import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_signals(raw_readings):
    filtered = [x for x in raw_readings if x > -50 and x < 50]
    baseline = sum(filtered) / len(filtered)
    normalized = [round(x - baseline, 3) for x in filtered]
    return normalized

# Irrelevant transformation - decoy function
def compress_signal(data):
    compressed = []
    for i in range(0, len(data), 3):
        chunk = data[i:i+3]
        if len(chunk) == 3:
            compressed.append(chunk[0] * chunk[1] + chunk[2])
    return compressed  # Never used in final path

# Core pattern extraction logic
def extract_features(signal_sequence):
    diffs = [abs(signal_sequence[i+1] - signal_sequence[i]) for i in range(len(signal_sequence)-1)]
    peaks = [i for i in range(1, len(diffs)-1) if diffs[i] > diffs[i-1] and diffs[i] > diffs[i+1]]
    return {'peaks': len(peaks), 'total_variation': round(sum(diffs), 3)}

# Data transformation with distractors
def transform_dataset(features_dict, mode='standard'):
    temp_result = {}
    scaling_factor = 3.14159 if mode == 'enhanced' else 1.0
    offset = 100

    # Distractor computation
    fake_moment = 0
    for i in range(5):
        fake_moment += (i + 1) * 1000
    fake_moment = fake_moment // 7  # Dead-end value

    temp_result['adjusted_peaks'] = features_dict['peaks'] * 2 + 1
    temp_result['smoothed_variation'] = round(features_dict['total_variation'] * scaling_factor, 3)
    
    # Unused branch
    if mode == 'experimental':
        temp_result['special_metric'] = temp_result['smoothed_variation'] / (temp_result['adjusted_peaks'] + 1)
    
    return temp_result

# Main analysis with conditional logic and set operations
def analyze_patterns(processed_data, criteria):
    feature_set_a = {i for i in range(len(processed_data)) if processed_data[i] > criteria['threshold_a']}
    feature_set_b = {i for i in range(len(processed_data)) if processed_data[i] < criteria['threshold_b']}
    
    intersection_size = len(feature_set_a & feature_set_b)
    symmetric_diff_size = len(feature_set_a ^ feature_set_b)
    
    # Complex conditional expression with misleading branches
    base_score = intersection_size * 17 if intersection_size > 5 else (symmetric_diff_size * 3 if symmetric_diff_size > 20 else 42)
    
    adjustment = 0
    # Nested conditionals with decoy logic
    if base_score > 100:
        adjustment += 10
        temp_cache = []
        for combo in itertools.combinations([1, 2, 3], 2):
            temp_cache.append(combo[0] * combo[1])
        adjustment -= len(temp_cache) % 7  # Irrelevant subtraction
    elif base_score < 50:
        adjustment -= 5
        # Dead code path
        for _ in range(3):
            adjustment *= 1.1
    else:
        adjustment += 3
    
    final_score = base_score + adjustment
    
    # Decoy variable that looks important but isn't used
    diagnostic_trace = {
        'raw_intersections': list(feature_set_a & feature_set_b),
        'computed_at': 'midnight',
        'status': 'nominal'
    }
    
    # Final result influenced by multiple abstraction layers
    final_diagnostic = final_score * 10 + len(diagnostic_trace['status'])
    
    return final_diagnostic

# Primary execution flow
if __name__ == '__main__':
    # Initial sensor readings (simulated input)
    sensor_log = [
        10.5, -20.3, 30.7, -40.2, 15.8, 25.1, -35.6, 45.9,
        -12.4, 18.3, -28.7, 38.2, -48.1, 5.9, -15.4, 22.8,
        -32.9, 42.7, -45.3, 3.1, -23.6, 33.4, -38.8, 48.5
    ]
    
    # Preprocess step
    cleaned_signal = preprocess_signals(sensor_log)
    
    # Extract core features
    signal_features = extract_features(cleaned_signal)
    
    # Transform data (with unused mode)
    transformed_data = transform_dataset(signal_features, mode='standard')
    
    # Define thresholds for analysis
    config_thresholds = {
        'threshold_a': 5.0,
        'threshold_b': -5.0
    }
    
    # Critical statement: compute final diagnostic
    final_diagnostic = analyze_patterns(transformed_data, config_thresholds)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")