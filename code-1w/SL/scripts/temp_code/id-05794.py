def calculate_final_score(scores, impact_weights):
    normalized = [score / max(scores) for score in scores]
    weighted_values = [n * w for n, w in zip(normalized, impact_weights)]
    aggregate = sum(weighted_values)
    penalty = 0.1 * len([v for v in scores if v < 50])
    return round(aggregate - penalty, 3)

raw_scores = [78, 92, 45, 88, 95]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]
extra_data = [x ** 0.5 for x in raw_scores]  # distractor: not used
initial_avg = sum(raw_scores) / len(raw_scores)
final_score = calculate_final_score(raw_scores, weights)
print(f"Result: {final_score}")