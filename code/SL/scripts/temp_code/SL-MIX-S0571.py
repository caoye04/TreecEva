def analyze_sensor_readings():
    sensor_data = [(1, 12.5), (2, 8.3), (3, 15.7), (4, 9.1), (5, 11.2), (6, 14.8)]
    exclude_set = {2, 4, 7}
    
    # This intermediate calculation is partially relevant but not directly used
    temp_sum = sum([reading for _, reading in sensor_data])
    average_reading = temp_sum / len(sensor_data)
    
    # This filtering step is the core logic
    filtered_data = [(id_val, reading) for id_val, reading in sensor_data if reading > 10.0]
    
    # This intermediate variable seems important but isn't used in final calculation
    high_readings = [reading for _, reading in filtered_data if reading > 14.0]
    
    # Critical statement - excludes certain sensor IDs and creates result dictionary
    result_dict = {k: v for k, v in filtered_data if k not in exclude_set}
    
    # Some additional processing that doesn't affect the final count
    temp_adjustment = [reading * 1.1 for reading in result_dict.values()]
    
    final_count = len(result_dict)
    print(f"Result: {final_count}")

analyze_sensor_readings()