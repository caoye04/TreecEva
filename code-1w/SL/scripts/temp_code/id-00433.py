import math

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper function (dead code path)
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data if x > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

# Unused but misleading transformation
def transform_signal(signal):
    transformed = []
    for s in signal:
        if s % 3 == 0:
            transformed.append(s // 3)
        elif s % 5 == 0:
            transformed.append(s * 2)
        else:
            transformed.append(s + 1)
    return transformed

# Decoy metrics with red herring calculations
cpu_load = [78, 85, 90, 88, 92, 76, 80]
memory_usage = [60, 65, 70, 72, 68, 75, 80]
disk_latency = [12, 15, 11, 14, 13, 16, 10]

baseline_shift = sum(cpu_load[:3]) / 3
reference_peak = max(memory_usage) - min(memory_usage)

# Distractor: complex but unused bitwise analysis
bit_analysis = 0
for val in disk_latency:
    bit_analysis ^= (val << 2) | (val >> 1)

# Real data path begins here
metric_data = [8, 6, 7, 5, 3, 0, 9]
base_threshold = 5
activation_flags = [x >= base_threshold for x in metric_data]

# String-based filtering mask (uses string method)
filter_mask_str = "1010110"
mask_bits = [int(b) for b in filter_mask_str.strip()]

# Conditional expression with dictionary lookup
status_map = {True: 'active', False: 'idle'}
status_log = [status_map[flag] for flag in activation_flags]

# Real logic obscured by noise
filtered_values = []
for i, val in enumerate(metric_data):
    if mask_bits[i] and activation_flags[i]:
        filtered_values.append(val)

# Secondary filter based on positional pattern
peak_count = analyze_pattern(filtered_values)

# Core computation buried in distractions
aggregate = sum(filtered_values) * (1 + peak_count * 0.1)

decay_factor = 0.95
for _ in range(len(filtered_values)):
    decay_factor *= 0.995  # minor decay accumulation

# Final calculation
intermediate_result = aggregate / (decay_factor + 0.05)

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

# Actual definition of the required function (was forward-referenced)
def evaluate_performance(data, threshold):
    valid_entries = [x for x in data if x != 0]  # exclude zero readings
    above_threshold = len([x for x in valid_entries if x >= threshold])
    pass_rate = above_threshold / len(valid_entries)
    
    # Apply non-linear bonus for high values
    bonus = sum(1 for x in valid_entries if x > threshold + 2)
    score = (pass_rate * 100) + (bonus ** 1.5) * 10
    
    # Additional adjustment based on distribution
    sorted_vals = sorted(valid_entries)
    if len(sorted_vals) > 4 and sorted_vals[-2] >= threshold:
        score *= 1.1
    
    return int(round(score))

# Print result as required
Result: {final_score}