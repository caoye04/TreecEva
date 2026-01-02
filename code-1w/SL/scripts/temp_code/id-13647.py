from itertools import combinations

# Simulate a ranked voting system where candidates receive scores from judges
# Some calculations are red herrings (e.g., average_deviation, redundant_combinations)

def main():
    # Raw judge rankings for 4 candidates: A, B, C, D
    rankings = [4, 3, 1, 2]  # Candidate C ranked highest (1), then D (2), B (3), A (4)
    
    # Weight vector reflecting judge bias toward early candidates
    weights = [0.1, 0.2, 0.4, 0.3]
    
    # Misleading intermediate stats
    total_rankings = sum(rankings)
    avg_ranking = total_rankings / len(rankings)
    ranking_variance = sum((r - avg_ranking) ** 2 for r in rankings) / len(rankings)
    average_deviation = sum(abs(r - avg_ranking) for r in rankings) / len(rankings)

    # Dummy combinatorial analysis – not used in final score
    redundant_combinations = []
    for r in range(2, len(rankings)):
        for combo in combinations(rankings, r):
            if sum(combo) > avg_ranking * r:
                redundant_combinations.append(combo)

    # Real scoring logic: weighted harmonic mean of inverse ranks (higher rank = lower number)
    def weighted_harmonic_mean(ranks, wts):
        if len(ranks) != len(wts):
            raise ValueError("Length mismatch")
        
        # Invert ranks so higher rank value = better performance
        inverted_ranks = [1 / r for r in ranks]
        numerator = sum(w * ir for w, ir in zip(wts, inverted_ranks))
        denominator = sum(wts)
        return numerator / denominator
    
    # Secondary metric: consistency bonus if top two are close in weight impact
    weighted_impact = [w * r for w, r in zip(weights, rankings)]
    max_impact = max(weighted_impact)
    second_max_impact = sorted(weighted_impact)[-2]
    
    consistency_bonus = 0
    if abs(max_impact - second_max_impact) < 0.5:
        consistency_bonus = 1.5
    
    # Final score calculation
    base_score = weighted_harmonic_mean(rankings, weights)
    adjustment_factor = 1 + (0.1 * consistency_bonus)
    
    # Apply adjustment and round to nearest integer
    final_score = int(round(base_score * adjustment_factor))
    
    # Debug printouts (not affecting logic)
    debug_values = {
        'inverted': [1/r for r in rankings],
        'base': base_score,
        'bonus': consistency_bonus,
        'adjusted': base_score * adjustment_factor
    }
    
    # Unused state tracking
    state_log = []
    for i, w in enumerate(weights):
        state_log.append(f'Judge {i}: applied')
    
    return final_score

# Execute
result = main()
print(f"Target result: {result}")