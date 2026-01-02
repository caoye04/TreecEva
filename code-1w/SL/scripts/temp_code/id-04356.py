import math

# Simulated sensor data with noise and redundant channels
data_stream = [0.7, 1.2, 3.5, 2.1, 4.8, 5.0, 3.3, 2.7, 4.4, 5.1] + [None] * 5  # Padding (irrelevant)

# Irrelevant calibration constants (distractors)
calib_a = 0.987
calib_b = 1.013
calibration_matrix = [[calib_a, calib_b], [calib_b, calib_a]]
offset = sum(sum(row) for row in calibration_matrix) / 4  # Unused computation

# Noise filter threshold (partially relevant but overcomplicated)
noise_threshold = lambda x: abs(x - 3.0) > 1.5
filtered_data = [x for x in data_stream if x is not None and not noise_threshold(x)]

# Signal amplification using exponentiation (only some values used later)
amplified = [round(math.exp(x / 10), 4) for x in filtered_data]
baseline = sum(amplified) / len(amplified) if amplified else 0  # Distractor baseline

# Temporal slicing: only middle segment is relevant
segment_window = filtered_data[1:6]  # Actual working data

# Secondary processing: apply logarithmic correction to dampen high values
log_corrected = [math.log(x + 1) for x in segment_window]

# Weight vector (overengineered)
weights = [0.1 * (i+1) for i in range(len(log_corrected))]
normalized_weights = [w / sum(weights) for w in weights]

# Apply weighted average (red herring: not used in final result)
pseudo_result = sum(log_corrected[i] * normalized_weights[i] for i in range(len(log_corrected)))

# Key transformation: bitwise manipulation on truncated integers (critical path)
truncated = [int(x) for x in segment_window]
bit_ops = [val ^ 3 | 1 & val for val in truncated]  # XOR with mask, then OR with masked AND

# Accumulation via controlled recursion (core logic step)
def accumulate_with_decay(values, decay=0.9):
    if not values:
        return 0
    return values[0] + decay * accumulate_with_decay(values[1:], decay)

recursive_sum = accumulate_with_decay(bit_ops, decay=0.75)

# Final adjustment: use slicing to extract pattern from amplified (unused distractor)
amplified_pattern = amplified[::2]  # Every other element — irrelevant
pattern_sum = sum(amplified_pattern)

# Control flow with misleading conditionals
if recursive_sum < 10:
    scaling_factor = 2.5
elif recursive_sum > 20:
    scaling_factor = 0.5  # Never reached
else:
    scaling_factor = 1.0  # This branch is taken

# Decoy function that looks important but does nothing
def finalize_signal(signal):
    signal *= 1.01
    signal -= 0.01
    return round(signal, 4)

# Actual final computation
intermediate = recursive_sum * scaling_factor

# Unrelated list comprehension (dead code)
decoys = [finalize_signal(x * 2) for x in amplified if x > 1.5]

# Core answer derivation
final_output = int(intermediate + 0.5)  # Round to nearest integer

print(f"Result: {final_output}")