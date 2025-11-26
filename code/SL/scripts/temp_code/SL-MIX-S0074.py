def analyze_data_sets(data_a, data_b):
    # Initialize tracking variables (some are irrelevant)
    temp_sum = sum(data_a) + sum(data_b)
    max_val = max(data_a + data_b)
    min_val = min(data_a + data_b)
    
    # Irrelevant computations that don't affect final result
    ratio_check = lambda x, y: x / y if y != 0 else 0
    irrelevant_ratio = ratio_check(temp_sum, max_val)
    
    # Misleading intermediate calculations
    avg_diff = (sum(data_a) / len(data_a)) - (sum(data_b) / len(data_b))
    squared_diff = avg_diff ** 2
    
    # Actual relevant computation path
    filtered_a = {x for x in data_a if x % 2 == 0}
    filtered_b = {x for x in data_b if x % 3 == 0}
    
    # Dead code path - never executed
    if len(filtered_a) > 10:
        dead_result = sum(filtered_a) * 2
    
    # Key logic with set operations
    common_elements = filtered_a & filtered_b
    union_elements = filtered_a | filtered_b
    
    # Conditional expression determining final value
    final_metric = (len(common_elements) * 100) if len(common_elements) > 0 else (len(union_elements) * 50)
    
    # More irrelevant computations
    redundant_check = max_val - min_val
    normalized_val = final_metric / (len(data_a) + len(data_b))
    
    return final_metric

# Data preparation with some distractors
primary_data = [4, 8, 12, 16, 20, 24, 28, 32, 36]
secondary_data = [6, 12, 18, 24, 30, 36, 42, 48]

# Additional irrelevant data sets
backup_data = [2, 4, 6, 8, 10]
validation_data = [3, 6, 9, 12, 15]

# Execute main analysis
result = analyze_data_sets(primary_data, secondary_data)

# Final output
print(f"Result: {result}")