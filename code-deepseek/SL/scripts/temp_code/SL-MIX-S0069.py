def analyze_sensor_data(sensor_readings):
    # Process sensor data with filtering and compression
    valid_readings = [reading for reading in sensor_readings if reading > 10]
    
    # Calculate average of valid readings
    reading_sum = sum(valid_readings)
    count_valid = len(valid_readings)
    raw_average = reading_sum / count_valid if count_valid > 0 else 0
    
    # Distractor: calculate median (not used in final result)
    sorted_readings = sorted(valid_readings)
    mid = len(sorted_readings) // 2
    median_value = (sorted_readings[mid] + sorted_readings[~mid]) / 2 if sorted_readings else 0
    
    # Apply filtering threshold
    threshold = 25
    filtered_readings = [reading for reading in valid_readings if reading > threshold]
    
    # Calculate filtered average
    filtered_sum = sum(filtered_readings)
    filtered_count = len(filtered_readings)
    filtered_avg = filtered_sum / filtered_count if filtered_count > 0 else 0
    
    # Compression ratio calculation
    total_readings = len(sensor_readings)
    compressed_ratio = filtered_count / total_readings if total_readings > 0 else 0
    
    # Final result calculation
    compression_ratio = 1.5 if compressed_ratio > 0.3 else 2.0
    final_result = filtered_avg * compression_ratio
    
    # Distractor: unused optimization factor
    optimization_factor = (raw_average + median_value) / 2
    
    print(f"Result: {final_result}")
    return final_result

# Sensor data simulation
sensor_data = [8, 15, 22, 45, 18, 60, 12, 33, 28, 9, 51, 24]
analyze_sensor_data(sensor_data)