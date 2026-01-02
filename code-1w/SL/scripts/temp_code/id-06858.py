def calculate_pressure():
    base_pressure = 101.3
    calibration_offset = 2.7
    temperature_factor = 14.2
    is_active = True
    is_calibrated = (base_pressure + calibration_offset) > 103
    
    # Initial adjustment based on altitude
    altitude_factor = 0.98
    adjusted_base = base_pressure * altitude_factor
    
    # Final pressure calculation with conditional logic
    final_pressure = adjusted_base + (temperature_factor if is_calibrated else 0)
    
    # Irrelevant tracking variable (minor distraction)
    status_log = "Calibration: " + ("OK" if is_calibrated else "FAILED")
    
    print(f"Result: {final_pressure}")

calculate_pressure()