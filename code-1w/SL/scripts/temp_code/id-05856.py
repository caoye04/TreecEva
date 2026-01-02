def aggregate_performance(feedback_set, base_rating):
    adjustment_factor = 0.85
    volatility_index = 0.07
    scaling_constant = 1.2
    
    # Preliminary transformation (not directly used in final logic)
    transformed_ratings = [round(r * scaling_constant, 2) for r in feedback_set if r > 0]
    
    # Irrelevant filtering based on arbitrary threshold
    filtered_positive = [r for r in feedback_set if r >= 3]
    suppression_count = sum(1 for r in feedback_set if r < 2)
    
    # Key computation begins
    weighted_sum = 0
    weight_accum = 0
    
    for i, rating in enumerate(feedback_set):
        confidence = 1 + (0.1 * i)  # Increases with position
        if rating >= 4:
            contribution = rating * confidence * adjustment_factor
        elif rating == 3:
            contribution = rating * confidence * 0.9
        else:
            contribution = rating * 0.5  # Lower-rated items have diminished impact
        
        weighted_sum += contribution
        weight_accum += confidence if rating >= 3 else 0.5
    
    # Secondary metric (distractor)
    avg_transformed = sum(transformed_ratings) / len(transformed_ratings) if transformed_ratings else 0
    
    # Final score calculation using conditional expression
    normalized_score = weighted_sum / weight_accum if weight_accum != 0 else base_rating
    final_score = normalized_score if suppression_count < 3 else normalized_score * 0.9
    
    # Additional red herring: unused volatility adjustment
    adjusted_volatility = volatility_index * (max(feedback_set) - min(feedback_set))
    projected_stability = round(100 * (1 - adjusted_volatility), 1)
    
    return final_score

# Input data
feedback_set = [5, 4, 3, 5, 2, 4, 5]
base_rating = 3.5

# Execution point
final_score = aggregate_performance(feedback_set, base_rating)
print(f"Result: {final_score}")