def calculate_processing_metrics(data_points):
    filtered_data = [x * 2 for x in data_points if x > 3]
    temp_calculation = sum([i * j for i, j in enumerate(filtered_data) if i % 2 == 0])
    intermediate_sum = temp_calculation + len(data_points)
    
    # Distractor calculations (not used in final result)
    unused_metric = max(data_points) - min(data_points) if data_points else 0
    secondary_check = intermediate_sum * 0.5
    
    processed_values = []
    for idx, val in enumerate(filtered_data):
        adjusted_val = val + idx if val > 10 else val - idx
        processed_values.append(adjusted_val)
    
    # More distraction operations
    verification_sum = sum(processed_values) + unused_metric
    final_result = processed_values[-1]
    
    print(f"Result: {final_result}")
    return final_result

# Main execution
input_data = [2, 5, 8, 3, 7, 4, 6]
result = calculate_processing_metrics(input_data)