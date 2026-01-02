from collections import defaultdict

def calculate_final_score(ranks, weight_map):
    base_scores = defaultdict(int)
    for player, rank_list in ranks.items():
        for i, rank in enumerate(rank_list):
            base_scores[player] += weight_map.get(i, 0) * (10 - rank)
    
    bonus_applied = {}
    for player, score in base_scores.items():
        if score > 25:
            bonus_applied[player] = score + 5
        else:
            bonus_applied[player] = score
    
    sorted_players = sorted(bonus_applied, key=lambda x: bonus_applied[x], reverse=True)
    champion = sorted_players[0]
    return bonus_applied[champion]

# Rankings for 3 events per player
rankings = {
    'Alice': [1, 3, 2],
    'Bob': [2, 1, 4],
    'Charlie': [3, 2, 1]
}

# Weight for each event position
weights = {0: 1, 1: 2, 2: 3}

final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")