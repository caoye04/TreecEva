from collections import defaultdict

def calculate_final_score(ranks):
    score = 0
    multiplier = 1
    for rank, count in sorted(ranks.items()):
        score += rank * count * multiplier
        multiplier += 1
    return score

# Player rank data (simulated tournament results)
player_ranks = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Count frequency of each rank
rank_counts = defaultdict(int)
for rank in player_ranks:
    rank_counts[rank] += 1

# Irrelevant auxiliary variable (minor distraction)
temp_buffer = [0] * 5

# Core computation step
final_score = calculate_final_score(rank_counts)

# Output result
print(f"Result: {final_score}")