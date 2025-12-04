def process_results(data_points, min_threshold):
    temp_buffer = []
    data_mapping = {}
    
    # Initialize with some irrelevant computations
    offset_calc = (len(data_points) * 3) - 7
    dummy_value = offset_calc % 5
    
    for idx, value in enumerate(data_points):
        if value >= min_threshold:
            processed_val = value * 2 + dummy_value
            temp_buffer.append(processed_val)
            data_mapping[idx] = processed_val
        else:
            # Distractor operation that doesn't affect final result
            shadow_calc = value * 3 - dummy_value
    
    # More intermediate computations that don't contribute to final answer
    intermediate_sum = sum(temp_buffer)
    unused_metric = intermediate_sum // len(temp_buffer) if temp_buffer else 0
    
    # The critical computation chain
    valid_entries = [data_mapping[i] for i in sorted(data_mapping.keys())]
    final_score = sum(valid_entries) - (len(valid_entries) * dummy_value)
    
    print(f"Result: {final_score}")
    return final_score

# Main execution
sample_data = [8, 12, 5, 15, 9, 3]
threshold = 6
result_analysis = process_results(sample_data, threshold)