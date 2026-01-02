def calculate_final_score(records, importance):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    
    # Irrelevant preprocessing: normalize names (not used in score)
    normalized_names = [name.strip().title() for name in records.get('participants', [])]
    
    # Actual scoring logic
    raw_values = records.get('metrics', [])
    weights_list = importance.get('factors', [])
    
    temp_product = 1
    for i in range(len(raw_values)):
        if i % 2 == 0:
            base_score += raw_values[i] * weights_list[i]
            temp_product *= raw_values[i]
        else:
            # Misleading branching: temp_product is never used
            if raw_values[i] > 50:
                penalty_adjustment -= 5
            else:
                penalty_adjustment -= 2
    
    # Dummy dictionary for distraction
    stats_summary = {
        'max_value': max(raw_values, default=0),
        'min_value': min(raw_values, default=0),
        'product_trace': temp_product  # Computed but unused
    }
    
    # Bonus logic based on count of high performers
    high_performers = [val for val in raw_values if val >= 75]
    if len(high_performers) >= 3:
        bonus_tracker.append(15)
    elif len(high_performers) >= 1:
        bonus_tracker.append(5)
    
    # Final computation
    final_score = base_score + penalty_adjustment + sum(bonus_tracker)
    
    # Dead code: this block doesn't affect anything
    if final_score < 0:
        final_score = 0
    
    return final_score

# Input data
experiment_data = {
    'participants': [' alice ', 'bob', 'charlie ', 'diana'],
    'metrics': [88, 45, 76, 82, 91, 67]
}

weights_config = {
    'factors': [1.2, 0.8, 1.5, 1.0, 1.3, 0.9]
}

# Execution point
final_score = calculate_final_score(experiment_data, weights_config)
print(f"Target result: {final_score}")