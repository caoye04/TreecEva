def transform_string(s):
    # Irrelevant string transformation (distractor)
    return s.upper().replace('A', 'X').swapcase()

# Misleading data structures
temp_buffer = [0] * 15
lookup_table = {i: (i * 3) % 7 for i in range(10)}
offset_cache = {'x': 5, 'y': -2, 'z': 12}

# Decoy function with unused recursion
def decoy_sum(n):
    if n <= 1:
        return 1
    return n + decoy_sum(n - 2)  # Never actually used

# Real processing function
def process_item(x, cfg):
    if x % 2 == 0:
        x = (x ^ cfg['key']) + cfg['shift']  # Bitwise manipulation
    else:
        x = (x * cfg['factor']) - cfg['offset']
    
    # String-based red herring
    flag_str = "TrUe" if x > 100 else "fAlSe"
    flag_bool = flag_str.lower() == 'true'
    
    if flag_bool and x % 3 == 0:
        x = x // 3
    return abs(x) % 97  # Normalize result

def process_sequence(data, config):
    result = 0
    index_map = tuple(range(len(data)))  # Unused tuple
    temp_state = []
    
    for i, val in enumerate(data):
        # Distracting conditional branch
        if i % 4 == 0:
            temp_state.append(val * 2)
        elif i % 4 == 2:
            temp_state.append(val - 1)
        
        # Core logic buried in noise
        processed = process_item(val, config)
        adjustment = offset_cache.get('z') if processed % 2 else offset_cache.get('x')
        result += processed - adjustment
    
    # More irrelevant list operations
    reversed_state = temp_state[::-1]
    sum_check = sum(reversed_state[:5]) if len(reversed_state) > 5 else 0
    
    # Final computation using string length as subtle clue
    tag = "FINAL_PASS"
    scale = len(tag.lower().replace('a', ''))  # Returns 9 (length of "finl_pss")
    
    return (result + 42) * scale  # Actual answer path

# Dead code path
unused_data = [{'id': i, 'val': decoy_sum(i)} for i in range(5)]

# Key configuration and input
data = [12, 23, 34, 45, 56]
config = {
    'key': 7,
    'shift': 3,
    'factor': 4,
    'offset': 5
}

# Trigger execution
intermediate = transform_string("example_string")
final_output = process_sequence(data, config)
print(f"Target result: {final_output}")