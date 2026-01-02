def compute_integrity_signature(input_sequence):
    # Irrelevant preprocessing: normalize input with unused transformation
    normalized = [((x + 17) * 3) % 256 for x in input_sequence]
    shadow_copy = normalized[::-1]  # Slicing used, but result not directly used later

    # Dead code path: this function is defined but never called
    def validate_consistency(arr):
        return all(a ^ b != 0 for a, b in zip(arr, arr[1:]))

    # Unused statistical measures (distractors)
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in normalized) / len(normalized) if normalized else 0

    # Key data extraction (only this part matters)
    filtered = [x for x in input_sequence if x % 2 == 1]  # Keep only odd values
    segment = filtered[1:6]  # Slice middle portion - slicing relevant here

    # Red herring: complex bit rotation that looks important but isn't final
    temp_rotation = 0
    for i, val in enumerate(segment):
        temp_rotation ^= (val << (i % 4)) | (val >> (8 - (i % 4)))

    # Another decoy checksum with similar naming
    pseudo_checksum = sum(segment) * 7 & 0xFFFFFFFF

    # Actual critical computation begins
    data_sum = sum(segment)  # Sum of sliced odd elements

    # Simulated key derived from length and bit pattern
    base_key = len(input_sequence) * 97
    rotation_key = 0
    for b in range(8):
        rotation_key |= ((base_key >> b) & 1) << (7 - b)  # Bit reversal

    # Critical statement: answer depends on this XOR and mask
    checksum = (data_sum ^ rotation_key) & 0xFFFF

    # More distraction: unused encoding pass
    encoded_stream = bytes([checksum & 0xFF, (checksum >> 8) & 0xFF])
    parity_check = bin(checksum).count('1') % 2  # Unused parity

    return checksum

# Input with specific structure
input_data = [12, 23, 45, 67, 89, 101, 111, 134, 157]

result = compute_integrity_signature(input_data)
print(f"Target result: {result}")