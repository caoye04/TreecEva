import itertools

# Simulated sensor data with noise and metadata
data_stream = [18, 23, 14, 59, 27, 31, 22, 46, 19, 38]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 1024
scaling_factor = 0.87
noise_floor = [0.1, 0.3, 0.2, 0.5]
temp_cache = {}
buffer_limit = 512
debug_mode = False

# Decoy function - looks important but unused in main logic
def apply_calibration(x):
    return [(val * scaling_factor) + baseline_offset for val in x if val > 20]

# Auxiliary transformation functions
def filter_outliers(seq, threshold=50):
    return list(filter(lambda x: x < threshold, seq))

def pair_wise_diff(seq):
    return [abs(a - b) for a, b in itertools.pairwise(seq)]

def rolling_window_avg(seq, window=3):
    if len(seq) < window:
        return [sum(seq)/len(seq)] if seq else [0]
    return [sum(seq[i:i+window]) / window for i in range(len(seq)-window+1)]

# Core processing pipeline
def transform_values(vals):
    # Step 1: Keep only values below 35
    stage1 = [v for v in vals if v < 35]
    
    # Step 2: Apply modulo 7 to each element
    stage2 = [v % 7 for v in stage1]
    
    # Step 3: Remove duplicates while preserving order
    seen = set()
    stage3 = [x for x in stage2 if not (x in seen or seen.add(x))]
    
    # Step 4: XOR each element with index
    stage4 = [val ^ i for i, val in enumerate(stage3)]
    
    return stage4

# Another decoy - complex but unused
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_sum(arr, idx + 1)

# Real pipeline function
memoized_results = {}
def process_pipeline(input_data):
    # Distractor: irrelevant dictionary operations
    stats = {
        'count': len(input_data),
        'max_val': max(input_data),
        'min_val': min(input_data),
        'range': max(input_data) - min(input_data)
    }
    
    # Distractor: unused string processing
    diagnostic_tag = "PROC_" + "".join([chr(65 + (len(input_data) % 26))] * 2)
    if debug_mode:
        print(f'Diagnostic: {diagnostic_tag}')
    
    # Main logic begins here
    cleaned = filter_outliers(input_data, threshold=60)  # All are <60, so no effect
    transformed = transform_values(cleaned)
    
    # Additional distraction: dead code path
    if len(transformed) > 100:
        buffer_overflow_handler(transformed)
    
    # More distractions: irrelevant combinatorics
    pairs = list(itertools.combinations(transformed, 2))
    sum_of_products = sum(a * b for a, b in pairs[:10]) if pairs else 0
    
    # Critical operation chain
    diffs = pair_wise_diff(transformed)
    averages = rolling_window_avg(diffs, window=2)
    
    # Final computation: hash-like aggregation
    accumulator = 0
    for i, val in enumerate(averages):
        accumulator += int(val) * (i + 1)
    
    # Key result derived from nested logic
    final_value = accumulator ^ (transformed[0] * 100)
    
    # This is the actual target
    return final_value

# Unused function - red herring
def buffer_overflow_handler(data):
    raise RuntimeError("This should never be called")

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Target result: {final_output}")