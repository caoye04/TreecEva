def process_data(input_list):
    # Initial processing - some operations are misleading
    temp_sum = sum(input_list) * 2
    processed_data = [x * 3 for x in input_list]
    
    # This intermediate calculation is a red herring
    intermediate = (temp_sum + len(input_list)) // 2
    
    # Conditional logic with multiple branches
    if len(input_list) > 3:
        result = max(processed_data) - min(processed_data)
        # Dead code path - never executed due to condition
        unused_var = intermediate * 10
    else:
        # This path actually gets executed
        sorted_data = sorted(processed_data)
        # Misleading variable name - not actually calculating average
        average_like = sum(sorted_data[1:-1]) if len(sorted_data) > 2 else 0
        result = sorted_data[-1] - sorted_data[0]
    
    # Bitwise operations that don't affect the final result
    bit_mask = 0b1010
    masked_result = result & bit_mask
    
    # Final transformation with conditional expression
    final_result = (result + 5) if result % 2 == 0 else (result - 3)
    
    return final_result

# Main execution
initial_values = [4, 8, 2, 6]
# These variables are distractions
secondary_data = [1, 3, 5, 7]
dummy_calc = sum(secondary_data) * len(initial_values)

# Key execution point
final_output = process_data(initial_values)

# Print the target result
print(f"Target result: {final_output}")