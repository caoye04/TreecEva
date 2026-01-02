import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x * 2 for x in data if x < 0]

# Decoy transformation with misleading intermediate results
def decoy_transform(seq):
    temp = [math.sin(x) for x in seq]
    scaled = [int(abs(t * 100)) for t in temp]
    return scaled[::-1]  # Reversed, never used

# Real transformation pipeline
def transform_entry(val):
    if val <= 0:
        return abs(val) ** 2 + 5
    else:
        return int(math.sqrt(val)) * 3

def apply_mask(sequence, mask):
    return [s ^ m for s, m in zip(sequence[:len(mask)], mask)]

def process_sequence(data_slice):
    # Slice operation: use only middle portion
    mid_section = data_slice[2:6]
    accumulated = 0
    for idx, item in enumerate(mid_section):
        if idx % 2 == 0:
            accumulated += item * (idx + 1)
        else:
            accumulated -= item // (idx + 1)
    return accumulated + len(mid_section)

# Initialization of various unrelated variables (distractors)
noise_level = 0.003
max_iterations = 500
convergence_threshold = 1e-6
temp_buffer = [0] * 10
counter_log = {'updates': 0, 'resets': 0}

# Primary data setup (real input)
raw_input = tuple(range(8, 16))  # (8, 9, 10, 11, 12, 13, 14, 15)

# Multiple assignment and destructuring (relevant)
a, b, c, d, e, f, g, h = raw_input
shifted_values = [b, c, d, e, f, g, h, a]  # Left rotation

# Apply real transformation chain
transformed_data = [transform_entry(x) for x in shifted_values]

# Masking step with bitwise XOR (critical step hidden among noise)
mask_pattern = [10, 5, 15, 8]
masked_data = apply_mask(transformed_data, mask_pattern)  # Affects first four elements

# More irrelevant computations (red herrings)
analysis_report = {
    'mean_noise': sum(temp_buffer) / len(temp_buffer),
    'peak_shift': max(shifted_values) - min(shifted_values),
    'entropy': math.log(len(raw_input)),
    'checksum': sum(decoy_transform(raw_input)) % 100
}

# Critical execution point
final_output = process_sequence(masked_data)

# Output result as required
print(f"Target result: {final_output}")