def calculate_quality_score(sensor_readings):
    # Irrelevant temperature conversion - never used
    temp_f = lambda c: (c * 9/5) + 32
    celsius_readings = [25, 30, 35, 40]
    fahrenheit_map = list(map(temp_f, celsius_readings))
    
    # Main processing with misleading intermediate
    base_offset = 12
    raw_sum = sum(sensor_readings)
    avg_reading = raw_sum / len(sensor_readings)
    
    # Distractor calculation that looks important
    variance_sum = sum((x - avg_reading) ** 2 for x in sensor_readings)
    misleading_variance = variance_sum / (len(sensor_readings) - 1)
    
    # Dead code path that seems relevant
    if avg_reading > 50:
        adjustment_factor = 0.8
    else:
        adjustment_factor = 1.2
    
    # More misleading operations
    bit_shift_temp = base_offset << 2
    redundant_xor = bit_shift_temp ^ 15
    
    # Critical path - actual calculation
    quality_adjustment = max(sensor_readings) - min(sensor_readings)
    normalized_range = quality_adjustment / 10
    
    # Final calibration (this is the answer)
    final_calibration = int((avg_reading + normalized_range) * 10)
    
    # Unused lambda that seems important
    normalize_fn = lambda x: (x - min(sensor_readings)) / quality_adjustment
    
    result = final_calibration
    print(f"Target result: {result}")

# Execute with sensor data
sensor_data = [45, 52, 48, 55, 50]
calculate_quality_score(sensor_data)