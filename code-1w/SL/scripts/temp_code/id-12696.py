from itertools import combinations

# Simulate a tournament ranking system with weighted scoring and tiebreakers
def calculate_final_score(ranks, coeffs):
    base_score = sum([100 // (r + 1) for r in ranks])
    
    # Irrelevant: Generate all possible rank pairs (distractor)
    pair_combinations = list(combinations(ranks, 2))
    unused_count = len(pair_combinations)
    
    # Apply weights with conditional scaling
    adjusted_weights = [w * 1.5 if w > 2 else w * 0.8 for w in coeffs]
    
    # Secondary score based on weight contribution
    weight_bonus = 0
    for i, w in enumerate(adjusted_weights):
        if i % 2 == 0:
            weight_bonus += w ** 2
        else:
            weight_bonus -= w

    # Tiebreaker logic using set operations
    unique_ranks = set(ranks)
    duplicate_penalty = 0
    if len(unique_ranks) < len(ranks):
        duplicate_penalty = -(len(ranks) - len(unique_ranks)) * 10

    # Main scoring logic
    multiplier = 2 if len(unique_ranks) > 3 else 1.5
    
    # Final composition
    raw_final = (base_score + weight_bonus) * multiplier + duplicate_penalty
    
    # Dead code: Unused normalization (red herring)
    max_possible = 400
    normalized = raw_final / max_possible if max_possible > 0 else 0
    
    # Actual answer computation
    final_score = int(raw_final)  # This is the key result
    return final_score

# Input data
rankings = [0, 2, 1, 3, 2]  # Ranks of participants (lower is better)
weights = [1, 3, 2, 4, 1]   # Importance coefficients for each event

# Misleading intermediate calculation
projected_outcome = sum(rankings) * sum(weights) // len(rankings)

# Key execution point
final_score = calculate_final_score(rankings, weights)

print(f"Result: {final_score}")