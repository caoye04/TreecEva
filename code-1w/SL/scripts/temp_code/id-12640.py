from collections import defaultdict

# Simulate a data integrity verification process with mixed operations
def compute_integrity_checksum(data_sequence):
    # Irrelevant tracking map (distractor)
    frequency_map = defaultdict(int)
    temp_magnitude = 0.0
    
    # Initialize key variables
    checksum = 0xAAAA  # Starting seed
    shift_offset = 3
    mask = 0xFFFF
    
    # Preprocess: count frequencies (semi-relevant, but not used directly)
    for val in data_sequence:
        frequency_map[val] += 1
        temp_magnitude += abs(val) ** 0.5
    
    # Normalize magnitude (dead code path - not used later)
    if temp_magnitude > 100:
        temp_magnitude /= len(data_sequence)

    # Main checksum logic with bitwise and arithmetic mixing
    for index, value in enumerate(data_sequence):
        # Transform value using index-dependent logic
        base_transform = (value + index * 2) % 256
        inverted = 255 - base_transform
        
        # Conditional expression to alter flow slightly
        adjustment = 7 if (base_transform & 3) == 0 else (inverted % 9)
        
        # Core processing step
        processed_value = (base_transform + adjustment) & 0xFF
        
        # Update checksum with bitwise shifts and XOR (key operation)
        checksum = (checksum << 1) ^ processed_value & mask
        
        # Extra masking to maintain 16-bit boundary (redundant but realistic)
        checksum &= mask
        
        # Spurious state update (distractor)
        if index % 5 == 0:
            checksum ^= (index >> 1)
    
    # Final irrelevant transformation (does not affect prior logic)
    string_artifact = "final" + "_tag" * (checksum % 3)
    string_length = len(string_artifact.upper())
    
    # Output target result
    print(f"Result: {checksum}")
    return checksum

# Input data derived from mathematical sequence
raw_data = [x**2 % 19 for x in range(1, 14)]
raw_data = [x for x in raw_data if x % 2 == 1]  # Filter odd remainders

# Execute computation
result = compute_integrity_checksum(raw_data)