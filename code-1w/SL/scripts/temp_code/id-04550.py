def calculate_final_score(ranks):
    base_scores = [10 - r for r in ranks if r < 10]
    bonus = len(base_scores) // 3
    adjusted_scores = [s + bonus for s in base_scores]
    sorted_scores = sorted(adjusted_scores, reverse=True)
    return sum(sorted_scores[:3])

rankings = [2, 5, 1, 8, 3, 12, 7]
counterfeit_rank = 99
placeholder_value = -1
temp_result = "unused"

final_score = calculate_final_score(rankings)
print(f"Result: {final_score}")