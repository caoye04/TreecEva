import math

# Irrelevant helper function (dead code path)
def validate_checksum(data):
    return sum(data) % 256 == 0

# Another decoy function that is never called
def encrypt_stream(data, key):
    return [d ^ key for d in data]

# Misleading global variables
temp_cache = [0] * 100
debug_flag = True
overflow_threshold = 999
padding_value = -1

# Real processing begins here
def analyze_pattern(seq):
    count = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            count += 1
    return count

# Dictionary-based transformation map (core concept)
transform_map = {
    'factor': lambda x: x * 3 if x % 2 else x * 2,
    'shift': lambda x: x + 7,
    'modulate': lambda x: x % 13 + 4
}

# Auxiliary function with red herring parameters
def normalize_values(arr, scale=1.0, invert=False, clamp=True):
    result = []
    max_val = max(arr) if max(arr) != 0 else 1
    for val in arr:
        normalized = val / max_val * scale
        if invert:
            normalized = 1 - normalized
        # Clamping is irrelevant due to input range
        if clamp and normalized > 1:
            normalized = 1
        result.append(round(normalized, 6))
    return result  # This return value is unused in main logic

# Core data processor combining multiple concepts
def process_data(buffer, settings):
    # Level 1: Initial filtering (list comprehension)
    filtered = [x for x in buffer if x > settings['min_level']]
    
    # Level 2: Apply dictionary-mapped transformations sequentially
    step1 = [transform_map['factor'](x) for x in filtered]
    step2 = [transform_map['shift'](x) for x in step1]
    step3 = [transform_map['modulate'](x) for x in step2]
    
    # Level 3: Accumulation with conditional logic
    total = 0
    for val in step3:
        if val in settings['special_flags']:
            total += val * 2
        elif val > settings['pivot']:
            total += int(val / 2)
        else:
            total += val // 3
    
    # Level 4: Nested control flow with bit manipulation red herring
    metadata = settings['meta']
    adjustment = 0
    if 'version' in metadata:
        if metadata['version'] == 'A':
            adjustment = 5
        elif metadata['version'] == 'B':
            # Bitwise distraction
            raw_flag = metadata.get('flag', 0)
            adjustment = (raw_flag & 7) ^ 3
        else:
            adjustment = -2
    else:
        adjustment = 1
    
    # Level 5: Final adjustment using summation and rounding
    raw_output = total + adjustment
    
    # Decoy operation (no effect on output)
    shadow_copy = temp_cache[:len(step3)]
    for i, v in enumerate(step3):
        shadow_copy[i] = v ^ padding_value
    
    # Actual final computation
    final_output = int(round(math.sqrt(raw_output ** 2)))  # Equivalent to abs(raw_output), but disguised
    
    return final_output

# Main execution block
if __name__ == '__main__':
    # Simulated sensor data stream (real input)
    stream_buffer = [12, 3, 8, 15, 2, 18, 5, 9, 11, 4, 13]
    
    # Configuration dictionary with relevant and irrelevant fields
    config = {
        'min_level': 6,
        'special_flags': [10, 11, 12],
        'pivot': 9,
        'meta': {
            'version': 'C',  # Triggers else branch (-2 adjustment)
            'timestamp': 1678899000,
            'flag': 15
        },
        'timeout': 30,
        'retries': 3,
        'debug_mode': False
    }
    
    # Dead code: simulate checksum validation (never used)
    status = validate_checksum(stream_buffer)
    
    # Key statement
    final_output = process_data(stream_buffer, config)
    
    # Print result for extraction
    print(f"Target result: {final_output}")
