def calculate_final_score(data, weight_map):
    base_score = 0
    penalty_offset = 0
    temp_adjustment = 0

    # Irrelevant preprocessing: normalize names (not used in score)
    normalized_names = [name.upper().strip() for name in data.get('participants', [])]
    
    rankings = data.get('rankings', [])
    tiers = data.get('tiers', [])

    # Misleading computation: complex-looking but unused entropy calc
    entropy = 0.0
    for r in rankings:
        if r > 0:
            entropy -= (1 / r) * (1 / r)
    
    # Actual scoring logic
    for i, rank in enumerate(rankings):
        if rank <= 3:
            base_score += weight_map['top']
        elif rank <= 10:
            base_score += weight_map['mid']
        else:
            base_score += weight_map['low']

        # Conditional bonus for tier-based performance
        if i < len(tiers) and tiers[i] == 'A':
            base_score += 2

    # Unused accumulator (distractor)
    cumulative_shift = sum([base_score >> n for n in range(3) if n % 2 == 0])

    # Lambda-based dynamic adjustment (used once)
    apply_bonus = lambda x, flag: x + 5 if flag else x
    final_score = apply_bonus(base_score, base_score > 20)

    # Dead code path: never executed due to constant condition
    debug_mode = False
    if debug_mode:
        print("Debug: Final calculation steps")
        temp_adjustment = 999

    return final_score

# Input data
rank_data = {
    'participants': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'rankings': [1, 4, 7, 12, 2],
    'tiers': ['A', 'B', 'A', 'C', 'A']
}

weights = {
    'top': 10,
    'mid': 6,
    'low': 2
}

# Execution point
final_score = calculate_final_score(rank_data, weights)
print(f"Target result: {final_score}")