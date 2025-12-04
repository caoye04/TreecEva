def encrypt_sensor_data(readings, offset=3):
    # Process sensor readings with filtering and encryption
    # First, filter out readings that might be anomalies
    valid_readings = [r for r in readings if 10 <= r <= 100]
    
    # Calculate average of valid readings (unused in final result)
    avg_reading = sum(valid_readings) / len(valid_readings) if valid_readings else 0
    
    # Apply initial transformation
    transformed = [(r + offset) * 2 for r in valid_readings]
    
    # Select specific readings based on position
    selected_readings = transformed[1::2]  # Every second reading starting from index 1
    
    # Apply second transformation - only odd indices matter
    processed_data = sum(selected_readings) if selected_readings else 0
    
    # Calculate a verification code (unused in final calculation)
    verification = (processed_data % 17) * 3
    
    # Apply bitwise operations for additional security
    result = (processed_data << 4) | (len(valid_readings) & 0xF)
    
    # Final encryption step
    encrypted_value = (result >> 2) ^ 42
    
    print(f"Sensor data processed. Verification: {verification}")
    print(f"Result: {encrypted_value}")
    return encrypted_value

# Test with sample sensor data
sensor_data = [15, 27, 8, 42, 53, 19, 105, 33, 61]
encrypt_sensor_data(sensor_data)