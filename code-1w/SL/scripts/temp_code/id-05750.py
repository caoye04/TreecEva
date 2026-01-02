from itertools import combinations
from math import log, ceil

# Simulated dataset for performance metrics
data = [89, 93, 78, 85, 96, 82, 91, 87]
weights = [0.1, 0.15, 0.05, 0.2, 0.1, 0.15, 0.1, 0.1]

# Irrelevant statistical summaries (distractors)
mean_val = sum(data) / len(data)
variance = sum((x - mean_val) ** 2 for x in data) / len(data)
std_dev = variance ** 0.5
median_val = sorted(data)[len(data)//2]
mode_approx = max(set(data), key=data.count)

# Dummy transformation using set operations (red herring)
unique_pairs = set(combinations(data, 2))
pair_sums = {sum(pair) for pair in unique_pairs if sum(pair) > 170}
filtered_medians = {ceil(log(s + 1)) for s in pair_sums if s % 2 == 0}

# Misleading normalization chain
normalized_data = []
for val in data:
    temp_z = (val - mean_val) / std_dev
    scaled = 50 + temp_z * 10
    adjusted = max(1, min(100, scaled))
    normalized_data.append(adjusted)

# Unused recursive function (dead code path)
def recursive_weight_sum(lst, idx=0):
    if idx >= len(lst):
        return 0
    return lst[idx] + 0.9 * recursive_weight_sum(lst, idx + 1)

# Another decoy: bit manipulation on weights (irrelevant)
weight_bits = []
for w in weights:
    fixed_point = int(w * 1000)
    flipped = fixed_point ^ 0b11111111
n    weight_bits.append(flipped >> 3)

# Real computation begins here — weighted harmonic mean disguised in noise
effective_weights = [w for w, d in zip(weights, data) if d > 80]
core_values = [d for d in data if d > 80]

# Compute harmonic contribution only on high performers
if core_values:
    weighted_inv_sum = sum(w / v for w, v in zip(effective_weights, core_values))
    harmonic_baseline = len(core_values) / weighted_inv_sum
else:
    harmonic_baseline = 0

# Secondary adjustment based on distribution shape
skew_influence = sum(1 for x in data if x >= 90) - sum(1 for x in data if x <= 80)
adjustment_factor = 1 + (skew_influence * 0.02)

# Final score calculation — this is the actual target
intermediate_result = harmonic_baseline * adjustment_factor
clamped_result = max(50, min(100, intermediate_result))

# Additional misdirection: dictionary-based lookup that's not used
stats_summary = {
    'count': len(data),
    'top_performer': max(data),
    'excellence_ratio': len([x for x in data if x >= 90]) / len(data),
    'stability': (max(data) - min(data)) < 20
}

diagnostic_codes = {k: hash(str(v)) % 1000 for k, v in stats_summary.items()}

# Actual final computation buried in logic
final_score = round(clamped_result * 1.05, 4)

# Print result as required
print(f"Target result: {final_score}")