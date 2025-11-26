def process_data_stream(input_data):
    # Irrelevant helper function with misleading computations
    dummy_values = [x * 2 for x in range(10)]
    temp_sum = sum(dummy_values)
    unused_result = temp_sum // 3  # Dead code path
    
    # Actual processing with set operations
    data_set = set(input_data)
    filtered_data = {x for x in data_set if x % 2 == 0}
    
    # Misleading intermediate calculation
    misleading_total = len(data_set) * 100
    
    # Lambda function for transformation
    transform_fn = lambda x: (x ** 2) - (x % 7)
    transformed_data = list(map(transform_fn, filtered_data))
    
    return sum(transformed_data) - len(transformed_data)

def compute_final_value(data_sequence):
    # Multiple irrelevant variables and computations
    base_value = 42
    offset_calc = (base_value << 2) + 15  # Bit shift distraction
    
    # Dead code path that looks important
    if offset_calc > 200:
        unused_branch = offset_calc // 10
    else:
        unused_branch = offset_calc * 5
    
    # Core logic with complex interdependencies
    stage1_result = process_data_stream(data_sequence)
    
    # More misleading calculations
    distraction_factor = len(data_sequence) * 3.14159
    
    # Final computation with actual answer
    actual_result = stage1_result - (len(data_sequence) % 11) + 7
    
    # Another irrelevant calculation that looks similar
    similar_calc = actual_result + distraction_factor
    
    return actual_result

# Main execution with data stream
input_stream = [3, 8, 12, 5, 8, 17, 12, 20, 3, 25]

# Multiple irrelevant intermediate variables
preliminary_check = sum(input_stream) % 9
secondary_analysis = [x for x in input_stream if x > 10]

# The critical execution point
final_result = compute_final_value(input_stream)

# Print the target result
print(f"Result: {final_result}")