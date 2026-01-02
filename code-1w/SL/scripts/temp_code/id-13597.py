import itertools

# Simulated sensor data with noise and calibration offsets
data_stream = [107, -53, 214, 88, -999, 156, 73, -999, 301, 122, -58, 999, 415, -999, 67]

# Calibration parameters (some are red herrings)
base_offset = 23
scaling_factor = 1.05
legacy_correction = 0.92
invalid_marker = -999
noise_floor = 50

# Step 1: Remove invalid readings marked by -999 (sensor error code)
cleaned_data = [x for x in data_stream if x != invalid_marker]

# Distractor: Apply legacy correction to a copy (not used later)
legacy_adjusted = [x * legacy_correction for x in cleaned_data]

# Step 2: Normalize using base offset and scaling
calibrated = [(x - base_offset) * scaling_factor for x in cleaned_data]

# Distractor: Compute statistical moments (unused)
mean_val = sum(calibrated) / len(calibrated)
variance = sum((x - mean_val) ** 2 for x in calibrated) / len(calibrated)
std_dev = variance ** 0.5

# Step 3: Filter out values below noise floor after calibration
filtered_positive = [x for x in calibrated if x > noise_floor]

# Distractor: Attempt clustering via pairwise differences (dead code path)
pairwise_diffs = [abs(a - b) for a, b in itertools.combinations(filtered_positive[:5], 2)]
cluster_threshold = 40
clusters = []
for diff in pairwise_diffs:
    if diff > cluster_threshold:
        clusters.append(diff * 0.5)  # Unused logic

# Step 4: Apply logarithmic weighting to emphasize high-confidence readings
weighted_values = [x * (1 + max(0, (x - 100) / 100)) for x in filtered_positive]

# Distractor: Sort in multiple ways (only last one matters)
sorted_reverse = sorted(weighted_values, reverse=True)
sorted_alpha = sorted([str(x) for x in weighted_values])  # Lexicographic sort, irrelevant
final_sorted = sorted(weighted_values)  # Actually used

# Step 5: Extract every second element after sorting to reduce bias
sampled_entries = [x for i, x in enumerate(final_sorted) if i % 2 == 0]

# Step 6: Validate entries against dynamic threshold
threshold_dynamic = sum(sampled_entries) / len(sampled_entries) if sampled_entries else 0
valid_entries = [x for x in sampled_entries if x >= threshold_dynamic * 0.85]

# Critical assignment point
filtered_sum = sum(valid_entries)

# Distractor: Complex bit manipulation on final result (no effect)
bit_analysis = 0
for val in valid_entries:
    int_val = int(abs(val))
    bit_analysis ^= (int_val >> 2) & 0xFF
    bit_analysis += int_val & 0x0F

# Final output
print(f"Result: {filtered_sum}")