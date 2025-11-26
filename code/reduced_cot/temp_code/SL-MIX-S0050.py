def analyze_sensor_data(readings):
    calibration_factor = 2.5
    noise_threshold = 15
    
    # Distractor: complex computation that doesn't affect final result
    temp_calc = sum([r * 1.1 for r in readings if r > 10])
    temp_offset = temp_calc * 0.8 - 25
    
    # Relevant processing with list comprehension
    filtered_readings = [r * calibration_factor for r in readings if r < noise_threshold]
    
    # Conditional expression with moderate nesting
    processing_result = (sum(filtered_readings) * 1.2 if len(filtered_readings) > 2 
                       else sum(filtered_readings) * 0.8)
    
    # Final computation - this is the key statement
    final_computation = processing_result - temp_offset + temp_offset
    
    print(f"Target result: {final_computation}")
    return final_computation

# Main execution
sensor_data = [8, 12, 5, 18, 3, 25, 9, 14]
result = analyze_sensor_data(sensor_data)