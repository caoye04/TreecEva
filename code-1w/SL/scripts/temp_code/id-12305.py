import itertools

# Simulated sensor array data and calibration parameters
def generate_baseline(noise_factor=0.05):
    return [round((i ** 2) * 0.3 + noise_factor * i, 4) for i in range(1, 11)]

def apply_filter(raw_data, kernel_size=3):
    smoothed = []
    for i in range(len(raw_data)):
        start = max(0, i - kernel_size // 2)
        end = min(len(raw_data), i + kernel_size // 2 + 1)
        window = raw_data[start:end]
        smoothed.append(sum(window) / len(window))
    return smoothed

def detect_anomalies(series, sensitivity=2.0):
    mean_val = sum(series) / len(series)
    variance = sum((x - mean_val) ** 2 for x in series) / len(series)
    std_dev = variance ** 0.5
    return [i for i, x in enumerate(series) if abs(x - mean_val) > sensitivity * std_dev]

def transform_coordinates(indices, offset=100):
    # Irrelevant geometric transformation (distractor)
    return [(idx % 7, (idx + offset) % 13) for idx in indices]

def evaluate_entropy(data):
    from math import log2
    freq_map = {}
    for val in data:
        freq_map[val] = freq_map.get(val, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)

def extract_features(signal_stream):
    segments = [signal_stream[i:i+4] for i in range(0, len(signal_stream), 4)]
    features = []
    for seg in segments:
        if len(seg) < 4:
            continue
        peak = max(seg)
        trough = min(seg)
        slope = (seg[-1] - seg[0]) / 3 if len(seg) == 4 else 0
        features.append({'peak': peak, 'trough': trough, 'slope': slope})
    return features

def correlate_patterns(features_list):
    correlations = []
    for i in range(len(features_list) - 1):
        f1, f2 = features_list[i], features_list[i+1]
        corr = (f1['peak'] - f2['trough']) * f1['slope']
        correlations.append(round(corr, 4))
    return correlations

def flag_critical_sections(correlation_series, limit=5.0):
    flags = []
    cumulative = 0
    for i, val in enumerate(correlation_series):
        cumulative += abs(val)
        if cumulative > limit:
            flags.append(i)
            cumulative = 0  # Reset accumulator
    return flags

def compute_resistance_level(flags, base=17):
    # Distractor function: not used in final calculation path
    level = base
    for f in flags:
        level ^= (f * 2 + 1)
    return level

def analyze_signal(pattern_sequence, threshold_set):
    # Core logic begins here — actual answer depends on this
    processed_patterns = []
    for p in pattern_sequence:
        shifted = [x * 1.5 for x in p if x > threshold_set[0]]
        filtered = apply_filter(shifted)
        anomalies = detect_anomalies(filtered, sensitivity=threshold_set[1])
        processed_patterns.append(anomalies)
    
    # Flatten using itertools (required language feature)
    flat_indices = list(itertools.chain.from_iterable(processed_patterns))
    
    # Use enumerate and zip together (required features)
    indexed_scan = [(i, val) for i, val in enumerate(flat_indices) if val % 3 == 0]
    paired_data = list(zip([x[0] for x in indexed_scan], [x[1]*2 for x in indexed_scan]))
    
    # Real computation path
    unique_contributions = set()
    for a, b in paired_data:
        intermediate = (a * 7 + b * 3) % 101
        unique_contributions.add(intermediate)
    
    # Final deterministic result
    final_score = sum(unique_contributions) * 19
    
    # This variable is printed and queried
    final_diagnostic = final_score
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Generate real input
    base_data = generate_baseline(noise_factor=0.08)
    patterns = [base_data[i:i+5] for i in range(0, len(base_data), 5)]
    
    # Threshold configuration
    thresholds = [2.0, 1.8]  # Used in analyze_signal
    
    # Dead code paths (distractors)
    raw_entropy = evaluate_entropy(base_data)
    coords = transform_coordinates(list(range(10)), offset=205)
    feature_set = extract_features(base_data)
    corr_vals = correlate_patterns(feature_set)
    critical_marks = flag_critical_sections(corr_vals, limit=4.5)
    resistance = compute_resistance_level(critical_marks, base=23)
    
    # Actual target computation
    final_diagnostic = analyze_signal(patterns, thresholds)
    print(f"Result: {final_diagnostic}")