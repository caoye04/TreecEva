from itertools import combinations

# Simulate sensor data analysis with weighted metric evaluation
def analyze_sensor_drift(readings):
    baseline = sum(readings[:5]) / 5
    drifts = [(r - baseline) ** 2 for r in readings[5:]]
    return sum(drifts) / len(drifts)

def extract_features(sequence):
    # Extract statistical features from character sequence
    char_freq = {c: sequence.count(c) for c in set(sequence)}
    unique_count = len(char_freq)
    repeat_penalty = sum(1 for v in char_freq.values() if v > 2)
    return unique_count - repeat_penalty

def compute_entropy(data_list):
    # Dummy entropy-like calculation (not real Shannon entropy)
    total = sum(data_list)
    if total == 0:
        return 0.0
    normalized = [x / total for x in data_list]
    return sum(x * x for x in normalized)

# Main processing pipeline
raw_data = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]  # ASCII for "hello world"
char_sequence = ''.join(chr(x) for x in raw_data if 32 <= x <= 126)

# Irrelevant transformation (distractor)
doubled_pairs = [(x, x*2) for x in raw_data]
processed_pairs = list(map(lambda p: (p[0]+1, p[1]-1), doubled_pairs))

# Feature extraction
feature_set = [
    len(char_sequence),
    extract_features(char_sequence),
    analyze_sensor_drift(raw_data),
    compute_entropy(raw_data)
]

# Weight configuration (some weights are misleading)
weights = {
    'length': 0.4,
    'uniqueness': 0.3,
    'drift': 0.2,
    'entropy': 0.1,
    'dummy': 0.0  # Unused weight (red herring)
}

# Generate all possible 2-char substrings (distractor computation)
substrings = [''.join(p) for p in combinations(char_sequence, 2)]
substring_count = len(substrings)  # Not used later

# Slice manipulation to derive auxiliary metric
rotated_slice = raw_data[3:] + raw_data[:3]
oscillation_metric = sum(abs(rotated_slice[i] - rotated_slice[i-1]) for i in range(1, len(rotated_slice)))

# Normalize features using slicing and lambda
normalizers = list(map(lambda x: max(x, 1), feature_set))
normalized_features = [f/n for f, n in zip(feature_set, normalizers)]

# Key metrics for evaluation
metrics = {
    'length': normalized_features[0],
    'uniqueness': normalized_features[1],
    'drift': 1 / (1 + feature_set[2]),  # Inverse relationship
    'entropy': feature_set[3]
}

# Final performance evaluation
redundant_calc = sum(1 for c in char_sequence if c in 'aeiou') * 0.05  # Distractor

def evaluate_performance(mets, wts):
    score = 0.0
    for key in mets:
        if key in wts:
            score += mets[key] * wts[key]
    # Additional logic that looks important but isn't impactful due to normalization
    if score > 0.5:
        adjustment = (score - 0.5) * 0.1
        score -= adjustment
    return int(score * 1000)  # Scale to integer

final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")