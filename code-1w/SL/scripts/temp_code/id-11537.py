from collections import defaultdict

def calculate_final_score(ranks, weight_map):
    score = 0
    for item, rank_list in ranks.items():
        avg_rank = sum(rank_list) / len(rank_list)
        weight = weight_map.get(item, 1.0)
        score += (1 / (avg_rank + 1e-5)) * weight
    return int(score)

# Simulated tournament rankings across multiple events
tournament_data = {
    'player_A': [1, 2, 1, 3],
    'player_B': [3, 1, 2, 1],
    'player_C': [2, 3, 4, 2]
}

# Weighting based on event importance
weights = {'player_A': 1.2, 'player_B': 1.5}

# Irrelevant auxiliary variable (minor distraction)
temp_result = [x**2 for x in range(3)]

final_score = calculate_final_score(tournament_data, weights)
print(f"Target result: {final_score}")