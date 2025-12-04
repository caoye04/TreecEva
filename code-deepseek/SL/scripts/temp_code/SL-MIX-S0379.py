def analyze_sensor_data():
    # Simulating sensor readings over time
    raw_readings = [12, 8, 15, 23, 7, 19, 4, 27, 11, 16]
    
    # Calculate threshold based on average (distractor - not used in final result)
    average_reading = sum(raw_readings) / len(raw_readings)
    threshold = average_reading * 1.2
    
    # Filter readings above median
    sorted_readings = sorted(raw_readings)
    median_index = len(sorted_readings) // 2
    median_value = sorted_readings[median_index]
    
    # Create dictionary to track processed values
    sensor_dict = {f'sensor_{i}': val for i, val in enumerate(raw_readings)}
    
    # Filter values above median (relevant operation)
    filtered_values = [val for val in raw_readings if val > median_value]
    
    # Calculate unused statistics (distractor)
    max_reading = max(raw_readings)
    min_reading = min(raw_readings)
    range_reading = max_reading - min_reading
    
    # Key processing step
    processed_data = [item * 2 - 1 for item in filtered_values]
    
    # Final calculation
    final_result = sum(processed_data) // len(processed_data)
    
    print(f"Target result: {final_result}")
    return final_result

analyze_sensor_data()