from itertools import compress

def calculate_final_score(ranks, multiplier):
    base_scores = [100 - rank for rank in ranks]
    valid_rank_flags = [rank <= 50 for rank in ranks]
    filtered_scores = list(compress(base_scores, valid_rank_flags))
    adjustment = sum(filtered_scores) * 0.1 if len(filtered_scores) > 3 else 5
    total_base = sum(filtered_scores)
    return int((total_base + adjustment) * multiplier)

# Irrelevant auxiliary data (minor distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
temp_log = [1, 1, 1]  # unused in computation

rank_data = [10, 25, 30, 45, 60, 75]
bonus_multiplier = 1.2
final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")