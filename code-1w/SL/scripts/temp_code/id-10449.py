def calculate_final_score(ranks, multiplier):
    base_points = 100
    penalty = 0
    temp_adjustment = 0  # Irrelevant tracking variable

    # Simulate some noise calculations
    for i in range(len(ranks)):
        if ranks[i] < 5:
            temp_adjustment += 2  # Distractor: not used later

    # Real computation begins
    filtered_ranks = [r for r in ranks if r <= 10]  # List comprehension: relevant
    rank_sum = sum(filtered_ranks)

    # Additional irrelevant computation
    average_rank = rank_sum / len(filtered_ranks) if filtered_ranks else 0
    deviation_score = 0
    for r in filtered_ranks:
        deviation_score += (r - average_rank) ** 2  # Computed but unused

    # Core logic with intermediate distractors
    scaling_factor = 1.5 if len(filtered_ranks) > 6 else 1.2
    adjusted_base = base_points * scaling_factor

    # Bonus logic with red herring condition
    extra_bonus = 0
    if len(ranks) % 2 == 0 and len(ranks) > 0:
        extra_bonus = 10  # Never actually added to final score

    raw_score = adjusted_base - (rank_sum // 2)
    
    # Final computation
    final_score = raw_score * multiplier

    # Print result as required
    return final_score

# Main execution
if __name__ == '__main__':
    player_ranks = [3, 7, 1, 12, 4, 6, 8, 15, 2]
    bonus_multiplier = 1.1
    debug_stats = [x**2 for x in player_ranks if x > 10]  # Dead-end list comp
    temp_cache = {'max': max(player_ranks), 'min': min(player_ranks)}  # Unused dict

    final_score = calculate_final_score(player_ranks, bonus_multiplier)
    print(f"Target result: {final_score}")