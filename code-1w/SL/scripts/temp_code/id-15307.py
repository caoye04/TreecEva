def transform_value(x, mode):
    if mode == 'A':
        return (x ^ 255) + 10
    elif mode == 'B':
        return (x * 3) % 100
    else:
        return x

# Irrelevant helper function (dead code path)
def unused_validator(seq):
    count = 0
    for item in seq:
        if isinstance(item, int) and item > 50:
            count += 1
    return count > 5

# Distractor data structure
decoy_map = {
    'alpha': [10, 20, 30],
    'beta': [40, 50, 60],
    'gamma': [70, 80, 90]
}

# Another red herring: unused transformation matrix
transform_matrix = [
    [1, 0, -1],
    [0, 1, 0],
    [1, -1, 1]
]

# Real processing begins here
def decode_segment(segment):
    result = 0
    for i, val in enumerate(segment):
        if i % 2 == 0:
            result += val & 15  # Bitwise AND with 15
        else:
            result -= val % 7
    return abs(result)

def analyze_pattern(seq):
    total = 0
    for item in seq:
        if item < 0:
            total += abs(item) // 3
        elif item > 100:
            total += item // 10
    return total

def process_sequence(data, config):
    temp_state = []
    checkpoint = 0

    # Meaningful but obfuscated computation
    for idx, chunk in enumerate(data):
        if idx in config['skip_indices']:
            continue
        
        transformed = []
        for num in chunk:
            # Apply bitwise and modular arithmetic
            step1 = (num << 1) ^ config['key']
            step2 = transform_value(step1, config['mode'])
            transformed.append(step2)
        
        # Decode the transformed chunk
        decoded = decode_segment(transformed)
        temp_state.append(decoded)
        
        # Red herring: conditional that never triggers due to data constraints
        if decoded > 1000:
            checkpoint += 1  # This will never happen

    # Core logic hidden among distractions
    aggregate = sum(temp_state)
    penalty = analyze_pattern(temp_state)
    final_score = aggregate - penalty
    
    # Decoy dictionary operation (no effect)
    decoy_map['delta'] = [final_score] if 'delta' not in decoy_map else None
    
    # Final computation
    scaling_factor = config.get('scale', 1)
    adjusted = final_score * scaling_factor
    
    # Critical assignment
    final_output = adjusted + len(temp_state)
    
    # Print required output
    print(f"Result: {final_output}")
    return final_output

# Input data
config_settings = {
    'key': 42,
    'mode': 'C',
    'skip_indices': [2],
    'scale': 2
}

data_stream = [
    [105, 203, 112],
    [97, 115, 116],
    [73, 78, 86],  # Skipped due to index 2
    [65, 76, 73]
]

# Execute main function
final_output = process_sequence(data_stream, config_settings)