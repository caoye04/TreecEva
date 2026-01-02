def process_sensor_data():
    raw_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
    offset = 0.5
    corrected_readings = [temp + offset for temp in raw_readings]
    
    # Filter out readings below average
    avg_temp = sum(corrected_readings) / len(corrected_readings)
    filtered_readings = [temp for temp in corrected_readings if temp >= avg_temp]
    
    # Apply smoothing using neighboring values (simple moving average)
    smoothed_readings = []
    for i in range(len(filtered_readings)):
        if i == 0 or i == len(filtered_readings) - 1:
            smoothed_readings.append(filtered_readings[i])
        else:
            avg_window = (filtered_readings[i-1] + filtered_readings[i] + filtered_readings[i+1]) / 3
            smoothed_readings.append(round(avg_window, 2))
    
    # Final adjustment based on calibration
    adjustment_map = {'low': 0.95, 'base': 1.0, 'high': 1.05}
    correction_factor = adjustment_map['base']
    adjusted_readings = [round(temp * correction_factor, 2) for temp in smoothed_readings]
    
    # Irrelevant diagnostic variable (minimal interference)
    diagnostic_flag = len(smoothed_readings) > 3
    
    final_temperature = adjusted_readings[-1] * correction_factor
    print(f"Result: {final_temperature}")

process_sensor_data()