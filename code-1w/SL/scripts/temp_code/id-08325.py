import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(math.sqrt(i) > 1 for i in x if i > 0)

# Distractor: complex-looking but unused transformation
def decoy_transform(seq):
    temp = [x ^ 255 for x in seq]
    shifted = [(x >> 2) & 0xFF for x in temp]
    return [math.floor(math.log(abs(x) + 1)) for x in shifted]

# Real processing components
def filter_relevant(stream):
    return [x for x in stream if x % 3 == 0 and x > 0]

def compute_weighted_sum(items):
    weights = [0.5 if i % 2 == 0 else 0.3 for i in range(len(items))]
    return sum(item * weight for item, weight in zip(items, weights))

def generate_checksum(values):
    checksum = 0
    for v in values:
        checksum = (checksum * 7 + v) % 10009
    return checksum

def enhance_resolution(num):
    return num if num <= 100 else int(sum(math.sin(i) * 10 for i in range(num % 11)))

# Conditional expression in action
def classify_magnitude(x):
    return 'large' if x > 50 else 'medium' if x > 20 else 'small'

# Core pipeline with red herrings
def process_pipeline(raw_data):
    stage1 = [x * 2 + 1 for x in raw_data]  # Transform each element
    
    # Misleading branch with conditional expression (does not affect outcome)
    audit_log = 'active' if len(stage1) > 10 else 'inactive'
    debug_trace = []
    if audit_log == 'active':
        debug_trace.append(sum(stage1) // len(stage1))
    
    # Actual filtering begins here
    stage2 = filter_relevant(stage1)
    
    # Decoy usage that appears important but isn't part of final result
    _ = decoy_transform(stage1)
    
    # Weighted accumulation
    base_score = compute_weighted_sum(stage2)
    
    # Secondary computation that seems critical but is only used conditionally
    temp_flag = any(classify_magnitude(x) == 'large' for x in stage2)
    adjustment = 0
    if temp_flag:
        adjustment = enhance_resolution(int(base_score))
    
    # Critical data dependency: checksum influences final logic
    integrity_key = generate_checksum(stage2)
    
    # Complex conditional expression combining multiple red herrings
    modifier = adjustment * 0.1 if integrity_key % 7 == 0 else (base_score * 0.05 if integrity_key % 3 == 0 else 0)
    
    # Final computation chain
    preliminary = base_score + modifier
    
    # Another layer of distraction: unused list comprehension
    _ = [math.ceil(preliminary / n) for n in range(1, min(len(stage2), 5))]
    
    # Actual answer derivation
    final_value = int(preliminary) + (integrity_key % 100)
    
    # Key variable assignment
    final_output = final_value
    
    return final_output

# Simulated input data
seed_data = list(range(8, 45, 3))  # [8, 11, 14, ..., 44]
data_chunk = [x * 3 + 1 for x in seed_data]  # Further transformed input

# Execute main logic
final_output = process_pipeline(data_chunk)

print(f"Target result: {final_output}")