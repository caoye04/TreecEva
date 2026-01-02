from collections import defaultdict

def calculate_final_score(performances, multipliers):
    base_scores = defaultdict(float)
    for category, values in performances.items():
        base_scores[category] = sum(values) * multipliers[category]
    
    total = sum(base_scores.values())
    bonus = 0
    if len(performances['engineering']) > 3:
        bonus += 5
    if sum(performances['design']) >= 25:
        bonus += 3
    
    adjusted_total = total + bonus
    penalty = 1 if len(performances) < 3 else 0
    return int(adjusted_total - penalty)

# Irrelevant auxiliary data (minor distraction)
legacy_data = {'old_metric_a': [1, 1], 'old_metric_b': [0]}
config_flag = True

rankings = {
    'engineering': [4, 5, 6, 7],
    'design': [8, 9, 8],
    'research': [3, 4, 5]
}

weights = {
    'engineering': 1.2,
    'design': 1.5,
    'research': 2.0
}

final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")