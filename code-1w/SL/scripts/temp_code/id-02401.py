from collections import defaultdict

def calculate_final_score(ranks, coeffs):
    score_map = defaultdict(float)
    for idx, (player, rank_list) in enumerate(ranks.items()):
        base = sum(rank_list)
        adjustment = len(rank_list) - idx
        score_map[player] = base * coeffs[idx] + adjustment
    
    temp_sum = 0
    for val in score_map.values():
        temp_sum += val
    
    return int(temp_sum)

# Irrelevant utility function (mild distraction)
def normalize(data):
    total = sum(data)
    return [x / total for x in data]

# Input data
rankings = {
    'Alice': [3, 1, 4],
    'Bob': [2, 3, 2],
    'Charlie': [1, 2, 3]
}
weights = [0.5, 1.0, 1.5]

final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")