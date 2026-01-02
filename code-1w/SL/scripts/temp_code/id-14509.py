import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_samples = [i * 0.5 + math.sin(i) for i in range(20)]
    offset = sum(raw_samples) / len(raw_samples)
    normalized = [x - offset for x in raw_samples]
    return normalized

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    outlier_count = len(data) - len(filtered)  # distractor
    return filtered

def generate_reference_pattern(n):
    pattern = []
    for i in range(n):
        pattern.append((i % 3 + 1) * 1.5)
    return pattern

def shift_sequence(seq, positions):
    p = positions % len(seq)
    return seq[-p:] + seq[:-p]  # right rotation

def compute_checksum(values):
    total = 0
    for i, v in enumerate(values):
        total += int(v * 10) ^ i
    return total % 97

def validate_integrity(arr):
    if len(arr) == 0:
        return False
    chk = compute_checksum(arr)
    return chk == (sum(arr) % 97)  # weak integrity check

def extract_features(signal):
    features = {
        'peaks': [],
        'valleys': [],
        'slope_changes': 0
    }
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            features['peaks'].append(i)
        elif signal[i] < signal[i-1] and signal[i] < signal[i+1]:
            features['valleys'].append(i)
        if (signal[i] - signal[i-1]) * (signal[i+1] - signal[i]) < 0:
            features['slope_changes'] += 1
    return features

def merge_signals(primary, secondary):
    merged = []
    min_len = min(len(primary), len(secondary))
    for i in range(min_len):
        merged.append((primary[i] + secondary[i]) / 2.0)
    return merged

def calculate_entropy(data):
    freq_map = {}
    for x in data:
        key = round(x, 1)
        freq_map[key] = freq_map.get(key, 0) + 1
    probabilities = [f / len(data) for f in freq_map.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def analyze_pattern(seq, meta_diag):
    base_score = 0
    n = len(seq)
    if n >= 10:
        mid_third = seq[n//3 : 2*n//3]
        avg_mid = sum(mid_third) / len(mid_third)
        base_score += int(avg_mid * 10)
    
    # Count upward trends in slices
    trend_count = 0
    for i in range(0, len(seq)-2, 3):
        window = seq[i:i+3]
        if len(window) == 3 and window[0] < window[1] < window[2]:
            trend_count += 1
    base_score += trend_count * 5

    # Apply adjustment based on global properties
    distinct_set = set(round(x, 2) for x in seq)
    diversity_bonus = len(distinct_set) // 4
    base_score += diversity_bonus

    # Final transformation
    final_score = (base_score * meta_diag['coherence']) // (meta_diag['noise_level'] or 1)
    return final_score

# Irrelevant auxiliary function (decoy)
def predict_next_value(pattern):
    if len(pattern) < 2:
        return 0.0
    delta = pattern[-1] - pattern[-2]
    return pattern[-1] + delta * 0.9

# Main execution flow
def main_pipeline():
    # Step 1: Collect and normalize sensor readings
    readings = collect_readings()  # 20 elements
    
    # Step 2: Remove outliers (some noise present)
    clean_signal = filter_outliers(readings, threshold=1.8)
    
    # Step 3: Generate reference pattern
    ref_pattern = generate_reference_pattern(12)
    
    # Step 4: Rotate signal for alignment test (not actually used later)
    rotated_signal = shift_sequence(clean_signal, 3)  # distractor
    
    # Step 5: Merge with reference (partial use)
    hybrid_sequence = merge_signals(clean_signal[:12], ref_pattern)
    
    # Step 6: Transform using slicing and scaling
    scaled_slice = [x * 1.2 for x in hybrid_sequence[2:10]]  # 8 elements
    extended_data = scaled_slice + [hybrid_sequence[i] for i in range(0,12,4)]  # add strided elements
    
    # Step 7: Apply non-linear transformation
    transformed_sequence = []
    for x in extended_data:
        transformed_sequence.append(math.cos(x) * 2.5)
    
    # Step 8: Extract unused feature set
    unused_features = extract_features(transformed_sequence)  # dead end
    
    # Step 9: Calculate entropy (distractor metric)
    entropy_metric = calculate_entropy(transformed_sequence)  # not used in result
    
    # Step 10: Build diagnostic metadata
    diagnostics = {
        'coherence': 7,
        'noise_level': 3,
        'sample_count': len(transformed_sequence),
        'version': '2.1-alpha',
        'timestamp': 1718943201
    }
    
    # Step 11: Perform final analysis
    final_diagnostic = analyze_pattern(transformed_sequence, diagnostics)
    
    # Step 12: Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main_pipeline()