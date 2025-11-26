def process_data(set_a, set_b):
    # Calculate intersections and differences
    common_elements = set_a.intersection(set_b)
    unique_to_a = set_a.difference(set_b)
    unique_to_b = set_b.difference(set_a)
    
    # Process unique elements (distractor operation)
    temp_sum_a = sum(unique_to_a) if unique_to_a else 0
    temp_sum_b = sum(unique_to_b) if unique_to_b else 0
    
    # Calculate XOR operations on elements
    xor_result = 0
    for i, val in enumerate(common_elements):
        xor_result ^= (val << 1)  # Shift and XOR
    
    # Additional distractor calculation that doesn't affect final result
    redundant_calc = (temp_sum_a * temp_sum_b) // 3
    
    # Final computation using bitwise operations
    result = xor_result + len(unique_to_a) - len(unique_to_b)
    
    return result

# Initialize data sets
primary_set = {4, 7, 12, 15}
secondary_set = {7, 12, 20, 25}

# Process the data
final_result = process_data(primary_set, secondary_set)

# Print the result
print(f"Result: {final_result}")