def calculate_final_score(ranks, bonuses):
    base_points = [10 - r for r in ranks]
    multiplier = sum(1 for b in bonuses if b > 7)
    adjusted = map(lambda x: x * (multiplier if x > 5 else 1), base_points)
    filtered_ranks = {i for i, r in enumerate(ranks) if r < 9}
    rank_sum = sum(filtered_ranks)
    bonus_contribution = sum(b // 3 for b in bonuses)
    temp_result = list(adjusted)
    total_base = sum(temp_result)
    final_score = total_base + bonus_contribution + (rank_sum % 4)
    return final_score

# Irrelevant auxiliary variable (mild distraction)
aux_data = [0.1, 0.2, 0.3]

rank_data = [1, 3, 8, 2, 7]
bonus_levels = [5, 9, 6, 10]

final_score = calculate_final_score(rank_data, bonus_levels)
print(f"Target result: {final_score}")