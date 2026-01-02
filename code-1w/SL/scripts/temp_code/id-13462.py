def analyze_system_performance(temperature, pressure, humidity):
    base_rating = 78
    calibration_offset = 12
    system_active = temperature < 90 and pressure in range(80, 120)
    
    # Environmental adjustments
    adjustment_factor = 1.0
    if humidity > 60:
        adjustment_factor = 0.85
    elif humidity < 30:
        adjustment_factor = 0.93

    # Simulated sensor noise (irrelevant to final result)
    sensor_noise = (temperature * 0.02) % 1.0
    debug_checksum = int((temperature + pressure + humidity) * sensor_noise)
    
    # Efficiency computation with conditional expression
    efficiency_factor = adjustment_factor * (1.1 if temperature > 75 else 1.0) * (0.95 if pressure < 90 else 1.0)
    
    # Distractor variables: power_state and load_profile
    power_state = "optimal" if system_active and efficiency_factor > 0.9 else "degraded"
    load_profile = [base_rating * i for i in range(1, 4) if i % 2 == 1]  # Unused list
    
    # Key execution point
    thermal_capacity = base_rating * efficiency_factor if system_active else 0
    
    # Additional red herring computation
    safety_margin = thermal_capacity * 0.1 if debug_checksum % 2 == 0 else 0
    status_code = 200 if thermal_capacity > 50 else 404
    
    # Final output
    print(f"Result: {thermal_capacity}")

# Fixed input conditions
temp_input = 85
pressure_input = 95
humidity_input = 45

analyze_system_performance(temp_input, pressure_input, humidity_input)