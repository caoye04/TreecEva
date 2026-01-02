def process_results(records, importance_map):
    temp_data = []
    total_weight = sum(importance_map.values())
    normalized_weights = {k: v / total_weight for k, v in importance_map.items()}

    # Irrelevant pre-processing: string cleaning
    clean_records = []
    for record in records:
        cleaned = {key.strip().lower(): val for key, val in record.items()}
        clean_records.append(cleaned)

    # Distractor: unused lambda
    transform = lambda x: x ** 2 + 1

    intermediate_sum = 0.0
    weight_contribution = 0.0

    for entry in clean_records:
        category = entry.get('type', 'unknown')
        if category in normalized_weights:
            raw_value = entry.get('value', 0)
            # Actual logic step
            intermediate_sum += raw_value * normalized_weights[category]
            weight_contribution += normalized_weights[category]

    # More distraction: dead code path with string method usage
    status_flags = [r.get('status', '') for r in records]
    active_count = len([s for s in status_flags if s.lower().startswith('act')])
    unused_flag_summary = ''.join(sorted(set(flag[0] for flag in status_flags if flag)))

    # Unused accumulation with set
    unique_types = set()
    for r in records:
        unique_types.add(r.get('type', 'default').upper())

    # Final computation – only this matters
    final_score = intermediate_sum / weight_contribution if weight_contribution != 0 else 0
    return final_score

# Input data
assessments = [
    {'type': 'accuracy',   'value': 85, 'status': 'active'},
    {'type': 'efficiency', 'value': 90, 'status': 'inactive'},
    {'type': 'accuracy',   'value': 95, 'status': 'active_pending'},
    {'type': 'scalability','value': 70, 'status': 'disabled'}
]

weights = {
    'accuracy':   3,
    'efficiency': 2,
    'scalability': 1
}

# Execution point
final_score = process_results(assessments, weights)
print(f"Result: {final_score}")