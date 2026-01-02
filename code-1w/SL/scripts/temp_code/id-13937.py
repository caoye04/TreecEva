def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [m / max(metrics) * 100 for m in metrics]
    above_threshold = 0
    weighted_sum = 0.0

    for i, metric in enumerate(metrics):
        if metric > thresholds[i % len(thresholds)]:
            above_threshold += 1
        # Semi-relevant computation with partial effect
        weight = (i + 1) / len(metrics)
        weighted_sum += metric * weight

    return above_threshold, weighted_sum


def build_report_keys(data_map):
    # Dead code path - never used in final logic
    keys = set(data_map.keys())
    types = set(type(v).__name__ for v in data_map.values())
    combined = keys.union(types)
    return sorted(combined)


def calculate_final_score(raw_values, config):
    # Misleading variable initialization
    temp_buffer = [0] * len(raw_values)
    for idx in range(len(raw_values)):
        temp_buffer[idx] = raw_values[idx] ** 0.5

    # Core logic begins
    adjusted = [v * config['multiplier'] for v in raw_values]
    
    # Use of zip to align values with flags
    valid_pairs = []
    for val, flag in zip(adjusted, config['validity_flags']):
        if flag:
            valid_pairs.append(val)
    
    # Secondary filtering using modular arithmetic
    filtered = []    
    for i, v in enumerate(valid_pairs):
        if i % config['skip_interval'] != 0:  # skip every Nth element
            filtered.append(v)
    
    # Accumulation with integer division and rounding
    total = sum(filtered)
    base_score = total // len(filtered) if filtered else 0
    
    # Tertiary adjustment using character count from labels (semi-relevant)
    label_chars = sum(len(label) for label in config['labels'])
    char_mod = label_chars % 7
    
    # Final composition
    final_score = base_score + char_mod
    
    # Unused distractor variables
    snapshot = {i: v for i, v in enumerate(temp_buffer)}
    debug_info = list(enumerate(zip(adjusted, config['validity_flags'])))
    
    return final_score

# Main execution context
raw_data = [45, 67, 23, 89, 56, 77, 33]
params = {
    'multiplier': 1.8,
    'skip_interval': 3,
    'validity_flags': [True, True, False, True, True, True, False],
    'labels': ['alpha', 'beta', 'gamma', 'delta'],
    'thresholds': [40, 60, 20, 80]
}

# Call helper function (its result is unused)
unused_analysis = analyze_performance(raw_data, params['thresholds'])
report_keys = build_report_keys({'alpha': 45, 'beta': 67})

# Critical statement
final_score = calculate_final_score(raw_data, params)
print(f"Result: {final_score}")