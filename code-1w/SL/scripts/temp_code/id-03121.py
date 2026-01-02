def calculate_final_score(ranks, coeffs):
    normalized = [(max(ranks) - x) / (max(ranks) - min(ranks)) if max(ranks) != min(ranks) else 0.5 for x in ranks]
    weighted_vals = list(map(lambda w, v: w * v, coeffs, normalized))
    adjustment = sum([i > 2 and val < 0.3 for i, val in enumerate(weighted_vals)]) * 0.1
    return round(sum(weighted_vals) + adjustment, 3)

# Irrelevant auxiliary data (mild distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
temp_log = [1, 1, 1]  # unused

rankings = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")