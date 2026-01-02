def process_data_stream():
    # Simulate sensor data with noise and calibration
    raw_readings = [14, 17, 23, 34, 45, 52, 61, 73]
    calibration_offsets = [3, -1, 0, 2, -2, 1, 0, -3]
    
    # Irrelevant backup buffer (distractor)
    backup_buffer = [0] * len(raw_readings)
    for i in range(len(raw_readings)):
        backup_buffer[i] = raw_readings[i] * 2  # Unused computation
    
    # Apply calibration (relevant)
    calibrated_readings = []
    for val, offset in zip(raw_readings, calibration_offsets):
        calibrated_readings.append(val + offset)
    
    # Noise filtering using moving average (partially relevant but diverted)
    filtered = []
    window_size = 3
    for i in range(len(calibrated_readings)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window_avg = sum(calibrated_readings[start:end]) / (end - start)
        filtered.append(round(window_avg))  # Computed but not fully used
    
    # Bitmask analysis on original data (red herring)
    bit_analysis = 0
    for reading in raw_readings:
        bit_analysis ^= (reading & 0xF)  # Truncate to lower 4 bits
    temp_debug = bin(bit_analysis)  # Dead code path
    
    # Extract every second reading above threshold (slicing + condition)
    high_freq_samples = [x for x in calibrated_readings[1::2] if x > 30]
    
    # Accumulate weighted contributions (key logic chain)
    weights = [0.5, 1.0, 1.5, 2.0]
    weighted_sum = 0.0
    for i, sample in enumerate(high_freq_samples):
        if i >= len(weights):
            break
        weighted_sum += sample * weights[i]
    
    # Secondary accumulator with offset tracking (distractor)
    dummy_accumulator = 0
    for j, w in enumerate(weights):
        dummy_accumulator += (j + 1) * w  # No impact on final result
    
    # Conditional adjustment based on list length parity (relevant)
    adjustment = 0
    if len(calibrated_readings) % 2 == 0:
        adjustment = 5
    else:
        adjustment = -5
    
    # Key aggregation step
    aggregate_result = int(weighted_sum) + adjustment
    
    # Correction factor derived from unused intermediate
    correction_factor = len(filtered) - len(raw_readings) + 8  # Neutralized base
    
    # Final output assignment (target execution point)
    final_output = aggregate_result + correction_factor
    
    # Print required for traceability
    print(f"Result: {final_output}")

    return final_output

# Execute function
process_data_stream()