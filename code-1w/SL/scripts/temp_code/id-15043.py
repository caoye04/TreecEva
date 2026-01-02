def preprocess_signal(raw_data, filter_threshold):
    filtered = []
    magnitude_sum = 0
    temp_cache = {}
    for i, val in enumerate(raw_data):
        if abs(val) > filter_threshold:
            corrected = val * 0.9 if val > 0 else val * 1.1
            filtered.append(int(corrected))
            magnitude_sum += abs(corrected)
            temp_cache[i] = magnitude_sum
    return filtered, magnitude_sum, temp_cache


def generate_reference_map(base_values):
    ref_map = {}
    for idx, v in enumerate(base_values):
        ref_map[v] = (idx ** 2) % 7
    return ref_map


def validate_integrity(check_sequence):
    if len(check_sequence) < 5:
        return False
    cumulative = 0
    for x in check_sequence:
        cumulative += x % 3
    return cumulative % 2 == 0


def extract_features(data_stream):
    features = []n    running_max = -float('inf')
    count_peaks = 0
    for i in range(1, len(data_stream) - 1):
        if data_stream[i] > data_stream[i-1] and data_stream[i] > data_stream[i+1]:
            count_peaks += 1
            running_max = max(running_max, data_stream[i])
            features.append((i, data_stream[i]))
    return features, count_peaks, running_max


def compute_entropy(values):
    from math import log2
    freq = {}
    total = len(values)
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)


def analyze_pattern(signal, config_thresholds):
    # Irrelevant pre-analysis (distractor)
    decoy_analysis = set()
    for t in config_thresholds:
        decoy_analysis.add(t % 13)
    
    # Real preprocessing
    processed_signal, total_energy, _ = preprocess_signal(signal, 3)
    
    # Misleading feature extraction (partially unused)
    peak_features, num_peaks, highest_peak = extract_features(processed_signal)
    
    # Decoy integrity validation
    is_valid = validate_integrity(processed_signal)
    
    # Dummy reference map (red herring)
    dummy_ref = generate_reference_map([1, 2, 4, 8, 16])
    
    # Core logic: find repeating triplets
    triplet_count = {}
    for i in range(len(processed_signal) - 2):
        triplet = tuple(processed_signal[i:i+3])
        triplet_count[triplet] = triplet_count.get(triplet, 0) + 1
    
    # Identify frequent patterns
    frequent_triplets = {k: v for k, v in triplet_count.items() if v >= 2}
    
    # Compute auxiliary metrics (some irrelevant)
    avg_value = sum(processed_signal) / len(processed_signal)
    mode_value = max(set(processed_signal), key=processed_signal.count)
    
    # Final diagnostic based on pattern entropy
    pattern_keys = list(frequent_triplets.keys())
    if not pattern_keys:
        pattern_entropy = 0.0
    else:
        flattened = []
        for t in pattern_keys:
            flattened.extend(t)
        pattern_entropy = compute_entropy(flattened)
    
    # Key distraction: redundant set operations
    s1 = set(range(5, 15))
    s2 = set(range(10, 20))
    overlap = s1 & s2
    diff = s1 - s2
    union_size = len(s1 | s2)
    
    # Actual final computation (non-obvious)
    base_score = len(frequent_triplets) * 100
    adjustment = int(abs(avg_value - mode_value))
    final_diagnostic = base_score - adjustment
    
    # Dead code path (never executed)
    if False:
        fallback = 0
        for k in dummy_ref:
            fallback += k * dummy_ref[k]
        final_diagnostic = fallback
    
    return final_diagnostic

# Main execution
raw_input_signal = [7, -5, 12, 8, -6, 7, -5, 12, 9, -4, 7, -5, 12, 8, -6]
threshold_settings = [1, 4, 9, 16, 25, 36]

# Execute main analysis
final_diagnostic = analyze_pattern(raw_input_signal, threshold_settings)

print(f"Result: {final_diagnostic}")