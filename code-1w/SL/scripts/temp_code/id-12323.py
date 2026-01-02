def process_sensor_data(readings):
    baseline = 20.0
    threshold = 25.0
    correction_factor = 1.05
    use_correction = False
    
    # Normalize readings by subtracting baseline
    normalized_readings = [temp - baseline for temp in readings]
    
    # Apply conditional scaling if any reading exceeds threshold
    if any(temp > threshold for temp in readings):
        adjusted_readings = [round(temp * 1.1, 2) for temp in normalized_readings]
        use_correction = True
    else:
        adjusted_readings = [round(temp, 2) for temp in normalized_readings]
    
    # Minor irrelevant operation (distractor)
    status_flag = 'OK' if all(temp >= 0 for temp in adjusted_readings) else 'ERROR'
    
    final_temperature = adjusted_readings[-1] * correction_factor if use_correction else adjusted_readings[-1]
    
    # Print result as required
    print(f"Result: {final_temperature}")

# Input data
sensor_inputs = [22.5, 24.0, 26.8, 23.1]
process_sensor_data(sensor_inputs)