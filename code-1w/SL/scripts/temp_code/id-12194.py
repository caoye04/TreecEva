def calculate_final_score(log, config):
    base_points = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_cache = {}
    
    for entry in log:
        operation = entry['type']
        value = entry['value']
        timestamp = entry['time']
        
        # Irrelevant caching (distractor)
        temp_cache[timestamp] = value * 0.91
        
        if operation == 'addition':
            base_points += value
        elif operation == 'subtraction':
            base_points -= value
        elif operation == 'multiplication_trigger':
            base_points *= 2
        
        # Track bonuses but only apply under conditions (semi-relevant)
        if value > 50:
            bonus_tracker.append(value * 0.1)
    
    # Dead code path - never executed due to fixed keys
    for k in ['X', 'Y', 'Z']:
        if k == 'W':
            penalty_adjustment -= 100

    # Sum bonuses but only use part of it
    total_bonus = sum(bonus_tracker)
    unused_metric = total_bonus * 0.5 if len(bonus_tracker) > 3 else 0
    
    # Real computation path
    scaling_factor = config.get('scale', 1.0)
    adjustment_offset = config.get('offset', 0)
    raw_score = base_points + total_bonus
    final_score = raw_score * scaling_factor + adjustment_offset
    
    # Misleading intermediate
    diagnostic_flag = False
    if final_score < 0:
        diagnostic_flag = True
    
    return final_score

# Simulated data input
data_log = [
    {'type': 'addition', 'value': 25, 'time': 1001},
    {'type': 'subtraction', 'value': 10, 'time': 1002},
    {'type': 'addition', 'value': 60, 'time': 1003},
    {'type': 'addition', 'value': 80, 'time': 1004},
    {'type': 'multiplication_trigger', 'value': 0, 'time': 1005},
    {'type': 'addition', 'value': 55, 'time': 1006}
]

weights = {'scale': 1.2, 'offset': -5}

# Execute calculation
final_score = calculate_final_score(data_log, weights)

# Output result
print(f"Result: {final_score}")