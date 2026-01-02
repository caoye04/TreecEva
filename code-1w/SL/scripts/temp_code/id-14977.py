import math

# Simulated sensor readings with noise and calibration factors
data_stream = [3, 8, 12, 15, 18, 22, 25, 27, 30, 33, 36, 39, 42, 45]
calibration_map = {3: 1.1, 12: 0.95, 18: 1.05, 25: 0.9, 33: 1.15, 42: 0.85}
offset_table = {'a': 2, 'b': -1, 'c': 3, 'd': 0}

# Irrelevant transformation: frequency analysis (dead code path)
frequencies = {}
for val in data_stream:
    freq_key = val % 7
    frequencies[freq_key] = frequencies.get(freq_key, 0) + 1

# Decoy statistical calculation (misleading intermediate)
mean_val = sum(data_stream) / len(data_stream)
adjusted_mean = mean_val * 1.02

# Bit manipulation red herring: simulate checksum (unused)
checksum = 0
for x in data_stream:
    checksum ^= (x << 1) | (x >> 2)

# Real processing begins: apply calibration using lambda and defaults
raw_calibrated = [
    val * calibration_map.get(val, 1.0) for val in data_stream
]

# Secondary adjustment with offset table (only key 'a' used)
partially_adjusted = [
    val + offset_table['a'] if i % 3 == 0 else val for i, val in enumerate(raw_calibrated)
]

# Distractor: string-based encoding (never used)
encoded_tags = [''.join([chr((val % 26) + 97) for _ in range(1)]) for val in data_stream]

# Set operations to filter outliers (core logic)
baseline_set = set(range(20, 40))
high_sensitivity_zones = {22, 27, 30, 36, 39}
allowed_range = baseline_set | high_sensitivity_zones

# Use enumerate and zip together in filtering (required feature)
indexed_data = list(enumerate(partially_adjusted))
reference_shifts = [math.sin(i * 0.5) for i in range(len(partially_adjusted))]
combined_pairs = zip(indexed_data, reference_shifts)

# Complex filtering logic with nested conditions and distractors
filtered_data = []
for (idx, value), shift in combined_pairs:
    if idx < 0 or value < 10:  # unreachable condition (red herring)
        continue
    calibrated_value = value + shift  # minor perturbation
    if idx % 4 == 3:
        continue  # artificial skip pattern
    base_val = int(data_stream[idx] * calibration_map.get(data_stream[idx], 1.0))
    if base_val in allowed_range:
        # Apply additional conditional via lambda (real but subtle)
        processor = lambda x: x * 1.1 if x > 30 else x * 0.95
        filtered_data.append(int(processor(calibrated_value)))

# Dead code: unused aggregation function
def compute_rolling_avg(lst, window=3):
    return [sum(lst[i:i+window]) / window for i in range(len(lst)-window+1)]

# Critical execution point
filtered_sum = sum(filtered_data)

# Output result as required
print(f"Result: {filtered_sum}")