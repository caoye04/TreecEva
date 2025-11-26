def process_data_sets(data_strings):
    temp_results = []
    irrelevant_sum = 0
    
    # Distractor computations
    unused_var = 0
    for i in range(5):
        unused_var += i * 2  # Dead code path
        
    # Main processing logic
    for data_str in data_strings:
        # String processing - relevant
        char_count = len(data_str.strip())
        first_char_ord = ord(data_str[0]) if data_str else 0
        
        # Misleading intermediate calculation
        temp_calc = (char_count << 2) ^ 15
        irrelevant_sum += temp_calc  # Red herring
        
        # Actual important calculation
        if char_count % 2 == 0:
            processed_val = (first_char_ord & 0x3F) | ((char_count * 3) & 0xC0)
        else:
            processed_val = (first_char_ord ^ 0x1F) & ((char_count + 7) | 0x80)
            
        temp_results.append(processed_val)
    
    # More distractor operations
    fake_total = sum(temp_results) + irrelevant_sum
    unused_result = fake_total >> 4  # Never used
    
    # Core logic chain
    processed_value = temp_results[1] if len(temp_results) > 1 else temp_results[0]
    mask_value = (temp_results[0] ^ temp_results[-1]) & 0xFF
    offset_val = (len(data_strings[0]) * 8) | 0x0F
    
    # Final critical computation
    final_result = processed_value | (mask_value & ~offset_val)
    
    print(f"Result: {final_result}")
    return final_result

# Test execution with specific input
data_inputs = ["alpha", "betaX", "gammaYZ"]
result = process_data_sets(data_inputs)
print(f"Target result: {result}")