def calculate_final_metric(scores_data):
    # Process scores with lambda functions and filtering
    base_scores = [x['value'] for x in scores_data if x.get('active', False)]
    processed_scores = list(map(lambda x: x * 2 - 5, base_scores))
    
    # Distractor operations that don't affect final result
    temp_max = max(processed_scores) if processed_scores else 0
    temp_min = min(processed_scores) if processed_scores else 0
    range_diff = temp_max - temp_min  # Unused variable
    
    # Calculate weighted sum with intermediate steps
    weights = [0.3, 0.5, 0.2]
    weighted_sum = sum(score * weight for score, weight in zip(processed_scores[:3], weights))
    
    # Additional unused calculation for distraction
    alternate_sum = sum(processed_scores) * 0.4
    
    # Final metric calculation
    adjustment_factor = 1.25
    final_result = weighted_sum * adjustment_factor
    
    return final_result

# Sample data
scores_data = [
    {'value': 15, 'active': True},
    {'value': 22, 'active': True},
    {'value': 18, 'active': True},
    {'value': 25, 'active': False},
    {'value': 19, 'active': True}
]

final_metric = calculate_final_metric(scores_data)
print(f"Result: {final_metric}")