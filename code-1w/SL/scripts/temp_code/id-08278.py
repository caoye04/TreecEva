def compute_diagnostic_signal():
    # Simulate sensor readings with embedded pattern analysis
    raw_readings = [23, 16, 45, 28, 34, 19, 41]
    baseline = 17
    adjustment_factor = 2.5
    temp_buffer = []
    cumulative_shift = 0
    checksum = 13
    
    for reading in raw_readings:
        # Normalize reading
        normalized = reading - baseline
        
        # Irrelevant transformation (distractor)
        scaled_normalized = int(normalized * adjustment_factor)
        temp_buffer.append(scaled_normalized)
        
        # State tracking with side effect (semi-relevant)
        if normalized > 10:
            cumulative_shift += 3
        elif normalized < 0:
            cumulative_shift -= 1

        # Core processing chain
        processed_value = normalized ^ (baseline & 7)  # Bitwise mix
        processed_value = (processed_value + len(temp_buffer)) % 23
        
        # Conditional expression affecting checksum
        checksum = (checksum << 1) ^ processed_value if processed_value % 2 else (checksum >> 1) ^ processed_value
        
        # Dead code path (red herring)
        if False:
            checksum = max(checksum, 50)  # Never executed

    # Additional irrelevant computation
    average_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    stability_index = cumulative_shift * 2

    # Output target result
    print(f"Result: {checksum}")

compute_diagnostic_signal()