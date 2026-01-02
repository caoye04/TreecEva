import math

# Simulated sensor array data with noise and redundant measurements
data_stream = [3.2, 1.8, 4.5, 2.1, 6.7, 3.3, 2.9, 5.0, 6.1, 3.6, 4.0, 2.2, 1.9, 7.2, 5.8, 6.6, 4.3, 3.9, 2.7, 8.1]

# Irrelevant calibration constants (distractor)
calibration_factor_a = 0.987
baseline_offset = -0.45
reference_power = 2.0 ** 10
max_theoretical_bandwidth = 100000

# Noise filter threshold (used later)
thresh = 3.0

# Outdated backup data (dead code path)
historical_data_backup = data_stream[::-1]
for i in range(len(historical_data_backup)):
    historical_data_backup[i] += 0.1  # Unused transformation

# Legacy function for deprecated protocol (decoy)
def legacy_process(seq):
    result = 0
    for x in seq:
        result += x * 0.5 if x > 2.5 else x * 0.1
    return result + 10  # Never called

# Auxiliary function: estimate entropy (unused but plausible)
def estimate_entropy(values):
    freq_map = {}
    for v in values:
        rounded = round(v, 1)
        freq_map[rounded] = freq_map.get(rounded, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Unused entropy calculation (misleading intermediate)
entropy_score = estimate_entropy(data_stream)

# Simulated interference mask (bit manipulation red herring)
interference_flags = 0b11010110
mask_shift = (interference_flags << 3) & 0xFF
inverted_mask = ~mask_shift & 0xFF

# Extract segments using slicing — relevant preprocessing
primary_slice = data_stream[2:15]          # Central region of interest
mirrored_tail = data_stream[-5:][::-1]   # Reverse last five elements
extended_buffer = primary_slice + mirrored_tail  # Augment data

# Spurious statistical measures (distractors)
mean_extended = sum(extended_buffer) / len(extended_buffer)
variance_proxy = sum((x - mean_extended) ** 2 for x in extended_buffer) / len(extended_buffer)
peak_deviation = max(extended_buffer) - min(extended_buffer)

# Real processing begins: filter by threshold
threshold = thresh  # Assign to clearer name
filtered_data = [x for x in extended_buffer if x >= threshold]

# Secondary filtering via set logic (comparison + set operations)
unique_values = set(filtered_data)
minimum_acceptable_set = {x for x in unique_values if x >= 4.0}  # High-value signals only
excluded_count = len(filtered_data) - len([x for x in filtered_data if x >= 4.0])

# Core analysis function (uses slicing and comparison logic)
def analyze_transmission(signal_seq, limit):
    if not signal_seq:
        return 0.0
    
    # Segment into thirds using slicing
    n = len(signal_seq)
    third = n // 3
    first_part = signal_seq[:third]
    mid_part = signal_seq[third:2*third]
    last_part = signal_seq[2*third:]
    
    # Weighted contribution (higher weight on later segments)
    early_avg = sum(first_part) / len(first_part) if first_part else 0
    mid_avg = sum(mid_part) / len(mid_part) if mid_part else 0
    late_avg = sum(last_part) / len(last_part) if last_part else 0
    
    # Composite score with decay adjustment (plausible engineering heuristic)
    raw_score = 0.2 * early_avg + 0.3 * mid_avg + 0.5 * late_avg
    
    # Apply non-linear boost if recent segment exceeds threshold average
    recent_window = signal_seq[-3:] if len(signal_seq) >= 3 else signal_seq
    recent_avg = sum(recent_window) / len(recent_window)
    
    boosted = raw_score * (1.25 if recent_avg > limit else 1.0)
    
    # Final adjustment based on data richness (set size diversity)
    diversity_bonus = len(set(round(x, 1) for x in signal_seq)) * 0.05
    
    final_strength = boosted + diversity_bonus
    
    return round(final_strength, 6)

# Misleading alternate computation (dead end)
temporary_diagnostic = 0
if len(filtered_data) > 10:
    temporary_diagnostic = sum(filtered_data) / 100
else:
    temp_result = [x ** 0.5 for x in filtered_data]
    temporary_diagnostic = sum(temp_result) / 10

# Critical statement
signal_strength = analyze_transmission(filtered_data, threshold)

# Print result as required
print(f"Result: {signal_strength}")