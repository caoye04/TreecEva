def calculate_final_score(assessments, weights):
    normalized = {k: v / 100 for k, v in assessments.items()}
    weighted_scores = [normalized[k] * weights[k] for k in weights]
    bonus = 0.05 if sum(weighted_scores) > 0.8 else 0
    raw_score = sum(weighted_scores) + bonus
    return int(round(raw_score * 100))

# Student assessment scores (out of 100)
assessments = {
    'homework': 95,
    'midterm': 87,
    'project': 90,
    'final_exam': 78
}

# Weight distribution for final score
weights = {
    'homework': 0.2,
    'midterm': 0.25,
    'project': 0.25,
    'final_exam': 0.3
}

# Irrelevant utility variable (minor distraction)
temp_scaling = 1.0

final_score = calculate_final_score(assessments, weights)
print(f"Result: {final_score}")