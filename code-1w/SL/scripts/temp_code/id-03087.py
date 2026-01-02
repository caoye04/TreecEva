from itertools import cycle

# Simulate a data integrity checker with redacted transformations
def main():
    raw_data = [12, 45, 67, 23, 89, 34, 76]
    key_sequence = [3, 1, 4, 1, 5]
    temp_offset = sum(raw_data) % 100  # Irrelevant summary stat

    processed = []
    for i, val in enumerate(raw_data):
        shifted = val ^ (i * 7)  # Bitwise obfuscation
        masked = shifted & 0xFF
        processed.append(masked)

    # State buffer built from transformed data
    state_buffer = [(x + temp_offset) % 256 for x in processed]

    running_sum = 0
    magnitude_tracker = []
    for j, byte in enumerate(state_buffer):
        if j % 2 == 0:
            running_sum += byte * 2
        else:
            running_sum -= byte
        magnitude_tracker.append(abs(running_sum))  # Distractor: not used later

    # Apply cyclic key mixing (only first 5 elements matter)
    mixed_state = []
    for b, k in zip(state_buffer[:5], cycle(key_sequence)):
        mixed_state.append((b + k) % 256)

    # Red herring: entropy-like calculation (unused)
    bit_entropy = 0
    for num in mixed_state:
        while num:
            bit_entropy += num & 1
            num >>= 1

    # Finalize hash using only mixed_state
    checksum = finalize_hash(mixed_state)
    
    # Additional distraction: unused transformation chain
    shadow_copy = state_buffer.copy()
    for idx in range(len(shadow_copy) - 1):
        shadow_copy[idx] = shadow_copy[idx] ^ shadow_copy[idx + 1]
    
    print(f"Result: {checksum}")


def finalize_hash(block):
    result = 0
    for i, val in enumerate(block):
        result += val * (3 ** i)  # Exponential weighting
    return result % 98765  # Bound result to reasonable range

if __name__ == "__main__":
    main()