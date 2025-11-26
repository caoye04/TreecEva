def compute_final_value(data_points):
    # Initial processing with set operations
    unique_values = set(data_points)
    processed_set = {x * 2 if x % 3 == 0 else x // 2 for x in unique_values}
    
    # Misleading intermediate calculations
    temp_sum = sum(data_points) * 2  # Dead code - never used
    alternative_result = len(unique_values) ** 3  # Distractor
    
    # Main logic with nested conditions
    result_list = []
    for value in processed_set:
        if value > 10:
            if value % 2 == 0:
                result_list.append(value + 5)
            else:
                result_list.append(value - 3)
        else:
            # Misleading branch that doesn't affect final result
            dummy_var = value * 10 + 7  # Dead code
            result_list.append(value * 2)
    
    # Final computation with early return check
    if len(result_list) == 0:
        return -1  # Never happens with our data
    
    final_calc = sum(result_list)
    
    # More distractions
    unused_set = processed_set.union({15, 25, 35})
    redundant_multiplier = final_calc * 0 + 1  # Always 1
    
    return final_calc

# Main execution
initial_data = [12, 8, 15, 12, 20, 8, 25]
data_copy = initial_data[:]  # Unnecessary copy

# Distractor operations that don't affect result
manipulated_data = [x + 100 for x in initial_data]  # Dead manipulation
preliminary_sum = sum(manipulated_data)  # Unused

final_result = compute_final_value(initial_data)

# Final output
print(f"Target result: {final_result}")