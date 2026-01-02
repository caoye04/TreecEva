def transform_value(x, mode):
    if mode == 'A':
        return (x ** 2) % 17
    elif mode == 'B':
        return (x * 3 + 5) % 19
    else:
        return x

# Irrelevant helper function (decoy)
def validate_checksum(seq):
    return sum(seq) % 11 == 0

# Misleading data transformation path
def deprecated_process(arr):
    result = []
    for item in arr:
        result.append((item + 7) * 2)
    return result  # Never used

# Core processing function
def process_sequence(sequence, settings):
    temp = []
    multiplier = settings['base']
    offset = settings.get('offset', 0)
    
    # Real logic begins
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            transformed = transform_value(val, 'A')
        else:
            transformed = transform_value(val, 'B')
        temp.append(transformed * multiplier)
    
    # Secondary transformation
    adjusted = [v + offset for v in temp]
    
    # Red herring: unused filtering
    filtered = [x for x in adjusted if x > 10]
    summary_stats = {
        'count': len(adjusted),
        'sum': sum(adjusted),
        'max': max(adjusted),
        'flag': False
    }
    
    # Distractor: fake validation check
    flag_check = any(x < 0 for x in adjusted)
    if flag_check:
        summary_stats['flag'] = True

    # Actual answer derivation
    accumulator = 0
    for idx, num in enumerate(adjusted):
        accumulator += num * (idx + 1)  # Weighted sum
    
    # Final computation
    final_hash = accumulator % 97
    scaling_factor = settings['scale']
    raw_output = (final_hash * scaling_factor) // 3
    
    # String manipulation as side distraction
    status_log = "Processing completed at level {}".format(settings['level'])
    log_parts = status_log.split(' ')
    code_word = log_parts[-1].lower()
    
    # Dictionary usage (required feature)
    code_map = {chr(i): i - ord('a') for i in range(ord('a'), ord('z')+1)}
    bonus = sum(code_map[c] for c in code_word if c in code_map) % 5
    
    # Final output with minor adjustment
    final_output = raw_output + bonus
    
    # Dead code path (never reached)
    if final_output < 0:
        final_output *= -1
    
    return final_output

# Main execution
if __name__ == '__main__':
    # Input data
    data = [12, 8, 15, 3, 9, 11, 6]
    
    # Configuration with meaningful and distracting keys
    config = {
        'base': 4,
        'scale': 6,
        'level': 'Gamma',
        'offset': 2,
        'mode': 'production',
        'debug': False,
        'timeout': 30
    }
    
    # Unused variables (distractors)
    backup_data = data[::-1]
    temp_result = deprecated_process(data)
    checksum_valid = validate_checksum(data)
    metadata_store = []
    
    # Key statement
    final_output = process_sequence(data, config)
    
    # Output result
    print(f"Result: {final_output}")