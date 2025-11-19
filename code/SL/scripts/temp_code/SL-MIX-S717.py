def simulate_sensor_processing():
    # Sensor readings (raw data)
    raw_readings = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
    
    # Initialize processing variables
    accumulator = 0
    mask_register = 0xF0
    
    # Process each reading
    for idx, reading in enumerate(raw_readings):
        # Step 1: Apply mask and XOR with index
        masked_value = reading & mask_register
        xor_result = masked_value ^ idx
        
        # Step 2: Rotate left by 2 bits (with wraparound)
        rotated = ((xor_result << 2) | (xor_result >> 6)) & 0xFF
        
        # Step 3: Conditional update of accumulator
        if rotated > 0x80 and (idx % 2 == 0):
            accumulator |= rotated  # Set bits in accumulator
        elif rotated <= 0x80 or not (idx % 3 == 0):
            accumulator &= ~rotated  # Clear bits in accumulator
        else:
            accumulator ^= rotated   # Toggle bits in accumulator
    
    # Post-processing transformation
    processed_output = (accumulator + 0x100) % 0x1FF
    
    # >>> PROCESSING COMPLETE <<<
    return processed_output

# Execute simulation
final_value = simulate_sensor_processing()
print(f"Result: {final_value}")