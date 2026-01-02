def evaluate_system_state():
    temperature = 37.5
    pressure_level = 80
    system_uptime_hours = 45
    calibration_offset = 2.5

    # Compute normalized temperature score
    normal_temp = 37.0
    temp_deviation = abs(temperature - normal_temp)
    temperature_score = int((1.0 - min(temp_deviation / 2.0, 1.0)) * 100)

    # System stability check based on heuristic thresholds
    is_stable = (temperature < 39.0) and (pressure_level >= 70)

    # Irrelevant telemetry (distractor variables at LOW interference level)
    last_maintenance_code = 'OK'
    sensor_array_status = [True, True, False]

    # Key computation with conditional expression and boolean logic
    result = temperature_score + (is_stable and (pressure_level > 75))
    
    # Final output
    print(f"Result: {result}")

evaluate_system_state()