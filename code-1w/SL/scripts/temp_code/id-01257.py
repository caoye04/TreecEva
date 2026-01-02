def process_data(data, settings):
    temp_result = 0
    scaling_factor = settings['gain'] * 1.5
    offset = settings['offset']
    accumulator = 0
    
    # Irrelevant preprocessing (distractor)
    normalized = [x * 0.9 + 1 for x in data if x > 0]
    filtered = [x for x in normalized if x < 50]
    stats = {'count': len(filtered), 'sum': sum(filtered)}
    
    # Core logic with nested conditions and dictionary use
    for i, val in enumerate(data):
        if i % 2 == 0:
            adjusted = val * scaling_factor
            if adjusted > 30:
                temp_result += int(adjusted - offset)
            else:
                temp_result -= int(adjusted)
        else:
            shifted = val >> 1
            if shifted % 3 == 0:
                temp_result ^= shifted
    
    # Auxiliary computation that doesn't affect final result
    checksum = 0
    for v in data:
        checksum = (checksum + v) % 97
    metadata = {'checksum': checksum, 'version': '2.1', 'active': True}
    
    # Final transformation using dictionary lookup
    mode = settings['mode']
    modifiers = {'fast': 2, 'normal': 1, 'slow': 0.5}
    modifier = modifiers.get(mode, 1)
    
    intermediate = abs(temp_result) + len(data)
    accumulator = intermediate * modifier
    
    # Additional distraction: unused loop over settings
    total_weight = 0
    for k, v in settings.items():
        if isinstance(v, float):
            total_weight += v * 0.1
    
    final_output = int(accumulator - 8)  # Key statement
    return final_output

# Setup inputs
stream_buffer = [12, 5, 8, 14, 6, 21, 3]
config = {
    'gain': 2.0,
    'offset': 5,
    'mode': 'normal',
    'debug': True,
    'threshold': 10
}

# Execute and print result
result_var = process_data(stream_buffer, config)
print(f"Target result: {result_var}")