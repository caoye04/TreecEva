def process_metrics(log, thresh):
    base_values = [entry['value'] for entry in log if entry['active']]
    indices = [i for i, entry in enumerate(log) if entry['flagged']]
    
    # Irrelevant tracking variables (distractors)
    total_scans = len(log)
    skipped_entries = sum(1 for e in log if not e['active'])
    temp_offset = sum(i * 2 for i in range(len(indices))) if indices else 0

    # Semi-relevant preprocessing
    adjusted_values = []
    for val in base_values:
        if val > thresh:
            adjusted_values.append(val * 0.9)
        else:
            adjusted_values.append(val + 5)

    # Auxiliary computation with set operations (partially relevant)
    unique_caps = list(set([min(v, 100) for v in adjusted_values]))
    capped_count = len(unique_caps)

    # Core logic: weighted efficiency calculation
    weights = [1.1 if i % 2 == 0 else 0.9 for i in range(len(adjusted_values))]
    weighted_sum = sum(adjusted_values[i] * weights[i] for i in range(len(adjusted_values)))
    
    # Secondary adjustment based on capped distribution
    cap_factor = 1.0
    if capped_count < 5:
        cap_factor = 0.8
    elif capped_count > 8:
        cap_factor = 1.1

    # Efficiency score computation (this is the answer target)
    raw_efficiency = weighted_sum / len(adjusted_values) if adjusted_values else 0
    efficiency_score = raw_efficiency * cap_factor

    # Dead code path - never executed under current logic
    if False and skipped_entries > 10:
        efficiency_score *= 0.95

    # Final output construction
    diagnostics = {
        'entries_processed': len(base_values),
        'adjustment_offset': temp_offset,
        'peak_value': max(adjusted_values) if adjusted_values else 0
    }
    
    final_output = efficiency_score  # Critical assignment point
    return final_output

# Input data
entries = [
    {'value': 12, 'active': True, 'flagged': False},
    {'value': 95, 'active': True, 'flagged': True},
    {'value': 43, 'active': False, 'flagged': False},
    {'value': 67, 'active': True, 'flagged': False},
    {'value': 105, 'active': True, 'flagged': True},
    {'value': 23, 'active': True, 'flagged': False},
    {'value': 88, 'active': True, 'flagged': True},
    {'value': 76, 'active': True, 'flagged': False},
    {'value': 150, 'active': True, 'flagged': True},
    {'value': 5, 'active': True, 'flagged': False}
]

threshold = 70
result = process_metrics(entries, threshold)
print(f"Result: {result}")