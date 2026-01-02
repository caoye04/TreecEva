def preprocess_signals(raw_data):
    filtered = [x * 0.9 for x in raw_data if x > 0]
    normalized = [y / max(filtered) for y in filtered]
    return normalized


def calculate_bands(signal):
    low_freq = sum(x for x in signal if x < 0.3)
    mid_freq = sum(x for x in signal if 0.3 <= x < 0.7)
    high_freq = sum(x for x in signal if x >= 0.7)
    return (low_freq, mid_freq, high_freq)


def validate_input(data, schema):
    if len(data) != schema['length']:
        return False
    if not all(isinstance(x, float) for x in data):
        return False
    return True


def compute_entropy(values):
    import math
    entropy = 0.0
    total = sum(values)
    if total == 0:
        return 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 6)


def extract_features(dataset):
    # Irrelevant preprocessing path (distractor)
    temp_log = []
    for i, record in enumerate(dataset):
        if i % 3 == 0:
            temp_log.append(f"Skipped index {i}")
        else:
            temp_log.append(f"Processed {record}")
    
    # Real feature extraction
    magnitudes = [sum(row) for row in dataset]
    variances = [sum((x - sum(row)/len(row))**2 for x in row) for row in dataset]
    return magnitudes, variances


def analyze_metrics(health_trace, config):
    # Misleading intermediate calculations
    baseline_shift = sum(health_trace) / len(health_trace)
    adjusted_trace = [x - baseline_shift + config['offset'] for x in health_trace]
    
    # Dead code branch (never executed due to fixed condition)
    diagnostic_flags = []
    if len(adjusted_trace) > 1000:  # Impossible under current inputs
        diagnostic_flags.append('OVERFLOW')
    else:
        diagnostic_flags.append('NORMAL')
    
    # Core logic disguised among distractors
    segment_a = adjusted_trace[:len(adjusted_trace)//2]
    segment_b = adjusted_trace[len(adjusted_trace)//2:]
    
    avg_a = sum(segment_a) / len(segment_a) if segment_a else 0
    avg_b = sum(segment_b) / len(segment_b) if segment_b else 0
    
    trend_score = (avg_b - avg_a) * config['sensitivity']
    
    # Red herring: unused complex transformation
    transformed = [abs(x)**0.5 * (-1 if x < 0 else 1) for x in adjusted_trace]
    secondary_index = sum(transformed[i] * transformed[-i-1] for i in range(len(transformed)//4))
    
    # Conditional expression determining final output
    stability_metric = compute_entropy([abs(avg_a), abs(avg_b), abs(trend_score)])
    final_diagnostic = trend_score if stability_metric > 0.5 else (avg_a + avg_b) * 1000
    
    # Decoy assignment with slicing that does nothing
    shadow_copy = [0] * len(health_trace)
    shadow_copy[::2] = [777] * (len(shadow_copy)//2)
    
    return final_diagnostic

# Simulated sensor input (real data)
raw_sensor_feed = [-2.0, -1.0, 0.5, 1.2, 0.8, 1.6, -0.3, 0.9, 1.1, 0.7]

# Unused validation schema (distractor)
schema_rules = {
    'length': 15,
    'dtype': 'float',
    'range': (-5.0, 5.0)
}

# Main processing pipeline
if __name__ == "__main__":
    cleaned = preprocess_signals(raw_sensor_feed)
    
    # Distractor: irrelevant band analysis
    power_bands = calculate_bands(cleaned)
    
    # Feature extraction on dummy structure (partially irrelevant)
    dummy_dataset = [[x*0.8, x*1.2] for x in cleaned]
    features = extract_features(dummy_dataset)
    
    # Critical configuration map with red herring entries
    threshold_map = {
        'offset': 0.1,
        'sensitivity': 5.0,
        'decay_rate': 0.95,
        'max_iter': 10,
        'padding': 3
    }
    
    # Actual health vector used in computation
    health_vector = [x**2 for x in cleaned]
    
    # Key execution point
    final_diagnostic = analyze_metrics(health_vector, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")