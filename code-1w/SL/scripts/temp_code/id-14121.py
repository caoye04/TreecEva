def calculate_final_score(records, importance_weights):
    base_score = 0
    adjustment_factor = 0.0
    temp_result = []
    
    # Irrelevant pre-processing: reverse and slice (distractor)
    reversed_names = [name[::-1] for name in ['Alice', 'Bob', 'Charlie']]
    truncated_list = reversed_names[1:3]
    
    # Actual computation begins
    for i in range(len(records)):
        entry = records[i]
        weight = importance_weights.get(i, 0.5)
        raw_value = entry['value'] * weight
        
        if entry['active']:
            if raw_value > 10:
                base_score += int(raw_value // 2)
            else:
                base_score += int(raw_value)
        
        # Dead code path - never executed due to logic, but looks relevant
        if entry['value'] < 0:
            adjustment_factor += 0.1  # This will not affect anything
    
    # Slicing operation on intermediate result (semi-relevant)
    if len(temp_result) > 2:
        temp_result = temp_result[:2]
    
    # Dictionary-based bonus calculation
    category_bonus = {'A': 5, 'B': 3, 'C': 1}
    bonus_key = records[0].get('category', 'C')
    bonus_score = category_bonus.get(bonus_key, 0)
    
    # Final score with red herring variables
    scaling_factor = 1.0  # Unused distraction
    offset_correction = -2  # Another misleading term not used
    final_score = base_score + bonus_score
    
    return final_score

# Main data setup
user_data = [
    {'value': 12, 'active': True, 'category': 'A'},
    {'value': 8, 'active': True, 'category': 'B'},
    {'value': 15, 'active': False, 'category': 'C'},
    {'value': 6, 'active': True, 'category': 'D'}
]

weights_map = {0: 1.2, 1: 0.8, 2: 1.5, 4: 2.0}  # Note: index 3 missing intentionally

# Execute main logic
final_score = calculate_final_score(user_data, weights_map)

# Print result as required
print(f"Result: {final_score}")