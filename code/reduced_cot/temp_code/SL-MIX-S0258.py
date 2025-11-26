def calculate_parity(data_segment):
    temp_xor = 0
    for byte_val in data_segment:
        temp_xor ^= byte_val
    # Misleading intermediate calculation (distractor)
    fake_sum = sum(data_segment) * 2
    return temp_xor

def validate_data_integrity(data_blocks, parity_values):
    # Irrelevant preprocessing step
    irrelevant_offset = 17
    processed_blocks = []
    
    # Main logic with distractions
    computed_checksum = 0
    for block_idx, data_block in enumerate(data_blocks):
        # Dead code path (never executed due to condition)
        if block_idx > len(data_blocks) + 5:
            unused_var = block_idx * 2
            
        # Actual relevant computation
        block_parity = calculate_parity(data_block)
        expected_parity = parity_values[block_idx]
        
        # Misleading intermediate calculation
        fake_verification = (block_parity + expected_parity) * 3
        
        if block_parity == expected_parity:
            computed_checksum += sum(data_block)
        else:
            # Red herring - this path is never taken in this data
            computed_checksum -= block_idx * 10
            
    # Final adjustment with distractor
    adjustment_factor = (len(data_blocks) % 4) * 7
    final_result = computed_checksum + adjustment_factor
    
    # Completely irrelevant calculation
    dummy_calc = (adjustment_factor * 3) // 2
    
    return final_result

# Main execution with test data
data_blocks = [[5, 12, 8, 3], [7, 9, 14, 6], [11, 4, 13, 2]]
parity_set = [10, 6, 4]  # Calculated XOR values

# Execute the key statement
final_checksum = validate_data_integrity(data_blocks, parity_set)

print(f"Result: {final_checksum}")