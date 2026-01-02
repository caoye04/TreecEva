def calculate_final_score(ranks, scores):
    rank_bonus = len(ranks.intersection({1, 2, 3})) * 15
    performance_multiplier = 1.2 if len(ranks) > 4 else 1.0
    base_total = sum(scores)
    adjustment = 10 if 5 in ranks else 0
    final_score = (base_total + rank_bonus + adjustment) * performance_multiplier
    return final_score

# Initial data
candidate_ranks = {2, 4, 6, 8, 1}
base_scores = [88, 76, 92]

# Computation path
rank_set = set(candidate_ranks)
score_input = base_scores.copy()
final_score = calculate_final_score(rank_set, base_scores)
print(f"Result: {final_score}")