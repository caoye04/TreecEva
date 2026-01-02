import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 17

# Misleading transformation chain
def decoy_transform(sequence):
    temp = [s * 2 for s in sequence if s < 5]
    return sorted(temp, reverse=True)

# Auxiliary calculation with red herring variables
counter_weight = 0.85
dummy_matrix = [[i * j for j in range(3)] for i in range(3)]
scaling_factor = sum(sum(row) for row in dummy_matrix)  # Irrelevant sum: 18

# Real data processing pipeline
config_flags = {
    'enable_frobnication': False,
    'use_legacy_mode': True,
    'debug_trace': False
}

intermediate_cache = {}

# Core logic disguised among distractions
def compute_hash(key):
    h = 0
    for c in key:
        h = (h * 31 + ord(c)) % 10007
    return h

# Conditional expression mixed with dictionary lookup
def evaluate_condition(x, y):
    mode = 'legacy' if config_flags['use_legacy_mode'] else 'modern'
    thresholds = {'legacy': 42, 'modern': 65}
    limit = thresholds[mode]
    return x >= limit if y % 2 == 0 else x <= limit

# Bit manipulation decoy
def obscure_bits(value):
    shifted = (value << 3) & 0xFF
    toggled = shifted ^ 0b11010110
    return toggled >> 2

# Real computation buried in noise
data_chunk = list(range(10, 20))  # [10, 11, ..., 19]

# Distractor: unused intermediate arrays
shadow_copy = [x + 100 for x in data_chunk]
phantom_map = {idx: val * 3 for idx, val in enumerate(data_chunk)}

# Key transformation with multiple steps and irrelevant branches
def process_pipeline(items):
    result = 0
    temp_log = []
    
    for i, item in enumerate(items):
        # Irrelevant branching
        if i % 7 == 0:
            temp_log.append(compute_hash(f'debug_{item}'))
            continue  # skips actual processing
        
        # Real operation: check condition using external flag
        if evaluate_condition(item, i):
            adjusted = item * 2
        else:
            adjusted = int(math.sqrt(item)) * 3
        
        # Red herring: bit manipulation that isn't used
        masked = obscure_bits(adjusted)
        
        # Conditional expression influencing accumulation
        multiplier = 1 if item % 4 == 0 else 2
        
        # Actual contribution to result
        result += adjusted * multiplier
        
        # Dictionary-based caching (partially relevant)
        intermediate_cache[item] = {
            'raw': item,
            'adj': adjusted,
            'mult': multiplier,
            'prod': adjusted * multiplier
        }
        
        # Fake early exit
        if item == 25:
            break
    
    # Final adjustment using dictionary operation
    cache_size = len(intermediate_cache)
    correction = cache_size // 5
    
    # Critical assignment point
    final = result - correction
    
    return final

# Execution flow with misleading calls
_ = decoy_transform(shadow_copy)
_ = unused_helper(123)

# Key execution point
final_output = process_pipeline(data_chunk)

print(f"Result: {final_output}")