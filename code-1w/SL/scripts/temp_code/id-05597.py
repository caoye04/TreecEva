def process_data_block(block):
    # Precompute transformation factors
    shift_factor = len(block) % 7
    mask = (1 << shift_factor) - 1
    masked_values = [v & mask for v in block if v > 0]  # Irrelevant filtering

    # Core logic: string-based rotation key
    rotation_key = ''.join([str((x * 2) % 10) for x in block])
    rotated = rotation_key[shift_factor:] + rotation_key[:shift_factor]

    # Convert back to integers for checksum
    digits = [int(d) for d in rotated]

    # Secondary distraction: unused frequency map
    freq_map = {d: digits.count(d) for d in set(digits)}
    threshold = sum(digits) / len(digits) if digits else 0

    # Real computation: weighted XOR with position
    weighted_xor = 0
    for i, d in enumerate(digits):
        if d % 2 == 1:
            weighted_xor ^= (d * i)  # Only odd digits contribute

    # Final transformation
    correction = len(masked_values) - shift_factor
    final_checksum = weighted_xor + correction

    return final_checksum

# Data setup
raw_sequence = [12, 7, 3, 8, 1, 4, 6]
data_segment = [(x ^ (x % 5)) + 2 for x in raw_sequence]  # Apply obfuscation

# Misleading auxiliary computation (dead-end)
dummy_analysis = [x for x in data_segment if x > 10]
temp_sum = sum(dummy_analysis) * 2 if dummy_analysis else 0

# Key execution point
final_checksum = process_data_block(data_segment)
print(f"Result: {final_checksum}")