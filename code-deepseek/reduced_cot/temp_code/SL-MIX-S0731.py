def analyze_sensor_readings(readings):
    # Process sensor data and calculate quality metrics
    processed_readings = [r * 1.5 for r in readings if r > 0]
    temp_sum = sum(processed_readings)
    
    # Calculate various quality metrics (some unused)
    quality_metrics = []
    for idx, value in enumerate(processed_readings):
        if idx % 2 == 0:
            metric = value * 2.5 - 10
        else:
            metric = value * 1.8 + 5
        quality_metrics.append(round(metric, 2))
    
    # Find maximum quality reading (distractor calculation)
    max_reading = max(processed_readings)
    min_reading = min(processed_readings)  # Unused variable
    
    # Calculate processing index based on multiple conditions
    reading_pairs = list(zip(readings, processed_readings))
    valid_pairs = [(orig, proc) for orig, proc in reading_pairs if proc > 15]
    
    if len(valid_pairs) > 0:
        processed_idx = len(valid_pairs) - 1
        adjustment_factor = 3.2  # Unused adjustment
    else:
        processed_idx = 0
    
    # The key variable assignment
    final_quality_score = quality_metrics[processed_idx]
    
    # Some additional unused calculations
    average_reading = temp_sum / len(processed_readings) if processed_readings else 0
    
    print(f"Result: {final_quality_score}")
    return final_quality_score

# Main execution with sensor data
sensor_data = [8, 12, 6, 15, 9, 11, 7]
analyze_sensor_readings(sensor_data)