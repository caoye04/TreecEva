from collections import Counter

def analyze_sensor_data(sensor_readings):
    # Distractor: unused frequency analysis
    frequency_counter = Counter(sensor_readings)
    common_vals = frequency_counter.most_common(3)
    
    # Misleading intermediate calculations
    total_sum = sum(sensor_readings)
    average_val = total_sum / len(sensor_readings) if sensor_readings else 0
    adjusted_avg = average_val * 2.5 - 15
    
    # Dead code path - never executed
    if adjusted_avg > 1000:
        threshold_bypass = adjusted_avg // 10
    else:
        threshold_bypass = 0
    
    # Relevant bitwise operations for data validation
    validation_mask = 0b10101101
    valid_count = 0
    for reading in sensor_readings:
        masked_value = reading & validation_mask
        if (masked_value | 0b00100000) == 0b10101101:
            valid_count += 1
    
    # More distractions with arithmetic
    noise_reduction = len(sensor_readings) * 3 - 7
    calibration_offset = (noise_reduction ^ 0b1111) + 12
    
    # Key relevant variables
    active_tracker = valid_count * 4
    false_positive = (len(sensor_readings) - valid_count) // 2
    correction_factor = (active_tracker >> 2) | 0b110
    
    # Final calculation (this is what matters)
    final_count = active_tracker + correction_factor - false_positive
    
    # Print irrelevant intermediate values for distraction
    print(f"Debug - Total sum: {total_sum}")
    print(f"Debug - Adjusted avg: {adjusted_avg}")
    print(f"Debug - Calibration offset: {calibration_offset}")
    
    # The actual result we care about
    print(f"Result: {final_count}")
    return final_count

# Test data with mixed patterns
sensor_data = [45, 173, 89, 237, 125, 189, 65, 173, 201]
result = analyze_sensor_data(sensor_data)