def process_sensor_data():
    raw_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8]
    calibration_factor = 0.98
    temperature_offset = 1.2
    
    # Apply calibration and filter unstable readings
    calibrated = [round(temp * calibration_factor, 2) for temp in raw_readings]
    filtered = [temp for temp in calibrated if temp >= 23.0]
    
    # Sort the readings and apply minor correction to extremes
    filtered.sort()
    if len(filtered) > 2:
        filtered[0] = round(filtered[0] + 0.2, 2)
        filtered[-1] = round(filtered[-1] - 0.3, 2)
    
    # Final adjustment using offset
    adjusted_readings = [round(temp + 0.1, 2) for temp in filtered]
    final_temperature = adjusted_readings[-1] + temperature_offset
    
    # Irrelevant string processing (minor distraction)
    status_msg = "Sensor OK: {} samples processed".format(len(raw_readings))
    status_code = status_msg.split()[0].lower()
    
    # Output result
    print("Result: {}".format(final_temperature))

process_sensor_data()