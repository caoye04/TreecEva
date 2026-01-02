def calculate_final_score(records, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_sum = 0

    for record in records:
        if 'status' not in record or record['status'] != 'active':
            continue

        raw_value = record.get('value', 0)
        category = record.get('category', 'default')
        weight = importance_weights.get(category, 1.0)

        # Significant computation that feeds into final score
        contribution = raw_value * weight

        # Distractor: complex but unused tracking
        if raw_value > 100:
            penalty_adjustment += 5
            bonus_tracker.append(contribution * 0.1)
        elif raw_value < 0:
            penalty_adjustment -= 3

        # Conditional expression used meaningfully
        multiplier = 1.2 if record.get('priority', False) else 1.0
        base_score += contribution * multiplier

        # Irrelevant string processing (distractor)
        name = record.get('name', '')
        if name and name[0].isupper():
            temp_sum += len(name.split())

    # Dictionary operation to filter and scale
    valid_weights = {k: v for k, v in importance_weights.items() if v >= 0.5}
    scaling_factor = sum(valid_weights.values()) / len(valid_weights) if valid_weights else 1.0

    # Real accumulation logic
    scaled_score = base_score * scaling_factor

    # More distractions: dead code path (never executed due to logic above)
    outlier_count = 0
    for record in records:
        if record.get('value', 0) > 1000:
            outlier_count += 1  # Never reached due to data constraints

    # Final adjustment using list method (bonus_tracker is semi-relevant)
    final_bonus = sum(bonus_tracker) * 0.5 if bonus_tracker else 0.0

    # The actual answer is built here
    final_score = int(scaled_score + final_bonus - penalty_adjustment)

    return final_score

# Input data
entry_data = [
    {'name': 'Project Alpha', 'value': 85, 'category': 'research', 'status': 'active', 'priority': True},
    {'name': 'Beta Test', 'value': 120, 'category': 'testing', 'status': 'inactive'},
    {'name': 'gamma review', 'value': 200, 'category': 'research', 'status': 'active', 'priority': False},
    {'name': 'delta audit', 'value': -50, 'category': 'compliance', 'status': 'active'}
]

weights_map = {
    'research': 1.5,
    'testing': 1.1,
    'compliance': 0.8,
    'default': 1.0
}

# Execution point
final_score = calculate_final_score(entry_data, weights_map)
print(f"Result: {final_score}")