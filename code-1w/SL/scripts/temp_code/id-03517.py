def compute_diagnostic_sequence():
    # Simulate sensor data processing with embedded integrity check
    raw_readings = [23, 17, 89, 45, 67]
    calibration_factor = 3
    adjustment_offset = -12
    checksum = 15
    temporal_accumulator = 0
    diagnostic_log = []

    for reading in raw_readings:
        # Pre-process step: apply calibration and offset (some readings are logged but not used)
        calibrated = reading * calibration_factor + adjustment_offset
        adjusted_reading = max(calibrated, 0)  # Clamp to non-negative
        
        # Red herring computation: tracking temporal pattern (not used in final result)
        temporal_accumulator += adjusted_reading % 11
        if adjusted_reading > 50:
            diagnostic_log.append(f"HIGH:{adjusted_reading}")

        # Core logic: determine processing mode based on bit pattern
        significant_bits = adjusted_reading & 0b111  # Lower 3 bits
        is_oscillating = (significant_bits > 4) != (reading % 2 == 0)
        processed_value = significant_bits | (reading >> 3)
        
        # Conditional transformation using conditional expression
        temp_flag = True if len(diagnostic_log) % 2 == 1 else False
        
        # Key statement: update checksum based on dynamic condition
        checksum = (checksum << 1) ^ processed_value if temp_flag else checksum + processed_value
        
        # Dead code path - never executed due to fixed list length, but looks relevant
        if len(raw_readings) > 10:
            reset_trigger = checksum & 0xFFFF
            checksum = reset_trigger % 100

    # Final irrelevant scaling (does not affect answer)
    normalized_checksum = checksum / 1.0
    submission_code = int(normalized_checksum) + 1000

    print(f"Result: {checksum}")

compute_diagnostic_sequence()