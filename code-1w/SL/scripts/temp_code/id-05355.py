import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Decoy transformation that is never called
def decoy_transform(seq):
    return [int(math.sqrt(x)) if x > 0 else 0 for x in seq]

# Real transformation function used in logic
def transform_values(arr):
    return [x * 2 + 1 for x in arr]

# Secondary processing with filtering and aggregation
def filter_and_map(values, threshold):
    filtered = [v for v in values if v > threshold]
    return [v + int(math.log(v + 1)) for v in filtered]

# Core data processing pipeline
def process_chunk(data_block, mode):
    temp_result = []
    scaling_factor = 3
    offset = 2
    
    # Nested list comprehension with slicing distraction
    sliced_view = data_block[::2]  # Every second element — actually relevant
    extended_view = data_block + [0] * 3
    
    for item in sliced_view:
        if item < 0:
            temp_result.append(abs(item) * scaling_factor)
        else:
            temp_result.append((item + offset) ** 2)
    
    # Dummy dictionary used to create noise
    stats = {
        'count': len(data_block),
        'sum': sum(data_block),
        'max': max(data_block),
        'useless_metric': sum([i*i for i in range(3)])  # Irrelevant computation
    }
    
    # This conditional is always true due to input; misleading complexity
    if stats['max'] >= 0:
        temp_result = [t - 1 for t in temp_result]
    
    return temp_result

# Orchestration function combining multiple concepts
def process_results(data_list, config_dict):
    intermediate = []
    backup_chain = []  # Unused but looks important
    
    # Simulate multi-stage processing
    for segment in data_list:
        processed = process_chunk(segment, config_dict['mode'])
        filtered_stage = filter_and_map(processed, config_dict['threshold'])
        intermediate.extend(filtered_stage)
    
    # Bit manipulation red herring
    mask = 0b1111
    masked_values = [i & mask for i in intermediate]  # Looks critical, not used
    
    # Actual key transformation
    transformed_intermediate = transform_values(intermediate)
    
    # Dictionary-based routing (only one branch taken)
    actions = {
        'compute': lambda x: sum(x) // len(x) if x else 0,
        'validate': lambda x: len([i for i in x if i % 2 == 0]),
        'debug_dump': lambda x: sum([i * i for i in x])  # Dead end
    }
    
    # Only 'compute' is used — others are distractors
    if config_dict['action'] in actions:
        result = actions['compute'](transformed_intermediate)
    else:
        result = 0
    
    # Final adjustment using float arithmetic and rounding
    final_adjustment = result * 1.5
    final_rounded = int(round(final_adjustment))
    
    # Critical variable assignment — answer lies here
    final_output = final_rounded - 7
    
    # Multiple print statements to distract
    debug_log = {
        'raw_intermediate_len': len(intermediate),
        'post_transform_sum': sum(transformed_intermediate),
        'mask_effect': sum(masked_values),
        'unreachable_calc': math.ceil(math.pi * 100)  # Misleading metric
    }
    
    return final_output

# Misleading data initialization block
raw_samples = [1, -2, 3, -4, 5]
decoys = [x - 10 for x in raw_samples if x % 2 != 0]
dummy_matrix = [[i+j for j in range(3)] for i in range(3)]

# Real input data structure — a list of lists
input_segments = [
    [2, -1, 4],
    [0, 3, -2],
    [1, 1, 5]
]

# Configuration dictionary with irrelevant fields
config = {
    'mode': 'standard',
    'threshold': 3,
    'action': 'compute',
    'verbosity': 99,  # Unused
    'timeout_ms': 5000,  # Dead parameter
    'retries': 3,  # Not used
    'cache_enabled': False  # Distractor
}

# Transform input using slicing and comprehension (actually used)
expanded_segment = [seg + [min(seg)] for seg in input_segments]
transformed_data = []
for part in expanded_segment:
    # Apply transformation that feeds into main pipeline
    transformed_data.append([x + 2 for x in part][::-1])  # Reverse slice

# Execute main logic
final_output = process_results(transformed_data, config)

# Output result as required
print(f"Result: {final_output}")