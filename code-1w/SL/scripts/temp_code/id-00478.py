def process_data(data, cfg):
    threshold = cfg['limit']
    mode = cfg['mode']
    accumulator = 0
    temp_result = 0
    
    # Irrelevant preprocessing (distractor)
    normalized = [x % 97 for x in data if x > 0]  # Modulo with prime (unused later)
    stats = {'max': max(data), 'min': min(data), 'range': 0}  # Incomplete usage
    stats['range'] = stats['max'] - stats['min']

    # Core logic with interference
    filtered = []
    for val in data:
        if mode == 'A' and val > threshold:
            filtered.append(val * 2)
        elif mode == 'B' and val < threshold:
            filtered.append(val + 10)
        else:
            filtered.append(val // 3)

    # Secondary transformation with lambda (required feature)
    transform = lambda x: x ^ 5 if x % 2 == 0 else x ^ 3
    transformed = [transform(x) for x in filtered]

    # Accumulate result with early exit condition
    for num in transformed:
        if accumulator > 100:
            break
        if num == 0:
            continue
        accumulator += num % 11

    # Dead code path (distractor)
    if len(transformed) > 50:
        temp_result = sum(transformed) // len(transformed)
    else:
        temp_result = -1  # Never used

    # Final computation
    checksum = 0
    for i in range(len(transformed)):
        if i % 3 == 0:
            checksum ^= transformed[i]

    final_output = accumulator ^ checksum
    return final_output

# Simulate input
stream_buffer = [12, 15, 20, 8, 25, 6, 18, 9, 14, 11]
config = {'mode': 'A', 'limit': 15}

# Execute
final_output = process_data(stream_buffer, config)
print(f"Result: {final_output}")