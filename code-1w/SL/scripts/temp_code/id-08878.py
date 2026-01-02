def calculate_performance(data):
    base_score = 0
    penalty_offset = 0.0
    temp_adjustment = 0  # Irrelevant tracking

    for entry in data:
        raw_value = entry['metric'] * entry['weight']
        if entry['active']:
            base_score += raw_value
            
        # Distractor: temperature-like adjustment with no real effect
        temp_adjustment += (raw_value % 7) - 3
    
    # Conditional expression with slicing distraction
    bonus = 10 if len(data) > 3 else 5
    slice_shadow = data[1:3]  # Slicing used but not affecting logic
    
    # Simulated calibration (irrelevant)
    calibration_factor = 1.0
    for i in range(2):
        calibration_factor *= 0.95  # Predictable decay, unused later
    
    # Actual performance calculation
    stability_bonus = 0
    for i, entry in enumerate(data):
        if i % 2 == 0 and entry['weight'] > 1:
            stability_bonus += 2
    
    final_score = base_score + bonus + stability_bonus
    
    # Red herring variable
    debug_trace = {'base': base_score, 'bonus_applied': bonus}
    
    return final_score

# Real data input
benchmark_data = [
    {'metric': 12, 'weight': 2, 'active': True},
    {'metric': 8,  'weight': 3, 'active': True},
    {'metric': 5,  'weight': 1, 'active': False},
    {'metric': 15, 'weight': 4, 'active': True}
]

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")