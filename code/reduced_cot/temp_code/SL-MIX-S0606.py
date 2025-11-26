def compute_validation_result(data_array, pattern_mask):
    # Initialize tracking variables (some are distractors)
    accumulator = 0
    temp_buffer = []
    validation_flag = False
    
    # Distractor computation - unused in final result
    noise_data = [x * 2 for x in data_array if x % 3 == 0]
    
    # Main processing logic
    for idx, value in enumerate(data_array):
        # Apply pattern mask using string operations
        pattern_char = pattern_mask[idx % len(pattern_mask)]
        
        # Misleading intermediate operation (distractor)
        if pattern_char.isdigit():
            processed_val = value + int(pattern_char) * 5
        else:
            processed_val = value + ord(pattern_char) % 10
        
        # Actual logic - only certain conditions contribute
        if (value % 2 == 0 and pattern_char.isalpha()) or (value % 3 == 0 and pattern_char.isdigit()):
            accumulator += processed_val
            temp_buffer.append(processed_val)
    
    # Dead code path - never executed but looks relevant
    if len(noise_data) > 5:
        validation_flag = True
        
    # Final computation with string operations
    mask_sum = sum(ord(c) for c in pattern_mask if c.isalpha())
    buffer_avg = sum(temp_buffer) // max(len(temp_buffer), 1) if temp_buffer else 0
    
    return accumulator - mask_sum + buffer_avg

# Main execution with mixed data structures
extracted_data = [12, 7, 25, 18, 9, 31, 42]
mask_pattern = "V3R1Fy9X"

# Distractor variables and operations
aux_data = [x - 5 for x in extracted_data if x > 15]
pattern_variations = [mask_pattern[i:] + mask_pattern[:i] for i in range(3)]

# Key computation
final_processed_value = compute_validation_result(extracted_data, mask_pattern)

# More distractor operations (unused in output)
validation_metric = sum(aux_data) * len(pattern_variations)
status_check = "VALID" if final_processed_value > 50 else "INVALID"

print(f"Result: {final_processed_value}")