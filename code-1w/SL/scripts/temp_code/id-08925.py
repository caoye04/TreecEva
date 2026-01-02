def transformer(sequence, threshold):
    transformed = []
    for i, val in enumerate(sequence):
        if val > threshold:
            transformed.append(val ** 0.5)
        elif val < threshold:
            transformed.append(val * -1)
        else:
            transformed.append(0)
    return transformed

# Irrelevant helper (distractor)
def dummy_filter(data):
    return [x for x in data if x % 2 == 0]

# Unused auxiliary function (dead code path)
def deprecated_normalizer(arr):
    max_val = max(arr)
    return [x / max_val for x in arr]

# Real processing begins
raw_input = [16, -9, 25, 4, 9, 36, -16]
noise_floor = 10

# Misleading intermediate transformation
noisy_adjustment = [x + 5 for x in raw_input if x > 0]
decoy_sum = sum(noisy_adjustment) * 0.1  # Distractor computation

# Key slicing and real preprocessing
primary_slice = raw_input[1:6]  # [-9, 25, 4, 9, 36]
secondary_slice = [x * 2 for x in raw_input[::2]]  # [32, 50, 18, -32] - irrelevant

# First meaningful transformation
intermediate_vals = transformer(primary_slice, noise_floor)

# Conditional manipulation with zip
paired_data = []
for idx, (a, b) in enumerate(zip(intermediate_vals, intermediate_vals[1:])):
    if idx % 2 == 0:
        paired_data.append(a + b)
    else:
        paired_data.append(a - b)

# Red herring set operation
unique_decoy = set(paired_data)
deleted_median = len(unique_decoy) * 0.5  # Meaningless

# Actual data path
processed_data = [x for x in paired_data if x > 0]
offset = len(primary_slice) - len(processed_data)

# Another decoy structure
shadow_buffer = []
for x in processed_data:
    shadow_buffer.append(x ^ 3)  # Bitwise red herring

# Finalization logic
def finalizer(data, shift):
    base = 0
    for i, v in enumerate(data):
        if i < shift:
            base += v * (i + 1)
        else:
            base += v
    return int(base * 1.5)  # Deterministic scaling

# Critical execution point
equilibrium_score = finalizer(processed_data, offset)

Result: equilibrium_score