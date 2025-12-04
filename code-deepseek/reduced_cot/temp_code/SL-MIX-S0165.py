def transform_data(input_seq, pattern_mask):
    temp_buffer = []
    irrelevant_sum = 0
    dummy_flag = False
    
    # Irrelevant string processing (distractor)
    text_data = "cryptographic_analysis"
    processed_text = text_data.upper().replace('_', '-').split('-')
    char_count = sum(len(word) for word in processed_text)
    
    # Main transformation logic
    for idx, value in enumerate(input_seq):
        # Dead code path that never executes
        if dummy_flag and idx > 100:
            irrelevant_sum += value * 2
            continue
            
        # Mask application with bitwise operations
        mask_value = pattern_mask[idx % len(pattern_mask)]
        transformed = (value ^ mask_value) & 0xFF
        
        # Irrelevant intermediate calculation
        temp_calc = (transformed << 2) | (transformed >> 6)
        irrelevant_sum += temp_calc
        
        temp_buffer.append(transformed)
    
    # Unused complex computation (distractor)
    unused_result = [(x | 0x80) for x in temp_buffer if x % 2 == 0]
    
    # Final computation using zip
    final_result = 0
    for a, b in zip(temp_buffer, pattern_mask * len(temp_buffer)):
        final_result = (final_result << 8) | (a ^ b)
    
    # Misleading intermediate assignment
    interim_value = final_result + irrelevant_sum
    return interim_value % 100000

# Data initialization
mask_pattern = [0x37, 0x5A, 0x89, 0xF2]
data_sequence = [120, 67, 255, 42, 189, 13, 200, 91]

# Irrelevant variable setup
unused_counter = 0
backup_data = data_sequence.copy()
redundant_flag = True

# Key execution point
final_encrypted = transform_data(data_sequence, mask_pattern)

# Print the result
print(f"Target result: {final_encrypted}")