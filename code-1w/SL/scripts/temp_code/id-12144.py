def process_metrics(log_entries, config):
    baseline = sum(entry['value'] for entry in log_entries if entry['active'])
    adjustments = [entry['value'] * 0.1 for entry in log_entries if entry['flagged']]
    temp_sum = sum(adjustments) + len(log_entries)

    # Irrelevant helper computation (distractor)
    outlier_check = lambda x: x > 3 * baseline / len(log_entries) if len(log_entries) > 0 else False
    outliers = [e['value'] for e in log_entries if outlier_check(e['value'])]

    # Core logic with conditional expression
    scaling_factor = 1.5 if any(e['urgent'] for e in log_entries) else 0.8

    # Semi-relevant transformation (only length matters, not content)
    processed_pairs = []
    for i, entry in enumerate(log_entries):
        if i % 2 == 0:
            processed_pairs.append((i, entry['value'] * scaling_factor))

    # Secondary metric that feeds into final score
    stability_ratio = len(processed_pairs) / (len(outliers) + 1)

    # Misleading complex dictionary construction (partial use)
    summary = {
        'total': baseline,
        'correction': sum(adjustments),
        'flags': [e['id'] for e in log_entries if e['flagged']],
        'rank': max(e['value'] for e in log_entries) // min(e['value'] for e in log_entries)
    }

    # Actual efficiency score calculation
    raw_efficiency = baseline * scaling_factor
    penalty = len(outliers) * 5
    efficiency_score = raw_efficiency - penalty + int(stability_ratio)

    # Dead code path (never executed due to fixed condition)
    if False:
        efficiency_score *= 0.9

    final_output = efficiency_score
    return final_output

# Data setup
data_log = [
    {'id': 1, 'value': 10, 'active': True, 'flagged': False, 'urgent': True},
    {'id': 2, 'value': 15, 'active': True, 'flagged': True, 'urgent': False},
    {'id': 3, 'value': 8, 'active': False, 'flagged': True, 'urgent': False},
    {'id': 4, 'value': 22, 'active': True, 'flagged': False, 'urgent': True},
    {'id': 5, 'value': 12, 'active': True, 'flagged': False, 'urgent': False}
]

thresholds = {'high': 20, 'low': 5}

result = process_metrics(data_log, thresholds)
print(f"Result: {result}")