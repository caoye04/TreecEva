def data_processor(dataset, criteria):
    # Distractor variables and computations
    temp_buffer = [x * 2 for x in range(10)]
    redundant_calc = sum(temp_buffer[:5]) - min(temp_buffer[3:7])
    
    # Misleading intermediate processing
    processed_set = {x % 7 for x in dataset}
    filtered_data = [x for x in dataset if criteria(x)]
    
    # Irrelevant string operations
    text_data = ['alpha', 'beta', 'gamma', 'delta']
    char_counts = [len(s) for s in text_data]
    max_chars = max(char_counts)
    
    # Dead code path
    if max_chars > 10:
        unused_var = sum(char_counts) * 2
    else:
        unused_var = len(text_data) ** 3
    
    # Actual relevant computation
    valid_entries = [x for x in filtered_data if x in processed_set]
    sorted_metrics = sorted(valid_entries, reverse=True)
    
    # Key slicing operation with conditional expression
    core_values = sorted_metrics[:3] if len(sorted_metrics) >= 3 else sorted_metrics
    result = sum(core_values) * len(processed_set)
    
    return result

# Main execution
metrics_data = [15, 8, 22, 5, 17, 9, 31, 12, 6, 19]
validation_criteria = lambda x: x > 10 and x % 2 != 0

# Misleading intermediate assignments
preliminary_score = sum(metrics_data[::2]) - min(metrics_data)
secondary_metric = (max(metrics_data) + min(metrics_data)) // 2

# The key execution point
final_metric = data_processor(metrics_data, validation_criteria)

# Final output
print(f"Result: {final_metric}")