def apply_thermal_correction(readings, calibration):
    # Irrelevant temperature conversions (dead code path)
    celsius_to_fahrenheit = lambda c: c * 9/5 + 32
    fahrenheit_to_kelvin = lambda f: (f + 459.67) * 5/9
    
    # Main processing logic
    valid_readings = {x for x in readings if x > -50 and x < 150}
    calibration_delta = calibration.difference({-5, 0, 5, 10})
    
    # Misleading intermediate calculation
    apparent_temp = sum(readings) / len(readings) if readings else 0
    thermal_drift = apparent_temp * 0.1  # Never used
    
    # Actual correction calculation
    if len(valid_readings) >= 3:
        base_temp = min(valid_readings) + max(valid_readings)
        correction_factor = len(calibration_delta) * 2.5
        corrected_temp = base_temp - correction_factor
        
        # Distractor condition that doesn't affect result
        if len(readings) > 10:
            redundant_check = sum(calibration) / len(calibration)
            
        return round(corrected_temp, 2)
    else:
        return apparent_temp - 15  # Dead code path

# Main execution
thermal_readings = [22.5, 23.1, 21.8, 24.2, 22.9, -100, 200]
calibration_set = {0, 2, 4, 6, 8}

# Irrelevant calculations
ambient_offset = 3.7
sensor_bias = 1.2
environment_factor = ambient_offset * sensor_bias  # Never used

# Key statement
temperature = apply_thermal_correction(thermal_readings, calibration_set)

# Final processing with distractions
stability_check = [temperature + i for i in range(3)]
calibration_error = max(calibration_set) - min(calibration_set)
final_temperature = temperature + (calibration_error / 10)

print(f"Result: {final_temperature}")