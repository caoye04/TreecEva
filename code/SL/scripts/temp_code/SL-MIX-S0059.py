def analyze_sensor_data():
    # Sensor data stream processing with calibration
    data_stream = [45, 82, 67, 93, 28, 74, 51, 88, 36, 95]
    calibration_offset = 5
    filter_base = 9
    threshold_modifier = 3
    
    # Pre-processing step (distractor)
    adjusted_data = [x + calibration_offset for x in data_stream]
    temp_calculation = sum(adjusted_data) // len(data_stream)
    
    # Critical filtering operation
    processed_data = [x for x in data_stream if x % filter_base == 0]
    
    # Secondary processing (semi-relevant)
    filtered_sum = sum(processed_data) if processed_data else 0
    backup_check = len(data_stream) * threshold_modifier
    
    # Final metric calculation
    final_metric = filtered_sum - backup_check
    
    # Unused intermediate variable (interference)
    unused_metric = max(data_stream) - min(data_stream)
    
    print(f"Target result: {final_metric}")
    return final_metric

analyze_sensor_data()