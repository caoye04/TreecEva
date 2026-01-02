from collections import Counter

def calculate_final_score(ranks):
    base_score = 0
    multiplier = 1
    for rank, count in ranks.items():
        if rank > 5:
            base_score += count * rank
        else:
            base_score += count * (rank + 1)
    return base_score * multiplier

# Simulate player ranking data
player_ranks = [3, 7, 4, 7, 2, 9, 7, 4, 3, 8, 9, 2, 6]

# Count frequency of each rank
rank_counts = Counter(player_ranks)

# Calculate final score based on weighted rules
bonus_flag = len(player_ranks) > 10  # Irrelevant flag (minimal distraction)
total_score = calculate_final_score(rank_counts)

print(f"Result: {total_score}")