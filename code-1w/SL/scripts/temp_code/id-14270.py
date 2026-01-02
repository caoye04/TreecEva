def calculate_final_score(ranks, coeffs):
    base_score = 0
    penalty = 0
    bonus = 0
    temp_sum = 0
    
    # Irrelevant pre-processing (distractor)
    normalized_ranks = [r / sum(ranks) for r in ranks]
    adjusted_coeffs = [c * 1.5 for c in coeffs]
    
    for idx, (rank, weight) in enumerate(zip(ranks, coeffs)):
        if rank <= 3:
            bonus += weight * 2
        else:
            penalty += rank // 2
        
        # Core scoring logic
        base_score += (idx + 1) * weight * (rank % 4)
        
        # Red herring computation (not used later)
        temp_sum += (rank ** 2) * weight

    # Additional distraction: unused helper calculation
    outlier_count = sum(1 for r in ranks if r > 5)
    scaling_factor = 1.0 if outlier_count < 3 else 0.8
    
    # Another irrelevant loop
    cumulative = 0
    for i in range(len(ranks)):
        cumulative += abs(ranks[i] - coeffs[i])

    # Actual result computation with subtle integer division and rounding
    intermediate = base_score - penalty + bonus
    final_score = int(intermediate // 1.5)  # Integer division affects outcome
    
    # Dead code path (never executed but adds confusion)
    if False:
        final_score *= 0.9
    
    return final_score

# Input data
rankings = [4, 2, 5, 1, 6]
weights = [3, 7, 2, 8, 4]

# Key execution point
final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")