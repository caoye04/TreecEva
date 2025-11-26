def analyze_data_patterns(data_points):
    # Initialize processing variables
    base_value = data_points[0]
    processed_values = []
    temp_aggregate = 0
    
    # Process each data point with some intermediate calculations
    for point in data_points:
        # Main processing: analyze growth patterns
        growth_factor = point * 2 if point > base_value else point // 2
        processed_values.append(growth_factor)
        
        # Some intermediate calculations (not directly used in final result)
        temp_aggregate += point * 3
        variance_check = point - base_value
    
    # Additional processing with list comprehensions
    filtered_values = [x for x in processed_values if x > 10]
    adjusted_values = [x * 1.5 if x % 2 == 0 else x * 0.8 for x in filtered_values]
    
    # Final result calculation with conditional expression
    final_result = processed_values[-1] if len(processed_values) > 0 else 0
    
    # Print the target variable
    print(f"Result: {final_result}")
    return final_result

# Test data with mixed patterns
test_data = [8, 15, 12, 20, 6, 25, 18]
analyze_data_patterns(test_data)