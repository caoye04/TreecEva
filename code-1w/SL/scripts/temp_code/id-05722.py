def analyze_performance(raw_data, threshold=0.75):
    total_points = 0
    bonus_awarded = False
    temp_buffer = []
    cumulative_shift = 0

    for entry in raw_data:
        if entry.get('active'):
            base_value = entry['value'] * entry['weight']
            adjusted_value = base_value * (1.2 if entry['priority'] > 1 else 1.0)
            
            # Irrelevant transformation
            temp_buffer.append(adjusted_value * 0.95)
            
            total_points += adjusted_value
            
            if adjusted_value > 50 and not bonus_awarded:
                total_points += 10
                bonus_awarded = True

    # Dead code: never used beyond this
    if len(temp_buffer) > 5:
        moving_avg = sum(temp_buffer[-3:]) / 3
        cumulative_shift = int(moving_avg % 7)

    # Distractor computation
    hypothetical_max = len(raw_data) * 120 * 1.2
    efficiency_ratio = total_points / hypothetical_max if hypothetical_max > 0 else 0

    # Normalization step
    normalized_total = (total_points / 100.0) * 1.1
    
    # Secondary logic path with conditional expression
    baseline_rating = 45 if efficiency_ratio < threshold else 65
    
    # Key statement
    final_score = max(normalized_total, baseline_rating)
    
    # Additional irrelevant tracking
    audit_log = {'entries_processed': len(raw_data), 'shift': cumulative_shift}
    
    print(f"Result: {final_score}")

# Input data
data = [
    {'value': 30, 'weight': 1.5, 'priority': 2, 'active': True},
    {'value': 25, 'weight': 2.0, 'priority': 1, 'active': True},
    {'value': 40, 'weight': 1.0, 'priority': 3, 'active': True},
    {'value': 10, 'weight': 1.0, 'priority': 1, 'active': False},
    {'value': 55, 'weight': 1.2, 'priority': 2, 'active': True},
    {'value': 20, 'weight': 1.8, 'priority': 1, 'active': True}
]

analyze_performance(data)