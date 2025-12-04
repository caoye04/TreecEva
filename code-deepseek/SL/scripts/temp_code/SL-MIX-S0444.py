def calculate_data_metrics(raw_readings):
    import itertools
    
    # Distractor variables and computations
    sensor_calibration = 3.14159
    redundant_factor = 42
    unused_buffer = [i * 2 for i in range(10)]
    misleading_sum = sum(range(1, 100))  # This won't be used
    
    # Actual processing logic
    filtered_readings = list(itertools.islice(raw_readings, 2, len(raw_readings) - 1))
    processed_data = [reading * 2 - 1 for reading in filtered_readings]
    
    # More distractions
    temp_calculation = sensor_calibration * redundant_factor
    dummy_metric = (temp_calculation + misleading_sum) / 1000  # Dead code path
    
    # Core computation
    processed_total = sum(processed_data)
    adjustment_factor = len(filtered_readings) / 4.0
    correction_offset = (processed_data[0] if processed_data else 0) + 15
    
    # Dead conditional path
    if temp_calculation > 1000:
        irrelevant_bonus = 25
    else:
        irrelevant_bonus = -10
    
    # Final computation - THIS IS THE KEY STATEMENT
    final_metric = processed_total * adjustment_factor - correction_offset
    
    # Print result for verification
    print(f"Result: {final_metric}")
    return final_metric

# Main execution with sample data
sensor_data = [8, 12, 5, 18, 7, 3, 15, 9, 11, 6]
result = calculate_data_metrics(sensor_data)
