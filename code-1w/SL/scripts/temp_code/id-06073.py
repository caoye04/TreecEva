def calculate_final_score(ranks, weights):
    base_scores = {name: 100 - rank for name, rank in ranks.items()}
    
    # Normalize weights to sum to 1.0
    total_weight = sum(weights.values())
    normalized_weights = {k: v / total_weight for k, v in weights.items()}
    
    # Apply weighted adjustment only to top 3 ranked participants
    top_3_names = sorted(ranks, key=ranks.get)[:3]
    adjusted_scores = {}
    for name in base_scores:
        if name in top_3_names:
            adjusted_scores[name] = base_scores[name] * (1 + normalized_weights.get(name, 0.1))
        else:
            adjusted_scores[name] = base_scores[name]
    
    # Return the highest adjusted score
    return max(adjusted_scores.values())

# Data inputs
rank_data = {'alice': 1, 'bob': 3, 'charlie': 2, 'diana': 5, 'evan': 4}
bonus_weights = {'alice': 0.5, 'bob': 0.3, 'charlie': 0.2}  # Only top 3 are eligible

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Target result: {final_score}")