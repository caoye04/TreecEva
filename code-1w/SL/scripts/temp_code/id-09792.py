import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 2 + 3 * x - 7

# Misleading transformation chain
def transform_v1(data):
    temp = [x * 1.5 for x in data]
    return [t for t in temp if t > 10]

def transform_v2(data):
    shifted = [x + 2 for x in data][::-1]  # slicing and shift
    filtered = [s for s in shifted if s % 2 == 0]
    return filtered

def apply_mask(sequence, mask_value=3):
    # Conditional expression used idiomatically
    return [val if i % mask_value != 0 else val // 2 
            for i, val in enumerate(sequence)]

# Core recursive processing function (simple recursion)
def recursive_reduce(lst):
    if len(lst) <= 1:
        return lst[0] if lst else 0
    mid = len(lst) // 2
    left = recursive_reduce(lst[:mid])
    right = recursive_reduce(lst[mid:])
    return left + (right * 0.5)

# Decoy accumulator with misleading intermediate values
def build_history(values):
    history = []
    total = 0
    for v in values:
        total += v
        if total > 100:  # unreachable condition due to input size
            history.append({'step': len(history), 'value': total})
    return history  # never actually used

# Main pipeline processor
def process_pipeline(raw_data, settings):
    stage1 = raw_data[1:-1]  # slicing to remove edge noise
    stage2 = apply_mask(stage1, mask_value=settings.get('mask', 3))
    
    # Conditional data route (only one branch is logically active)
    if sum(stage2) > 50:
        processed = transform_v1(stage2)
    else:
        processed = transform_v2(stage2)  # This will be taken
    
    # Introduce decoy variables with plausible but unused calculations
    avg_decoy = sum(processed) / len(processed) if processed else 0
    peak_sim = max(processed) * math.sin(math.pi / 4) if processed else 0
    
    # Critical computation path
    cleaned = [x for x in processed if x > 5]  # final filtering
    reduced = recursive_reduce(cleaned)
    
    # Secondary distraction: early break in loop that doesn't affect outcome
    checksum = 0
    for item in cleaned:
        checksum += item * 2
        if checksum > 1000:  # will never trigger
            break
    
    # Final output formation
    scaling_factor = settings.get('scale', 1.0)
    offset = settings.get('offset', -2)
    final_output = (reduced * scaling_factor) + offset
    
    return final_output

# Irrelevant global constants
data_source_version = "v2.1-alpha"
optimization_threshold = 0.85
max_iterations = 500

# Input setup
data = [4, 6, 3, 8, 2, 9, 1]
config = {
    'mask': 3,
    'scale': 4.0,
    'offset': -2,
    'debug': True
}

# Execution point of interest
final_output = process_pipeline(data, config)
print(f"Target result: {final_output}")