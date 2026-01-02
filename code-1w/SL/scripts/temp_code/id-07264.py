def analyze_system_performance(input_data):
    # Initialize core parameters
    base_rating = len(input_data) % 79
    efficiency_factor = 0
    adjustment_offset = -5
    temp_buffer = []

    # Irrelevant pre-processing: character frequency analysis (distractor)
    char_freq = {}
    for item in input_data:
        if isinstance(item, str):
            cleaned = item.lower().replace(' ', '')
            for ch in cleaned:
                char_freq[ch] = char_freq.get(ch, 0) + 1
    
    # Secondary distraction: build unused transformation list
    transformed = [x.upper() if isinstance(x, str) else x * 2 for x in input_data]

    # Determine efficiency factor through conditional logic chain
    valid_count = 0
    for item in input_data:
        if isinstance(item, int):
            if item > 0 and item % 2 == 1:
                valid_count += 1

    if valid_count > 3:
        efficiency_factor = 12
    elif valid_count == 3:
        efficiency_factor = 8
    elif valid_count > 0:
        efficiency_factor = 4
    else:
        efficiency_factor = 2

    # Compute adjustment offset using modular arithmetic (only partially relevant)
    sum_keys = sum(k % 5 for k in char_freq.values()) if char_freq else 0
    adjustment_offset += (sum_keys * 3) % 17

    # Dead code path: this block never executes due to prior conditions (misleading)
    debug_mode = False
    if debug_mode and len(temp_buffer) > 100:
        reset_counter = 0
        while reset_counter < 10:
            reset_counter += 1
        adjustment_offset -= reset_counter

    # Key computation embedded in moderate nesting
    if base_rating > 10:
        if efficiency_factor >= 8:
            adjustment_offset += 10
        else:
            adjustment_offset += 3
    elif base_rating > 0:
        adjustment_offset += 7
    else:
        adjustment_offset += 1

    # Critical statement: target variable assignment
    thermal_capacity = base_rating * efficiency_factor + adjustment_offset

    # Redundant post-processing (no effect on result)
    final_data = []
    for i, x in enumerate(transformed):
        if isinstance(x, int) and i % 2 == 0:
            final_data.append(x + 1)

    return thermal_capacity

# Simulate system input with mixed data types
input_stream = [15, "sensor_A", 23, "calib_X", 7, "sensor_B", 19, "status_OK", 11]
result = analyze_system_performance(input_stream)
print(f"Result: {result}")