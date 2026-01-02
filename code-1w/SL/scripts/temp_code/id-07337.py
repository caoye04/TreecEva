def process_sensor_data(raw_data):
    readings = raw_data.split(',')
    numeric_values = list(map(lambda x: float(x.strip()), readings))
    
    # Normalize values by subtracting baseline
    baseline = 27.5
    normalized = [val - baseline for val in numeric_values]
    
    # Apply filtering to remove noise (simple threshold)
    filtered = [val for val in normalized if abs(val) > 1.0]
    
    # Simulate calibration adjustment using linear transform
    adjustment_factor = 1.8
    adjusted_readings = [val * adjustment_factor for val in filtered]
    
    # Final conversion to target scale
    conversion_factor = 0.95
    offset = 32.0
    final_temperature = adjusted_readings[0] * conversion_factor + offset
    
    # Irrelevant auxiliary calculation (minimal interference)
    average_temp = sum(adjusted_readings) / len(adjusted_readings)
    status_msg = "OK" if average_temp > 0 else "ERROR"
    
    print(f"Result: {final_temperature}")
    return final_temperature

# Input data string from sensor
sensor_input = " 29.0, 27.6, 25.0, 30.2 "
process_sensor_data(sensor_input)