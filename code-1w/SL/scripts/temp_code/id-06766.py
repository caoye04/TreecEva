def analyze_competition_results():
    # Simulated competition data: participant rankings across multiple events
    rankings = [3, 1, 4, 2, 5]
    weights = [0.1, 0.2, 0.3, 0.25, 0.15]

    # Irrelevant intermediate calculation: average rank (not used in final score)
    total_rank = sum(rankings)
    avg_rank = total_rank / len(rankings)
    normalized_ranks = [r / max(rankings) for r in rankings]

    # Misleading transformation: inverted ranks with offset (dead computation)
    inverted_ranks = [6 - r for r in rankings]
    offset_correction = 0.5
    adjusted_inverted = [ir + offset_correction for ir in inverted_ranks]

    # Auxiliary function to compute weighted performance score
    def calculate_weighted_penalty(ranks, wts):
        penalty = 0
        for i, (rank, weight) in enumerate(zip(ranks, wts)):
            if rank <= 2:
                bonus_factor = 0.9
            else:
                bonus_factor = 1.1
            penalty += rank * weight * bonus_factor
        return penalty

    # Another red herring: sort and reindex using enumerate (not impacting final result)
    sorted_with_index = list(enumerate(sorted(rankings, reverse=True)))
    index_map = {val: idx for idx, val in sorted_with_index}
    position_shift = sum([i - index_map[r] for i, r in enumerate(rankings)])

    # Core logic: calculate final score based on adjusted weighted sum
    base_penalty = calculate_weighted_penalty(rankings, weights)

    # Additional adjustment based on rank stability (uses enumerate over zip)
    stability_adjustment = 0
    for idx, (a, b) in enumerate(zip(rankings, rankings[1:])):
        if abs(a - b) > 1:
            stability_adjustment += 0.05

    # Final score computed from meaningful and slightly modified components
    final_score = (base_penalty - stability_adjustment) * (1 + 0.01 * position_shift)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Execute function
analyze_competition_results()