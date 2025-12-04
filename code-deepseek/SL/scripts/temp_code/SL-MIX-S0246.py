def compute_final_value(data_list):
    # Initialize processing variables
    temp_sum = 0
    intermediate_result = 0
    processed_count = 0
    
    # Process each element with zip and enumerate
    for idx, (val_a, val_b) in enumerate(zip(data_list, [x * 2 for x in data_list])):
        # Calculate intermediate values (some are relevant, some are distractors)
        temp_product = val_a * val_b
        temp_sum += temp_product
        
        # Distractor calculation that doesn't affect final result
        unused_value = idx * 3 + temp_product % 7
        
        # Relevant logic with bitwise operations
        if idx % 2 == 0:
            intermediate_result |= (temp_product & 0xFF)
        else:
            intermediate_result ^= (temp_product >> 2)
        
        processed_count += 1
    
    # Additional distractor operations
    redundant_avg = temp_sum / len(data_list) if data_list else 0
    normalized_value = redundant_avg * 0.5
    
    # Final computation using processed results
    final_value = intermediate_result - (temp_sum % 256)
    return final_value

# Main execution
input_data = [12, 8, 15, 6, 20]
secondary_data = [x + 3 for x in input_data]  # Distractor data not used

# Process the data through multiple steps
processed_data = [x | (x % 4) for x in input_data]
final_output = compute_final_value(processed_data)

print(f"Target result: {final_output}")