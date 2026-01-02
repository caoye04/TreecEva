import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_stream(raw_data, window_size=3):
    filtered = [x for x in raw_data if x > 0]
    reshaped = [filtered[i:i+window_size] for i in range(0, len(filtered), window_size)]
    transposed = list(itertools.zip_longest(*reshaped, fillvalue=0))
    flattened = [item for sublist in transposed for item in sublist]
    return [x ^ 0x5A for x in flattened]  # Irrelevant bit manipulation

# Decoy function – never called but looks important
def compute_entropy(data):
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    return -sum((count / total) * log2(count / total) for count in freq.values())

# Complex state machine with dead branches
def update_state(state, input_val, mode='A'):
    temp_state = state.copy()
    temp_state['counter'] += 1
    temp_state['history'].append(input_val)

    if mode == 'X':  # Dead branch — condition never met
        temp_state['flag'] = True
        temp_state['buffer'] = [input_val * 2 for _ in range(5)]
    elif mode == 'Y':  # Another dead branch
        temp_state['checksum'] = sum(temp_state['buffer'])
    else:
        if input_val % 2 == 0:
            temp_state['even_sum'] += input_val
        else:
            temp_state['odd_product'] *= (input_val % 7)

        if len(temp_state['history']) > 4:
            temp_state['history'] = temp_state['history'][-4:]

    return temp_state

# Legitimate transformation chain
def generate_features(seq):
    a = sum(x * (i+1) for i, x in enumerate(seq))
    b = max(seq) ^ min(seq)
    c = len([x for x in seq if x % 3 == 0])
    d = a & b | c  # Bitwise mix
    return {'f1': a, 'f2': b, 'f3': c, 'f4': d}

# Critical path obscured by distractions
def finalize_digest(buffer):
    base = 1
    for val in buffer:
        base = (base * 33 + val) % 997  # Rolling hash
    return base ^ 0xDEADBEEF % 1000000  # Final masking

# Main execution flow
if __name__ == '__main__':
    raw_sensor_data = [15, -3, 8, 0, 12, 7, 21, -5, 4, 6]
    
    # Irrelevant transformations
    cleaned = preprocess_stream(raw_sensor_data)
    feature_set = generate_features(cleaned)
    
    # Initialize complex state with decoy fields
    state_buffer = {
        'counter': 0,
        'even_sum': 10,
        'odd_product': 1,
        'flag': False,
        'buffer': [],
        'history': [],
        'checksum': None
    }
    
    # Apply real logic on meaningful subset
    relevant_subset = [x for x in raw_sensor_data if x % 2 == 1 and x > 0]  # [15, 7, 21]
    processed_values = [x // 3 for x in relevant_subset]  # [5, 2, 7]
    
    # Update state using valid mode only (mode='A')
    for val in processed_values:
        state_buffer = update_state(state_buffer, val)
    
    # This is the key statement
    checksum = finalize_digest(processed_values)
    
    # Print result as required
    print(f"Result: {checksum}")