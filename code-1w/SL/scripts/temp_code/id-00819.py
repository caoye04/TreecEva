def analyze_pattern(sequence, threshold=5):
    count = 0
    temp_sum = 0
    result_map = {}
    for idx, val in enumerate(sequence):
        if val > threshold:
            count += 1
            temp_sum += val ** 2
        else:
            temp_sum -= val
        result_map[idx] = temp_sum % (idx + 1) if idx != -1 else 0

    # Irrelevant transformation
    transformed = [x ^ 7 for x in sequence]
    decoy_value = sum(transformed) / len(transformed) if transformed else 0

    # Distractor: unused branch with complex logic
    if len(sequence) > 10 and all(x % 2 == 0 for x in sequence):
        alternate_path = [x << 2 for x in sequence]
        normalization = sum(alternate_path) // len(alternate_path)
    else:
        normalization = None  # Dead path

    return count, temp_sum


def evaluate_conditions(flags, data_stream):
    flag_state = flags.get('active', False) and not flags.get('paused', True)
    accumulator = 0

    for i, (f, d) in enumerate(zip(flags.get('inputs', []), data_stream)):
        if i % 3 == 0:
            accumulator += d * (2 if f else 1)
        elif i % 3 == 1:
            accumulator -= d & 15  # Bitwise mask
        else:
            accumulator += (d + i) // 2

    # Decoy computation
    fake_moving_avg = [sum(data_stream[j:j+3]) / 3 for j in range(len(data_stream)-2)]
    spike_count = sum(1 for x in fake_moving_avg if x > 50)

    return flag_state, accumulator


def compute_checksum(items):
    checksum = 0
    for item in items:
        if isinstance(item, int):
            checksum ^= item  # XOR accumulation
        elif isinstance(item, str):
            checksum += sum(ord(c) for c in item.lower())
    return checksum % 97


def compute_aggregate(payload):
    raw_data = payload['values']
    config = payload['config']
    
    # Real processing begins
    pattern_count, base_total = analyze_pattern(raw_data, config['threshold'])
    
    # Conditional expression with distractors
    adjustment_factor = 1.5 if config['mode'] == 'aggressive' else (0.8 if config['mode'] == 'conservative' else 1.0)
    
    # Extract secondary evaluation
    flag_result, signal_total = evaluate_conditions(config['flags'], raw_data)
    
    # Combine multiple concepts: bitwise, arithmetic, conditional
    intermediate = (base_total + signal_total) >> 1
    if pattern_count > 3:
        intermediate = int(intermediate * adjustment_factor)
    
    # Checksum as integrity verification (used in final score)
    metadata_checksum = compute_checksum([config['version'], config['timestamp']])
    
    # Irrelevant list transformation
    mirrored = [raw_data[-i-1] for i in range(len(raw_data))]
    symmetry_score = sum(a ^ b for a, b in zip(raw_data, mirrored)) // 2 if len(raw_data) > 1 else 0
    
    # Final score calculation — this is the key point
    final_score = intermediate - metadata_checksum + pattern_count
    
    # Unused but misleading derived values
    volatility_index = max(raw_data) - min(raw_data) if raw_data else 0
    entropy_approx = sum(x * x for x in raw_data) / len(raw_data) if raw_data else 0
    
    return final_score

# Main execution
if __name__ == '__main__':
    input_payload = {
        'values': [3, 8, 12, 4, 16, 7, 20],
        'config': {
            'threshold': 6,
            'mode': 'aggressive',
            'flags': {
                'active': True,
                'paused': False,
                'inputs': [True, False, True, True, False, False, True]
            },
            'version': 'v2.1',
            'timestamp': 1718943201
        }
    }
    
    # Call the main function
    final_score = compute_aggregate(input_payload)
    
    # Print result
    print(f"Result: {final_score}")