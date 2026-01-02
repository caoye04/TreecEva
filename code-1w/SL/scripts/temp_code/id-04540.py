import itertools

def preprocess_signal(raw_readings):
    # Irrelevant preprocessing (dead path)
    filtered = [x * 0.98 for x in raw_readings if x > 0]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    return [x - baseline for x in raw_readings]

def compute_entropy(sequence):
    # Misleading complexity: computes bit entropy but not used in final result
    total_bits = ''.join(format(int(x), 'b') for x in sequence)
    ones = total_bits.count('1')
    zeros = total_bits.count('0')
    if zeros == 0 or ones == 0:
        return 0.0
    from math import log2
    p1 = ones / (ones + zeros)
    p0 = zeros / (ones + zeros)
    return -p1*log2(p1) - p0*log2(p0)

def validate_checksum(data_chunk):
    # Decoy function: looks important but unused
    checksum = 0
    for val in data_chunk:
        checksum ^= int(val * 31) & 0xFF
    return checksum == 0x5A

def extract_features(signal, window_size=4):
    # Distractor: feature extraction that isn't used
    features = []
    for i in range(0, len(signal) - window_size + 1):
        window = signal[i:i+window_size]
        features.append(sum(w * (i+1) for w in window))
    return features

def analyze_phase_coherence(readings):
    # Looks critical but is actually a red herring
    if len(readings) < 3:
        return 0.0
    diffs = [readings[i+1] - readings[i] for i in range(len(readings)-1)]
    coherence = 0
    for d1, d2 in zip(diffs, diffs[1:]):
        if (d1 > 0 and d2 > 0) or (d1 < 0 and d2 < 0):
            coherence += 1
    return coherence / (len(diffs) - 1) if len(diffs) > 1 else 0.0

def aggregate_metrics(sensor_data, key_vector):
    # Core logic hidden among distractions
    
    # Irrelevant transformation chain
    temp_buffer = [x ^ 0xAA for x in key_vector]  # bitwise decoy
    scaled = [x * 1.5 for x in temp_buffer]
    offset = sum(scaled[:3]) % 7
    
    # Real computation starts here — non-obvious dependency
    masked_values = []
    for i, val in enumerate(sensor_data):
        if i % 2 == 0:
            masked_values.append(val & 0x0F)  # keep lower 4 bits
        else:
            masked_values.append(val & 0xF0 >> 4)  # upper 4 bits as lower
    
    # Key transformation using itertools
    paired = list(itertools.pairwise(masked_values))  # relevant: consecutive pairs
    weighted_sum = 0
    
    for idx, (a, b) in enumerate(paired):
        # Complex-looking but deterministic weighting
        factor = (idx + 1) * (a ^ b)  # XOR combined with position
        weighted_sum += factor
    
    # One more distraction: unused conditional branch
    if weighted_sum > 1000:
        weighted_sum = weighted_sum // 3 + 17
    
    # Final computation buried in middle
    adjustment = len(key_vector) & 0x7
    final_diagnostic = weighted_sum - adjustment * 12
    
    # Dead code block (never reached due to above)
    outlier_count = 0
    for v in sensor_data:
        if v in [0xDE, 0xAD, 0xBE, 0xEF]:
            outlier_count += 1

    return final_diagnostic  # This is the real output

# Simulated input data
baseline_probe = [23, 87, 156, 201, 94, 113, 67, 144]
turbine_data = [211, 173, 92, 58, 204, 137, 88, 102, 73]
calibration_sequence = [18, 29, 44, 61, 70]

# Unused intermediate calls (distraction)
entropy_score = compute_entropy(calibration_sequence)
signal_features = extract_features(baseline_probe)
phase_stability = analyze_phase_coherence(baseline_probe)

# Critical execution point
final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)

print(f"Result: {final_diagnostic}")