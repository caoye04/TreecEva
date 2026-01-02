def calculate_final_score(scores, weight_map):
    normalized = [score / 100 for score in scores]
    weighted = [n * weight_map[i] for i, n in enumerate(normalized)]
    aggregate = sum(weighted)
    bonus = 0.05 if aggregate > 0.8 else 0
    return int((aggregate + bonus) * 100)

# Irrelevant utility function (minor distraction)
def format_percentage(val):
    return f"{val:.1f}%"

# Main computation
raw_scores = [85, 90, 78, 92]
weights = {0: 0.2, 1: 0.3, 2: 0.15, 3: 0.35}
initial_total = sum(raw_scores)
final_score = calculate_final_score(raw_scores, weights)
print(f"Result: {final_score}")