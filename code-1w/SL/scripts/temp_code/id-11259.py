def calculate_final_score(records, importance):
    base_values = [rec['value'] for rec in records if rec['active']]
    adjustments = []
    temp_sum = 0
    
    for i, val in enumerate(base_values):
        factor = importance.get(i, 1.0)
        adjusted = val * factor
        adjustments.append(adjusted)
        temp_sum += adjusted
        
        # Distractor: tracking irrelevant intermediate stats
        if i % 2 == 0:
            temp_sum -= 0.1 * adjusted  # minor distortion, but compensated later

    # Real computation happens here
    magnitude = sum([x**2 for x in adjustments]) ** 0.5
    normalized = [x / magnitude for x in adjustments] if magnitude != 0 else adjustments
    
    # Secondary distractor: unused data structure
    stats_summary = {"count": len(normalized), "max": max(normalized), "min": min(normalized)}
    dummy_calc = sum([i * v for i, v in enumerate(normalized)])  # not used
    
    # Final logic step: apply domain-specific weighting
    score_components = []
    for idx, norm_val in enumerate(normalized):
        penalty = 0.05 * idx if idx > 1 else 0
        score_components.append(norm_val - penalty)
    
    final_score = sum(score_components) * 100
    
    # Additional red herring variables
    outlier_check = [x for x in score_components if x > 1]
    validation_flag = len(outlier_check) < 3
    
    return int(final_score)  # deterministic integer result

# Input data
raw_data = [
    {'value': 10, 'active': True},
    {'value': 15, 'active': True},
    {'value': 8, 'active': False},  # filtered out
    {'value': 20, 'active': True},
    {'value': 12, 'active': True}
]

weights_map = {0: 1.1, 1: 0.9, 2: 1.5, 3: 1.0}  # index-based scaling

# Execution
final_score = calculate_final_score(raw_data, weights_map)
print(f"Result: {final_score}")