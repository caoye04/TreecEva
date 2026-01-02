def calculate_final_score(records, importance):
    base_score = 0
    adjustment_factor = 0.0
    temp_result = []
    outlier_count = 0

    for record in records:
        raw_value = record.get('value', 0)
        category = record.get('type', 'unknown')
        
        # Irrelevant computation - distractor
        squared_sum = raw_value ** 2 + 3  
        temp_result.append(squared_sum)
        
        if raw_value > 100 or raw_value < 0:
            outlier_count += 1
            continue

        if category == 'critical':
            base_score += raw_value * 1.5
        elif category == 'standard':
            base_score += raw_value
        else:
            base_score += raw_value * 0.8

    # Dead code path - misleading
    if outlier_count == 0:
        adjustment_factor = 1.1
    elif outlier_count > 5:
        adjustment_factor = 0.7
    else:
        adjustment_factor = 0.9

    # Unused helper list - distractor
    processed_flags = [True if x > 50 else False for x in temp_result]

    # Actual logic: apply weight multipliers from dictionary
    multiplier = 0.0
    for key, weight in importance.items():
        if key == 'precision':
            multiplier += weight * 0.3
        elif key == 'coverage':
            multiplier += weight * 0.4
        elif key == 'timeliness':
            multiplier += weight * 0.3

    # Final score depends only on base_score and multiplier
    final_score = base_score * (1 + multiplier)

    # Additional red herring calculation
    average_temp = sum(temp_result) / len(temp_result) if temp_result else 0
    decay_correction = average_temp * 0.05  # Not used

    return int(final_score)

# Input data
data = [
    {'value': 85, 'type': 'critical'},
    {'value': 40, 'type': 'standard'},
    {'value': 70, 'type': 'enhanced'},
    {'value': 90, 'type': 'critical'},
    {'value': 55, 'type': 'standard'},
    {'value': 105, 'type': 'standard'},  # outlier
    {'value': 60, 'type': 'enhanced'}
]

weights = {
    'precision': 0.8,
    'coverage': 0.9,
    'timeliness': 0.7
}

final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")