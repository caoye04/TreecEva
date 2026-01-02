def compute_diagnostic_checksum():
    # Simulate sensor data sequence (deterministic)
    raw_readings = [234, 157, 89, 192, 77]
    
    # Irrelevant transformation: convert to voltage readings (not used in final result)
    voltage_map = lambda x: round((x * 3.3) / 1024, 3)
    voltage_readings = [voltage_map(val) for val in raw_readings]
    
    # State tracking variables
    checksum = 0xACE1  # Initial magic seed
    temp_accum = 0
    decay_factor = 0.9
    
    # Secondary unused accumulator for distraction
    shadow_state = 0xBABA
    
    for i, reading in enumerate(raw_readings):
        # Pre-process reading with modular arithmetic and bit rotation
        rotated = ((reading >> (i % 3)) | (reading << (8 - (i % 3)))) & 0xFF
        inverted = (~rotated) & 0xFF
        processed_value = (rotated + inverted) % 251  # Prime mod for dispersion
        
        # Update shadow state (distractor - not used in output)
        shadow_state = (shadow_state * 17 + processed_value) % 0xFFFF
        
        # Main checksum update with bit shifting and XOR
        checksum = (checksum << 1) ^ processed_value & 0xFFFF
        
        # Temp accumulation with decay (semi-relevant but doesn't affect final answer)
        temp_accum = (temp_accum * decay_factor + reading) // 1
        
        # Conditional flip based on index parity (has no effect due to masking)
        if i % 2 == 0:
            checksum += 1  # Will be masked out in next line
        checksum &= 0xFFFF  # Normalize to 16-bit
    
    # Final processing step that does nothing (dead code)
    final_mask = 0xFFFF
    unused_diagnostic = (shadow_state ^ temp_accum) & final_mask
    
    print(f"Result: {checksum}")

compute_diagnostic_checksum()