def calculate_final_score(ranks, scores):
    rank_set = {r for r in ranks if r > 0}
    filtered_scores = [s for s in scores if s >= 50]
    passed_count = len(filtered_scores)
    bonus = 10 if passed_count >= 3 else 5
    total = sum(filtered_scores) // passed_count if passed_count > 0 else 0
    adjustment = 2 * len(rank_set & {1, 2, 3})
    return total + bonus + adjustment

# Base inputs
base_ranks = [1, 4, 2, 0, 5]
base_scores = [45, 70, 85, 30, 90]

# Irrelevant distraction variable
aux_data = [x * 2 for x in base_ranks]

rank_set = set(base_ranks)
final_score = calculate_final_score(rank_set, base_scores)

print(f"Target result: {final_score}")