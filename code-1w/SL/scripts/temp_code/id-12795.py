def evaluate_performance(log, config):
    base_score = 0
    adjustments = []
    temp_result = 0

    # Irrelevant preprocessing: string manipulation distractor
    keys = list(config.keys())
    key_fragment = ''.join([k[1:3] for k in keys if len(k) > 2])
    hash_value = sum([ord(c) for c in key_fragment]) % 7

    # Semi-relevant data filtering
    threshold = config.get('threshold', 5)
    weight_factor = config['weights'][1]

    for entry in log:
        raw_value = entry['metric']
        category = entry['type']

        # Conditional branching with nested logic
        if category == 'execution':
            if raw_value > threshold:
                base_score += raw_value * weight_factor
            else:
                base_score += raw_value * 0.5
        elif category == 'latency':
            penalty = (raw_value // 10) * config['penalty']['base']
            base_score -= penalty if penalty < 15 else 10

        # Dead computation - collected but never used
        squared_dev = (raw_value - threshold) ** 2
        adjustments.append(squared_dev)

    # Distractor loop: computes unused metric
    cumulative = 0
    for i in range(len(log)):
        if i % 2 == 0:
            cumulative += len(str(log[i]['metric']))

    # Actual result computation
    multiplier = len(log) if base_score > 0 else 1
    temp_result = base_score * multiplier

    # Final adjustment using slicing and dictionary lookup
    recent_entries = log[-2:]
    recent_sum = sum([e['metric'] for e in recent_entries])
    final_score = int(temp_result + config['bonus'].get(recent_sum, 3))

    return final_score

# Setup input data
dataset_config = {
    'threshold': 4,
    'weights': [2, 3, 1],
    'penalty': {'base': 2},
    'bonus': {12: 5, 15: 8}
}

feedback_log = [
    {'metric': 6, 'type': 'execution'},
    {'metric': 7, 'type': 'latency'},
    {'metric': 5, 'type': 'execution'},
    {'metric': 8, 'type': 'execution'}
]

# Execute and print result
result_var = evaluate_performance(feedback_log, dataset_config)
print(f"Result: {result_var}")