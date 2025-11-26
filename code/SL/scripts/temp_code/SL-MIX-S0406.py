def analyze_data_points():
    data_stream = [4, 7, 2, 9, 5, 8, 3, 6]
    threshold_map = {4: 2, 7: 1, 2: 4, 9: 0, 5: 3, 8: 1, 3: 2, 6: 1}
    
    # Main processing logic
    processed_values = []
    temp_buffer = 0
    
    for value in data_stream:
        modifier = threshold_map.get(value, 0)
        adjusted = value * modifier
        processed_values.append(adjusted)
        
        # Distractor operation - doesn't affect final result
        temp_buffer += value % 3
    
    # Filter and calculate final tally
    valid_entries = [x for x in processed_values if x > 5]
    
    # More distractor operations
    dummy_sum = sum(data_stream) + temp_buffer
    
    if len(valid_entries) > 0:
        final_tally = sum(valid_entries) // len(valid_entries)
    else:
        final_tally = -1
    
    print(f"Result: {final_tally}")
    return final_tally

final_tally = analyze_data_points()