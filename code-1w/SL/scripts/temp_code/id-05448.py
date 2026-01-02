from collections import defaultdict

# Simulate player ranking data from tournament rounds
ranks = [1, 2, 3, 2, 1, 4, 3, 1, 2, 4, 5, 3, 2, 1]
base_points = 10

def calculate_final_score(rank_freq, base):
    score = 0
    for rank, count in rank_freq.items():
        if rank == 1:
            score += count * (base + 5)
        elif rank <= 3:
            score += count * base
        else:
            score += count * (base // 2)
    return score

# Count frequency of each rank
rank_counts = defaultdict(int)
for rank in ranks:
    rank_counts[rank] += 1

# Calculate final score based on performance tiers
final_score = calculate_final_score(rank_counts, base_points)

print(f"Target result: {final_score}")