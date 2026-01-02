from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundancy
data_stream = [18, 23, 18, 45, 23, 45, 45, 18, 29, 35, 35, 29, 18, 23]

# Irrelevant transformation: frequency mapping (distractor)
frequency_map = defaultdict(int)
for val in data_stream:
    frequency_map[val] += 1

# Decoy calculation: entropy of frequencies (misleading intermediate)
total = sum(frequency_map.values())
entropy = 0.0
for count in frequency_map.values():
    p = count / total
    entropy -= p * math.log2(p)

# Signal filtering: extract unique values while preserving order
seen = set()
filtered_signal = [x for x in data_stream if not (x in seen or seen.add(x))]

# Noise floor estimation (unused red herring)
noise_floor = sum(x for x in data_stream if x < 20) // len([x for x in data_stream if x < 20])

# Critical path: pattern analysis
pattern_gaps = []
for i in range(1, len(filtered_signal)):
    pattern_gaps.append(filtered_signal[i] - filtered_signal[i-1])

gap_counter = Counter(pattern_gaps)
dominant_gap = gap_counter.most_common(1)[0][0]  # Most frequent gap

# Secondary signal feature: symmetry check around median
sorted_signal = sorted(filtered_signal)
median_val = sorted_signal[len(sorted_signal) // 2]
symmetric_pairs = 0
for i in range(len(sorted_signal)):
    for j in range(i+1, len(sorted_signal)):
        if (sorted_signal[i] + sorted_signal[j]) == 2 * median_val:
            symmetric_pairs += 1

# Phantom correction factor (dead computation path)
correction_matrix = [[i*j for j in range(3)] for i in range(3)]
phantom_factor = 0
for row in correction_matrix:
    for elem in row:
        phantom_factor ^= elem  # Bitwise distraction

# Core diagnostic logic
aggregate_score = 0
if dominant_gap > 0:
    aggregate_score += dominant_gap * 17
if symmetric_pairs >= 2:
    aggregate_score += 42

# Red herring: checksum validation (never used)
data_checksum = 0
for i, v in enumerate(data_stream):
    data_checksum = (data_checksum + v * (i + 1)) % 100

# Threshold adjustment based on initial sequence stability
stability_metric = abs(filtered_signal[0] - filtered_signal[1])
if stability_metric <= 10:
    threshold_adjustment = 13
else:
    threshold_adjustment = -7

# Key assignment statement
final_diagnostic = aggregate_score + threshold_adjustment

# Distractor: slice-based anomaly detection (irrelevant)
anomaly_slices = [data_stream[i:i+4] for i in range(len(data_stream)-3)]
high_var_slices = 0
for s in anomaly_slices:
    mean_val = sum(s) / len(s)
    var = sum((x - mean_val)**2 for x in s) / len(s)
    if var > 100:
        high_var_slices += 1

# Output the target result
print(f"Result: {final_diagnostic}")