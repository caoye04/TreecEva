def calculate_data_stats(input_values):
    # Irrelevant processing that creates misleading intermediate values
    temp_sum = sum(input_values)
    max_val = max(input_values)
    min_val = min(input_values)
    
    # Distractor operations that don't affect final result
    avg_val = temp_sum / len(input_values)
    range_val = max_val - min_val
    
    # Redundant calculations for interference
    product_val = 1
    for val in input_values:
        product_val *= val
    
    # Main logic path with bitwise operations
    processed = []
    for i, val in enumerate(input_values):
        if i % 2 == 0:
            processed.append((val << 1) | 0b1)  # Left shift and OR
        else:
            processed.append((val >> 1) & 0b1111)  # Right shift and AND
    
    # Set operations for interference
    unique_vals = set(processed)
    common_elements = unique_vals & {3, 7, 15}
    
    # Dictionary operations with misleading keys
    data_map = {k: v * 2 for k, v in enumerate(processed)}
    adjustment_factor = len(common_elements) * 5
    
    # Conditional expression with logical operations
    penalty_offset = 10 if len(processed) > 3 and max(processed) < 20 else 15
    
    # Dead code path that's never executed
    if product_val > 1000:
        bonus = 25
    else:
        bonus = 0
    
    # The actual computation that matters
    final_score = processed[2] + adjustment_factor - penalty_offset
    
    # Print irrelevant values for distraction
    print(f"Debug - temp_sum: {temp_sum}, range_val: {range_val}")
    print(f"Debug - unique_count: {len(unique_vals)}, common_count: {len(common_elements)}")
    
    # Critical output
    print(f"Target result: {final_score}")
    return final_score

# Test execution with specific input
sample_data = [4, 9, 12, 7, 3]
result = calculate_data_stats(sample_data)