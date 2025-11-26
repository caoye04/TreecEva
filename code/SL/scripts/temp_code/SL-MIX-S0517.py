def process_sensor_readings(readings):
    # Filter readings above threshold and square them
    threshold = 8
    filtered_data = [x for x in readings if x > threshold]
    squared_values = [x ** 2 for x in filtered_data]
    
    # Calculate result using list operations
    data_points = [15, 12, 9, 7, 11, 14, 6, 10]
    result_calculation = sum(squared_values) // len(data_points)
    
    # Final computation with minimal interference
    base_value = 25
    adjustment_factor = 3
    final_sum = result_calculation + base_value - adjustment_factor
    
    print(f"Target result: {final_sum}")
    return final_sum

# Execute the function
sensor_data = [5, 10, 8, 12, 7, 15, 9, 11]
process_sensor_readings(sensor_data)