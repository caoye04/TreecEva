def calculate_final(data_map):
    # Preprocessing: filter valid entries based on criteria
    valid_items = [v for v in data_map.values() if v['status'] == 'active']
    
    # Irrelevant distraction: counting inactive items (not used later)
    inactive_count = sum(1 for v in data_map.values() if v['status'] == 'inactive')
    temp_sum = sum(item['value'] * 0.1 for item in data_map.values())  # Distractor calc

    # Compute base score using active items only
    base_scores = list(map(lambda x: x['value'] * x['weight'], valid_items))
    base_total = sum(base_scores)

    # Apply bonus logic based on count
    bonus = 0
    if len(valid_items) > 3:
        bonus = 10
    elif len(valid_items) == 2:
        bonus = 5
    else:
        bonus = 2

    # Secondary processing: adjust for penalties
    penalties = []
    for item in valid_items:
        if item['value'] < 0:
            penalties.append(abs(item['value']) * 0.2)
    total_penalty = sum(penalties)

    # Red herring: unused transformation
    squared_values = [x['value']**2 for x in data_map.values() if x['value'] > 5]

    # Final aggregation
    adjustment_factor = 1.1 if base_total > 50 else 0.95
    intermediate = (base_total + bonus) * adjustment_factor
    final_score = intermediate - total_penalty

    # Debug line that doesn't affect result
    debug_info = {'base': base_total, 'bonus': bonus, 'penalty': total_penalty}
    
    return final_score

# Data setup
config_data = {
    'A': {'value': 10, 'weight': 1.2, 'status': 'active'},
    'B': {'value': 8,  'weight': 1.5, 'status': 'active'},
    'C': {'value': 12, 'weight': 0.8, 'status': 'active'},
    'D': {'value': 5,  'weight': 2.0, 'status': 'inactive'},  # ignored
    'E': {'value': 15, 'weight': 0.7, 'status': 'active'},
    'F': {'value': -4, 'weight': 1.0, 'status': 'active'}   # triggers penalty
}

# Execution entry point
final_score = calculate_final(config_data)
print(f"Target result: {final_score}")