def calculate_final_score(scores, bonuses):
    base_total = sum(scores)
    bonus_multiplier = 1.0
    
    # Apply multiplier based on bonus conditions
    if len(bonuses) > 0 and bonuses[0] > 0:
        bonus_multiplier += 0.1
    
    # Use dictionary to map index to adjusted score
    adjusted_scores = {}
    for i, score in enumerate(scores):
        adjusted_scores[i] = score * (1 + 0.05 * (i < 3))
    
    # Slice first three scores for special consideration
    top_base_scores = sorted(scores, reverse=True)[:3]
    performance_boost = sum(top_base_scores) * 0.02
    
    intermediate_total = sum(adjusted_scores.values()) + performance_boost
    final_total = intermediate_total * bonus_multiplier
    
    return int(final_total)

# Input data
scores = [88, 92, 76, 94, 85]
bonuses = [10, 5]

# Calculation entry point
result = calculate_final_score(scores, bonuses)
print(f"Result: {result}")