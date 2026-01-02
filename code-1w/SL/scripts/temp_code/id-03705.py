from collections import defaultdict

# Simulate student assessment scores across different categories
def calculate_final_score(assessments, bonus_active):
    category_totals = defaultdict(float)
    weight_map = {'quiz': 0.2, 'homework': 0.3, 'exam': 0.5}
    
    for category, score in assessments:
        category_totals[category] += score

    weighted_sum = 0.0
    for cat, total in category_totals.items():
        weighted_sum += total * weight_map.get(cat, 0)
    
    # Apply bonus if active and minimum base score achieved
    base_score = sum(category_totals.values())
    if bonus_active and base_score >= 80:
        extra_bonus = 5.0 if base_score > 90 else 3.5
        weighted_sum += extra_bonus
    
    return round(weighted_sum, 2)

# Data setup
assessments = [
    ('quiz', 15), ('quiz', 20),
    ('homework', 25), ('homework', 30),
    ('exam', 45), ('exam', 50)
]
bonus_active = True

# Computation entry point
final_score = calculate_final_score(assessments, bonus_active)
print(f"Target result: {final_score}")