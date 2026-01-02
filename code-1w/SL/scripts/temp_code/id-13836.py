def calculate_final_score(ranks, coeffs):
    # Initialize various tracking variables (some are distractions)
    total_contributions = []
    normalization_factor = sum(1 << i for i in range(len(coeffs)))  # Irrelevant bit-shift calc
    scaling_offset = len(ranks) * 0.5
    
    temp_adjustments = {i: val ** 0.5 for i, val in enumerate(coeffs)}  # Distractor dict
    
    # Core logic with meaningful computation
    weighted_sum = 0
    weight_magnitude = sum(abs(w) for w in coeffs)
    
    for idx, (rank, weight) in enumerate(zip(ranks, coeffs)):
        contribution = (1 / (rank + 1)) * weight
        if contribution > 0:
            adjusted_contribution = contribution * (idx % 3 + 1)
        else:
            adjusted_contribution = contribution
        weighted_sum += adjusted_contribution
    
    # Additional red herring using dictionary operations
    stats_summary = {
        'max_rank': max(ranks),
        'min_weight': min(coeffs),
        'count_high_rank': len([r for r in ranks if r < 2]),
        'dummy_metric': sum(temp_adjustments.values())  # Unused
    }
    
    # Final calculation - only this matters
    final_score = round(weighted_sum / (weight_magnitude or 1) * 100, 4)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
rankings = [0, 2, 1, 3, 0]
weights = [1.2, -0.8, 1.5, 0.3, -1.0]

# Dead code path (never executed but looks relevant)
def legacy_scoring(seq):  
    return sum(x * x for x in seq)

# Key execution point
final_score = calculate_final_score(rankings, weights)