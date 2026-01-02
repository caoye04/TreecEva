import itertools

# Simulated sensor data preprocessing with red herrings
def collect_diagnostics(sensor_log):
    checksum = 0
    for val in sensor_log:
        checksum ^= val % 255
    return checksum

# Irrelevant transformation chain (dead path)
def legacy_normalization(x):
    if x < 0:
        return 0
    elif x > 100:
        return 100
    return x * 0.76

# Unused but plausible function (distractor)
def compute_entropy(sequence):
    freqs = {}
    for item in sequence:
        freqs[item] = freqs.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freqs.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, misleading
    return round(entropy, 4)

# Core logic disguised among distractions
def apply_phase_shift(values, shift):
    shifted = []
    for i in range(len(values)):
        shifted.append((values[i] * (i + 1)) >> shift if shift else values[i] * (i + 1))
    return shifted

# Conditional transformation based on flag patterns
def evaluate_threshold_breach(data, threshold=45):
    return sum(1 for x in data if x > threshold)

# Main processing with multiple concepts
control_flags = {
    'enable_bit_correction': True,
    'use_legacy_path': False,
    'validate_checksum': False,
    'debug_mode': True  # Unused but distracting
}

raw_readings = [12, 15, 23, 34, 45, 56, 67, 78]
diagnostic_trace = [255, 192, 128, 64, 32]

# Distractor: unused diagnostic computation
diag_checksum = collect_diagnostics(diagnostic_trace)

# Real pipeline begins here — heavily masked by noise
filtered_data = [x for x in raw_readings if x % 2 == 0]  # Only even values

expanded_grid = list(itertools.product(filtered_data[:3], [2, 3]))
grid_sum = sum(a * b for a, b in expanded_grid)

# Bit manipulation and arithmetic mix
temp_buffer = []
for idx, val in enumerate(filtered_data):
    temp_val = val ^ 255  # Invert bits
    if idx % 2 == 0:
        temp_val = (temp_val << 1) & 511  # Shift left, mask to 9 bits
    temp_buffer.append(temp_val)

# Conditional expression with set operations
reference_set = {10, 20, 30, 40, 50}
candidate_pool = {x % 50 for x in temp_buffer}
overlap_count = len(reference_set & candidate_pool)

# Key conditional expression
adjustment_factor = 1.75 if overlap_count >= 2 else 0.85

# Apply phase shift (bitwise + arithmetic)
shift_level = 1 if control_flags['enable_bit_correction'] else 0
transformed_signal = apply_phase_shift(temp_buffer, shift_level)

# Min/max/average calculations (some used, some not)
signal_min = min(transformed_signal)
signal_max = max(transformed_signal)
signal_avg = sum(transformed_signal) / len(transformed_signal)

# Unused statistical distraction
variance_proxy = sum((x - signal_avg) ** 2 for x in transformed_signal) / len(transformed_signal)

# Logical operations and comparisons
breach_count = evaluate_threshold_breach(transformed_signal, threshold=400)
valid_condition = (signal_avg > 300) and (breach_count > 0) or (overlap_count == 0)

# Data structure fusion via tuple unpacking (relevant)
stats_bundle = (grid_sum, overlap_count, diag_checksum, variance_proxy)
base_score, match_count, _, _ = stats_bundle  # Unpacking with ignored values

# Final transformation chain
intermediate_result = base_score + (match_count * 50)

# Critical statement: complex mixed operations
final_output = int(intermediate_result * adjustment_factor)

# Output result as required
print(f"Result: {final_output}")