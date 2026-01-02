def analyze_sequence(data):
    # Irrelevant transformation: bit manipulation red herring
    bit_accum = 0
    for x in data:
        bit_accum ^= x << 2
        bit_accum += x & 7

    # Distractor: unused statistical calculation
    avg = sum(data) / len(data) if data else 0
    variance = sum((x - avg) ** 2 for x in data) / len(data) if data else 0

    # Real logic disguised among noise: detect arithmetic progression
    if len(data) < 3:
        return len(data)
    
    count = 2
    for i in range(2, len(data)):
        if data[i] - data[i-1] == data[i-1] - data[i-2]:
            count += 1
        else:
            break
    return count

# Decoy function that looks important but is never called
def compute_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return entropy

# Simulated sensor readings with embedded pattern
raw_data = [3, 7, 11, 15, 19, 23, 25, 27]

def process_metrics(raw_data):
    # Extract increasing sequence length (correct path)
    seq_length = analyze_sequence(raw_data)
    
    # Distractor variables: plausible but irrelevant
    temp_normalization = max(raw_data) / (min(raw_data) + 1)
    adjusted_rms = (sum(x**2 for x in raw_data) / len(raw_data)) ** 0.5
    
    # Real signal extraction: position of first non-AP element
    ap_end_index = 0
    for i in range(2, len(raw_data)):
        if raw_data[i] - raw_data[i-1] == raw_data[i-1] - raw_data[i-2]:
            ap_end_index = i
        else:
            break
    
    # Meaningful derived metric
    valid_ap_count = ap_end_index + 1
    
    # Dead code path: looks like calibration but unused
    calibration_factor = 1.0
    if valid_ap_count > 5:
        calibration_factor *= 0.95
    elif valid_ap_count < 3:
        calibration_factor *= 1.1

    return {'sequence_quality': seq_length, 'ap_span': valid_ap_count, 'peak': max(raw_data)}

# Weighting scheme with decoy entries
metric_weights = {
    'sequence_quality': 3.0,
    'ap_span': 2.5,
    'peak': 0.1,  # Low weight - subtle hint it's less important
    'noise_floor': 0.0,  # Completely irrelevant
    'signal_ratio': 0.0   # Unused placeholder
}

raw_results = process_metrics(raw_data)

# Core computation buried in distractions
baseline_offset = 10
scaling_factor = 2  # Used in final calculation

# Multiple assignment distraction
total, count, _ = sum(raw_results.values()), len(raw_results), min(raw_results.values())

# Real answer computation - depends on weighted combination
weighted_sum = 0
for key, weight in metric_weights.items():
    if key in raw_results and weight > 0:  # Filter out zero-weight decoys
        weighted_sum += weight * raw_results[key]

# Secondary adjustment based on AP continuity
ap_continuity_bonus = 0
if raw_results['ap_span'] >= 6:
    ap_continuity_bonus = 5

# Final score calculation - this is the critical point
interim = weighted_sum + baseline_offset
final_score = int(interim * scaling_factor + ap_continuity_bonus)

# Print result as required
print(f"Result: {final_score}")