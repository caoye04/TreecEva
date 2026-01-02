from itertools import combinations
from math import log

# Simulate sensor data processing with weighted aggregation
def preprocess_entry(entry):
    raw_value = entry['value']
    noise_floor = entry.get('noise', 0.1)
    adjusted = raw_value - noise_floor
    if adjusted < 0:
        adjusted = 0.05
    return {'adjusted': adjusted, 'flag': entry['flag']}

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log(prob)
    return round(entropy, 4)

def calculate_stability_index(sequence):
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    return sum(diffs) / len(diffs) if diffs else 0

# Main computation path
data_entries = [
    {'value': 85, 'weight': 0.3, 'flag': True, 'noise': 0.2},
    {'value': 90, 'weight': 0.4, 'flag': False, 'noise': 0.4},
    {'value': 78, 'weight': 0.2, 'flag': True, 'noise': 0.15},
    {'value': 92, 'weight': 0.1, 'flag': True, 'noise': 0.3}
]

weights = [d['weight'] for d in data_entries]

# Irrelevant precomputations (distractors)
mean_weight = sum(weights) / len(weights)
weight_variance = sum((w - mean_weight) ** 2 for w in weights) / len(weights)

# Semi-relevant: analyze flag patterns
flagged_count = sum(1 for d in data_entries if d['flag'])
duplicate_check = list(combinations([d['value'] for d in data_entries], 2))

# Preprocess all entries
processed = [preprocess_entry(entry) for entry in data_entries]

# Extract relevant features
adjusted_values = [p['adjusted'] for p in processed]
valid_flags = [p['flag'] for p in processed]

# Compute auxiliary metrics (not used in final score but look important)
entropy_metric = compute_entropy(adjusted_values)
stability = calculate_stability_index(adjusted_values)

# Key intermediate calculation
weighted_sum = sum(p['adjusted'] * d['weight'] for p, d in zip(processed, data_entries))
normalization_factor = sum(weights)  # Redundant but adds cognitive load

# Decision logic with red herring branch
if flagged_count >= 2:
    adjustment_multiplier = 1.1
else:
    adjustment_multiplier = 0.95  # Not taken, but looks significant

# Another distraction: simulate calibration lookup
calibration_map = {i: round(1 + 0.01 * i, 2) for i in range(5)}
current_calibration = calibration_map.get(flagged_count, 1.0)

# Final score computation (core logic)
base_score = weighted_sum / normalization_factor
final_score = int(base_score * adjustment_multiplier * 10) / 10  # Rounded to 1 decimal

# Output result as required
print(f"Result: {final_score}")