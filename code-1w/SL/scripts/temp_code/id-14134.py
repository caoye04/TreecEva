from collections import defaultdict

# Simulate sensor data with noise and redundancy
data_stream = [15, 23, 15, 47, 23, 58, 47, 15, 91, 58, 91, 91]

# Track frequency of readings (distractor: not directly used in final score)
frequency_map = defaultdict(int)
for reading in data_stream:
    frequency_map[reading] += 1

# Filter unique values while preserving order
seen = set()
unique_readings = [x for x in data_stream if not (x in seen or seen.add(x))]

# Misleading transformation: apply bitwise scrambling (semi-relevant)
scrambled_values = []
for val in unique_readings:
    scrambled = val ^ 17  # arbitrary XOR mask
    if scrambled % 3 == 0:
        scrambled = scrambled << 1  # left shift if divisible by 3
    scrambled_values.append(scrambled)

# Secondary distractor: simulate calibration offsets
baseline_offset = 101
adjusted_values = [val - baseline_offset for val in scrambled_values]

# Process relevant features: extract high-confidence signals
high_confidence = [v for v in unique_readings if v > 30]

# Derive signal quality metrics (distractor computation)
signal_entropy = 0
for v in high_confidence:
    if v > 50:
        signal_entropy += 1.5
    else:
        signal_entropy += 0.7

# Core logic: compute weighted stability index
stability_weights = {15: 1, 23: 1, 47: 2, 58: 2, 91: 3}
weighted_sum = sum(stability_weights[v] * v for v in unique_readings)
total_weight = sum(stability_weights[v] for v in unique_readings)
stability_index = weighted_sum / total_weight if total_weight > 0 else 0

# Noise threshold filter (dead code path - never triggered due to data)
noise_floor = 5
if stability_index < 10:
    stability_index = 0  # would reset if too low, but won't occur

# Distractor: unused helper function
def analyze_variance(data):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** 2 for x in data) / len(data)

# Key processing step: transform stability into normalized score
normalized_stability = int(stability_index * 1.75)

# Apply conditional bonus based on pattern presence
pattern_bonus = 10 if 91 in high_confidence and len(high_confidence) >= 3 else 0

# Final aggregation with red herring variables included
auxiliary_correction = len(adjusted_values) * 2  # looks important but unused
reference_anchor = [x for x in frequency_map.values() if x > 2]  # computed but irrelevant

# Critical assignment
final_score = normalized_stability + pattern_bonus

print(f"Result: {final_score}")