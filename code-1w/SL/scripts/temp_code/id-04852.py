def process_data(data, key):
    # Initialize tracking variables
    checksum = 0
    temp_state = []
    shift_register = 7
    
    # Irrelevant pre-processing (distractor)
    noise_filter = [x ^ 255 for x in data[:10] if x % 2 == 0]
    filtered_size = len(noise_filter) * 2 // 3 + 1
    
    # Core logic begins
    for i, val in enumerate(data):
        if i % 3 == 0:
            transformed = val ^ key  # XOR with key
            checksum += transformed
        elif i % 5 == 0 and val > 50:
            shifted = val >> 2
            temp_state.append(shifted)
        else:
            # Conditional expression usage (required feature)
            adjusted = val + 10 if val < 100 else val - 5
            checksum -= (adjusted % 17)
    
    # Secondary processing on temp_state (semi-relevant)
    aggregate = sum(temp_state) // len(temp_state) if temp_state else 0
    
    # Slice operation usage (required feature)
    history_log = data[5:15]
    log_sum = sum(history_log)
    
    # Final computation chain
    intermediate = (checksum ^ aggregate) & 0xFFFF
    scaling_factor = (log_sum // 10) or 1
    final_output = (intermediate // scaling_factor) + shift_register
    
    # Dead code path (distractor)
    if False:
        final_output *= 2
        final_output += len(noise_filter)
    
    return final_output

# Setup input
stream_buffer = [120, 45, 67, 89, 52, 78, 91, 103, 44, 66, 134, 88, 59]
validation_key = 42

# Execute
result = process_data(stream_buffer, validation_key)
print(f"Result: {result}")