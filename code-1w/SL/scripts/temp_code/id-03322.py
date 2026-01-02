def calculate_final_score(ranks, multiplier):
    base_points = [10 - r for r in ranks if r <= 10]
    weighted_sum = sum([p * multiplier for p in base_points])
    adjustment = 5 if len(base_points) >= 3 else 0
    return weighted_sum + adjustment

# Competition ranking data (lower is better)
rank_data = [2, 4, 1, 12, 6]  # 12 is invalid and filtered out
bonus_multiplier = 1.5

initial_offset = 3  # Irrelevant variable (minimal distraction)
temp_result = [x * 2 for x in rank_data]  # Unused computation

final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")