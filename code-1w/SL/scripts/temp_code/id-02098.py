import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Unused transformation map
decoys = {
    'a': lambda z: z * 2,
    'b': lambda z: z + 10,
    'c': lambda z: z ** 0.5
}

# Misleading intermediate calculations
shadow_buffer = [i ^ (i >> 2) for i in range(15) if i % 3 != 0]
temp_offset = sum(shadow_buffer[:5]) // 3
offset_adjustment = (temp_offset * 0.75) - 4.2  # Unused in final logic

# Core data stream with embedded signal
raw_values = [8, 3, 12, 7, 19, 5, 14]
data_stream = list(map(lambda x: (x << 1) + 1, raw_values))  # Bit-shift encoding

# Decoy data structure
audit_log = {i: {'raw': raw_values[i], 'encoded': data_stream[i], 'valid': False} for i in range(len(raw_values))}

# Flag manipulation via bit operations
flags = 0
for val in data_stream:
    if val & 1:
        flags ^= val % 11
    if val > 20:
        flags += 1  # Red herring increment

# Real processing begins here — recursive filtering
def recursive_reduce(seq, threshold=15):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    mid = len(seq) // 2
    left = recursive_reduce(seq[:mid], threshold)
    right = recursive_reduce(seq[mid:], threshold)
    if left + right > threshold:
        return (left ^ right) + 1
    else:
        return left - right

# Distractor: unused accumulator
rolling_stats = []
for i, v in enumerate(data_stream):
    rolling_stats.append({
        'index': i,
        'value': v,
        'moving_avg': sum(data_stream[max(0, i-2):i+1]) / (i+1)
    })

# Conditional transform based on flag state
transform_mode = 'xor' if flags & 8 else 'add'

# Actual pipeline function
def process_pipeline(stream):
    # Nested dictionary comprehension — distractor
    meta = {
        f"item_{i}": {
            'shifted': v >> 1,
            'residual': v % 3,
            'active': (v % 4) == 0
        } for i, v in enumerate(stream)
    }
    
    # List comprehension with filtering and transformation
    cleaned = [v for v in stream if (v % 5) != 0 and v < 40]
    
    # Apply conditional transformation
    if transform_mode == 'xor':
        cleaned = [v ^ 7 for v in cleaned]
    else:
        cleaned = [v + 3 for v in cleaned]
    
    # Secondary filter: keep only values where second least significant bit is set
    filtered = [v for v in cleaned if (v & 2)]
    
    # Final reduction using recursive function
    result = recursive_reduce(filtered, threshold=25)
    
    # Apply mathematical adjustment
    adjusted = math.floor(abs(result) * 1.5)
    
    # Dummy assignment to confuse tracking
    adjusted = adjusted if adjusted > 0 else 999
    
    # Final output computation
    final_shift = adjusted >> 2
    return final_shift

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output result
print(f"Target result: {final_output}")