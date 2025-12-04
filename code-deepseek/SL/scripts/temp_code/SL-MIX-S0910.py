from collections import Counter

def encrypt_data(data_values):
    # Initial processing phase (irrelevant to final result)
    temp_buffer = [x * 2 + 1 for x in data_values]
    hash_cache = {}
    
    # Main encryption logic
    checksum = 0
    byte_shift = 3
    mask_pattern = 0b10101010
    
    for idx, value in enumerate(data_values):
        # Distractor: complex but unused calculation
        hash_cache[idx] = (value << byte_shift) ^ mask_pattern
        
        # Actual checksum calculation
        if idx % 2 == 0:
            checksum += value & 0xFF
        else:
            checksum -= value | 0x7F
    
    # Validation phase (dead code path)
    if checksum > 1000:
        validation_flag = checksum // 10
        byte_shift = validation_flag ^ 0x55  # Red herring
    
    # Final adjustment
    checksum = checksum % 256
    
    # Misleading intermediate operation
    dummy_calc = (checksum << 2) + byte_shift
    
    return checksum

# Test data
data_sequence = [45, 128, 77, 201, 63, 92, 144, 31]

# Irrelevant processing
data_backup = data_sequence.copy()
processed_data = [x ^ 0xFF for x in data_backup]
frequency_map = Counter(processed_data)

# Main execution
encryption_checksum = encrypt_data(data_sequence)

# Print result
print(f"Result: {encryption_checksum}")