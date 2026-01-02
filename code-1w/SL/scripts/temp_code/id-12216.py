def calculate_performance_rating():
    # Simulate employee performance evaluation across multiple metrics
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    
    # Irrelevant distraction: unused variable and dead computation
    temp_multiplier = 1.05
    adjusted_base = [score * 1.02 for score in base_scores]  # Not used later
    
    weighted_sum = 0.0
    total_weight = 0.0
    
    for i, (score, weight) in enumerate(zip(base_scores, weights)):
        if i % 2 == 0:
            bonus = 2.0 if score >= 80 else 0.0
        else:
            bonus = -1.0 if score < 85 else 0.0
        
        # Apply conditional adjustment based on position and score
        adjusted_score = score + bonus
        weighted_sum += adjusted_score * weight
        total_weight += weight

    # Distractor block: computes something irrelevant
    outlier_count = 0
    for idx, val in enumerate(base_scores):
        if abs(val - 85) > 10:
            outlier_count += 1
    avg_deviation = sum(abs(s - 85) for s in base_scores) / len(base_scores)  # Unused

    # Simulate tier-based performance classification
    if weighted_sum >= 85:
        tier_bonus = 5.0
    elif weighted_sum >= 75:
        tier_bonus = 2.5
    else:
        tier_bonus = 0.0

    # Final calculation with distractor variables not affecting outcome
    raw_score = weighted_sum  # Already computed correctly
    scaling_factor = 1.0  # Placeholder for potential extension (not used)
    final_score = raw_score + tier_bonus

    return final_score

# Execute and print result
target_result = calculate_performance_rating()
print(f"Result: {target_result}")