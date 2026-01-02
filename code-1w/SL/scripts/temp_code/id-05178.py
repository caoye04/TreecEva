def process_data(data):
    # Irrelevant transformation: bit manipulation with no effect on final result
    shadow_state = [x ^ 255 for x in data[:10]]
    
    # Actual relevant logic begins
    filtered = [x for x in data if x % 3 == 0]
    shifted = list(map(lambda x: x >> 1, filtered))
    
    # Accumulate sum with conditional adjustment
    temp_sum = 0
    for val in shifted:
        if val > 10:
            temp_sum += val // 2
        else:
            temp_sum += val * 2
    
    # Dead code path (never executed due to data constraints)
    anomaly_flag = False
    if any(x < 0 for x in shadow_state):
        anomaly_flag = True
        correction_factor = sum(shadow_state)
    
    # Red herring variable: calculated but unused
    checksum = sum(data[i] * (i + 1) for i in range(len(data))) % 1000
    
    # Key computation using slicing and arithmetic
    segment = data[5:15]
    peak_value = max(segment) if len(segment) > 0 else 0
    normalized = peak_value / 2.0
    
    # Final output derived from two independent chains
    final_output = temp_sum + int(normalized)
    return final_output

# Simulated sensor data stream
stream_buffer = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54]

# Execute main logic
final_output = process_data(stream_buffer)
print(f"Result: {final_output}")