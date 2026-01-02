from itertools import combinations

# Simulate sensor readings and anomaly detection in an environmental monitoring system
def generate_noise(length):
    return [i % 7 + (i * 0.5) for i in range(length)]

def filter_outliers(data, limit=50):
    return [x for x in data if x < limit]

def count_peaks(signal):
    peaks = 0
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks += 1
    return peaks

def evaluate_stability(metric):
    # Irrelevant helper function - not used in final computation
    return metric ** 2 < 1000

def analyze_pattern(readings, config):
    # Step 1: Preprocess sequence by filtering and thresholding
    processed = [val for val in readings if abs(val) > config['min_signal']]
    
    # Distractor: unused intermediate calculation
    smoothed = [sum(processed[i:i+3]) / 3 for i in range(len(processed)-2)] if len(processed) > 2 else processed
    
    # Step 2: Detect repeating sub-patterns using string-like encoding
    encoded = ''.join(['H' if x > config['high_threshold'] else 'L' for x in processed])
    
    # Step 3: Count occurrences of specific pattern 'HLH' (critical)
    pattern_count = 0
    for i in range(len(encoded) - 2):
        if encoded[i:i+3] == 'HLH':
            pattern_count += 1
    
    # Step 4: Use itertools to find all length-2 index pairs where values exceed dynamic threshold
    indices = [i for i, val in enumerate(processed) if val > config['high_threshold']]
    significant_pairs = list(combinations(indices, 2))
    
    # Step 5: Compute diagnostic score based on pattern_count and pair density
    pair_density = len(significant_pairs) / (len(processed) or 1)
    raw_score = pattern_count * 100 + int(pair_density * 100)
    
    # Step 6: Apply correction factor based on peak count in original signal
    correction = count_peaks(readings) * 5
    final_score = raw_score - correction
    
    # Step 7: Final adjustment using modulo arithmetic to simulate cyclic calibration
    final_diagnostic = (final_score + 11) % 97
    
    return final_diagnostic

# Main execution
sequence = generate_noise(40)
sequence[5] += 20
sequence[12] -= 15
sequence[22] += 18
sequence[35] -= 12

# Misleading auxiliary transformation (not affecting result)
temp_adjusted = [round(x * 1.03, 2) for x in sequence]

thresholds = {
    'min_signal': 3.0,
    'high_threshold': 15.0
}

# Key statement
final_diagnostic = analyze_pattern(sequence, thresholds)
print(f"Result: {final_diagnostic}")