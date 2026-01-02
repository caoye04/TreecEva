def calculate_final_score(scores, weight_map):
    normalized = {k: v / 10 for k, v in scores.items() if v > 5}
    adjusted = [normalized[k] * weight_map[k] for k in normalized if k in weight_map]
    base = sum(adjusted)
    penalty = 0
    for key in scores:
        if scores[key] < 5:
            penalty += 1
    final_score = base - penalty * 0.5
    return final_score

raw_scores = {'math': 8, 'physics': 7, 'chemistry': 9, 'history': 4, 'art': 3}
weights = {'math': 1.2, 'physics': 1.5, 'chemistry': 1.3, 'history': 1.0, 'art': 0.8}

# Irrelevant variable (minor distraction)
temp_data = [x for x in range(5)]

final_score = calculate_final_score(raw_scores, weights)
print(f"Result: {final_score}")