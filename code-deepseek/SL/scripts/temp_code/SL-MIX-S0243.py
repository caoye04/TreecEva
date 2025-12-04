def analyze_data_patterns():
    raw_data = [45, 78, 23, 91, 56, 34, 82, 67]
    processed_values = []
    temp_buffer = 0
    
    # Process and filter data points
    for idx, value in enumerate(raw_data):
        if value > 50:
            processed = value ^ 0x3F  # XOR with mask
            processed_values.append(processed)
        else:
            temp_buffer += value  # Distractor - not used in final result
    
    # Calculate validation metrics
    validation_mask = 0
    for i, val in enumerate(processed_values):
        if i % 2 == 0:
            validation_mask |= (val & 0xF)  # Bitwise OR accumulation
        else:
            temp_buffer -= val  # Distractor operation
    
    processed_data = sum(processed_values) & 0xFF  # Keep lower 8 bits
    intermediate_check = temp_buffer ^ processed_data  # Red herring
    
    # Final computation
    final_score = processed_data | validation_mask
    print(f"Target result: {final_score}")

analyze_data_patterns()