from itertools import combinations

def process_leaderboard(ranks, extra):
    base_scores = {player: (10 - rank) for player, rank in ranks.items()}
    
    # Apply bonus for top performers using set intersection
    elite_group = {'Alice', 'Bob', 'Charlie'}
    qualifiers = set(ranks.keys()) & elite_group
    for player in qualifiers:
        base_scores[player] += extra
    
    # Deduct points if any pair of top 3 players have consecutive ranks
    rank_values = list(ranks.values())
    has_consecutive = any(abs(a - b) == 1 for a, b in combinations(rank_values[:3], 2))
    if has_consecutive:
        for player in base_scores:
            base_scores[player] -= 1
    
    final_score = sum(base_scores.values())
    return final_score

# Input data
rankings = {'Alice': 1, 'Bob': 2, 'Charlie': 4, 'Diana': 7}
bonus_points = 3

final_score = process_leaderboard(rankings, bonus_points)
print(f"Result: {final_score}")