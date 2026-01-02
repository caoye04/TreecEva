def analyze_signal(values):
    if len(values) < 5:
        return sum(values) * 2
    else:
        temp = [v ** 2 for v in values if v > 0]
        return sum(temp[:4])

# Irrelevant helper (distractor)
def compute_entropy(data):
    import math
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

# Unused function (dead code path)
def legacy_transform(x):
    return (x + 32) * (5/9)

# Another red herring
def evaluate_threshold(signal, limit=100):
    count = 0
    for i in range(len(signal)):
        if signal[i] > limit:
            count += 1
            break
    return count > 0

# Core processing with distractors
def process_metrics(raw_data, config):
    # Distractor variables
    buffer_cache = {}
    debug_log = []
    temp_result = 0
    
    # Real computation begins
    base_values = [raw_data.get(k, 0) for k in ['input_a', 'input_b', 'input_c']]
    scaling_factors = config.get('scale', [1, 1, 1])
    
    # Apply scaling
    scaled = [base_values[i] * scaling_factors[i] for i in range(len(base_values))]
    
    # Conditional adjustment based on derived property
    magnitude = sum(abs(x) for x in scaled)
    if magnitude > 50:
        adjustment = 0.8
    elif magnitude > 20:
        adjustment = 1.1
    else:
        adjustment = 1.3
    
    adjusted = [x * adjustment for x in scaled]
    
    # Accumulation with early exit logic
    accumulator = 0
    for val in adjusted:
        if abs(val) > 40:
            accumulator += val * 0.5
            break
        accumulator += val
    else:
        accumulator += 5  # Only if no break
    
    # Dictionary-based post-processing
    flags = {
        'high_input': raw_data.get('input_a', 0) > 15,
        'boost_mode': config.get('boost', False),
        'legacy_compat': False
    }
    
    if flags['high_input'] and flags['boost_mode']:
        accumulator *= 1.2
    elif flags['high_input']:
        accumulator += 7
    
    # Final transformation
    final_value = int(round(accumulator))
    
    # Red herring: unused transformation branch
    metadata_snapshot = {
        'version': '2.1',
        'computed_at': '2023-11-05',
        'intermediate': temp_result,
        'final_raw': accumulator
    }
    
    # This is the key output
    final_score = final_value + 10
    
    # Debug side-effect (no impact)
    debug_log.append(f"Processed: {final_score}")
    
    return final_score

# Setup inputs
input_data = {
    'input_a': 12,
    'input_b': 8,
    'input_c': 5,
    'aux_x': 99,  # irrelevant field
    'aux_y': 101  # irrelevant field
}

weights_config = {
    'scale': [1.5, 2.0, 0.8],
    'boost': True,
    'mode': 'advanced'
}

# Simulate signal analysis (distractor call)
signal_test = [-2, 3, 5, 8, 1]
analyze_signal(signal_test)

# Actual target computation
final_score = process_metrics(input_data, weights_config)

# Output result as required
print(f"Result: {final_score}")