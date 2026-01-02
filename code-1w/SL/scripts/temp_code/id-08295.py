def transform_value(x, shift=3):
    # Irrelevant transformation function (dead code path)
    return (x << 2) ^ shift

def helper_sum(seq):
    # Misleading utility that's not used in critical path
    return sum([i * 2 for i in seq if i % 2 == 0])

def validate_checksum(arr):
    # Distractor: computes a checksum but doesn't affect main logic
    checksum = 0
    for i, val in enumerate(arr):
        checksum += val * (i + 1)
    return checksum % 1007

def decode_pattern(seq, mask):
    # Another red herring with bit manipulation
    result = 0
    for s, m in zip(seq, mask):
        if m:
            result ^= s & (s >> 1)
    return result

def process_sequence(data, config):
    temp_result = 0
    scaling_factor = config.get('scale', 1)
    offset = config.get('offset', 0)
    
    # Decoy variables and irrelevant computations
    shadow_buffer = [0] * len(data)
    accumulator = 0
    for idx, item in enumerate(data):
        accumulator += item * (idx + 1)
        shadow_buffer[idx] = (item ^ 5) + 2  # Unused buffer
    
    # Real logic begins here — subtle and buried
    active_flags = config.get('flags', [])
    intermediate = 0
    
    for i, val in enumerate(data):
        if i % 2 == 0:
            intermediate += val * scaling_factor
        else:
            intermediate -= (val + offset) // 2
    
    # Conditional mutation based on decoy checksum (but actually deterministic)
    fake_check = validate_checksum(data)
    if fake_check > 100:
        intermediate = abs(intermediate)  # Always true, but looks conditional
    
    # Key transformation using enumerate and zip (required features)
    multipliers = [2, 1, 3, 4, 2]
    for (i, v), m in zip(enumerate(data), multipliers):
        if i < len(multipliers):
            temp_result += (v + m) * (i + 1)
    
    # Early return red herring — never triggered due to data constraints
    if len(data) > 100:
        return -999  # Dead code
    
    # Actual output depends only on intermediate and temp_result
    final_component = intermediate + (temp_result % 197)
    
    # Final distraction: unused dictionary mapping
    metadata_map = {
        'source': 'input_data',
        'version': 2.1,
        'processed': True,
        'debug_flag': decode_pattern(data, [1,0,1,0,1])
    }
    
    return final_component

# Main execution block
if __name__ == '__main__':
    # Input setup
    data = [8, 12, 5, 19, 3]
    config = {
        'scale': 4,
        'offset': 6,
        'flags': ['A', 'B'],
        'mode': 'legacy'
    }
    
    # Irrelevant pre-processing
    processed_data = [x for x in data if x > 4]
    backup_copy = tuple(data)
    data.append(1000)  # Does not affect since list copy already made
    
    # Critical execution point
    final_output = process_sequence(data, config)
    
    # Output result as required
    print(f"Result: {final_output}")