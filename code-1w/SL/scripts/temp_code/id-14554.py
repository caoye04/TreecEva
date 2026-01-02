from collections import defaultdict

# Simulate student assessment scores across different categories
def calculate_final_score(assessments):
    category_totals = defaultdict(float)
    category_counts = defaultdict(int)

    # Aggregate scores by category
    for category, score in assessments:
        category_totals[category] += score
        category_counts[category] += 1

    # Compute average per category and apply weighting
    weighted_sum = 0.0
    weights = {'homework': 0.3, 'quiz': 0.2, 'exam': 0.5}
    total_weight = 0.0

    for cat in category_totals:
        avg_score = category_totals[cat] / category_counts[cat]
        weight = weights.get(cat, 0)
        if weight > 0:
            weighted_sum += avg_score * weight
            total_weight += weight

    # Normalize by total applied weight
    final_normalized_score = weighted_sum / total_weight if total_weight > 0 else 0
    return round(final_normalized_score, 3)

# Irrelevant helper (mild distraction)
def get_grade_letter(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    else: return 'F'

# Dataset: (category, score)
assessments_data = [
    ('homework', 85), ('homework', 90), ('homework', 88),
    ('quiz', 78), ('quiz', 82),
    ('exam', 94), ('exam', 89)
]

# Unused variable (minor interference)
extreme_scores = [min(assessments_data, key=lambda x: x[1]), max(assessments_data, key=lambda x: x[1])]

final_score = calculate_final_score(assessments_data)
print(f"Result: {final_score}")