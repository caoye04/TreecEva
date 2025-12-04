def analyze_data_patterns(dataset):
    # Initialize tracking variables
    pattern_sum = 0
    irrelevant_counter = 17
    temp_buffer = []
    
    # Process dataset with multiple operations
    for item in dataset:
        # Main processing logic
        if item % 2 == 0:
            pattern_sum += item * 2
            temp_buffer.append(item + 5)  # Irrelevant side effect
        else:
            pattern_sum -= item // 3
            irrelevant_counter += item % 7  # Misleading calculation
    
    # Complex intermediate processing
    intermediate = pattern_sum * 3
    misleading_temp = intermediate // 2 + irrelevant_counter
    
    # Dictionary operations for analysis
    analysis_dict = {
        'primary': pattern_sum,
        'secondary': intermediate,
        'distractor': misleading_temp,
        'buffer_size': len(temp_buffer)
    }
    
    # Final computation with bitwise operations
    result = (analysis_dict['primary'] ^ analysis_dict['secondary']) & 0xFF
    result += analysis_dict['buffer_size'] * 8
    
    return result

def compute_final_value(input_data):
    # Initial setup with distractors
    base_value = 42
    dummy_accumulator = 0
    shadow_var = 127
    
    # Call main analysis function
    analysis_result = analyze_data_patterns(input_data)
    
    # Complex conditional processing
    if analysis_result > 100:
        final = analysis_result - base_value + (shadow_var >> 3)
        dummy_accumulator = final * 2  # Dead code path
    else:
        final = analysis_result + base_value - (shadow_var & 0x1F)
    
    # Additional misleading operations
    temp_var = final ^ 0xAA
    another_temp = temp_var // 4
    
    # Return the actual result
    return final

# Main execution
sample_data = [12, 7, 25, 18, 9, 31, 14]
data_analysis = sample_data
final_result = compute_final_value(data_analysis)

# Print the target variable
print(f"Result: {final_result}")