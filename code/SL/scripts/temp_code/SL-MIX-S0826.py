def processing_pipeline(input_data, phase_count, optimize_flag):
    # Initialize tracking variables
    base_value = 42
    temp_buffer = [0] * 10
    offset_calc = 17
    
    # Distractor: misleading intermediate computation
    shadow_sum = sum(range(phase_count * 5)) + base_value
    
    # Main processing logic
    if optimize_flag:
        step_multiplier = 3
        phase_adjustment = 7
    else:
        step_multiplier = 2
        phase_adjustment = 5
    
    # Core computation with list comprehension
    data_stream = [x * step_multiplier for x in input_data]
    
    # Irrelevant bit manipulation
    bit_ops = (offset_calc << 2) & 0xFF
    
    # Slicing operations with meaningful logic
    window_size = min(phase_count, len(data_stream))
    active_window = data_stream[-window_size:]
    
    # Dead code path that never executes
    if phase_count > 10:
        unused_result = shadow_sum * 2 - bit_ops
    
    # Key calculation with multiple steps
    intermediate = sum(active_window) + phase_adjustment
    
    # More distractions
    redundant_check = intermediate % 13
    temp_buffer[0] = redundant_check
    
    # Final computation that matters
    final_result = (intermediate * base_value) // (phase_count + 1)
    
    return final_result

# Main execution
input_sequence = [2, 5, 8, 3, 7]

# Multiple irrelevant variable assignments
backup_calc = sum(input_sequence) * 4
placeholder_var = backup_calc - 17

# The critical execution point
final_analysis = processing_pipeline(input_sequence, 3, True)

# Final output
print(f"Result: {final_analysis}")