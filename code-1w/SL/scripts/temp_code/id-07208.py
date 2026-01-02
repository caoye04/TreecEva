import itertools

# System calibration constants (distractors)
CALIBRATION_FACTOR = 0.987
BASELINE_OFFSET = -42
TEMPORAL_DELAY = 1729

# Signal processing parameters
def generate_kernel(size):
    return [((i * i) % 13) - 6 for i in range(size)]

# Irrelevant helper function – dead code path
def deprecated_normalizer(x):
    return sum([val ** 2 for val in x]) ** 0.5 if x else 0

# Real transformation logic
def cyclic_modular_transform(seq, key):
    result = []
    for i, val in enumerate(seq):
        shifted = (val + key) % 11
        adjusted = shifted if shifted < 7 else shifted - 11
        result.append(adjusted * 2)
    return result

# Buffer transformation with slicing and conditional logic
def transform_buffer(data, weight_vector):
    # Distractor: unused slice
    mid_section = data[3:7]
    extended_data = data + [x * -1 for x in data[:4]]

    # Weight application with conditional expression
    applied_weights = [
        weight_vector[i % len(weight_vector)] * val 
        if i % 3 != 0 else val + BASELINE_OFFSET // 10
        for i, val in enumerate(extended_data)
    ]

    # Real computation branch
    processed = cyclic_modular_transform(applied_weights[:8], 5)

    # Decoy accumulation (never used)
    accumulator = 0
    for x in applied_weights:
        accumulator += x * CALIBRATION_FACTOR
        if accumulator > 100:
            accumulator = 0  # Reset logic (misleading)

    # Final transformation using slicing and itertools.cycle
    cycle_iter = itertools.cycle([1, -1])
    final = [
        a + b * next(cycle_iter) 
        for a, b in zip(processed, processed[1:] + [processed[0]])
    ]

    # Insert irrelevant intermediate check
    if sum(final) % 7 == 0:
        final[1] += 1  # Minor perturbation (doesn't affect target index)

    return final

# Initialization vectors (mix of relevant and irrelevant)
raw_input = [3, 7, 2, 8, 5, 1, 9, 4]
weights = [0.5, 1.5, 0.8]
cyclic_shift = raw_input[2:] + raw_input[:2]  # Rotate left by 2

# Unused signal chain components (red herrings)
decimated_signal = [x for i, x in enumerate(raw_input) if i % 2 == 0]
filtered_noise = [x - CALIBRATION_FACTOR for x in decimated_signal]

# Key computational steps
normalized_input = [x - min(raw_input) for x in raw_input]
indexed_map = {i: v * 3 for i, v in enumerate(normalized_input)}

# Dead-end recursive function (distractor)
def trace_path(val, depth):
    if depth <= 0:
        return val
    return trace_path((val * 2) % 19, depth - 1)

# Actual execution flow
staged_data = cyclic_modular_transform(normalized_input, 3)
buffer_state = staged_data[::-1]  # Reverse

# Critical statement
phase_output = transform_buffer(cyclic_shift, weights)[2]

# Irrelevant aggregation
summary_stats = {
    'peak': max(buffer_state),
    'range': max(buffer_state) - min(buffer_state),
    'calib_ref': trace_path(7, 5)
}

# Output only the target result
print(f"Target result: {phase_output}")