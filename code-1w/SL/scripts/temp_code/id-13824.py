def process_entries(data_list):
    """ Irrelevant data processing function (dead code path) """
    temp_result = 0
    for item in data_list:
        if isinstance(item, str):
            temp_result += len(item)
    return temp_result

# Misleading initialization block
counterfeit_sum = 0
for i in range(100):
    counterfeit_sum += (i * 2) % 7

# Unused complex transformation
def transform_value(x):
    return ((x ^ 5) + 3) * 2

# Distractor: fake assessment with decoy metrics
decoy_metrics = {
    'alpha': 120,
    'beta': 87,
    'gamma': 94
}

baseline_offset = 5
adjustment_factor = 1.2

# Real logic begins here — deeply nested and mixed with noise
status_flags = {True, False, True, False}
active_modes = {True, True}

flag_state = len(status_flags) > 2  # evaluates to True

assessment_log = [
    {'type': 'entry', 'value': 85, 'active': True},
    {'type': 'entry', 'value': 92, 'active': False},
    {'type': 'entry', 'value': 78, 'active': True},
    {'type': 'entry', 'value': 96, 'active': True}
]

benchmark = [80, 90, 75, 88]

# Decoy list used nowhere
phantom_data = [x ** 2 for x in range(10) if x % 3 == 0]

# Linear search disguised as utility
def find_match(sequence, target):
    for idx, val in enumerate(sequence):
        if val == target:
            return idx
    return -1

# Core evaluation logic buried under distractions
def evaluate_performance(log, ref):
    total = 0
    match_count = 0
    
    # Nested filtering and case conversion (simulated via string op)
    valid_entries = [e for e in log if e['active']]
    
    for entry in valid_entries:
        raw_val = entry['value']
        
        # Simulate case normalization (conceptual mapping)
        normalized_val = raw_val + baseline_offset  # now 90, 83, 101
        
        # Find closest benchmark using linear scan
        closest = None
        min_diff = float('inf')
        for b_val in ref:
            diff = abs(normalized_val - b_val)
            if diff < min_diff:
                min_diff = diff
                closest = b_val
        
        # Scoring based on proximity
        score_contribution = 100 - min_diff * 2
        total += score_contribution
        
        # Track matches
        if min_diff == 0:
            match_count += 1
    
    # Set operation: active vs reference indices
    log_indices = {i for i, e in enumerate(log) if e['active']}
    ref_set = {i for i in range(len(ref))}
    overlap = log_indices & ref_set  # intersection: {0, 2, 3}
    
    bonus = len(overlap) * 5
    
    # Final adjustment using logical conditions
    if flag_state and len(active_modes) == 2:
        bonus += 7
    
    return int(total + bonus)

# Red herring computation
checksum = 0
for k in decoy_metrics:
    checksum += decoy_metrics[k] // 3

# Critical execution point
final_score = evaluate_performance(assessment_log, benchmark)

# Output result as required
print(f"Result: {final_score}")