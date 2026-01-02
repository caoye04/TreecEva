def compute_harmonic_sequence(indices):
    harmonic_seq = []
    temp_buffer = []
    cumulative_shift = 0
    
    for idx, val in enumerate(indices):
        shifted_val = val + (idx % 4)
        temp_buffer.append(shifted_val)
        
        if shifted_val % 2 == 0:
            cumulative_shift += idx
        else:
            cumulative_shift -= 1
    
    # Irrelevant normalization pass
    normalized_buffer = [x / (max(temp_buffer) + 1e-5) for x in temp_buffer]
    scaling_factor = sum(normalized_buffer)  # Unused later
    
    secondary_pairs = list(zip(temp_buffer[:-1], temp_buffer[1:]))
    
    running_harmonic = 0.0
    for a, b in secondary_pairs:
        if b != 0:
            running_harmonic += a / b
    
    # Main computation using original indices and enumeration
    total_harmonic = 0
    for i, num in enumerate(indices):
        if i > 0 and num != 0:
            total_harmonic += (i * num) / (num + i)
    
    # Dead code branch - never executed under normal input
    debug_mode = False
    if debug_mode:
        print(f'Debug: {cumulative_shift}, {scaling_factor}')
    
    return int(running_harmonic + total_harmonic)

# Input setup
nested_indices = [3, 1, 4, 1, 5]
dummy_mask = [x % 2 for x in nested_indices]  # Unused
auxiliary_sum = sum(dummy_mask)  # Distractor

intermediate_result = [x * 2 for x in nested_indices]  # Semi-relevant but unused

# Critical execution point
total_harmonic = compute_harmonic_sequence(nested_indices)

Result: {total_harmonic}