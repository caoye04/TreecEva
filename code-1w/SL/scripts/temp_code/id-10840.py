def process_results(data, importance):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_sum = 0

    for entry in data:
        category = entry['type']
        value = entry['value']
        status = entry['status']

        if category == 'primary':
            base_score += value * importance['primary']
            if status == 'verified':
                bonus_tracker.append(value * 0.1)
        elif category == 'secondary':
            temp_sum += value
            if value > 50:
                penalty_adjustment -= 5

    # Irrelevant aggregation (distractor)
    avg_temp = temp_sum / len([e for e in data if e['type'] == 'secondary']) if temp_sum > 0 else 0
    decay_factor = lambda x: x * 0.95 ** len(bonus_tracker)

    intermediate_result = base_score + sum(bonus_tracker)
    
    # Dummy dictionary operations (distractor)
    stats = {
        'count': len(data),
        'bonus_count': len(bonus_tracker),
        'average_secondary': avg_temp,
        'decay_influence': decay_factor(intermediate_result)
    }

    # Actual final computation
    final_score = intermediate_result + penalty_adjustment

    # Dead code path (misleading)
    if stats['average_secondary'] < 0:
        final_score *= 1.1

    return final_score

# Input data
user_data = [
    {'type': 'primary', 'value': 80, 'status': 'verified'},
    {'type': 'primary', 'value': 70, 'status': 'pending'},
    {'type': 'secondary', 'value': 60, 'status': 'verified'},
    {'type': 'secondary', 'value': 45, 'status': 'verified'},
    {'type': 'primary', 'value': 90, 'status': 'verified'}
]

weights = {
    'primary': 1.2,
    'secondary': 0.8
}

# Execution
final_score = process_results(user_data, weights)
print(f"Result: {final_score}")