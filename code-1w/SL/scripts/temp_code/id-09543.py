from collections import defaultdict

# Simulate analytics processing for ranked features
rank_data = [87, 92, 78, 94, 85, 88]
weights = [0.15, 0.20, 0.10, 0.25, 0.15, 0.15]

# Irrelevant preprocessing: reverse and scale (not used in final logic)
temp_normalized = [round(x / max(rank_data) * 100) for x in reversed(rank_data)]
duplicate_tracker = defaultdict(int)
for val in temp_normalized:
    duplicate_tracker[val] += 1

# Misleading transformation: pairwise differences (dead computation)
pairwise_diffs = []
for i in range(len(temp_normalized) - 1):
    pairwise_diffs.append(abs(temp_normalized[i] - temp_normalized[i+1]))

# Auxiliary function with red herring parameters
def apply_weighting(data, factors, offset=0, invert=False):
    # This function appears complex but ignores several parameters
    adjusted = [d + offset for d in data]  # offset is zero, so no effect
    if invert:
        adjusted = [100 - x for x in adjusted]  # not triggered
    return adjusted

# Real computation begins here
weighted_values = []
for i in range(len(rank_data)):
    weighted_values.append(rank_data[i] * weights[i])

# Secondary validation check (semi-relevant, but only used for filtering thought)
effective_weights = [w for w in weights if w > 0.12]
threshold_met = len(effective_weights) >= 4

# Simulated confidence adjustment (no impact on result)
confidence_factor = 1.0
if threshold_met:
    temp_sum = sum(pairwise_diffs[:3])  # uses dead data
    if temp_sum > 50:
        confidence_factor = 1.05  # never applied

# Core aggregation
raw_score = sum(weighted_values)

# Normalize to a 100-point scale (standard practice)
max_possible = sum([100 * w for w in weights])
normalized_score = (raw_score / max_possible) * 100

# Final scoring with dummy state tracking
status_log = []
status_log.append(f'Starting score: {raw_score:.2f}')
status_log.append(f'Normalized: {normalized_score:.2f}')

# Final computation step — this is the key statement
final_score = round(normalized_score)

# Print result as required
print(f"Result: {final_score}")