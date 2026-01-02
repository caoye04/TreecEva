from collections import defaultdict

# Simulate student test scores with bonus points
def calculate_final_score(scores, bonuses):
    base_total = sum(scores)
    multiplier = 1.5 if len(scores) > 3 else 1.0
    
    # Apply bonus only to subjects with score below 70
    adjusted_bonus = 0
    for subject, score in scores.items():
        if score < 70:
            adjusted_bonus += bonuses.get(subject, 0)
    
    final_score = (base_total + adjusted_bonus) * multiplier
    return int(final_score)

# Irrelevant distraction: unused variable (minimal interference)
dummy_data = [0] * 5

# Input data
scores = {'math': 85, 'physics': 65, 'chemistry': 72, 'biology': 58}
bonuses = {'physics': 8, 'biology': 12, 'history': 10}  # history not in scores

result = calculate_final_score(scores, bonuses)
print(f"Target result: {result}")