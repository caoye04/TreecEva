def process_sensor_data():
    data_flags = 0b11010110
    processed_mask = 0b00111001
    calibration_offset = 12
    
    # Main computation
    result = (data_flags & 0x0F) ^ (processed_mask | 0x03)
    
    # Final output calculation
    final_output = result + calibration_offset
    
    print(f"Result: {final_output}")
    return final_output

final_output = process_sensor_data()