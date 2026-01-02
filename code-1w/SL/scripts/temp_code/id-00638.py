def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def compute_entropy(values):
    from math import log2
    frequency = {}
    for v in values:
        freq_key = int(v * 10)
        frequency[freq_key] = frequency.get(freq_key, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in frequency.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def generate_checksum(sequence):
    # Irrelevant function - red herring
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) + i
    return checksum


def rolling_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        smoothed.append(sum(data[i:i+window]) / window)
    return smoothed


def extract_features(signal):
    peaks = [signal[i] for i in range(1, len(signal)-1) if signal[i-1] < signal[i] > signal[i+1]]
    troughs = [signal[i] for i in range(1, len(signal)-1) if signal[i-1] > signal[i] < signal[i+1]]
    peak_avg = sum(peaks) / len(peaks) if peaks else 0.0
    feature_set = {
        'peak_mean': peak_avg,
        'trough_count': len(troughs),
        'amplitude': max(signal) - min(signal),
        'zero_crossings': sum(1 for i in range(1, len(signal)) if signal[i-1] * signal[i] < 0)
    }
    return feature_set


def validate_calibration(calib_sequence):
    # Dead code path - never actually used
    if len(calib_sequence) < 5:
        return False
    sorted_seq = sorted(calib_sequence)
    return all(abs(a - b) < 0.01 for a, b in zip(calib_sequence, sorted_seq))


def recursive_transform(seq, depth=0):
    if depth >= 3 or len(seq) < 2:
        return seq[0] if seq else 0
    transformed = [seq[i] + seq[i+1] * (0.5 ** depth) for i in range(len(seq)-1)]
    return recursive_transform(transformed, depth + 1)


def analyze_readings(data_segments, config_map):
    results = []
    threshold = config_map['primary']
    for segment in data_segments[:5]:  # Only process first 5 segments
        entropy_val = compute_entropy(segment)
        features = extract_features(segment)
        score = 0
        
        if features['amplitude'] > threshold:
            score += 30
        if entropy_val > 2.0:
            score += 20
        if features['zero_crossings'] > 8:
            score += 25
            
        # Misleading intermediate calculation
        dummy_weight = sum(features.values()) * 0.01
        
        results.append(score)
    
    # Key computation - aggregate across segments
    base_result = sum(results)
    adjustment = int(recursive_transform(results))
    final_score = base_result - adjustment
    
    # Distractor: unused but plausible-looking normalization
    if final_score > 100:
        final_score = 100 - (final_score % 10)
    
    return final_score

# Main execution
raw_input_data = [
    0.0, 0.15, -0.22, 0.33, -0.12, 0.45, -0.38, 0.29, -0.11, 0.51,
    -0.44, 0.37, -0.21, 0.62, -0.55, 0.48, -0.31, 0.73, -0.66, 0.59
]

# Irrelevant calibration data - distractor
calibration_refs = [0.11, 0.12, 0.13, 0.14, 0.15]
dummy_hash = sum(int(x*100) for x in calibration_refs) ^ 0xABCD

# Preprocess and segment
cleaned = preprocess_signal(raw_input_data)
smoothed = rolling_average(cleaned, 2)
data_windows = [smoothed[i:i+4] for i in range(0, len(smoothed), 4) if len(smoothed[i:i+4]) == 4]

# Feature extraction (partially irrelevant)
all_features = [extract_features(window) for window in data_windows]
feature_summary = {"avg_peak": sum(f['peak_mean'] for f in all_features) / len(all_features)}

# Threshold configuration map (used in analysis)
threshold_map = {
    'primary': 0.65,
    'backup': 0.75,
    'aux': 0.45
}

# Process each window through full pipeline
processed_data = []
for win in data_windows:
    processed = preprocess_signal(win + [0.0] * 2)  # Padding to affect filtering
    processed_data.append(processed)

# Key statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")