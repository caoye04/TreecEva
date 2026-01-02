def calculate_performance_rating():
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    
    # Compute weighted score using lambda and zip
    weighted_components = list(map(lambda x: x[0] * x[1], zip(base_scores, weights)))
    raw_total = sum(weighted_components)
    
    # Adjustment factor based on team performance index
    team_index = 1.05
    adjusted_total = raw_total * team_index
    
    # Apply conditional bonus if above threshold
    bonus = 5 if adjusted_total >= 88 else 0
    final_score = adjusted_total + bonus
    
    # Irrelevant metrics (distractors for intervention level 5)
    avg_score = sum(base_scores) / len(base_scores)
    max_weight = max(weights)
    normalized = [round(s * w, 2) for s, w in zip(base_scores, weights)]
    
    return final_score

# Execute and print result
target_result = calculate_performance_rating()
print(f"Target result: {target_result}")