import itertools

# Simulate a data processing pipeline with multiple transformation stages
# Some components are decoys; only specific paths affect final output

def apply_filter(x, threshold):
    return x > threshold

def transform_value(x, mode):
    if mode == 'square':
        return x * x
    elif mode == 'negate':
        return -x
    else:
        return x + 1  # default red herring

def compute_checksum(seq):
    # Irrelevant function - never called in critical path
    return sum(seq) % 100

def generate_sequence(base, count):
    # Distractor: generates unused sequences
    return [base * (i + 1) for i in range(count)]

def deep_merge_dicts(d1, d2):
    # Complex but irrelevant dictionary operation
    result = dict(d1)
    for k, v in d2.items():
        if k in result and isinstance(result[k], list) and isinstance(v, list):
            result[k] = result[k] + v
        else:
            result[k] = v
    return result

def analyze_pattern(arr):
    # Dead-end analysis function
    return {"length": len(arr), "peaks": sum(1 for i in range(1, len(arr)-1) if arr[i-1] < arr[i] > arr[i+1])}

def main_processing_phase(raw_data, strategy):
    temp_storage = []
    intermediate_log = []
    
    for item in raw_data:
        # Multiple layers of processing
        stage1 = transform_value(item, strategy['stage1_op'])
        stage2 = transform_value(stage1, strategy['stage2_op'])
        
        # Filtering based on dynamic condition
        if apply_filter(stage2, strategy['threshold']):
            temp_storage.append(stage2)
        
        # Logging irrelevant metrics
        intermediate_log.append({"input": item, "post_stage1": stage1, "flagged": stage2 > 50})
    
    # Real computation happens here: sum filtered results
    primary_result = sum(temp_storage)
    
    # Decoy aggregation
    secondary_result = len(intermediate_log) * 2
    
    return primary_result  # Only this matters

# Orchestration function that combines data structures and logic
def process_transformations(pipeline_config, settings):
    data_stream = pipeline_config.get('data', [])
    flow_mode = pipeline_config.get('mode')
    
    # Dictionary-based routing (some keys are distractions)
    mode_ops = {
        'aggressive': {'stage1_op': 'square', 'stage2_op': 'negate', 'threshold': -10},
        'conservative': {'stage1_op': 'negate', 'stage2_op': 'square', 'threshold': 20},
        'balanced': {'stage1_op': 'square', 'stage2_op': 'square', 'threshold': 10}
    }
    
    if flow_mode not in mode_ops:
        flow_mode = 'balanced'
    
    resolved_strategy = mode_ops[flow_mode]
    
    # Augment with settings override (potential distraction)
    for k in ['stage1_op', 'stage2_op']:
        if k in settings:
            resolved_strategy[k] = settings[k]  # But settings doesn't override in this case
    
    # Core processing
    core_value = main_processing_phase(data_stream, resolved_strategy)
    
    # Begin decoy chain: complex data structure manipulations
    history_tracker = []
    for i in range(3):
        snapshot = {
            'epoch': i,
            'data_slice': generate_sequence(i + 1, 5),
            'analysis': analyze_pattern(generate_sequence(i + 1, 5))
        }
        history_tracker.append(snapshot)
    
    # Bitwise obfuscation layer (irrelevant)
    metadata_flag = 0b1010
    for ht in history_tracker:
        metadata_flag ^= len(ht['data_slice'])
        metadata_flag <<= 1
        if metadata_flag > 255:
            metadata_flag = metadata_flag % 256
    
    # Red herring dictionary merge
    decoy_config = {'debug': True, 'buffers': [1, 2, 3], 'stage1_op': 'unknown'}
    merged_profile = deep_merge_dicts(settings, decoy_config)
    
    # Spurious itertools usage to distract
    permutations_test = list(itertools.permutations([1, 2, 3], 2))
    permutation_sum = sum(a + b for a, b in permutations_test)  # Unused
    
    # Final computation uses only core_value with fixed adjustment
    final_adjustment = 7
    final_output = core_value + final_adjustment
    
    # Print required at end
    print(f"Result: {final_output}")
    return final_output

# Setup inputs
config_settings = {
    'log_level': 'DEBUG',
    'buffers': [5, 10, 15],
    'timeout': 30
}

data_pipeline = {
    'data': [2, 3, 4, 5],
    'mode': 'aggressive'
}

# Execute
final_output = process_transformations(data_pipeline, config_settings)