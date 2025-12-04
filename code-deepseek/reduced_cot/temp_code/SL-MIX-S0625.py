def process_set_operations(data_values, limit):
    # Distractor: unused lambda function
    square_if_even = lambda x: x**2 if x % 2 == 0 else x
    
    # Relevant preprocessing
    processed = [x * 2 if x > 5 else x + 1 for x in data_values]
    
    # Misleading intermediate operation
    temp_sum = sum(processed) * 3
    
    # Distractor: dead code path
    if temp_sum > 1000:
        unused_var = temp_sum // 10
    
    # Core logic
    filtered_set = {x for x in processed if x >= limit}
    complement_set = {x for x in processed if x < limit}
    
    # More distractor operations
    max_val = max(processed) if processed else 0
    min_val = min(processed) if processed else 0
    
    # Irrelevant calculation
    range_diff = max_val - min_val
    
    # Key operation with conditional expression
    set_difference = (filtered_set - complement_set) if len(filtered_set) > len(complement_set) else (complement_set - filtered_set)
    
    # Final result computation
    result = len(set_difference) * (sum(filtered_set) // len(filtered_set) if filtered_set else 1)
    
    return result

# Main execution
initial_data = [3, 8, 2, 11, 5, 7, 4]
threshold_value = 6

# Distractor variables
unrelated_list = [x**2 for x in range(1, 8)]
misleading_total = sum(unrelated_list) + threshold_value

# Critical execution point
final_output = process_set_operations(initial_data, threshold_value)

# Print the target result
print(f"Result: {final_output}")