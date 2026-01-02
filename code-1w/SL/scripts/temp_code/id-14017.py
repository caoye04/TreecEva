def transform_sequence(seq, key_offset):
    """Apply complex transformation with red herrings."""
    transformed = []
    temp_accum = 0
    decoy_counter = 0  # Irrelevant tracking
    for i, val in enumerate(seq):
        if i % 3 == 0:
            temp_accum += val * (i + 1)
        elif i % 3 == 1:
            temp_accum -= (val ^ key_offset) >> 1
        else:
            temp_accum += (val + key_offset) % 7
        transformed.append(temp_accum * (i + 1))  # Real transformation
        decoy_counter += 1  # Unused variable
    return transformed


def mask_data(data, threshold=100):
    """Mask values above threshold (distractor function)."""
    masked = []
    total_masked = 0
    for x in data:
        if x > threshold:
            masked.append(-1)
            total_masked += 1
        else:
            masked.append(x)
    # This function is never used in critical path
    return masked


def filter_by_bit_condition(data):
    """Filter elements where number of set bits is even."""
    filtered = [x for x in data if bin(x).count('1') % 2 == 0]
    return filtered


def compute_checksum(data):
    """Compute XOR-based checksum with offset."""
    checksum = 0
    for idx, num in enumerate(data):
        checksum ^= (num + idx) & 0xFFFF
    return checksum

# Initialization block with mixed relevance
raw_input_stream = [12, 89, 45, 67, 23, 91, 34, 78]
key_rotation = 5
offset_correction = 17  # Used only once

# Apply primary transformation
processed_signal = transform_sequence(raw_input_stream, key_rotation)

# Decoy operations: create illusion of signal filtering
normalized_signal = [round(x / 10.0) for x in processed_signal]  # Not used later
clipped_signal = [min(max(x, 0), 255) for x in normalized_signal]  # Dead end

# Actual relevant path begins here
working_data = [int(x + offset_correction) for x in processed_signal]

# Conditional filtering based on bit parity (key logic)
filtered_data = filter_by_bit_condition(working_data)

# Compute final result
filtered_checksum = compute_checksum(filtered_data)

# Print result as required
print(f"Result: {filtered_checksum}")