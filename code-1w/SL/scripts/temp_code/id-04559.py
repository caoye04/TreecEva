from collections import defaultdict

def calculate_final_score(grades, weights):
    weighted_sum = 0
    total_weight = 0
    for i, (subject, score) in enumerate(grades.items()):
        weight = weights.get(subject, 1)
        if score >= 60:
            weighted_sum += score * weight
            total_weight += weight
    return weighted_sum / total_weight if total_weight != 0 else 0

# Student performance data
student_grades = {
    'math': 85,
    'physics': 78,
    'chemistry': 92,
    'literature': 88,
    'history': 73
}

bonus_weights = defaultdict(int, {'math': 2, 'physics': 1.5})
extra_credit = 5  # Irrelevant distractor variable

# Computation of final score
total_score = calculate_final_score(student_grades, bonus_weights)

# Output result
print(f"Result: {total_score}")