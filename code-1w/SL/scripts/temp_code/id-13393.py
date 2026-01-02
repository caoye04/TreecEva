import math

# Irrelevant helper function (decoy)
def compute_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

# Unused transformation lambdas (distractors)
bit_flip = lambda x: x ^ 0xFF
reverse_case_all = lambda s: ''.join(c.lower() if c.isupper() else c.upper() for c in s)
square_input = lambda x: x ** 2

# Simulated dataset with mixed types and red herrings
data_set = [
    {'id': 1, 'raw_value': 128, 'status': 'active', 'meta': [1, 0, 1]},
    {'id': 2, 'raw_value': 64, 'status': 'inactive', 'meta': [0, 1, 1]},
    {'id': 3, 'raw_value': 256, 'status': 'active', 'meta': [1, 1, 0]},
    {'id': 4, 'raw_value': 32, 'status': 'active', 'meta': [0, 0, 1]}
]

# Decoy data structure transformations
processed_stack = []
for item in data_set:
    processed_stack.append({
        'shifted': item['raw_value'] >> 3,
        'flag_sum': sum(item['meta']),
        'squared_meta': [m ** 2 for m in item['meta']]
    })

# Misleading intermediate calculation (dead path)
total_flags = sum(sum(d['meta']) for d in data_set)
adjusted_flags = total_flags * 1.5 if total_flags > 5 else total_flags * 0.8

# Red herring list comprehension
encoded_ids = [d['id'] * 2 + (100 if d['status'] == 'active' else 0) for d in data_set]

# Unused recursive function (distractor)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Core logic disguised among noise
def transform_value(x):
    if x <= 0:
        return 0
    log_val = math.log(x, 2)
    shifted = int(log_val) << 2
    return shifted + (x & 7)

# Simulate conditional scoring with nested logic
def score_entry(entry):
    base = transform_value(entry['raw_value'])
    
    # Complex conditional mask (appears significant but only partially used)
    mask_score = 0
    meta = entry['meta']
    if len(meta) >= 3:
        if meta[0] and not meta[1]:
            mask_score += 5
        elif not meta[0] and meta[2]:
            mask_score += 3
        else:
            mask_score += 2
    
    # Only active items get performance bonus
    bonus = 7 if entry['status'] == 'active' else 0
    
    # Critical: only base and bonus are actually used in final result
    return base + bonus  # mask_score calculated but not returned

# Higher-order function distractor
def apply_transformation(func, lst):
    return [func(x) for x in lst]

# Real evaluation chain buried in complexity
def evaluate_performance(dataset):
    scores = []
    temp_buffer = []
    
    for record in dataset:
        # Intermediate transformation with side storage (partly irrelevant)
        transformed = {
            'orig_id': record['id'],
            'computed': score_entry(record)
        }
        temp_buffer.append(transformed['computed'] * 0.95)  # unused buffer
        scores.append(transformed['computed'])
    
    # Final aggregation uses only main scores
    raw_total = sum(scores)
    
    # Apply decay function via lambda (actual use)
    decay_factor = lambda t: t * 0.98 ** (len(scores) - 1)
    adjusted_total = decay_factor(raw_total)
    
    # Final nonlinear adjustment
    final = int(adjusted_total + math.sqrt(len(scores) * 10))
    
    # Dead code below (never reached)
    if final < 0:
        fallback = 0
        for s in scores:
            fallback += s // 2
        return fallback
    
    return final

# Execution point of interest
final_score = evaluate_performance(data_set)

# Print required output
print(f"Target result: {final_score}")