def calculate_fluid_flow():
    raw_measurements = [125, 80, 210, 155, 95, 180, 110, 245, 75, 200]
    filtered_data = []
    calibration_offset = 15
    temp_buffer = []
    
    for i in range(len(raw_measurements)):
        calibrated_value = raw_measurements[i] + calibration_offset
        filtered_data.append(calibrated_value)
        
        # Distractor operation - doesn't affect final result
        if i % 2 == 0:
            temp_buffer.append(calibrated_value * 2)
        else:
            temp_buffer.append(calibrated_value // 2)
    
    window_size = 3
    processed_data = []
    running_sum = 0
    
    for i in range(len(filtered_data)):
        running_sum += filtered_data[i]
        
        # Redundant calculation that's never used
        redundant_calc = running_sum * len(temp_buffer)
        
        if i >= window_size - 1:
            window_avg = sum(filtered_data[i-window_size+1:i+1]) // window_size
            processed_data.append(window_avg)
    
    final_volume = processed_data[-1]
    print(f"Result: {final_volume}")

calculate_fluid_flow()