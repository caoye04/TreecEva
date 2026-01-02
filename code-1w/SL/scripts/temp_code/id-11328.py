def main():
    # Initial sensor readings in degrees Celsius
    raw_readings = {'sensor_a': 23.5, 'sensor_b': 24.1, 'sensor_c': None, 'sensor_d': 22.8}
    
    # Environmental correction factors
    corrections = {'humidity': 0.9, 'pressure': 1.1}
    
    # Baseline calibration offset
    calibration_offset = -1.2
    
    # Count valid sensors (ignore None)
    valid_count = sum(1 for v in raw_readings.values() if v is not None)
    
    # Compute average from valid sensors
    total = sum(v for v in raw_readings.values() if v is not None)
    avg_temperature = total / valid_count
    
    # Apply environmental corrections
    corrected_temp = avg_temperature * corrections['humidity'] * corrections['pressure']
    
    # Final calibrated temperature
    final_temperature = corrected_temp + calibration_offset
    
    # Irrelevant auxiliary variable (minor distraction)
    status_flag = 'NORMAL' if final_temperature > 20 else 'LOW'
    
    print(f"Result: {final_temperature}")

main()