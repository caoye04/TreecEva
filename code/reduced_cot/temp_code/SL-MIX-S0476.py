def compute_final_value(data_stream, mask_pattern):
    temp_buffer = [x * 2 for x in data_stream if x > 0]
    intermediate_sum = sum(temp_buffer)
    
    # Distractor operations that don't affect final result
    dummy_shift = intermediate_sum << 2
    unused_xor = dummy_shift ^ 0xFF
    
    filtered_set = set(data_stream) & set(mask_pattern)
    filtered_sum = sum(filtered_set)
    
    # More irrelevant computations
    backup_calc = (len(data_stream) * 3) // 2
    shadow_value = backup_calc + 10
    
    result = (intermediate_sum - filtered_sum) % 256
    
    # Final distraction that's unused
    alternative_result = result | 0x80
    
    return result

data_stream = [15, 22, 8, 31, 45, 12, 19]
mask_pattern = [8, 12, 19, 27, 33]

# Execute the key statement
final_checksum = compute_final_value(data_stream, mask_pattern)
print(f"Result: {final_checksum}")