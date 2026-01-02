def analyze_pattern(sequence):
    """Irrelevant helper function that analyzes sequence patterns but is never used."""
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] % 2 == 0 and sequence[i+1] % 2 == 1:
            count += 1
    return count

# Unused data structures as distractors
temp_buffer = [x ** 2 for x in range(15)]
lookup_table = {i: chr(65 + i % 26) for i in range(30)}
shadow_cache = {k: v for k, v in enumerate(temp_buffer) if k % 3 == 0}

# Core problem variables
raw_input = [8, 12, 5, 19, 3, 7, 14]
weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.1, 0.1]

# Misleading intermediate calculations
normalization_factor = sum(w ** 2 for w in weights) ** 0.5
scaled_weights = [w / normalization_factor for w in weights]  # Not actually used

# Another red herring: bit manipulation with no impact
bit_fingerprint = 0
for val in raw_input:
    bit_fingerprint ^= (val << 2) | (val >> 1)
bit_fingerprint &= 0xFFFF

# Real processing begins here
filtered_data = [x for x in raw_input if x > 6]
index_map = {i: idx for i, idx in enumerate(filtered_data)}  # unused mapping

# Distractor: complex dictionary comprehension with side computation
stats_summary = {
    'max_val': max(raw_input),
    'min_filtered': min(filtered_data),
    'range': max(raw_input) - min(raw_input),
    'avg_sq': sum(x**2 for x in filtered_data) / len(filtered_data),
    'dummy_key': sum(1 for x in raw_input if x % 3 == 0)
}

# Actual signal buried in noise
offset_correction = len(raw_input) - len(weights)  # should be 0
if offset_correction != 0:
    weights = weights[:len(raw_input)]

# Key transformation with slicing and zip
trimmed_input = raw_input[1:-1]  # Remove first and last
paired = list(zip(trimmed_input, weights[1:-1]))  # Align middle elements

# Decoy loop: computes something irrelevant
aggregate_noise = 0
for i, (val, w) in enumerate(paired):
    aggregate_noise += val * (w + i) * (-1)**i

# Real calculation path
weighted_sum = 0
weight_total = 0
for i, val in enumerate(raw_input):
    contribution = val * weights[i]
    weighted_sum += contribution
    weight_total += weights[i]

mean_weighted = weighted_sum / weight_total

# Secondary metric using enumerate and slicing
reversed_slice = raw_input[::-1][1:6]  # Reverse and take middle
position_bonus = 0
for idx, value in enumerate(reversed_slice):
    if value % 2 == 1:
        position_bonus += idx * 0.5

# Final composite score — this is the answer
baseline = stats_summary['min_filtered']
adjustment = position_bonus * stats_summary['range'] / 100.0
final_score = mean_weighted + adjustment + 5  # Final deterministic result

print(f"Target result: {final_score}")