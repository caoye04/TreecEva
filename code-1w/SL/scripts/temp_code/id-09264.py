import itertools

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant transformation - distractor
def frequency_shift(signal, shift=2):
    return [(val * 1.05) ** 2 for val in signal]

# Unused function - dead code path (distractor)
def legacy_compatibility_layer(data):
    return {i: round(v * 0.99, 3) for i, v in enumerate(data)}

# Signal pattern extractor - relevant
def extract_patterns(seq):
    patterns = []
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] > seq[i+2]:  # Local maxima
            patterns.append(int(abs(seq[i+1]) * 1000))
    return patterns

# Bit manipulation for checksum - relevant
def compute_checksum(values):
    checksum = 0
    for v in values:
        checksum ^= v  # XOR all pattern values
        checksum = (checksum << 1) & 0xFFFF  # Left shift with mask
    return checksum

# Secondary analysis - misleading intermediate result
def evaluate_coherence(patterns):
    if not patterns:
        return 0
    avg = sum(patterns) / len(patterns)
    variance = sum((x - avg) ** 2 for x in patterns) / len(patterns)
    return round(variance / 1000, 4)

# Main analysis function - critical
def analyze_signal(buffer, threshold):
    raw_peaks = [x for x in buffer if x > threshold]
    if len(raw_peaks) < 3:
        return -1
    
    # Generate sliding triplets
    triplets = list(itertools.combinations([int(p*100) for p in raw_peaks], 3))
    valid_triplets = [t for t in triplets if (t[2] - t[0]) > 50]
    
    # Destructuring assignment - relevant
    first_sum, second_sum, third_sum = 0, 0, 0
    for a, b, c in valid_triplets[:10]:  # Limit to first 10
        first_sum += a
        second_sum += b
        third_sum += c
    
    # Complex conditional logic
    adjustment_factor = 0
    if first_sum > 500:
        if second_sum % 2 == 0:
            adjustment_factor = 3
        else:
            adjustment_factor = -2
    else:
        adjustment_factor = 1
    
    # Final computation chain
    base_score = (third_sum // 7) + (len(valid_triplets) * adjustment_factor)
    final_correction = base_score ^ 0xABCD  # Bitwise XOR with fixed key
    return final_correction

# Simulated input data
sensor_input = [-0.5, 0.2, 1.3, 0.4, 1.8, 0.3, 1.6, 0.9, 2.1, 0.25, 1.9, 0.8]
tmp_results = {}

# Preprocessing stage
processed_signal = preprocess_signal(sensor_input)
activation_threshold = 0.5

# Extract temporal patterns
pattern_list = extract_patterns(processed_signal)
signal_checksum = compute_checksum(pattern_list)  # Decoy usage

# Misleading coherence metric
coherence_metric = evaluate_coherence(pattern_list)

# Key data structure transformation
pattern_buffer = [x / 100.0 for x in pattern_list if x > 100]

# Dead code - irrelevant dictionary construction
stats_summary = {
    'count': len(pattern_list),
    'checksum': signal_checksum,
    'coherence': coherence_metric,
    'peak_ratio': len([x for x in processed_signal if x > 0.7]) / len(processed_signal)
}

# Noise injection simulation - unused
augmented_buffer = [x + 0.01 for x in pattern_buffer]

# Critical execution point
final_diagnostic = analyze_signal(pattern_buffer, activation_threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")