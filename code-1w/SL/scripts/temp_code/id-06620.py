def process_rankings(ranks, types):
    base_values = {k: v * 1.5 for k, v in ranks.items() if k in types}
    offset = len(types) * 2
    adjusted = sum(base_values.values()) + offset
    
    # Irrelevant tracking variable (mild distraction)
    temp_log = [f'{key}: {val}' for key, val in base_values.items()]
    
    multiplier = 1.0
    if len(base_values) > 3:
        multiplier = 1.2
    
    return int(adjusted * multiplier)

# Core data structures
rank_map = {
    'alpha': 8,
    'beta': 12,
    'gamma': 5,
    'delta': 10,
    'epsilon': 3
}

categories = {'alpha', 'gamma', 'delta', 'beta'}

# Secondary unused variable (minor interference)
reference_weights = {'alpha': 0.8, 'beta': 0.9, 'gamma': 0.7}

final_score = process_rankings(rank_map, categories)
print(f"Result: {final_score}")