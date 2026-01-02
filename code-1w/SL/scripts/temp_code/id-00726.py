def calculate_final_score(scores, weight_list):
    normalized = [score / 100 for score in scores]
    weighted = [n * w for n, w in zip(normalized, weight_list)]
    aggregate = sum(weighted)
    bonus = 0.05 if aggregate > 0.8 else 0
    return round((aggregate + bonus) * 100, 2)

# Student test scores and corresponding weights
test_scores = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.15, 0.35]

# Irrelevant distraction: unused variable
baseline_average = sum(test_scores) // len(test_scores)

# Compute final score
raw_scores = test_scores[1:]  # Slicing to use recent test performances only
final_score = calculate_final_score(raw_scores, weights[1:])

print(f"Target result: {final_score}")