def calculate_pressure():
    initial_reading = 897.5
    offset = 12.3
    calibration_factor = 0.98
    
    # Apply offset and scale for sensor calibration
    corrected_reading = (initial_reading - offset) * calibration_factor
    
    # Simulate volume adjustment using string-based condition check
    status_flag = "NORMAL"
    if status_flag.lower().startswith("normal"):
        adjusted_volume = corrected_reading * 1.05
    else:
        adjusted_volume = corrected_reading * 0.95
    
    # Temperature compensation factor based on comparison logic
    base_temp = 25
    current_temp = 27
    temp_diff = abs(current_temp - base_temp)
    temperature_factor = 1 + (temp_diff * 0.02) if temp_diff > 1 else 1.0
    
    # Final pressure calculation
    final_pressure = adjusted_volume / temperature_factor
    
    # Irrelevant tracking variable (minor distraction)
    measurement_count = 1
    
    print(f"Result: {final_pressure}")
    
    return final_pressure

result = calculate_pressure()