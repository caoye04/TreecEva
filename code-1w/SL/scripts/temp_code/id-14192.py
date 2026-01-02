from itertools import compress, cycle

# Simulated sensor data with noise and redundant readings
data_stream = [105, 92, 110, 88, 95, 120, 76, 103, 89, 98, 115, 85]
threshold = 90
smoothing_factor = 0.1

# Noise mask generated for irrelevant filtering (distractor)
noise_pattern = [(i % 3 == 0) for i in range(len(data_stream))]
cleaned_data = list(compress(data_stream, [not x for x in noise_pattern]))

# Extract high-confidence readings above threshold
high_confidence = [x for x in data_stream if x > threshold]

# Misleading transformation: exponential smoothing (not used in final result)
smoothed = [high_confidence[0]]
for i in range(1, len(high_confidence)):
    smoothed.append(smoothing_factor * high_confidence[i] + (1 - smoothing_factor) * smoothed[i-1])

# Validation based on alternating pattern (relevant)
validation_cycle = cycle([True, False])
is_valid = [next(validation_cycle) for _ in range(len(data_stream))]
valid_entries = [data_stream[i] for i in range(len(data_stream)) if is_valid[i]]

# Weight assignment using modular arithmetic (semi-relevant)
basic_weights = [(i % 4) + 1 for i in range(len(valid_entries))]
adjusted_weights = [w ** 0.5 for w in basic_weights]  # Transform not ultimately used
weights = [w if w <= 2 else 2 for w in adjusted_weights]  # Clamp values

# Auxiliary calculation: peak-to-peak difference in valid entries (distraction)
if valid_entries:
    ptp_diff = max(valid_entries) - min(valid_entries)
    correction_offset = ptp_diff // 10
    for i in range(len(weights)):
        weights[i] += correction_offset * 0.1  # Minor tweak ignored in logic

# Core processing function
def process_results(entries, weight_profile):
    base_total = sum(entries)
    weight_multiplier = sum(weight_profile) / len(weight_profile) if weight_profile else 1
    
    # Conditional boost based on entry count parity (relevant)
    if len(entries) % 2 == 0:
        adjustment = 1.1
    else:
        adjustment = 0.95
    
    # Apply multiplier and adjustment
    intermediate = base_total * weight_multiplier * adjustment
    
    # Red herring: normalize by fake scale
    fake_scale = 123.45
    normalized = intermediate / fake_scale
    denormalized = normalized * fake_scale  # Undo normalization (no effect)
    
    # Final non-trivial mapping via character counting logic
    modifier_key = "calibration_override"
    char_count_mod = len(modifier_key) % 7  # Yields 18 % 7 = 4
    final = int(denormalized + char_count_mod * 10)
    
    return final

# Execute main logic
temp_var = [x * 2 for x in data_stream if x < 80]  # Dead-end computation
flag_check = any(x > 150 for x in data_stream)  # Irrelevant check

final_score = process_results(valid_entries, weights)
print(f"Target result: {final_score}")