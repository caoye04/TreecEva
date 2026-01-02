from collections import defaultdict

# Simulate ranking points from tournament rounds
def calculate_round_points(position):
    points_map = {1: 100, 2: 75, 3: 50}
    return points_map.get(position, 25)

def calculate_final_score(ranks, extra):
    base_scores = defaultdict(int)
    for player, positions in ranks.items():
        for pos in positions:
            base_scores[player] += calculate_round_points(pos)
    
    # Apply bonus multiplier only if player participated in all rounds
    final_scores = {}
    for player, total in base_scores.items():
        if len(ranks[player]) >= 4:
            final_scores[player] = total * (1 + extra / 100)
        else:
            final_scores[player] = total
    
    # Return top score
    return int(max(final_scores.values()))

# Tournament data
rank_data = {
    'Alice': [1, 3, 2, 1],
    'Bob': [2, 1, 4],
    'Charlie': [4, 4, 3, 2, 1],
    'Diana': [1, 2]
}

bonus = 10

# Irrelevant utility (mild distraction)
def normalize_name(name):
    return name.strip().capitalize()

unused_counter = defaultdict(int)
for name in rank_data:
    unused_counter[normalize_name(name)] += 1

final_score = calculate_final_score(rank_data, bonus)
print(f"Result: {final_score}")