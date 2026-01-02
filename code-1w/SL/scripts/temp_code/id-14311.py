import itertools

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    triplets = list(itertools.combinations(sequence, 3))
    valid = [t for t in triplets if t[0] + t[2] == 2 * t[1]]  # arithmetic sequence
    return len(valid)

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = sum(-(count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 4)

# Unused transformation chain
def transform_data(x):
    x = x << 2
    x = x ^ 255
    x = x >> 1
    return x

# Misleading statistical function that looks important but isn't used in final path
def get_outlier_count(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    threshold = 2 * std_dev
    outliers = [v for v in values if abs(v - mean_val) > threshold]
    return len(outliers)

# Core logic obscured by noise
baseline = [1, 2, 4, 8, 16]
raw_inputs = [3, 5, 9, 17, 33]

# Distractor: complex-looking but unused bitwise cascade
temp_flag = 0b1010
for i in range(len(raw_inputs)):
    temp_flag ^= raw_inputs[i] & 0b1111
    temp_flag = (temp_flag << 1) | (temp_flag >> 3)
    temp_flag &= 0b11111

# Real data preparation buried in noise
processed = []
for val in raw_inputs:
    if val % 2 == 1:
        processed.append(val - 1)

# Another red herring: set operations that look relevant but aren't part of main logic
duplicate_check = set(raw_inputs)
extensions = set(baseline + [32, 64])
suspicious_overlap = duplicate_check & extensions  # This is never used again

# Decoy dictionary aggregation
stats_summary = {
    'max_input': max(raw_inputs),
    'min_base': min(baseline),
    'input_range': max(raw_inputs) - min(raw_inputs),
    'base_length': len(baseline)
}

# Actual key computation hidden among distractions
def evaluate_performance(metrics, reference):
    shift_scores = []
    for m, r in zip(metrics, reference):
        # Key operation: difference then bit manipulation
        diff = abs(m - r)
        shifted = (diff << 1) ^ 3  # XOR with prime to obscure pattern
        shift_scores.append(shifted)
    
    # Real answer derived here
    base_total = sum(shift_scores)
    adjustment = analyze_pattern(shift_scores)  # uses itertools combinations
    final_value = base_total - adjustment
    
    # Dead code branch - never executed but looks important
    if final_value < 0:
        fallback = 0
        for bit in range(8):
            fallback |= (1 << bit)
        return fallback
    
    return final_value

# Critical execution point
final_score = evaluate_performance(processed, baseline)
print(f"Result: {final_score}")