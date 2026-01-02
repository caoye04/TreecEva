from collections import defaultdict

def calculate_final_score(performances, multipliers):
    base_scores = defaultdict(float)
    for category, values in performances.items():
        base_scores[category] = sum(values) * multipliers.get(category, 1.0)
    
    adjustment = 0.0
    total_categories = len(base_scores)
    if total_categories > 3:
        adjustment = 5.0
    
    intermediate = sum(base_scores.values()) + adjustment
    scaling_factor = 1.2 if intermediate > 100 else 1.0
    return int(intermediate * scaling_factor)

# Input data
rankings = {
    'accuracy': [8, 7, 9],
    'speed': [6, 8, 7, 9],
    'efficiency': [7, 7],
    'usability': [9, 8, 8]
}

weights = {
    'accuracy': 1.5,
    'speed': 1.2,
    'efficiency': 1.0,
    'usability': 1.3
}

# Irrelevant auxiliary variable (minor distraction)
temp_data = [1, 2, 3]

final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")