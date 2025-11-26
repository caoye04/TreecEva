def analyze_sensor_readings(readings):
    filtered_readings = [r for r in readings if r > 50 and r % 2 == 0]
    sensor_sum = sum(filtered_readings)
    
    # Configuration parameters
    calibration_offset = 12
    scaling_factor = 2.5
    
    # Main computation
    base_value = sensor_sum + calibration_offset
    adjusted_value = base_value * scaling_factor
    final_computation = adjusted_value // 10
    
    target_result = final_computation
    print(f"Result: {target_result}")

# Test data
sensor_data = [45, 62, 78, 33, 54, 91, 68, 29]
analyze_sensor_readings(sensor_data)