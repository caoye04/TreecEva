def calculate_final_score(ranks, scores):
    rank_set = set(ranks)
    bonus_multiplier = 1.0
    
    # Determine bonus based on unique rank count
    if len(rank_set) > 3:
        bonus_multiplier = 1.5
    elif len(rank_set) == 3:
        bonus_multiplier = 1.3
    else:
        bonus_multiplier = 1.1
    
    base_total = sum(scores)
    adjustment = 0
    
    # Apply combinatorial adjustment based on presence of key ranks
    critical_ranks = {1, 2, 5}
    matched_ranks = rank_set.intersection(critical_ranks)
    
    if 1 in matched_ranks:
        adjustment += 15
    if len(matched_ranks) >= 2:
        adjustment += 10
    
    adjusted_total = base_total + adjustment
    final_score = adjusted_total * bonus_multiplier
    
    return final_score

# Input data
base_scores = [88, 76, 92]
rank_list = [4, 1, 2, 4, 2]

# Execution point of interest
final_score = calculate_final_score(rank_list, base_scores)

print(f"Result: {final_score}")