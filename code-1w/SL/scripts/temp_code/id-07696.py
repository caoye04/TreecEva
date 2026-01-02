def process_results(data, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    temp_offset = 0

    # Irrelevant initialization (distractor)
    debug_trace = [0] * len(data)
    snapshot_log = []

    for i, record in enumerate(data):
        # Extract values with meaningful computation
        raw_value = record['metric_a'] * importance_weights[i]
        bonus = record['metric_b'] ** 0.5 if record['metric_b'] > 10 else 0

        # Conditional adjustment with side tracking (semi-relevant)
        if raw_value > 50:
            penalty_adjustment -= 3
            temp_offset += 2
        elif raw_value < 20:
            temp_offset -= 1

        # Core accumulation
        base_score += raw_value + bonus

        # Dead code path (distractor)
        if False:
            snapshot_log.append(f"Skipped: {raw_value}")

    # Use of lambda for filtering valid high performers (relevant)
    valid_high = list(filter(lambda x: x['metric_a'] > 40, data))
    bonus_multiplier = len(valid_high) * 1.5 if valid_high else 1.0

    # String-based flag processing (irrelevant but plausible)
    status_flags = [r.get('status', '').upper() for r in data]
    critical_count = sum(1 for f in status_flags if 'CRITICAL' in f)
    temp_offset -= critical_count  # Minor interference

    # Core result calculation
    final_score = int((base_score + penalty_adjustment) * bonus_multiplier)

    # Extra unused transformation (distractor)
    normalized = [round(v / sum(importance_weights), 4) for v in importance_weights]

    return final_score

# Input setup
evaluation_data = [
    {'metric_a': 45, 'metric_b': 16, 'status': 'active'},
    {'metric_a': 18, 'metric_b': 25, 'status': 'warning'},
    {'metric_a': 52, 'metric_b': 8, 'status': 'critical'},
    {'metric_a': 33, 'metric_b': 36, 'status': 'normal'}
]
weights = [0.8, 1.2, 1.5, 0.9]

# Execution
final_score = process_results(evaluation_data, weights)
print(f"Result: {final_score}")