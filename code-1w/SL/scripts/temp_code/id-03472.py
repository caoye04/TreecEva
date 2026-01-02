def calculate_final_score(data, weights):
    base_scores = [d.get('rank', 0) * 10 for d in data]
    
    # Irrelevant transformation (distractor)
    temp_names = [d.get('name', '').upper() for d in data if 'name' in d]
    name_length_sum = sum(len(name) for name in temp_names)

    # Semi-relevant normalization (not used later)
    max_base = max(base_scores) if base_scores else 1
    normalized = [score / max_base for score in base_scores]

    # Actual weighting logic
    weighted_bonus = 0
    for i, entry in enumerate(data):
        if i % 2 == 0:
            multiplier = weights.get(f'bonus_{i}', 1)
            offset = entry.get('offset', 0)
            weighted_bonus += (entry.get('rank', 0) + offset) * multiplier
        else:
            # Unused branch (dead code path)
            fake_value = entry.get('rank', 0) ** 2
            continue

    # Real contribution: sum of base scores plus weighted even-indexed bonuses
    total_base = sum(base_scores)
    final_score = total_base + weighted_bonus * 2

    # More distractions
    stats_summary = {
        'count': len(data),
        'total_weighted': weighted_bonus,
        'dummy_flag': name_length_sum > 10
    }
    
    return final_score

# Input data
rank_data = [
    {'rank': 3, 'name': 'alpha', 'offset': 1},
    {'rank': 5, 'name': 'beta'},
    {'rank': 2, 'name': 'gamma', 'offset': 2},
    {'rank': 7, 'name': 'delta'}
]

bonus_weights = {
    'bonus_0': 4,
    'bonus_2': 3,
    'bonus_extra': 99  # unused key
}

# Execution
final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")