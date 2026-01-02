def evaluate_performance(raw_scores, threshold=65):
    # Normalize scores by subtracting the threshold and taking absolute distance
    adjusted_scores = [abs(score - threshold) for score in raw_scores]
    
    # Determine which scores are above threshold (bonus points)
    bonus_eligible = {score for score in raw_scores if score >= threshold}
    bonus_points = len(bonus_eligible) * 2
    
    # Apply non-linear transformation to adjusted scores
    transformed = [100 / (1 + adjusted) for adjusted in adjusted_scores]
    
    # Create a set of normalized scores and add bonus points to each
    normalized_set = {t + bonus_points for t in transformed}
    
    # Irrelevant tracking variable (minimal distraction)
    processed_count = len(raw_scores)
    
    final_score = max(normalized_set)
    return final_score

result = evaluate_performance([78, 54, 82, 69, 43])
print(f"Result: {result}")