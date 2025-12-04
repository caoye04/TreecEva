def calculate_performance(data):
    temp_sum = sum(data.values())
    irrelevant_counter = len([x for x in data if x.startswith('x')])
    
    # Distractor calculations
    fake_average = temp_sum / max(len(data), 1) * 2.5
    offset_value = (temp_sum % 7) * 3.14
    
    processed = []
    for key, value in data.items():
        if key.endswith('_score'):
            processed.append(value * 0.8)
        elif 'metric' in key:
            processed.append(value + 5)
        else:
            # Dead code path
            processed.append(value - irrelevant_counter)
    
    # Misleading intermediate
    intermediate = sum(processed) + offset_value
    
    # Actual relevant calculation
    relevant_scores = [v for k, v in data.items() if k.endswith('_score')]
    weighted_sum = sum(relevant_scores) * 1.2
    
    bonus = len([k for k in data if 'bonus' in k.lower()]) * 15
    penalty = (intermediate - weighted_sum) % 10
    
    result = weighted_sum + bonus - penalty
    return int(result)

metrics = {
    'response_score': 85,
    'accuracy_score': 92,
    'speed_metric': 78,
    'quality_score': 88,
    'bonus_efficiency': 10,
    'x_factor': 5,
    'irrelevant_data': 42
}

# Distractor variables
fake_result = calculate_performance({'test': 100})
temp_calc = (fake_result * 3) // 2
unused_var = temp_calc + metrics['x_factor']

final_score = calculate_performance(metrics)
print(f"Result: {final_score}")