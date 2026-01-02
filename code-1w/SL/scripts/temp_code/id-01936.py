def calculate_performance(bonuses, weights):
    base_scores = {'speed': 85, 'accuracy': 92, 'consistency': 78}
    adjusted = {k: base_scores[k] * weights[k] for k in base_scores}
    
    # Apply bonus if condition met
    total_base = sum(adjusted.values())
    multiplier = bonuses['x2'] if total_base > 200 else bonuses['x1']
    
    # Secondary adjustment using lambda for dynamic threshold
    threshold_fn = lambda x: 1.15 if x < 90 else 1.05
    final_parts = [adjusted[k] * threshold_fn(base_scores[k]) for k in adjusted]
    
    raw_sum = sum(final_parts)
    final_score = raw_sum * multiplier
    return final_score

# Weight mapping for performance dimensions
level_weights = {'speed': 1.2, 'accuracy': 1.5, 'consistency': 0.8}

# Bonus map with scalar values
bonus_map = {'x1': 1.0, 'x2': 1.25}

# Execute calculation
final_score = calculate_performance(bonus_map, level_weights)
print(f"Result: {final_score}")