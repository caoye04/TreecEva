import math

# Simulated sensor data from environmental monitoring stations
data_stream = [14, 28, 19, 35, 42, 13, 22, 31, 45, 29, 36, 17, 25, 33, 41]
offsets = [3, -1, 2, 0, -2, 1, 4]
correction_factors = [1.1, 0.95, 1.05, 1.2, 0.8, 1.0, 0.9]

# Irrelevant auxiliary data (distractor)
legacy_codes = [(101, 'A'), (205, 'B'), (302, 'C')]
metadata_log = {k: f'record_{i}' for i, k in enumerate(legacy_codes)}

# Noise filtering using moving average (relevant)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Misleading transformation (dead path - never called)
def deprecated_filter(x):
    return [val for val in x if val > 20]  # Unused

# Signal normalization (relevant)
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return [0 for _ in signal]
    return [(x - mean_val) / std_dev for x in signal]

# Bitmask-based anomaly detection (partially relevant)
def detect_anomalies(values):
    flags = []
    for v in values:
        raw = int(abs(v * 10))
        # Use bit patterns: more than 3 bits set indicates anomaly
        bit_count = bin(raw).count('1')
        flags.append(1 if bit_count > 3 else 0)
    return flags

# Decoy function with plausible name but unused (distractor)
def evaluate_stability(indices, history=None):
    if history is None:
        history = []
    cumulative = 0
    for idx in indices:
        cumulative += idx ** 2 % 7
    return cumulative > 50

# Core analysis logic
threshold_map = {i: 0.8 + i * 0.05 for i in range(15)}

# Apply corrections with zip and enumerate (required feature)
adjusted_data = []
for i, val in enumerate(data_stream):
    factor_index = i % len(correction_factors)
    corrected = val * correction_factors[factor_index]
    offset_index = i % len(offsets)
    corrected += offsets[offset_index]
    adjusted_data.append(corrected)

# Smooth and normalize (relevant chain)
processed_data = normalize_signal(smooth_signal(adjusted_data))

# Anomaly tagging
anomaly_flags = detect_anomalies(processed_data)

# Auxiliary diagnostic (distractor)
count_high_flags = sum(1 for f in anomaly_flags if f == 1)
avg_position_weight = sum(i * f for i, f in enumerate(anomaly_flags)) / (count_high_flags or 1)

# Fake aggregation using slicing (irrelevant)
slice_proxy = anomaly_flags[::2]  # Every other flag
temp_diagnostic = sum(slice_proxy) * 0.7

# Real diagnostic logic: count how many normalized values exceed dynamic thresholds
exceedance_count = 0
for i, val in enumerate(processed_data):
    threshold_key = i % 15
    if abs(val) > threshold_map[threshold_key]:
        exceedance_count += 1

# Secondary filter based on bit pattern of index (combined logic)
index_bit_mask = 0
for i in range(len(processed_data)):
    if bin(i).count('1') % 2 == 1:  # Odd number of bits
        index_bit_mask |= (1 << (i % 8))

masked_count = 0
for i in range(len(processed_data)):
    if (index_bit_mask >> (i % 8)) & 1:
        if abs(processed_data[i]) > threshold_map.get(i % 15, 0.8):
            masked_count += 1

# Final decision heuristic
base_score = exceedance_count * 100
adjustment = bin(masked_count).count('1') * 15  # Use bit count as weight
final_diagnostic = base_score - adjustment

# Output result as required
Result: final_diagnostic