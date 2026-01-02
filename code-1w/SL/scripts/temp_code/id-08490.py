def process_sensor_data():
    raw_readings = [23.4, 19.8, 25.1, 18.2, 24.3, 20.0, 26.7, 17.5, 22.9]
    valid_range = lambda x: 18 <= x <= 26
    
    # Filter out-of-range sensor values
    filtered_readings = [temp for temp in raw_readings if valid_range(temp)]
    
    # Calculate average of valid readings
    total = sum(filtered_readings)
    count = len(filtered_readings)
    average_temp = total / count
    
    # Final processing step
    final_temperature = round(average_temp, 2)
    
    # Irrelevant auxiliary variables (minimal distraction)
    outlier_count = len(raw_readings) - len(filtered_readings)
    status_flag = 'OK' if outlier_count == 0 else 'CALIBRATE'
    
    print(f"Result: {final_temperature}")

process_sensor_data()