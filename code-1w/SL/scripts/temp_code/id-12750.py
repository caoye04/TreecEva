def process_sensor(stream, config_map):
    accumulator = 0
    temp_log = []
    for i, val in enumerate(stream):
        if i % 3 == 0:
            accumulator += (val * config_map.get('gain', 1)) ** 2
        elif i % 5 == 0:
            accumulator -= val // 2
        else:
            temp_log.append(val)
    return accumulator

def validate_sequence(seq):
    seen = set()
    for x in seq:
        if x in seen:
            return False
        seen.add(x)
    return True

def transform_key(data_str, shift):
    # Irrelevant string transformation
    shifted = ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.islower() else c for c in data_str)
    return shifted[::-1]

def compute_entropy(values):
    from math import log2
    freq_map = {}
    total = len(values)
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def analyze_metrics(data, limits):
    # Core logic begins
    baseline = sum(data['readings']) // len(data['readings'])
    
    # Distractor: unused variable with plausible name
    outlier_flags = [x for x in data['readings'] if abs(x - baseline) > limits['deviation']]
    
    # Dead code path - never executed due to constant condition
    debug_mode = False
    if debug_mode:
        print("Debug: Starting deep analysis")
        redundant_check = validate_sequence(data['readings'])

    # Real computation starts
    filtered = [x for x in data['readings'] if limits['min'] < x < limits['max']]
    adjusted = [x + len(data['tags']) for x in filtered]
    
    # Bit manipulation red herring
    magic_mask = 0b101010
    masked_values = [x ^ magic_mask for x in adjusted]  # Not used later
    
    # Accumulation with modular arithmetic
    rolling_sum = 0
    for idx, val in enumerate(adjusted):
        rolling_sum = (rolling_sum + val * (idx + 1)) % 999983  # Large prime modulus
    
    # Dictionary-based weighting
    weights = {tag: i+1 for i, tag in enumerate(data['tags'])}
    weight_factor = sum(weights.values())
    
    # Final computation
    intermediate = (rolling_sum * weight_factor) // (baseline + 1)
    
    # Secondary distractor: complex but unused string operation
    encoded_tags = ','.join(data['tags']).upper()
    transformed = transform_key(encoded_tags.lower(), 7)
    _ = compute_entropy([len(transformed), len(encoded_tags), baseline])
    
    # Critical assignment
    final_diagnostic = (intermediate - 54321) * 2
    
    # Another decoy variable
    diagnostic_checksum = process_sensor([final_diagnostic % 100], {'gain': 3})
    
    return final_diagnostic

# Main execution
health_data = {
    'readings': [120, 150, 130, 145, 160, 110, 135],
    'tags': ['cardio', 'pulmonary', 'metabolic'],
    'device_id': 'DX-7890'
}

thresholds = {
    'min': 100,
    'max': 200,
    'deviation': 40
}

final_diagnostic = analyze_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")