def calculate_performance_rating():
    base_values = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    
    # Normalize base values to a 0-1 scale
    normalized = [val / 100 for val in base_values]
    
    # Use enumerate and weighted sum via zip
    weighted_sum = 0
    for i, (norm_val, weight) in enumerate(zip(normalized, weights)):
        weighted_sum += norm_val * weight
    
    # Apply performance bonus if above threshold
    if weighted_sum > 0.85:
        bonus = 0.05
    else:
        bonus = 0.02
    
    final_score = int((weighted_sum + bonus) * 100)
    
    # Irrelevant auxiliary variable (minimal distraction)
    temp_debug_log = f'Raw: {weighted_sum}, Bonus: {bonus}'
    
    return final_score

result = calculate_performance_rating()
print(f"Result: {result}")