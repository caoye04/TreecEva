def analyze_signal(x):
    return (x ** 2 + 3 * x + 1) % 100

# Simulated sensor data preprocessing
def preprocess(data):
    cleaned = []
    for val in data:
        if val < 0:
            cleaned.append(abs(val))
        else:
            cleaned.append(val)
    return [v for v in cleaned if v % 2 == 1]  # Keep only odd values

# Auxiliary function with misleading relevance
def calculate_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Core processing pipeline
def validate_sequence(seq):
    if not seq:
        return False
    for i in range(1, len(seq)):
        if seq[i] <= seq[i-1]:
            return False
    return True

def transform_entry(x, shift):
    shifted = (x << 1) + shift
    masked = shifted & 0xFF  # Apply byte mask
    return masked ^ 0xAA  # XOR with magic number

def process_metrics(data, limits):
    # Irrelevant entropy calculation (distractor)
    _ = calculate_entropy(data)
    
    # Preprocess and filter signal
    processed = preprocess(data)
    
    # Generate derived features
    features = []
    for item in processed:
        analyzed = analyze_signal(item)
        transformed = transform_entry(analyzed, len(processed))
        features.append(transformed)
    
    # Misleading branch: appears important but unused
    if len(features) > 5:
        summary = sum(f * f for f in features) // len(features)
        normalized = [f / summary for f in features]
    else:
        baseline = max(features) if features else 1
        adjusted = [f * 1.5 for f in features]
        # Dead code path — never used
        scaled = [int(a * baseline) for a in adjusted]

    # Actual logic: find strictly increasing subsequence
    candidate = []
    for f in sorted(set(features)):
        if f > limits['min_feature'] and f % 3 != 0:
            candidate.append(f)
    
    # Final validation
    if validate_sequence(candidate):
        score = sum(candidate) * len(candidate)
    else:
        score = sum(c for c in candidate if c % 2 == 1) * limits['penalty_factor']
    
    # Key computation
    adjustment_factor = 0.85 if len(candidate) >= 4 else 1.2
    raw_diagnostic = score * adjustment_factor
    final_diagnostic = int(round(raw_diagnostic))

    return final_diagnostic

# Decoy data structures
aux_table = {
    'meta': {'version': '2.1', 'active': False},
    'flags': [0x10, 0x20, 0x30],
    'unused_result': None
}

# Primary input data (simulated biomedical readings)
health_data = [42, -17, 86, 13, 71, -23, 58, 4, 91, 34]

# Threshold configuration
default_thresholds = {
    'min_feature': 40,
    'penalty_factor': 3,
    'debug_mode': False
}

# Unused transformation chain
legacy_mapping = tuple((x % 25) for x in health_data if x > 30)
shadow_buffer = list(reversed(legacy_mapping))

# Trigger point: this line produces the target result
final_diagnostic = process_metrics(health_data, default_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")