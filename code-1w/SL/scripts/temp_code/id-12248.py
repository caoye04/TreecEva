from collections import defaultdict

def calculate_final_score(scores, weight_map):
    normalized = defaultdict(float)
    total_weight = sum(weight_map.values())
    
    for key, value in scores.items():
        if key in weight_map:
            normalized[key] = (value / 100) * weight_map[key]
    
    return int(sum(normalized.values()) * 100)

# Irrelevant auxiliary variable (distractor)
user_preferences = {'theme': 'dark', 'notifications': True}

raw_scores = {
    'math': 92,
    'physics': 87,
    'chemistry': 95,
    'literature': 83
}

weights = {
    'math': 0.3,
    'physics': 0.25,
    'chemistry': 0.25,
    'literature': 0.2
}

final_score = calculate_final_score(raw_scores, weights)
print(f"Result: {final_score}")