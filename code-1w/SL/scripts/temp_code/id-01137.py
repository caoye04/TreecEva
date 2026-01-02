import itertools
import math

def compute_entropy(weights):
    entropy = 0.0
    for w in weights:
        if w > 0:
            entropy -= w * math.log2(w)
    return entropy

# System calibration data
baseline_signals = [0.1, 0.2, 0.3, 0.4]
correction_factors = [1.1, 0.9, 1.0, 1.2]

# Apply corrections (some are red herrings)
adjusted_signals = []
for i, sig in enumerate(baseline_signals):
    adj = sig * correction_factors[i]
    adjusted_signals.append(adj)

# Normalize to form probability distribution
sum_signals = sum(adjusted_signals)
normalized_powers = [x / sum_signals for x in adjusted_signals]

# Simulate redundant secondary system (distractor)
duplicate_system = [x * 1.005 for x in normalized_powers]
consistency_check = all(0 <= x <= 1 for x in duplicate_system)

# Weight adjustment using combinatorics (relevant)
combination_pairs = list(itertools.combinations([0, 1, 2, 3], 2))
pair_count_map = {i: 0 for i in range(4)}
for a, b in combination_pairs:
    pair_count_map[a] += 1
    pair_count_map[b] += 1

# Convert counts to adjustment weights
dynamic_weights = [pair_count_map[i] for i in range(4)]
sum_dw = sum(dynamic_weights)
scaled_dynamic = [x / sum_dw for x in dynamic_weights]

# Final weight fusion (only normalized_powers and scaled_dynamic are used)
final_weights = []
for i in range(4):
    # Misleading operation: unused intermediate
    temp_fusion_score = (normalized_powers[i] + scaled_dynamic[i]) / 2 * 1.0
    final_weights.append(normalized_powers[i] * 0.7 + scaled_dynamic[i] * 0.3)

# Dead code path - irrelevant transformation
if len(final_weights) > 5:
    final_weights = [x ** 0.5 for x in final_weights]

# Key computation point
total_entropy = compute_entropy(final_weights)

# Print result as required
print(f"Result: {total_entropy}")