def calculate_final_score(ranks, weights):
    normalized = {k: (1 / (v + 1)) for k, v in ranks.items()}
    weighted_scores = [normalized[cat] * weights[cat] for cat in ranks if cat in weights]
    avg_weighted = sum(weighted_scores) / len(weighted_scores)
    bonus = 10 if avg_weighted > 0.4 else 5
    return int(avg_weighted * 100 + bonus)

# Irrelevant auxiliary data (minimal distraction)
temp_log = {'user_init': 'sys_admin', 'timestamp': 12032024}

rank_data = {'usability': 1, 'performance': 2, 'security': 1, 'maintainability': 3}
base_weights = {'usability': 0.4, 'performance': 0.3, 'security': 0.2, 'maintainability': 0.1}

final_score = calculate_final_score(rank_data, base_weights)
print(f"Result: {final_score}")