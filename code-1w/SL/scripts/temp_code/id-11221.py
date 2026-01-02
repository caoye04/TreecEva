def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    normalized = [round(x - baseline, 3) for x in filtered]
    return normalized


def generate_reference(size):
    pattern = []
    for i in range(size):
        if i % 5 == 0:
            pattern.append((i * 3) % 25)
        elif i % 3 == 0:
            pattern.append((i * 7) % 19)
        else:
            pattern.append(i % 7)
    return pattern

# Irrelevant auxiliary function (dead code path)
def deprecated_checksum(data):
    acc = 0
    for val in data:
        acc = (acc + val) * 7 % 13
    return acc

# Another decoy function with misleading logic
def evaluate_coherence(sequence):
    score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            score += 1
        elif sequence[i] == sequence[i-1]:
            score -= 1
    return score * len(sequence)

# Core diagnostic logic
def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Signal transformation with red herring variables
def extract_features(signal):
    magnitude_peak = max(signal, default=0)
    magnitude_trough = min(signal, default=0)
    zero_crossings = 0
    for i in range(1, len(signal)):
        if signal[i-1] < 0 <= signal[i] or signal[i-1] >= 0 > signal[i]:
            zero_crossings += 1
    
    # Distractor computation
    cumulative_drift = sum(signal[i+1] - signal[i] for i in range(len(signal)-1))
    
    # Real feature used downstream
    avg_magnitude = sum(abs(x) for x in signal) / len(signal) if signal else 0
    return {
        'peak': magnitude_peak,
        'trough': magnitude_trough,
        'zero_crossings': zero_crossings,
        'avg_mag': avg_magnitude,
        'drift': cumulative_drift  # unused later
    }

# Main analysis with conditional branching and list comprehension
def analyze_threshold(readings, template):
    readings_set = set(readings)
    template_set = set(template)
    intersection_size = len(readings_set & template_set)
    
    # Conditional expression used
    base_score = intersection_size * 10 if intersection_size > 5 else intersection_size * 3
    
    # Bitwise manipulation as red herring
    masked_score = base_score ^ 255
    inverted = ~masked_score & 0xFF
    
    # Actual logic: entropy-based adjustment
    if len(readings) > 0:
        entropy_value = compute_entropy(readings)
        adjustment_factor = 1 + (entropy_value / 10)
        final_score = base_score * adjustment_factor
    else:
        final_score = base_score
    
    # Multiple assignments (some irrelevant)
    status_code, final_status, final_diagnostic = 200, 'OK', int(round(final_score))
    
    # Dead assignment (distractor)
    final_status = 'ANALYZED' if final_score > 100 else 'PENDING'
    
    return final_diagnostic

# Entry point with realistic context: sensor diagnostics
if __name__ == '__main__':
    # Simulated input data
    raw_input_stream = [12, -8, 33, 41, -22, 17, 33, 9, 12, 41, 55, -8, 17, 9, 33, 41, 12]
    
    # Irrelevant preprocessing result (distractor)
    processed_buffer = preprocess_signal(raw_input_stream)
    
    # Feature extraction (partially relevant)
    features = extract_features(processed_buffer)
    
    # Reference pattern generation (used)
    reference_pattern = generate_reference(15)
    
    # Diagnostic vector derived from features
    diagnostics = [
        features['peak'],
        features['trough'],
        features['avg_mag'],
        features['zero_crossings']
    ]
    
    # Key statement where answer is determined
    final_diagnostic = analyze_threshold(diagnostics, reference_pattern)
    
    # Output result
    print(f"Target result: {final_diagnostic}")