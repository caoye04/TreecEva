def analyze_sensor_data():
    base_readings = [12, 15, 8, 23, 17, 9, 20]
    min_reading = 10
    system_active = True
    correction_factor = 1.25
    
    # Filter readings above minimum threshold
    filtered_readings = [x for x in base_readings if x > min_reading]
    
    # Auxiliary variable for diagnostics (irrelevant to main result)
    diagnostic_code = 200
    
    # Determine energy threshold based on system status and corrected sum
    energy_threshold = sum(filtered_readings) * correction_factor if system_active else 0
    
    # Log final state (irrelevant to computation)
    status_msg = "System operational" if system_active else "Standby mode"
    
    print(f"Result: {energy_threshold}")

analyze_sensor_data()