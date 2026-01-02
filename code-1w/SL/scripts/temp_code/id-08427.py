def calculate_final_score(ranks, multiplier):
    base_points = {rank: 10 - idx for idx, rank in enumerate(sorted(ranks))}
    
    # Irrelevant transformation - distractor
    temp_adjusted = [val * 1.5 for val in ranks if val > 2]
    temp_adjusted = [t for t in temp_adjusted if t < 20]  # Dead filtering

    # Real logic begins
    valid_categories = set(range(1, 11))
    filtered_ranks = [r for r in ranks if r in valid_categories]
    
    # Conditional expression with actual impact
    penalty = 5 if len(filtered_ranks) < len(ranks) else 0
    
    raw_sum = sum(base_points[r] for r in filtered_ranks)
    
    # Secondary adjustment using set difference - semi-relevant
    missing = valid_categories - set(ranks)
    completeness_bonus = 3 if len(missing) < 5 else 0
    
    # Multiple assignments - some distracting
    extra_weight = 1.2
    decay_factor = 0.95  # Unused in final path but looks important
    scaling_factor = multiplier if multiplier > 0 else 1
    
    intermediate_score = (raw_sum - penalty) * scaling_factor
    final_score = int(intermediate_score + completeness_bonus)
    
    # Distractor: complex unused computation
    outlier_count = sum(1 for x in ranks if x < 3 or x > 9)
    trend_analysis = [ranks[i+1] - ranks[i] for i in range(len(ranks)-1)] if len(ranks) > 1 else []
    stability_score = 10 - len([t for t in trend_analysis if abs(t) > 2])
    
    return final_score

# Main execution
rank_data = [5, 8, 2, 9, 1, 7]
bonus_multiplier = 2
final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")