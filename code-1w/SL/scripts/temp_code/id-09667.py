from collections import defaultdict, Counter

# Simulated sensor data processing pipeline with diagnostic analysis
def preprocess_stream(raw_points):
    processed = []
    for p in raw_points:
        if p < -100 or p > 100:
            continue
        processed.append(abs(p) ** 0.5)
    return processed

def generate_signature(values):
    sig = 0
    for v in values[:10]:
        sig ^= int(v * 10) & 255
    return sig

def filter_anomalies(data_seq):
    counts = Counter(data_seq)
    threshold = len(data_seq) * 0.02
    return [d for d in data_seq if counts[d] > threshold]

def build_hierarchy(items):
    tree = defaultdict(list)
    for i, item in enumerate(items):
        level = i % 4
        tree[level].append(item * (level + 1))
    return tree

def extract_features(dataset):
    features = []
    for i in range(0, len(dataset), 3):
        chunk = dataset[i:i+3]
        if len(chunk) == 3:
            features.append(sum(x ** 2 for x in chunk))
    return features

def compute_margins(values):
    margins = []n    for i in range(1, len(values)):
        margins.append(values[i] - values[i-1])
    return margins

def derive_weights(margins):
    total = sum(abs(m) for m in margins)
    return [m / total for m in margins] if total != 0 else [1/len(margins)] * len(margins)

def aggregate_score(weights, features):
    return sum(w * f for w, f in zip(weights, features))

def shift_sequence(seq, key):
    # Irrelevant transformation - red herring
    rotated = seq[-key:] + seq[:-key]
    return [x ^ key for x in rotated]

def validate_integrity(data):
    # Dead code path - never actually used in final computation
    checksum = 0
    for i, val in enumerate(data):
        checksum += val * (i + 1)
    return checksum % 1024

def temporal_align(signal):
    # Unused function - distractor
    aligned = []
    for i, s in enumerate(signal):
        aligned.append(s * (i % 5 + 1))
    return aligned

def dummy_enhancement(arr):
    # Decoy operation with no impact
    enhanced = [a + 10 for a in arr]
    return enhanced

def classify_regime(score):
    if score < 50:
        return 'STABLE'
    elif score < 100:
        return 'VOLATILE'
    else:
        return 'CRITICAL'

def analyze_pattern(clean_data, config_map):
    # Core logic begins
    feat = extract_features(clean_data)
    margin_diffs = compute_margins(feat)
    norm_weights = derive_weights(margin_diffs)
    
    # Introduce slicing distraction
    subset = clean_data[::2]
    alt_analysis = [x * 1.5 for x in subset]  # unused branch
    
    # Actual critical calculation
    primary_score = aggregate_score(norm_weights, feat)
    
    # Bitwise interference - misleading but irrelevant
    magic_key = 0
    for x in feat:
        magic_key ^= int(x) & 15
    
    # Final decision logic
    if primary_score > config_map['critical_threshold']:
        adjusted = primary_score * 0.85
    else:
        adjusted = primary_score * 1.15
    
    return int(adjusted)

# Main execution flow
if __name__ == '__main__':
    # Initial sensor readings (simulated)
    raw_readings = [
        85, -120, 44, 76, 92, -55, 33, 67, 81, 90,
        22, 54, 63, 77, 88, 41, 69, 74, 58, 66,
        73, 82, 59, 68, 79, 91, 64, 75, 86, 57
    ]

    # Irrelevant constants and configurations
    calibration_matrix = [[i*j for j in range(5)] for i in range(5)]
    baseline_offset = sum(sum(row) for row in calibration_matrix) / 25

    # Real preprocessing
    cleaned_signal = preprocess_stream(raw_readings)
    
    # Signature generation - red herring
    device_fingerprint = generate_signature(cleaned_signal)
    
    # Filtering step
    filtered_data = filter_anomalies([int(x) for x in cleaned_signal])
    
    # Hierarchical organization - partially relevant
    structured_levels = build_hierarchy(filtered_data)
    flattened = []
    for level in sorted(structured_levels.keys()):
        flattened.extend(structured_levels[level])
    
    # Transform via feature extraction
    transformed_data = extract_features(flattened)
    
    # Configuration map with decoy entries
    threshold_map = {
        'stable_threshold': 30,
        'warning_ceiling': 75,
        'critical_threshold': 90,
        'heartbeat_interval': 250,  # irrelevant
        'retry_limit': 3           # irrelevant
    }
    
    # Secondary analysis path (unused)
    margins_test = compute_margins(transformed_data)
    weights_test = derive_weights(margins_test)
    test_result = aggregate_score(weights_test, transformed_data)
    regime = classify_regime(test_result)
    
    # Core diagnostic call
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")