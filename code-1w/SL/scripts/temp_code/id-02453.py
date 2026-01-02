def calculate_final_score(ranks, weights):
    base_score = 0
    penalty_adjustment = 0
    temp_multiplier = 1.0
    rank_sum = sum(ranks)
    rank_count = len(ranks)
    
    # Irrelevant normalization (distractor)
    normalized_ranks = {i: ranks[i] / max(ranks) for i in range(len(ranks))}
    
    # Real logic starts: only entries with rank < 3 contribute
    for i, rank in enumerate(ranks):
        if rank < 3:
            base_score += weights.get(i, 1) * (4 - rank)
        elif rank == 4:
            penalty_adjustment -= 1
        else:
            continue  # early skip for high ranks

    # Misleading floating point accumulation (semi-relevant but unused)
    cumulative_effect = 0.0
    for w in weights.values():
        cumulative_effect += w ** 0.5
    
    # Another distractor: sorting that doesn't affect result
    sorted_ranks = sorted(ranks, reverse=True)
    rank_gap = sorted_ranks[0] - sorted_ranks[-1] if len(sorted_ranks) > 1 else 0

    # Actual adjustment via conditional expression
    modifier = 1.5 if rank_sum < 10 else 1.2
    
    intermediate_total = base_score + penalty_adjustment
    
    # Final computation
    final_score = int(intermediate_total * modifier)
    
    return final_score

# Main data
rank_data = [1, 4, 2, 5, 1]
bonus_weights = {0: 3, 2: 2, 4: 4}  # Only indices 0,2,4 have bonuses

# Extra irrelevant variables (distractors)
dummy_stats = {'avg': sum(rank_data)/len(rank_data), 'max_rank': max(rank_data)}
scaling_factor = 0.85
offset_correction = -2

# Key statement
final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")