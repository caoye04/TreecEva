def calculate_final_score(ranks, w):
    normalized = [max(0, 10 - r) for r in ranks]
    weighted_vals = [n * f for n, f in zip(normalized, w)]
    penalty = sum(1 for v in ranks if v > 8)
    bonus = 5 if all(r < 9 for r in ranks) else 0
    return sum(weighted_vals) - penalty + bonus

# Irrelevant auxiliary data (minor distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
temp_log = [f"Event: {i}" for i in range(3)]

# Main computation
rank_data = [3, 7, 6, 9, 4]
weights = [1.2, 0.8, 1.0, 0.5, 1.1]
final_score = calculate_final_score(rank_data, weights)

print(f"Result: {final_score}")