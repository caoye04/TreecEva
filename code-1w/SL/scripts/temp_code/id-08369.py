def evaluate_performance(data):
    base_score = 0
    penalty_adjustment = 0.0
    bonus_multiplier = 1.0
    temp_result = 0
    intermediate_values = []

    for entry in data:
        raw_value = entry['value']
        weight = entry['weight']
        category = entry['category']

        if category == 'primary':
            if raw_value > 80:
                base_score += raw_value * weight
                intermediate_values.append(raw_value * weight)
            else:
                base_score -= 5 * weight
        elif category == 'secondary':
            adjusted = raw_value - (10 if raw_value > 50 else 0)
            temp_result += adjusted * 0.5

    # Distractor: complex-looking but unused calculation
    outlier_count = sum(1 for v in intermediate_values if v > 200)
    hypothetical_max = len(data) * 100 * 1.5
    efficiency_ratio = hypothetical_max / (sum(intermediate_values) + 1) if intermediate_values else 0

    # Real logic continues
    if base_score >= 300:
        bonus_multiplier = 1.2
    elif base_score >= 200:
        bonus_multiplier = 1.1

    stability_check = len([x for x in data if x['value'] > 90])
    if stability_check < 2:
        penalty_adjustment = -15

    final_score = int((base_score * bonus_multiplier) + penalty_adjustment)

    # Additional red herring variables
    normalized_score = final_score / hypothetical_max if hypothetical_max > 0 else 0
    trend_projection = [final_score + i*5 for i in range(3)]

    return final_score

# Main execution
metric_data = [
    {'value': 85, 'weight': 2, 'category': 'primary'},
    {'value': 92, 'weight': 3, 'category': 'primary'},
    {'value': 78, 'weight': 1, 'category': 'primary'},
    {'value': 65, 'weight': 2, 'category': 'secondary'},
    {'value': 88, 'weight': 1, 'category': 'primary'},
    {'value': 45, 'weight': 3, 'category': 'secondary'}
]

result_tracker = {}
execution_time_ms = 127
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")