def analyze_sensor_readings(readings):
    base_threshold = 42
    correction_factor = 0.85
    temp_buffer = []
    outlier_count = 0
    rolling_avg_window = []
    filtered_data = []
    
    for i, val in enumerate(readings):
        if i > 0 and abs(val - readings[i-1]) > 15:
            outlier_count += 1
            continue
        
        temp_buffer.append(val * 0.95)
        
        if val % 2 == 0:
            temp_val = val ^ 3
            if temp_val > 20:
                rolling_avg_window.append(temp_val)
    
    if len(rolling_avg_window) > 3:
        avg_temp = sum(rolling_avg_window[:3]) / 3
        adjustment = avg_temp * 0.1
        correction_factor += adjustment / 100
    
    for j, cleaned in enumerate(temp_buffer):
        if j % 3 == 0:
            cleaned = int(cleaned)
            if cleaned > base_threshold - 5:
                filtered_data.append(cleaned)
        else:
            backup_check = cleaned * 2
            validation_flag = (backup_check % 7 == 0)
    
    # Irrelevant list slicing for distraction
    slice_test = filtered_data[::2] if len(filtered_data) > 2 else [0]
    extra_metric = sum(slice_test) / (len(slice_test) or 1)
    
    filtration_score = sum(filtered_data) * correction_factor
    
    # Dead code path - never executed due to prior logic
    if len(temp_buffer) < 5 and False:
        fallback_mode = True
        filtration_score *= 1.2
    
    return filtration_score

sensor_inputs = [86, 87, 74, 73, 92, 68, 69, 88, 41, 43]
result = analyze_sensor_readings(sensor_inputs)
print(f"Result: {result}")