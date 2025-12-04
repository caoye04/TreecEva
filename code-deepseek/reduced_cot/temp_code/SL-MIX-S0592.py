def compute_final_value(data_values, cutoff):
    # Distractor: unrelated computation that looks relevant
    temp_calc = sum([x * 2 for x in range(10) if x % 2 == 0])
    irrelevant_sum = temp_calc + 25  # Dead code path - never used
    
    # Main logic with conditional expressions
    filtered = [x for x in data_values if x > cutoff]
    processed = [x * 2 if x % 3 == 0 else x - 1 for x in filtered]
    
    # Misleading intermediate result
    dummy_total = sum(processed) + temp_calc  # Red herring
    
    # Actual calculation path
    if len(processed) > 0:
        result = max(processed) - min(processed)
    else:
        result = temp_calc  # This branch is never taken but adds complexity
    
    # More distractions
    unused_var = [result * i for i in range(5)]
    decoy_result = sum(unused_var) / len(unused_var) if unused_var else 0
    
    return result

# Main execution with mixed operations
data_sequence = [8, 15, 3, 22, 9, 17, 6, 11]
threshold_value = 7

# Irrelevant preprocessing
shifted_data = [x << 1 for x in data_sequence]  # Bit shift distraction
redundant_max = max(shifted_data)  # Dead computation

# The actual call that matters
final_output = compute_final_value(data_sequence, threshold_value)

# Final output
print(f"Target result: {final_output}")