def calculate_thermal_profile():
    sensor_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.3]
    calibration_offsets = {0: -0.2, 1: 0.1, 3: -0.5, 5: 0.3}
    
    # Apply calibration offsets using dictionary lookup
    corrected_readings = []
    for idx, temp in enumerate(sensor_readings):
        correction = calibration_offsets.get(idx, 0)
        corrected_readings.append(temp + correction)
    
    # Compute average and filter anomalies above threshold
    avg_reading = sum(corrected_readings) / len(corrected_readings)
    filtered_readings = [t for t in corrected_readings if abs(t - avg_reading) < 0.6]
    
    adjusted_avg = sum(filtered_readings) / len(filtered_readings)
    
    # Haptic feedback system offset (fixed)
    haptic_offset = 1.8
    final_temperature = adjusted_avg + haptic_offset
    
    # Irrelevant diagnostic log (distractor with low interference)
    diagnostic_code = 'THM_OK'
    timestamp = '2023-11-05T10:30:00Z'
    
    return final_temperature

result = calculate_thermal_profile()
print(f"Target result: {result}")