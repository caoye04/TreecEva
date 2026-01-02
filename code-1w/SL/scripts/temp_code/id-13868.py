def process_ranking(ranks, cutoff):
    filtered = {k: v for k, v in ranks.items() if v <= cutoff}
    bonus_points = 0
    
    # Irrelevant computation - distractor
    temp_values = [x**2 for x in range(len(ranks))]
    cumulative = sum(temp_values[:3]) // 2 if len(temp_values) > 2 else 0
    
    # Misleading state tracking
    status_log = []
    for key in sorted(ranks.keys()):
        if ranks[key] < cutoff:
            status_log.append(f'{key}: promoted')
        else:
            status_log.append(f'{key}: reviewed')
    
    # Real logic starts here
    elite_group = set(k for k, v in ranks.items() if v == 1)
    strong_contenders = set(k for k, v in ranks.items() if 2 <= v <= 4)
    overlap = elite_group & strong_contenders  # Always empty, but included for confusion
    
    # Scoring logic
    base_score = len(filtered) * 10
    tier_bonus = 0
    if len(elite_group) >= 1:
        tier_bonus += 25
    if len(strong_contenders) >= 3:
        tier_bonus += 15
    
    # Another distraction: slicing unused list
    slices = temp_values[1:5:2]
    phantom_impact = sum(slices) % 7 if slices else 0  # Not actually used
    
    # Final adjustments
    adjustment = 0
    rank_list = sorted(ranks.values())
    if len(rank_list) >= 5:
        median_rank = rank_list[len(rank_list)//2]
        adjustment = 5 if median_rank <= 3 else -5
    
    final_score = base_score + tier_bonus + adjustment
    
    # Dead code path - never executed in this context
    debug_mode = False
    if debug_mode:
        print("Debug:", locals())
    
    return final_score

# Main execution
rankings_data = {
    'Alice': 1,
    'Bob': 3,
    'Charlie': 2,
    'Diana': 1,
    'Eve': 4,
    'Frank': 7,
    'Grace': 5
}

intermediate_total = sum(rankings_data.values()) // len(rankings_data)  # Distractor
snapshot = rankings_data.copy()  # Unused

final_score = process_ranking(rankings_data, cutoff=6)
print(f"Result: {final_score}")