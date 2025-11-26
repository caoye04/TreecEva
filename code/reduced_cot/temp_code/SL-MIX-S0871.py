def process_data(stream):
    # Process sensor readings with filtering and transformation
    temp_calc = lambda x: (x * 9/5) + 32  # Temperature conversion (distractor)
    
    readings = [25, 18, -5, 12, 30, 7, -2]
    threshold = 15
    filtered_readings = []
    
    # Filter readings above threshold
    for reading in readings:
        if reading > threshold:
            filtered_readings.append(reading)
        temp_val = temp_calc(reading)  # Unused temperature calculation
    
    # Calculate average of filtered values
    if filtered_readings:
        avg_reading = sum(filtered_readings) / len(filtered_readings)
    else:
        avg_reading = 0
    
    # Apply scaling factor with lambda
    scale_factor = lambda x: x * 2.5
    scaled_result = scale_factor(avg_reading)
    
    # Final adjustment (unused intermediate step)
    adjustment = scaled_result - 10
    
    final_result = round(scaled_result, 2)
    print(f"Target result: {final_result}")
    return final_result

# Main execution
data_stream = [25, 18, -5, 12, 30, 7, -2]
final_result = process_data(data_stream)