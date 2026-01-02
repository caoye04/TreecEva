import math

# Irrelevant helper function (dead code path)
def compute_legacy_score(x):
    return sum(i ** 2 for i in x if i % 3 == 0)

# Misleading auxiliary computation
temp_offsets = [i * 1.5 for i in range(7)]
offset_correction = sum(temp_offsets) / len(temp_offsets)

# Real data pipeline setup
data = {
    'readings': [3, 7, 1, 9, 4, 8, 2],
    'weights': [0.1, 0.3, 0.1, 0.2, 0.1, 0.1, 0.1],
    'flags': [True, False, True, True, False, True, False]
}

config = {
    'threshold': 5,
    'boost_factor': 1.25,
    'decay_rate': 0.9,
    'activation_key': 'readings'
}

# Decoy dictionary with unused transformations
transform_map = {
    'linear': lambda x: x * 1.1,
    'square': lambda x: x ** 2,
    'logit': lambda x: math.log(x / (1 - x)) if 0 < x < 1 else 0,
    'identity': lambda x: x
}

# Unused transformation chain
decoys = []
for k, func in transform_map.items():
    decoys.append(func(0.5) if k != 'square' else func(2))

# Auxiliary state tracker (partially relevant)
cumulative_state = {
    'active_count': 0,
    'sum_above_threshold': 0.0,
    'weighted_accum': 0.0,
    'suppressed': []
}

# Simulated preprocessing step (some parts are distractions)
processed_readings = []
for idx, val in enumerate(data['readings']):
    adjusted = val
    if data['flags'][idx]:
        adjusted *= config['boost_factor']
    if val > config['threshold']:
        adjusted *= config['decay_rate']
    processed_readings.append(round(adjusted, 3))

# Red herring: complex string-based encoding (unused)
status_tags = ['A', 'B', 'C']
encoded_tag = ''.join(f'{ord(t) % 31}' for t in status_tags)
checksum = sum(int(c) for c in encoded_tag)

# Core logic disguised among distractors
def process_metrics(dataset, cfg):
    readings = dataset[cfg['activation_key']]
    weights = dataset['weights']
    flags = dataset['flags']
    
    # Intermediate accumulators
    base_total = 0.0
    bonus_applied = 0
    penalty_factor = 1.0
    
    # Logical filtering and weighted accumulation
    for i in range(len(readings)):
        if not flags[i]:
            continue  # Skip inactive entries
        contribution = readings[i] * weights[i]
        base_total += contribution
        
        # Conditional bonus logic
        if readings[i] >= cfg['threshold']:
            bonus_applied += 1
        else:
            penalty_factor *= cfg['decay_rate']  # Compounding decay
    
    # Apply bonus only if at least two high-readings were boosted
    if bonus_applied >= 2:
        base_total *= cfg['boost_factor']
    
    # Final suppression adjustment based on unused decoy
    if checksum > 10:  # This will always be true but diverts attention
        base_total -= 0.5
    
    # Destructuring-like assignment (tuple unpacking distraction)
    _, _, _, misc_val = (10, 20, 30, base_total * 0.1)
    
    # Apply penalty and round
    result = base_total * penalty_factor
    return round(result, 3)

# Additional red herring: list comprehension with side effects (no impact)
_ = [math.sqrt(x) for x in temp_offsets if x > 5]

# Critical execution point
final_score = process_metrics(data, config)

# Update cumulative state (only partially used)
cumulative_state['weighted_accum'] = final_score

cumulative_state['sum_above_threshold'] = sum(x for x in data['readings'] if x > 5)

# Output the target result
print(f"Result: {final_score}")