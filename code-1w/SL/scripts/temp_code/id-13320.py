from collections import Counter

def calculate_final_score(ranks, base_vals):
    rank_counts = Counter(ranks)
    weighted_sum = 0
    total_entries = len(ranks)
    
    for rank, count in rank_counts.items():
        weight = (5 - rank) if rank <= 5 else 1
        contribution = weight * base_vals.get(rank, 0) * count
        weighted_sum += contribution
    
    average_bonus = total_entries // 4
    final_adjustment = weighted_sum + average_bonus
    return final_adjustment

# Base score configuration
base_scores = {1: 10, 2: 7, 3: 5, 4: 3, 5: 2}

# Player rank history (simulated log entries)
player_ranks = [1, 2, 2, 3, 1, 4, 2, 5, 3, 1]

# Irrelevant auxiliary variable (minor distraction)
dummy_flag = True

# Compute final score
total_score = calculate_final_score(player_ranks, base_scores)

# Output result
print(f"Result: {total_score}")