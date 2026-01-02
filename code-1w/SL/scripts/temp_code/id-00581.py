def calculate_final_score(data, weights):
    base_score = 0
    penalty = 0
    temp_result = []
    
    # Irrelevant pre-processing (distractor)
    normalized_data = {k: v / sum(data.values()) for k, v in data.items()}
    
    for key, value in data.items():
        if value > 10:
            base_score += value * 2
        elif value > 5:
            base_score += value
        else:
            penalty += 1

    # Semi-relevant transformation
    adjusted_weights = {}
    total_weight = sum(weights.values())
    for k, v in weights.items():
        adjusted_weights[k] = v / total_weight

    # Complex but partially irrelevant aggregation
    weighted_sum = 0
    for category, weight in adjusted_weights.items():
        if category in data:
            weighted_sum += data[category] * weight
    
    # Secondary scoring logic with early termination
    if penalty >= 3:
        return -1  # Early exit not taken in this case
    
    multiplier = 1.0
    if len(data) > 4:
        multiplier = 1.2
    
    # Final computation chain
    raw_score = base_score - penalty
    scaled_score = raw_score * multiplier
    final_score = int(scaled_score + weighted_sum)

    # Dead code path (never reached due to above logic)
    if final_score < 0:
        final_score = 0

    return final_score

# Main execution
rank_data = {
    'alpha': 12,
    'beta': 8,
    'gamma': 15,
    'delta': 6,
    'epsilon': 9,
    'zeta': 4
}

bonus_weights = {
    'alpha': 3,
    'gamma': 5,
    'delta': 2,
    'eta': 4  # Not in rank_data, adds distraction
}

intermediate_total = sum(rank_data.values())  # Distractor computation
ignored_flag = False

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")