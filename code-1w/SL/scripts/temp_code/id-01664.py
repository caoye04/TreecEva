from collections import defaultdict, Counter
import math

# Simulated sensor data stream with noise and redundant readings
data_stream = [18, 23, 14, 25, 22, 18, 23, 28, 14, 25, 22, 19, 27, 23, 18, 14]

# Irrelevant preprocessing: frequency count of values (distractor)
frequency_map = Counter(data_stream)
unique_values = list(frequency_map.keys())
mode_value = frequency_map.most_common(1)[0][0]

# Redundant transformation path A: normalize around mean (dead code path)
mean_val = sum(data_stream) / len(data_stream)
normalized_data = [round(x - mean_val, 2) for x in data_stream]

# Redundant transformation path B: binary encoding of LSB (misleading intermediate)
binary_flags = [x & 1 for x in data_stream]
flag_distribution = Counter(binary_flags)

# Core signal extraction: isolate repeating triplets above base_threshold
base_threshold = 20
windowed_triplets = [data_stream[i:i+3] for i in range(len(data_stream) - 2)]
valid_triplets = [t for t in windowed_triplets if all(val > base_threshold for val in t)]

# Secondary filter: only keep triplets where middle element is max (logic dependency)
refined_triplets = [t for t in valid_triplets if t[1] == max(t)]

# Transform: map each refined triplet to product of differences
transformed_triplet_data = []
for t in refined_triplets:
    diff1 = abs(t[1] - t[0])
    diff2 = abs(t[2] - t[1])
    transformed_triplet_data.append(diff1 * diff2)

# Accumulate results using defaultdict (required feature)
accumulated_metrics = defaultdict(int)
for i, val in enumerate(transformed_triplet_data):
    accumulated_metrics[i % 3] += val

# Extract core sequence for analysis
transformed_data = [accumulated_metrics[k] for k in sorted(accumulated_metrics)]

# Decoy analysis function (never called)
def deprecated_analysis(seq):
    return sum(x ** 0.5 for x in seq if x % 2 == 0)

def evaluate_stability(seq, limit):
    score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            score += 1
    return score > limit

# Critical analysis function: detect oscillation pattern in transformed data
def analyze_pattern(seq, thresh):
    if len(seq) < 2:
        return -1
    
    # Compute pairwise XOR as signature (bitwise operation)
    xor_signature = [seq[i] ^ seq[i+1] for i in range(len(seq)-1)]
    
    # Apply dynamic threshold filter
    filtered_vals = [x for x in xor_signature if x > thresh]
    
    # Accumulate weighted sum based on position
    weighted_sum = 0
    for idx, val in enumerate(filtered_vals):
        weight = 1 + (0.1 * idx)  # increasing importance
        weighted_sum += val * weight
    
    # Final adjustment: average with min if non-empty, else fallback
    if filtered_vals:
        result = (weighted_sum + min(filtered_vals)) / 2
    else:
        result = sum(seq) / len(seq) * -1
    
    # Apply rounding to 3 decimal places
    return round(result, 3)

# Misleading diagnostic call (short-circuited due to condition)
spurious_trigger = False
interim_result = 0
if spurious_trigger and len(normalized_data) > 10:
    interim_result = deprecated_analysis(transformed_data)

# Threshold derived from mode and flag stats (red herring computation)
dummy_threshold = (mode_value + flag_distribution[1]) / 2

# Actual execution point — this is the key statement
dynamic_threshold = len(refined_triplets) * 3
final_diagnostic = analyze_pattern(transformed_data, dynamic_threshold)

# Output result in required format
print(f"Result: {final_diagnostic}")