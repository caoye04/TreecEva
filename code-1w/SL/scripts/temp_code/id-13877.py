def calculate_entropy(values):
    """Misleading helper: not used in final computation."""
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        entropy -= prob * math.log2(prob)
    return entropy


def find_outlier_indices(lst):
    """Another red herring function: computes but unused outliers."""
    mean_val = sum(lst) / len(lst)
    std_dev = (sum((x - mean_val) ** 2 for x in lst) / len(lst)) ** 0.5
    threshold = 2 * std_dev
    return [i for i, x in enumerate(lst) if abs(x - mean_val) > threshold]


def calculate_final_score(data, weights):
    # Step 1: Extract relevant sensor readings
    base_values = [data['sensor_A'], data['sensor_B'], data['sensor_C']]
    
    # Step 2: Apply weighted transformation
    weighted_sum = 0
    temp_adjustment = 0
    for i, key in enumerate(['sensor_A', 'sensor_B', 'sensor_C']):
        raw_val = data[key]
        weight = weights[key]
        adjusted_val = raw_val * weight
        temp_adjustment += adjusted_val * 0.1  # Partial accumulation
        weighted_sum += adjusted_val
    
    # Step 3: Normalize using dynamic range
    max_base = max(base_values)
    min_base = min(base_values)
    range_correction = (max_base - min_base) or 1
    normalized_score = weighted_sum / range_correction
    
    # Step 4: Apply conditional bonus based on pattern
    bonus_applied = False
    if data['sensor_A'] > data['sensor_B'] and data['sensor_B'] < data['sensor_C']:
        normalized_score += 5.5
        bonus_applied = True
    
    # Step 5: Track state in dictionary (semi-relevant)
    status_log = {
        'processed': True,
        'bonus': bonus_applied,
        'peak_value': max_base,
        'debug_code': 207  # Irrelevant metadata
    }
    
    # Step 6: Final adjustment using auxiliary calculation
    aux_factor = 1.0
    if status_log['bonus']:
        aux_roots = [normalized_score ** 0.5, normalized_score ** 0.25]  # Computed but mostly unused
        aux_factor = aux_roots[0] / (aux_roots[1] + 1e-5)
    
    # Step 7: Compute final score (this is the critical result)
    final_score = normalized_score * 0.9 + aux_factor * 2
    
    # Irrelevant tracking variables
    debug_snapshot = {
        'timestamp': 1678886400,
        'mode': 'diagnostic',
        'dummy_counter': 42
    }
    
    return final_score

# Main execution
weights = {
    'sensor_A': 0.6,
    'sensor_B': 0.3,
    'sensor_C': 0.8
}

data = {
    'sensor_A': 12,
    'sensor_B': 7,
    'sensor_C': 15,
    'calibration_offset': 3.2,      # Unused field
    'legacy_mode': False            # Dead field
}

# Misleading pre-computations
entropy = calculate_entropy([weights[k] for k in weights])  # Distractor call
outliers = find_outlier_indices([data[k] for k in ['sensor_A', 'sensor_B', 'sensor_C']])  # Unused
intermediate_avg = sum(data[k] for k in ['sensor_A', 'sensor_B']) / 2  # Semi-relevant only

# Critical statement
final_score = calculate_final_score(data, weights)

# Output result
print(f"Result: {final_score}")