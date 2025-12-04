def process_sensor_data(initial_readings):
    # Initial sensor processing with irrelevant calculations
    temperature_variance = sum([r * 2 for r in initial_readings]) - 15  # Distractor
    pressure_offset = (initial_readings[0] << 2) & 0xFF  # Unused
    
    # Core sensor correction calculation
    valid_readings = [r for i, r in enumerate(initial_readings) if i % 2 == 0]
    sensor_correction = sum([x * y for x, y in zip(valid_readings, valid_readings[1:] + [valid_readings[0]])])
    
    # Bitwise adjustments with misleading intermediate values
    bitwise_adjustment = (sensor_correction & 0b1010) | (sensor_correction & 0b0101)
    temp_adjust = bitwise_adjustment ^ 0b1111  # Dead code path
    
    # Parity and checksum calculations
    parity_check = 0
    for reading in initial_readings:
        parity_check ^= (reading % 8)
    
    checksum_dummy = parity_check << 1  # Irrelevant calculation
    
    # Final calibration combining relevant components
    final_calibration = sensor_correction + (bitwise_adjustment ^ parity_check)
    
    # Print result for verification
    print(f"Result: {final_calibration}")
    return final_calibration

# Test execution with specific sensor readings
sensor_data = [12, 8, 5, 17, 9, 3]
result = process_sensor_data(sensor_data)