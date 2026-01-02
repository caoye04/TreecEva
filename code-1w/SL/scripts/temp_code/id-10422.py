def calculate_final_score(records, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    
    # Irrelevant pre-processing: normalizing weights (not actually used)
    normalized_weights = [w / sum(importance_weights) for w in importance_weights]
    temp_result = 0
    for idx, weight in enumerate(importance_weights):
        temp_result += weight * idx  # Distractor computation
    
    # Core logic: score calculation with conditional adjustments
    for record in records:
        category = record['type']
        value = record['value']
        if category == 'A':
            base_score += value * 3
            if value > 10:
                penalty_adjustment -= 2
        elif category == 'B':
            base_score += value * 2
            bonus_tracker.append(value)
        elif category == 'C':
            base_score += value
            if value % 4 == 0:
                penalty_adjustment += 1
    
    # Secondary adjustment using lambda (required feature)
    apply_multiplier = lambda x, m: x * m if x > 0 else 0
    adjusted_bonus = sum(apply_multiplier(b, 1.5) for b in bonus_tracker)
    
    # Misleading complex expression that doesn't affect final result
    outlier_check = [v for v in records if v['value'] > 100]
    safety_offset = len(outlier_check) * -5  # Dead code path: never applied
    
    # Final composition
    stability_factor = len(records) // 2
    final_score = base_score + penalty_adjustment + int(adjusted_bonus) + stability_factor
    
    return final_score

# Input data
input_records = [
    {'type': 'A', 'value': 12},
    {'type': 'B', 'value': 8},
    {'type': 'A', 'value': 5},
    {'type': 'C', 'value': 16},
    {'type': 'B', 'value': 3}
]

weights = [4, 2, 5, 1]  # Used only for distraction

# Execution point
final_score = calculate_final_score(input_records, weights)
print(f"Result: {final_score}")