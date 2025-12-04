import itertools

def calculate_priority(data, threshold=50):
    # Transform data with conditional expressions
    transformed = [x * 2 if x % 2 == 0 else x // 2 for x in data]
    
    # Apply a simple filter using lambda
    is_valid = lambda x: x < threshold and x > 0
    valid_items = filter(is_valid, transformed)
    
    # Prepare some additional values (not needed for final calculation)
    supplementary = list(itertools.repeat(10, 3))
    
    # Calculate priority based on filtered values
    filtered_values = list(valid_items)
    if not filtered_values:
        return 0
        
    # This is our target calculation
    priority_value = sum(filtered_values)
    
    # Additional processing (not affecting the result)
    max_value = max(filtered_values) if filtered_values else 0
    
    print(f"Result: {priority_value}")
    return priority_value

# Sample data
sensor_readings = [75, 12, 30, 42, 8]
calculate_priority(sensor_readings)