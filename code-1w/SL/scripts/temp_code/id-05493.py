import math

# Irrelevant helper function (dead code path)
def compute_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

# Misleading transformation chain
temp_cache = [0] * 100
temporary_sum = 0
for i in range(100):
    temp_cache[i] = (i ** 2) % 17
    temporary_sum += temp_cache[i]

# Decoy data structure with red herring computations
stats_log = {
    'max_val': 0,
    'min_val': float('inf'),
    'count_above_5': 0,
    'rolling_avg': 0.0
}

# Unused but plausible-looking processing pipeline
def prefilter_noise(sequence):
    return [x for x in sequence if x % 3 != 0]

# Complex but irrelevant bit manipulation decoy
def obscure_transform(n):
    n = ((n << 3) & 0xFF) ^ 0b10101010
    n = (n >> 1) | (n << 7)
    return n & 0xFF

# Distractor: fake checksum used nowhere
current_checksum = 0
for byte in b'phantom_data_anchor':
    current_checksum = (current_checksum + byte) % 257

# Real computational core buried in noise
data_stream = list(range(1, 51))  # Source data

# Multi-stage filtering and transformation with distractions
decoy_mask = [obscure_transform(i) for i in range(50)]

# Actual relevant logic starts here — deeply nested and obscured
def evaluate_conditional_magnitude(x):
    if x < 10:
        return x ** 2
    elif x < 25:
        return (x * 2) - 8
    else:
        return int(math.sqrt(x) * 3)

# Real transformation chain (buried)
processed = []
for val in data_stream:
    transformed = evaluate_conditional_magnitude(val)
    processed.append(transformed)

# Conditional expression with list comprehension and dictionary operation
summary_stats = {
    k: v for k, v in {
        'total': sum(processed),
        'valid_count': len([p for p in processed if p > 20]),
        'threshold_ratio': len([p for p in processed if p > 20]) / len(processed)
    }.items() if k != 'placeholder'  # dummy filter
}

# Key intermediate result disguised among noise
aggregation_key = summary_stats['total'] // summary_stats['valid_count']

# Lambda-based secondary adjustment (relevant)
adjustment_factor = lambda x: x * 1.5 if x < 50 else x * 1.25
interim_result = adjustment_factor(aggregation_key)

# Final processing stage with decoys
buffer_zone = [0] * 10
for j in range(10):
    buffer_zone[j] = (j * interim_result) % 97  # distraction

# Real final computation
final_output = 0
for item in processed:
    if item % 2 == 0:
        final_output += item // 4
    else:
        final_output -= item % 7

# Misdirection: another unused statistic
phantom_accumulator = 0
for k in range(1, 21):
    phantom_accumulator += math.factorial(k % 6)

# Critical output statement
print(f"Target result: {final_output}")