def analyze_sensor_data(readings, threshold=50):
    # Process sensor readings and identify active ones
    active_sensors = [i for i, reading in enumerate(readings) if reading > threshold]
    
    # Track which sensors have been calibrated
    calibration_status = [False] * len(readings)
    
    # Calibration simulation - sensors divisible by 3 or 5 are calibrated
    for i in range(len(readings)):
        if i % 3 == 0 or i % 5 == 0:
            calibration_status[i] = True
    
    # Some sensors need recalibration if their readings are too high
    high_readings = [i for i, reading in enumerate(readings) if reading > 85]
    for sensor in high_readings:
        if sensor in active_sensors and sensor % 2 == 0:
            calibration_status[sensor] = False
    
    # Calculate maintenance priority score (not used in final result)
    maintenance_priority = sum(1 for i in range(len(readings)) 
                              if readings[i] < 30 and calibration_status[i])
    
    # Convert calibration status to sensor indices
    calibrated_sensors = [i for i, status in enumerate(calibration_status) if status]
    
    # Find sensors that are both active and calibrated
    common_elements_count = len(set(active_sensors).intersection(calibrated_sensors))
    
    # Calculate a different metric (distractor)
    uncalibrated_active = len([s for s in active_sensors if s not in calibrated_sensors])
    
    # Compute ratio of calibrated to total (not used in final result)
    calibration_ratio = len(calibrated_sensors) / len(readings) if readings else 0
    
    print(f"Result: {common_elements_count}")
    return common_elements_count

# Sensor readings for a system with 10 sensors
sensor_readings = [45, 67, 23, 89, 72, 55, 91, 31, 18, 76]

# Run the analysis
result = analyze_sensor_data(sensor_readings)