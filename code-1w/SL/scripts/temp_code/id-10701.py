from collections import defaultdict

# Simulate student marks and subject weights
def rank_data(scores, weight_map):
    normalized = defaultdict(float)
    total_weight = sum(weight_map.values())
    
    for subject, score in scores.items():
        if subject in weight_map:
            normalized[subject] = score * (weight_map[subject] / total_weight)
    
    aggregate = sum(normalized.values())
    adjustment = len(scores) > 3
    
    # Apply bonus logic for multidisciplinary performance
    bonus = 0.5 if adjustment else 0
    final = aggregate + bonus
    
    return round(final, 3)

# Input data
marks = {'math': 85, 'physics': 90, 'chemistry': 78, 'biology': 88}
weights = {'math': 4, 'physics': 5, 'chemistry': 3, 'biology': 4}

# Irrelevant distractor variables (minimal interference)
temp_data = [1.2, 3.4, 5.6]
dummy_flag = True

final_score = rank_data(marks, weights)
print(f"Result: {final_score}")