def process_data_chain(input_data):
    # Distractor: Irrelevant data processing
    temp_analysis = {}
    temp_analysis['length'] = len(str(input_data))
    temp_analysis['digits'] = sum(c.isdigit() for c in str(input_data))
    
    # Main processing path with misleading intermediate steps
    processed = input_data * 3
    processed = processed - 15  # Red herring subtraction
    
    # Conditional branching with dead code path
    if processed > 50:
        processed = processed // 2
        # Unused computation that looks important
        shadow_value = processed * 7 + 3
    else:
        processed = processed * 4
        # Another misleading computation
        shadow_value = processed - 25
    
    # Dictionary operations with irrelevant entries
    data_map = {'primary': processed, 'secondary': shadow_value, 'tertiary': input_data * 2}
    
    # More distractor computations
    verification_sum = sum(data_map.values())  # Never used
    
    # Actual key computation
    result = data_map['primary'] + data_map['secondary']
    result = result - data_map['tertiary']
    
    # Final adjustment with more distractions
    adjustment_factor = (result % 10) + 1
    final_result = result // adjustment_factor
    
    # Dead code path that looks relevant
    if final_result < 0:
        final_result = abs(final_result) * 2
    
    return final_result

original_data = 27
final_processed = process_data_chain(original_data)
print(f"Result: {final_processed}")