def analyze_sensor_readings():
    raw_readings = [105, 23, 78, 91, 60, 45, 110, 50]
    offset = 5
    adjusted_readings = [x - offset for x in raw_readings]
    
    # Apply calibration factor for temperature drift
    calibrated_readings = [int(x * 0.9) for x in adjusted_readings]
    
    # Identify stable readings above noise floor
    noise_floor = 40
    stable_readings = [x for x in calibrated_readings if x >= noise_floor]
    
    # Compute moving average over window of size 2
    smoothed_readings = []
    for i in range(len(stable_readings) - 1):
        avg = (stable_readings[i] + stable_readings[i+1]) // 2
        smoothed_readings.append(avg)
    
    # Remove duplicates while preserving order
    unique_smoothed = list(dict.fromkeys(smoothed_readings))
    
    # Define dynamic threshold based on median
    sorted_vals = sorted(unique_smoothed)
    median_val = sorted_vals[len(sorted_vals) // 2]
    threshold = median_val + 5
    
    # Final processing: sum values above threshold
    processed_data = [x * 2 for x in unique_smoothed]  # Amplify signal
    filtered_sum = sum([x for x in processed_data if x > threshold])
    
    # Irrelevant auxiliary variable (minimal distraction)
    dummy_counter = 0
    for _ in raw_readings:
        dummy_counter += 1
    
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()