from itertools import accumulate

def process_data_stream():
    sensor_readings = [12, 8, 15, 3, 20, 6, 18, 9]
    threshold = 10
    
    # Filter readings above threshold (distractor - not used in final result)
    high_readings = [x for x in sensor_readings if x > threshold]
    
    # Process calibration offset (irrelevant calculation)
    calibration_factor = sum(sensor_readings) // len(sensor_readings)
    
    # Transform data with scaling and offset
    transformed = [x * 2 + 5 for x in sensor_readings]
    
    # Remove outliers (semi-relevant but not critical)
    filtered_data = [x for x in transformed if x % 3 != 0]
    
    # Critical execution point
    result_sequence = list(accumulate(filtered_data))
    
    # Compute final result
    final_result = result_sequence[-1] - result_sequence[1]
    
    # Additional unused computation (distraction)
    average_temp = sum(transformed) / len(transformed)
    
    print(f"Result: {final_result}")
    return final_result

if __name__ == "__main__":
    process_data_stream()