def analyze_sensor_data():
    raw_readings = [15, 23, 7, 45, 19, 31, 11]
    offset = 2
    
    # Extract relevant window of sensor data
    window = raw_readings[1:5]  # indices 1 to 4
    
    # Simulate calibration adjustment
    calibrated = [x - 3 for x in window]
    
    # Compute derived metrics
    magnitude = sum(calibrated) // len(calibrated)
    peak_index = len(calibrated) - 1
    
    # Irrelevant auxiliary variable (distractor)
    temp_buffer = [calibrated[i] for i in range(0, len(calibrated), 2)]
    
    # Processed features
    processed_data = [magnitude, calibrated[0], calibrated[peak_index]]
    
    # Bitwise shift based on control signal
    control_signal = 0b101
    shift_amount = control_signal & 0b11
    final_shift = 8 >> shift_amount  # Right shift 8 by 1
    
    result = processed_data[1] + final_shift
    print(f"Result: {result}")

analyze_sensor_data()