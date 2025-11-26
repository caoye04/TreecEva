def analyze_sensor_data():
    sensor_readings = [45, 78, 32, 91, 67, 54, 83, 29, 76, 61]
    calibration_offset = 15
    
    # Find maximum reading using list comprehension
    max_reading = max([reading for reading in sensor_readings])
    
    # Apply calibration offset to get final measurement
    final_measurement = max_reading - calibration_offset
    
    print(f"Result: {final_measurement}")

analyze_sensor_data()