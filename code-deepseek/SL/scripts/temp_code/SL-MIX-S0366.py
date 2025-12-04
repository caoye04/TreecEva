def analyze_sensor_readings(readings):
    temp_sum = 0
    valid_readings = []
    # Intermediate calculation that doesn't affect final result
    max_temp = max(readings) if readings else 0
    
    for idx, temp in enumerate(readings):
        if temp >= 20 and temp <= 80:
            valid_readings.append(temp)
            temp_sum += temp
    
    # Distractor operation that seems relevant but isn't used
    avg_temp = temp_sum / len(valid_readings) if valid_readings else 0
    
    paired_readings = list(zip(valid_readings, valid_readings[1:]))
    valid_pairs = 0
    
    for pair in paired_readings:
        temp_diff = abs(pair[1] - pair[0])
        # This condition check is the key logic
        valid_pairs += 1 if temp_diff <= 15 else 0
    
    # Intermediate variable for distraction
    total_possible = len(paired_readings)
    
    # Unused calculation that looks important
    efficiency_rate = (valid_pairs / total_possible * 100) if total_possible > 0 else 0
    
    correction_factor = 3 if len(valid_readings) > 5 else 1
    final_count = valid_pairs * 2 + correction_factor
    
    print(f"Result: {final_count}")
    return final_count

# Test data
sensor_data = [25, 42, 38, 60, 55, 72, 68, 85, 90]
result = analyze_sensor_readings(sensor_data)
