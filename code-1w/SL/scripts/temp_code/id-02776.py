import math

# Simulated sensor data processing with noise filtering and pattern analysis
def generate_signal(base, length):
    return [(base * (i + 1)) % 127 for i in range(length)]

def apply_noise(data, intensity=3):
    return [d ^ intensity for d in data]  # Bitwise XOR as noise

def extract_peaks(signal, min_magnitude):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > min_magnitude:
            peaks.append(signal[i])
    return peaks

def compute_entropy(values):
    from collections import Counter
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def shift_window(data, window_size):
    """Dummy function - not actually used in final computation"""
    result = []
    for i in range(len(data) - window_size + 1):
        result.append(sum(data[i:i+window_size]))
    return result

def dummy_transform(x):
    # Irrelevant transformation
    return (x * 7 + 13) % 101

def evaluate_stability(seq):
    # Distractor: computes variance but not used
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val) ** 2 for x in seq) / len(seq)
    return round(variance, 4)

def filter_outliers(data, factor=1.5):
    if len(data) == 0:
        return []
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data) // 4]
    q3 = sorted_data[3 * len(sorted_data) // 4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def reduce_bits(value, keep=6):
    """Keep only the lowest 'keep' bits"""
    return value & ((1 << keep) - 1)

def analyze_pattern(sequence, limit):
    # Core relevant logic starts here
    processed = [reduce_bits(x, 5) for x in sequence]  # Use list comprehension
    
    # Apply threshold filter using boolean logic
    filtered = [p for p in processed if p > limit // 10]
    
    # Introduce decoy operations
    temp_sum = sum([dummy_transform(f) for f in filtered])  # Red herring
    temp_sum += 1  # Dead operation

    # Actual key transformation
    mapped = []
    for val in filtered:
        if val % 2 == 0:
            mapped.append(val ** 2)
        else:
            mapped.append((val + 1) * 3)
    
    # Another irrelevant set operation (distractor)
    unique_mapped = set(mapped)
    duplicate_check = len(mapped) - len(unique_mapped)

    # More misdirection: unused nested structure
    stats = {
        'max': max(mapped) if mapped else 0,
        'min': min(mapped) if mapped else 0,
        'range': max(mapped) - min(mapped) if mapped else 0
    }
    
    # Critical step: compute checksum via bitwise mixing
    checksum = 0
    for i, v in enumerate(mapped):
        checksum ^= (v << 1) ^ (i + 1)
    
    # Final reduction to scalar score
    final_score = checksum % 97
    
    # Decoy assignment
    stability_metric = evaluate_stability(mapped)  # Not used
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    raw_signal = generate_signal(base=13, length=50)
    noisy_signal = apply_noise(raw_signal, intensity=5)
    peak_values = extract_peaks(noisy_signal, min_magnitude=30)
    cleaned_peaks = filter_outliers(peak_values, factor=2.0)
    
    # Dummy structures to distract
    windowed_sums = shift_window(noisy_signal, 4)  # Unused
    transformed_cleaned = [dummy_transform(z) for z in cleaned_peaks]  # Unused
    
    # Threshold derived from entropy (used later)
    signal_entropy = compute_entropy(noisy_signal)
    threshold = int(signal_entropy * 10)
    
    bit_sequence = [ord(ch) % 64 for ch in 'DynamicPatternAnalysis']
    bit_sequence.extend(cleaned_peaks[:10])
    
    # Key statement
    filtration_score = analyze_pattern(bit_sequence, threshold)
    
    # Print result as required
    print(f"Result: {filtration_score}")