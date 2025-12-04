def analyze_data_subsets(data_points):
    processed_data = []
    temp_buffer = []
    
    for idx, value in enumerate(data_points):
        processed_value = value * 2 + idx
        processed_data.append(processed_value)
        temp_buffer.append(processed_value // 2)
    
    sorted_results = sorted(processed_data)
    filtered_values = [x for x in sorted_results if x % 3 == 0]
    
    final_values = []
    for val in filtered_values:
        adjusted_val = val - (val % 5)
        final_values.append(adjusted_val)
    
    processed_count = len([x for x in final_values if x > 10])
    aggregate_result = sum(final_values[:3]) // processed_count
    
    print(f"Result: {aggregate_result}")

# Main execution
sample_data = [8, 12, 5, 15, 7, 20, 3]
analyze_data_subsets(sample_data)