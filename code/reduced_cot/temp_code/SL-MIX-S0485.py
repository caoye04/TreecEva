def process_data(data_stream):
    temp_buffer = []
    data_analysis = {'valid': 0, 'invalid': 0, 'total': 0}
    
    # Process incoming data points
    for item in data_stream:
        if item % 2 == 0:
            temp_buffer.append(item * 2)
            data_analysis['valid'] += 1
        else:
            data_analysis['invalid'] += 1
        data_analysis['total'] += 1
    
    # Intermediate calculations (distractor)
    mean_value = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    range_check = max(temp_buffer) - min(temp_buffer) if temp_buffer else 0
    
    # Filter relevant data using lambda and slicing
    filter_func = lambda x: x > 10
    filtered_data = list(filter(filter_func, temp_buffer))
    critical_section = filtered_data[1:4] if len(filtered_data) >= 4 else filtered_data
    
    # Core computation
    target_value = sum(critical_section) if critical_section else 0
    adjustment_factor = len([x for x in critical_section if x % 3 == 0])
    
    # Final result (answer)
    final_result = target_value * adjustment_factor
    
    # Distractor operations that don't affect final_result
    verification_sum = sum(temp_buffer[-2:]) if len(temp_buffer) >= 2 else 0
    duplicate_check = len(set(filtered_data))
    
    print(f"Result: {final_result}")

# Execute with test data
data_stream = [3, 8, 5, 12, 7, 14, 9, 6, 11, 10]
process_data(data_stream)