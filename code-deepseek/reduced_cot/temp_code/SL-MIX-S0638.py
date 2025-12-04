def analyze_data_points(data_points):
    # Initialize base values
    base_total = sum(data_points)
    data_count = len(data_points)
    
    # Calculate some intermediate metrics (distractor operations)
    average_point = base_total / data_count if data_count > 0 else 0
    squared_points = [x**2 for x in data_points]
    sum_squares = sum(squared_points)
    
    # Process data using enumerate and set operations
    processed_data = []
    for idx, value in enumerate(data_points):
        if value % 2 == 0:
            processed_data.append(value * 2)
        else:
            processed_data.append(value + 3)
    
    # More intermediate calculations (distractor)
    unique_values = set(processed_data)
    unique_count = len(unique_values)
    
    # Key computation using lambda functions
    transform_func = lambda x: x - 5 if x > 10 else x + 2
    transformed_data = list(map(transform_func, processed_data))
    
    # Final calculations
    processed_total = sum(transformed_data)
    adjustment_factor = len([x for x in transformed_data if x < 8])
    
    # Additional distractor operation
    unused_metric = average_point * unique_count
    
    final_value = processed_total + adjustment_factor
    print(f"Result: {final_value}")

# Test data
sample_data = [4, 7, 12, 9, 6, 15]
analyze_data_points(sample_data)