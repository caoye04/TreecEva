from itertools import combinations

# Simulate sensor data quality assessment for a distributed system
raw_readings = [12, 7, 9, 15, 4, 11]
noise_floor = 3
signal_threshold = 10

def is_valid_pair(x, y):
    return (x + y) % 7 == 0 and abs(x - y) > noise_floor

# Generate all possible pairs above threshold
valid_pairs = []
temporary_sum = 0
for val in raw_readings:
    if val > signal_threshold:
        temporary_sum += val  # Irrelevant accumulation (distractor)

# Evaluate pairwise compatibility using combinatorics
pair_candidates = list(combinations(raw_readings, 2))
compatibility_flags = []
for pair in pair_candidates:
    flag = is_valid_pair(pair[0], pair[1])
    compatibility_flags.append(flag)
    if flag:
        valid_pairs.append(pair)

# Track metadata that won't be used later
metadata_log = {
    'total_pairs': len(pair_candidates),
    'valid_count': len(valid_pairs),
    'redundant_ratio': len(valid_pairs) / (len(pair_candidates) or 1)
}

# Secondary filter: only pairs where both elements are odd
strict_pairs = []
for p in valid_pairs:
    if p[0] % 2 == 1 and p[1] % 2 == 1:
        strict_pairs.append(p)

# Compute aggregate score based on strict valid pairs
aggregate_value = 0
for sp in strict_pairs:
    aggregate_value += sp[0] * sp[1]  # Product sum as weight

# Misleading transformation chain (only final value matters)
binary_weight = bin(aggregate_value).count('1')
scaling_factor = binary_weight if binary_weight > 4 else 4
dummy_shift = aggregate_value << 2
intermediate_offset = dummy_shift - aggregate_value

final_score = aggregate_value + len(strict_pairs)
print(f"Result: {final_score}")