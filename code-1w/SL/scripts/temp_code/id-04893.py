def compute_diagnostic_checksum():
    sensor_data = [23, 16, 89, 44, 73, 58, 11]
    calibration_factors = [3, 7, 2, 5, 8, 4, 6]
    
    # Irrelevant pre-processing (distractor)
    normalized = []
    for val in sensor_data:
        temp_normalized = (val - min(sensor_data)) / (max(sensor_data) - min(sensor_data))
        normalized.append(round(temp_normalized, 3))
    
    # Misleading intermediate calculation (dead computation)
    avg_normalized = sum(normalized) / len(normalized)
    deviation_score = sum(abs(n - avg_normalized) for n in normalized)

    # Actual relevant logic starts here
    base_offset = 13
    checksum = 0
    temp_buffer = []
    
    for idx, (raw_val, calib) in enumerate(zip(sensor_data, calibration_factors)):
        adjusted = raw_val * calib + base_offset
        
        # Bit manipulation chain
        shifted = adjusted >> 2
        inverted = ~shifted & 0xFF  # Emulate 8-bit inversion
        processed_value = (inverted + idx) % 256
        
        # Key update step — target execution point
        checksum = (checksum << 1) ^ processed_value
        
        # Buffer storage (semi-relevant, not used later but plausible)
        temp_buffer.append((idx, adjusted, processed_value))
        
        # Extra conditional with no effect on checksum (distractor)
        if checksum > 1000:
            base_offset -= 1  # Never reached due to bit bounds
    
    # More irrelevant post-processing
    final_stats = {
        'count': len(temp_buffer),
        'sum_temp': sum(t[1] for t in temp_buffer),
        'peak_process': max(t[2] for t in temp_buffer)
    }
    
    # Output required result
    print(f"Result: {checksum}")

compute_diagnostic_checksum()